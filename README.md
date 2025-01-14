# viral-fission-task
# Full Stack Application: Frontend on Firebase & Backend on AWS EC2

This project is a full-stack web application where the **frontend** is hosted on **Firebase** and the **backend** is hosted on **AWS EC2**. The frontend communicates with the backend via HTTP requests and displays data fetched from the backend.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Project Setup](#project-setup)
    - [Frontend Setup](#frontend-setup)
    - [Backend Setup](#backend-setup)
3. [Running the Application Locally](#running-the-application-locally)
4. [Deployment Steps](#deployment-steps)
    - [Frontend Deployment (Firebase)](#frontend-deployment-firebase)
    - [Backend Deployment (AWS EC2)](#backend-deployment-aws-ec2)
5. [Notes](#notes)

## Prerequisites
Before you begin, ensure that you have the following installed:
- [Firebase CLI](https://firebase.google.com/docs/cli) (for frontend deployment)
- [Python 3.x](https://www.python.org/downloads/) (for backend development on Ec2)
- [Flask](https://flask.palletsprojects.com/) (for backend framework)
- [Git](https://git-scm.com/) (for version control)


## Project Setup

### Backend Setup (AWS EC2 with Flask API)

1. **Launch an EC2 instance on AWS:**
   - Set up a Linux-based EC2 instance (e.g., Ubuntu or Amazon Linux).
   - Ensure the instance has access to port 5000 (used by Flask) in the Security Group settings.

2. **Install necessary dependencies on EC2:**
   - SSH into your EC2 instance and install Python and Flask:
     ```bash
     sudo apt update
     sudo apt install python3-pip
     pip3 install flask
     pip3 install flask-cors
     ```

3. **Create the Flask backend:**
   - On your EC2 instance, create a `app.py` file with the following content:
     ```python
     from flask import Flask, jsonify
     from flask_cors import CORS

     app = Flask(__name__)
     CORS(app)  # Enable CORS for all domains

     @app.route('/')
     def home():
         return jsonify({'message': 'Hello from AWS EC2 Backend!'})

     if __name__ == '__main__':
         app.run(host='0.0.0.0', port=5000)
     ```

4. **Run the Flask server:**
   - Start the Flask app on your EC2 instance by running:
     ```bash
     python3 app.py
     ```
   - Ensure the server is accessible by visiting `http://<your-ec2-public-ip>:5000` in your browser. You should see the JSON response `{"message":"Hello from AWS EC2 Backend!"}`.

5. **Test the backend with a curl command:**
   - You can test the backend by running the following command on your EC2 instance:
     ```bash
     curl http://65.2.57.41:5000/
     ```
   - You should receive the same JSON response: `{"message":"Hello from AWS EC2 Backend!"}`.

6. **Allow CORS in your Flask API:**
   - Make sure you have the `flask-cors` package installed and that CORS is enabled in your Flask app. This is essential for the frontend to communicate with the backend across different domains (Firebase frontend and EC2 backend).


### Frontend Setup (Firebase Hosting)

1. **Create a folder for your frontend application:**
   - You can create a folder manually where you want to store your frontend files.

2. **Inside the folder, create your frontend files (e.g., `index.html`, `styles.css`):**
   - Your `index.html` will contain the structure and logic to connect with your backend API (running on AWS EC2).
   - You can style it with `styles.css` and write JavaScript to fetch data from the backend.
  
### Frontend-Backend Communication

1. **Update the frontend JavaScript:**
   - In your `index.html`, ensure that your JavaScript fetches data from the backend:
     ```javascript
     async function fetchData() {
         const response = await fetch('http://65.2.57.41:5000/');
         const data = await response.json();
         document.getElementById('response').textContent = data.message;
     }
     fetchData();
     ```

2. **Test the entire system:**
   - Once your frontend is deployed to Firebase and your backend is running on EC2, you can test the system by visiting your Firebase URL in a browser.
   - The frontend should display "Hello from AWS EC2 Backend!" fetched from the backend.

### Applicaton Deployment
1. **Install Firebase CLI (if not installed):**
   - Open your terminal and install the Firebase CLI globally:
     ```bash
     npm install -g firebase-tools
     ```

2. **Login to Firebase:**
   - Run the following command to authenticate with Firebase:
     ```bash
     firebase login
     ```

3. **Initialize Firebase Hosting:**
   - In your project folder, run:
     ```bash
     firebase init
     ```
   - Select **Hosting** and choose the Firebase project you want to deploy to.
   - When prompted, specify the folder to deploy (e.g., `public` if you placed your frontend files there).
   - Make sure to choose **No** when asked about configuring as a Single Page App, unless you are building a SPA.

4. **Deploy to Firebase Hosting:**
   - To deploy your frontend to Firebase Hosting, run:
     ```bash
     firebase deploy
     ```
   - This will upload your files to Firebase and provide you with a URL where your frontend will be live.

7. **Access your live website:**
   - After the deployment, you will receive a unique URL to access your hosted frontend on Firebase.



### Conclusion

This setup connects your frontend hosted on Firebase with a backend hosted on AWS EC2. You have successfully:

- Set up Firebase Hosting for your frontend.
- Set up an AWS EC2 instance with Flask for your backend.
- Configured CORS in your Flask app to allow communication between the frontend and backend.

Enjoy developing and deploying your web application!
