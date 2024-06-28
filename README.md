# Gesture-Based Drawing for Math Problems

This project is a gesture-based drawing application that enables users to draw mathematical diagrams and equations on a virtual canvas using hand gestures. The application uses OpenCV, MediaPipe, and Streamlit 
for real-time hand tracking and interactive UI, providing an intuitive and interactive way to create math problems.

*Table of Contents*

- Installation
- Usage
- Features
- How It Works
- Contributing
- License

## Installation
To run this project on your local machine, follow these steps:

Clone the repository: git clone git@github.com:pantpujan017/Maths-with-Gestures-using-AI-.git

Navigate to the project directory: cd Maths-with-Gestures-using-AI

Install dependencies using pip: pip install -r requirements.txt

## Usage
Run streamlit run mathAI.py on terminal.
Once the application is running, use your index finger to draw on the virtual canvas. The system will track your hand movements in real-time and send it to AI for solutions.

## Features
Real-time hand tracking using MediaPipe
Gesture-based drawing on a virtual canvas
Creation of mathematical diagrams and equations
Interactive UI with Streamlit

## How It Works
OpenCV: For capturing video from the webcam and drawing on the canvas.
MediaPipe: For real-time hand detection and tracking.
Hand Tracking Module: A custom module to detect hands, find landmarks, and determine the state of fingers.
Streamlit: For creating an interactive web application interface.

## Contributing
Contributions to this project are welcome and encouraged! If you want to contribute to the project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.

Final Image of the project
![Screenshot 2024-06-23 161505](https://github.com/pantpujan017/Maths-with-Gestures-using-AI-/assets/173246130/f25bd2c3-27e9-41fe-a22e-11c92390d6b6)




## License
This project is licensed under the MIT License. See the LICENSE file for details.
