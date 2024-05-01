# Use Node.js base image
FROM node:14

# Set working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock) to container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app
COPY . .

# Build the React application
RUN npm run build

# Install serve to serve the build folder on port 3000
RUN npm install -g serve

# Expose the port the app runs on
EXPOSE 3000

# Command to serve the app using serve
CMD ["serve", "-s", "build", "-l", "3000"]
