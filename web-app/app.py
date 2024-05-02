from flask import Flask, render_template, request, redirect, url_for, session
from bson import ObjectId  
import pymongo
from pymongo import MongoClient
import os

from dotenv import load_dotenv

#Connecting to the DB 


client = MongoClient(os.getenv('MONGO_URI'))
db = client[os.getenv('MONGO_DBNAME')]
collection=db["logs"]

app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return render_template('index.html')
   
@app.route('/workout_list')
def workout_list():
    workouts = collection.find()
    return render_template('workout_list.html', workouts=workouts)

# Edit a specific workout
@app.route('/edit_workout/<string:workout_id>', methods=['GET', 'POST'])
def edit_workout(workout_id):
    workout = collection.find_one({'_id': ObjectId(workout_id)})  # Retrieve workout for both GET and POST
    if not workout:
        return "Workout not found", 404  # Always handle the possibility that the workout does not exist

    if request.method == 'POST':
        # Process form data here
        # Example: Update the workout in the database
        updated_data = {
            'workout_type': request.form['type'],
            'length_minutes': int(request.form['duration']),
            'intensity': request.form['intensity'],
            'date': request.form['date']
        }
        collection.update_one({'_id': ObjectId(workout_id)}, {'$set': updated_data})
        # Optionally, re-fetch the workout to update the data shown on the same form
        workout = collection.find_one({'_id': ObjectId(workout_id)})
        return redirect(url_for('workout_list'))  # or re-render the form to show updated data
    else:
        return render_template('edit_workout.html', workout=workout)

    
# Delete a specific workout
@app.route('/delete_workout/<string:workout_id>', methods=['POST'])
def delete_workout(workout_id):
    # Handle deletion of workout
    collection.delete_one({'_id': ObjectId(workout_id)})
    return redirect(url_for('workout_list'))

#Add a workout
@app.route('/add_workout', methods=['GET', 'POST'])
def add_workout():
    if request.method == 'POST':
        # Extract data from the form
        workout_type = request.form.get('type')
        length_minutes = request.form.get('duration', type=int)
        intensity = request.form.get('intensity')
        date = request.form.get('date')

        # Create workout dictionary
        new_workout = {
            'workout_type': workout_type,
            'length_minutes': length_minutes,
            'intensity': intensity,
            'date': date
        }
        # Insert new workout into the database
        collection.insert_one(new_workout)
        return redirect(url_for('workout_list'))

    # Render form for adding new workout
    return render_template('add_workout.html')


# Reset the workout log
@app.route('/reset_workout_log', methods=['GET', 'POST'])
def reset_workout_log():
    if request.method == 'POST':
        if request.form['confirm'] == 'yes':
            # Delete all documents from the collection to reset the workout log
            collection.delete_many({})
            return redirect(url_for('workout_list'))
        else:
            # Redirect back to the workout list if the user cancels the reset
            return redirect(url_for('workout_list'))
    else:
        # Render the confirmation form to reset the workout log
        return render_template('reset_workout_log.html')
    

# Display workout statistics
@app.route('/workout_stats')
def workout_stats():
    workouts = list(collection.find())

    if workouts:
        total_time = sum(workout['length_minutes'] for workout in workouts)
        total_workouts = len(workouts)

        category_counts = {
            'muscular': sum(1 for workout in workouts if workout['workout_type'] == 'muscular'),
            'cardio': sum(1 for workout in workouts if workout['workout_type'] == 'cardio'),
            'flexibility': sum(1 for workout in workouts if workout['workout_type'] == 'flexibility')
        }

        intensity_counts = {
            'low': sum(1 for workout in workouts if workout['intensity'] == 'low'),
            'medium': sum(1 for workout in workouts if workout['intensity'] == 'medium'),
            'high': sum(1 for workout in workouts if workout['intensity'] == 'high')
        }

        category_percentages = {category: (count / total_workouts * 100) if total_workouts else 0 for category, count in category_counts.items()}
        intensity_percentages = {intensity: (count / total_workouts * 100) if total_workouts else 0 for intensity, count in intensity_counts.items()}
    else:
        total_time = 0
        category_counts = {}
        intensity_counts = {}
        category_percentages = {}
        intensity_percentages = {}

    return render_template('workout_stats.html', total_time=total_time, category_counts=category_counts, intensity_counts=intensity_counts, category_percentages=category_percentages, intensity_percentages=intensity_percentages)


if __name__ == '__main__':
    app.run(debug=True)
