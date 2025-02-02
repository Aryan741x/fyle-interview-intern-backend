# Building and Running the Application with Docker

This document provides clear instructions on how to build and run the Flask application with Docker, ensuring your app runs smoothly in a containerized environment.

### Prerequisites: 

Before starting, make sure you have the following installed:
1. **Docker**: The platform for building and running containers.
2. **Docker Compose**: A tool for defining and running multi-container Docker applications.
3. **Git**: For cloning the repository.

### Step 1: Clone the Repository
```
git clone https://github.com/Aryan741x/fyle-interview-intern-backend.git
cd fyle-interview-intern-backend
```

### Step 2: Build the Docker Image
#### Option 1: Using Dockerfile
In the project directory, you should have a Dockerfile which defines the environment for your Flask application.

To build the Docker image, run the following command:
```
docker build -t my-flask-app .
``` 
Here, my-flask-app is the name you're giving to your Docker image. The . refers to the current directory (where the Dockerfile is located).

#### Option 2: Using Docker Compose
Alternatively, if you have a docker-compose.yml file set up for multi-container configurations, you can use docker-compose to build the image and run the container.

To build the application using Docker Compose, run the following command:
```
docker-compose build
```
This will read the docker-compose.yml file and build the image as defined in the Dockerfile.

### Step 3: Run the Application
#### Option 1: Using Docker Command
Once the image is built, you can run the container using the following command:
```
docker run -p 5000:5000 my-flask-app
```
This command runs the Flask app inside a container. The -p 5000:5000 option binds port 5000 from the container to port 5000 on your local machine, allowing you to access the app at http://localhost:5000.

#### Option 2: Using Docker Compose
If you are using docker-compose.yml, you can start the application by running:
```
docker-compose up
```
This will run the Flask app as defined in the docker-compose.yml file. It also takes care of setting up any required services (like databases) and networking.

To run the app in detached mode (in the background), use:
```
docker-compose up -d
```
To stop the containers, use:
```
docker-compose down
```
### Step 4: Access the Application
Once the application is up and running, you can access it in your browser at:
```
http://localhost:5000
```

## Conclusion
By following the steps outlined above, you can easily build, run, and test your Flask application within Docker. Docker simplifies the deployment process and provides an isolated environment for running your application.
