<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, session
from bson import ObjectId  
import pymongo
from pymongo import MongoClient
import os

from dotenv import load_dotenv

#Connecting to the DB 


client = MongoClient(os.getenv('MONGO_URI'))
db = client[os.getenv('MONGO_DBNAME')]
=======
from flask import Flask, render_template, request, redirect, url_for
import pymongo


cxn = pymongo.MongoClient(f"mongodb+srv://doadmin:y98s36dH7TXG20C4@db-mongodb-nyc3-08772-c20abe3e.mongo.ondigitalocean.com/admin")
db = cxn["mongodb_dockerhub"]
>>>>>>> e22af11c0e7d06df959c939ce7c71be770d5a078
collection=db["logs"]

app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return render_template('home.html')
   
@app.route('/workout_list')
def workout_list():
    workouts = collection.find()
    return render_template('workout_list.html', workouts=workouts)

# Edit a specific workout
@app.route('/edit_workout/<string:workout_id>', methods=['GET', 'POST'])
def edit_workout(workout_id):
    if request.method == 'POST':
        # Handle form submission for editing workout (similar to previous example)
        pass
    else:
        # Retrieve the workout from the database by its ID
        workout = collection.find_one({'_id': ObjectId(workout_id)})
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
        # Get form data
        workout_type = request.form['workout_type']
        length_minutes = int(request.form['length_minutes'])
        intensity = request.form['intensity']
        date = request.form['date']
        
        # Insert the new workout into the database
        new_workout = {
            'workout_type': workout_type,
            'length_minutes': length_minutes,
            'intensity': intensity,
            'date': date
        }
        collection.insert_one(new_workout)
        
        # Redirect to the workout log page after adding the workout
        return redirect(url_for('workout_list'))
    
    # Render the form to add a new workout
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
    # Query all workout entries from the database
    workouts = list(collection.find())
    
    # Calculate the total time logged working out
    total_time = sum(workout['length_minutes'] for workout in workouts)
    
    # Calculate the counts for each workout category (muscular, cardio, flexibility)
    category_counts = {
        'muscular': sum(1 for workout in workouts if workout['workout_type'] == 'muscular'),
        'cardio': sum(1 for workout in workouts if workout['workout_type'] == 'cardio'),
        'flexibility': sum(1 for workout in workouts if workout['workout_type'] == 'flexibility')
    }
    
    # Calculate the counts for each intensity level (low, medium, high)
    intensity_counts = {
        'low': sum(1 for workout in workouts if workout['intensity'] == 'low'),
        'medium': sum(1 for workout in workouts if workout['intensity'] == 'medium'),
        'high': sum(1 for workout in workouts if workout['intensity'] == 'high')
    }
    
    # Calculate the percentages for each category
    total_workouts = len(workouts)
    category_percentages = {category: (count / total_workouts) * 100 for category, count in category_counts.items()}
    
    # Calculate the percentages for each intensity
    intensity_percentages = {intensity: (count / total_workouts) * 100 for intensity, count in intensity_counts.items()}
    
    # Check if the total time logged is greater than 2 hours
    if total_time > 120:
        message = "Great Job! Keep it Up!"
    else:
        message = "Let's Get Started!"
    
    # Render the template with the calculated statistics and message
    return render_template('workout_stats.html', 
                           category_percentages=category_percentages, 
                           intensity_percentages=intensity_percentages, 
                           total_time=total_time,
                           message=message)





if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run(host='0.0.0.0', port=5000)
>>>>>>> e22af11c0e7d06df959c939ce7c71be770d5a078
