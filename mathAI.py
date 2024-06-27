import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import google.generativeai as genai
from PIL import Image
import streamlit as st

st.set_page_config(layout="wide")
st.image("pi.jpg")

col1,col2=st.columns([2,1])
with col1:
    run=st.checkbox('Run',value=True)
    FRAME_WINDOW=st.IMAGE([])




genai.configure(api_key="AIzaSyA9Skj7ZEjB6SGLBObNpwfi0zbHRPzgW6Q")
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize the webcam to capture video
# The '2' indicates the third camera connected to your computer; '0' would usually refer to the built-in camera
cap = cv2.VideoCapture(0)

cap.set(4,720)

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

def getHandInfo(img):
    # Find hands in the current frame
    # The 'draw' parameter draws landmarks and hand outlines on the image if set to True
    # The 'flipType' parameter flips the image, making it easier for some detections
    hands, img = detector.findHands(img, draw=True, flipType=True)

    # Check if any hands are detected
    if hands:
        # Information for the first hand detected
        hand = hands[0]  # Get the first hand detected
        lmList = hand["lmList"]  # List of 21 landmarks for the first hand
        # Count the number of fingers up for the first hand
        fingers = detector.fingersUp(hand)
        print(fingers)
        return fingers,lmList
    else:
        return None

def draw(info,prev_pos,canvas):
    fingers,lmList=info
    current_pos=None

    if fingers==[0,1,0,0,0]:
        current_pos = tuple(map(int, lmList[8][0:2]))

        if prev_pos is None:
            prev_pos=current_pos

        if current_pos and prev_pos:
            cv2.line(canvas, prev_pos, current_pos, (255, 0, 255), 10)
        prev_pos = current_pos  # Update prev_pos to current_pos for next frame

    elif fingers==[1,0,0,0,0]:
        canvas = np.zeros_like(img)
    else:
        prev_pos = None  # Reset prev_pos when the finger is lifted

    return prev_pos, canvas


def sendToAI(model,canvas,fingers):
    if fingers==[1,1,1,1,0]:
        pil_image=Image.fromarray(canvas)
        response=model.generate_content(["Solve this Math Problem",pil_image])
        print(response.text)





prev_pos=None
canvas=None

# Continuously get frames from the webcam
while True:

    # Capture each frame from the webcam
    # 'success' will be True if the frame is successfully captured, 'img' will contain the frame
    success, img = cap.read()
    img=cv2.flip(img,1)

    if canvas is None:
        canvas=np.zeros_like(img)

    info=getHandInfo(img)
    if info:
        fingers,lmlist=info
        print(fingers)
        prev_pos, canvas = draw(info, prev_pos, canvas)
        sendToAI(model,canvas,fingers)

    image_combined=cv2.addWeighted(img,0.7,canvas,0.3,0)



    # Display the image in a window
    # cv2.imshow("Image", img)
    cv2.imshow("Canvas", canvas)
    cv2.imshow("image_combined", image_combined)


    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    cv2.waitKey(1)
