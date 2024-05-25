import cv2
import autopy
import time
import numpy as np
import math
import mediapipe as mp
import streamlit as st
from PIL import Image

# Class definition for hand detection
class HandDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )
        self.mpDraw = mp.solutions.drawing_utils
        self.lmList = []
        self.wScr, self.hScr = autopy.screen.size()
        self.plocX, self.plocY = 0, 0

    # Method to find hands in the image
    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
                    lmList = []
                    for id, lm in enumerate(handLms.landmark):
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        lmList.append([id, cx, cy])
                    self.lmList = lmList
        return img

    # Method to detect fingers up
    def fingersUp(self):
        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[0]
            tipIds = [4, 8, 12, 16]
            fingers = []
            for id in tipIds:
                if hand.landmark[id].y < hand.landmark[id - 1].y:
                    fingers.append(1)
                else:
                    fingers.append(0)
            return fingers

    # Method to find distance between points
    def findDistance(self, p1, p2, img):
        if self.lmList:
            x1, y1 = self.lmList[p1][1:]
            x2, y2 = self.lmList[p2][1:]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            length = math.hypot(x2 - x1, y2 - y1)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            return length, img, [x1, y1, x2, y2, cx, cy]
        else:
            return None, img, None

def main():
    pTime = 0

    detector = HandDetector(detectionCon=0.5, trackCon=0.5)

    # Set page configuration
    im = "favicon/logo.png"
    st.set_page_config(
        page_title="Motion-Cue",
        page_icon=im,
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Create three columns
    col1, col2, col3 = st.columns([1, 2, 3])

    # Content in column 2 (center)
    with col2:
        # Markdown for the title
        st.markdown("""
            <div style='font-size: 130px; 
            font-family: Poppins, sans-serif;
            width: 1200px; margin-right:-20px; font-waight:700px;
            '>Virtual Mouse</div>
        """, unsafe_allow_html=True)

    
    col1, col2, col3 = st.columns([1, 2, 1])    

    with col2:    
        st.markdown("""
            <div style='font-size: 35px;font-align: center;
        font-family: Poppins, sans-serif; margin-left: 120px;
        justify-content: center; color: rgb(0, 0, 0);'>Click, set sail, explore!!</div>
        """, unsafe_allow_html=True)

        image_path = "favicon/abc.png"
        image = Image.open(image_path)

        col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        st.image(image, caption='', use_column_width=True)


        # Button to start tracking
    with col2:    
        start_button = st.button("Launch Virtual Pointer 👆")
        placeholder = st.empty()

        if start_button:
            # Video capture setup
            cap = cv2.VideoCapture(0)
            wCam, hCam = 640, 480
            cap.set(3, wCam)
            cap.set(4, hCam)

            frameR = 100  # Frame Reduction
            smoothening = 7  # Increase smoothening factor

            while True:
                success, img = cap.read()
                if not success:
                    break

                img = cv2.flip(img, 1)
                img = detector.findHands(img)

                lmList = detector.lmList
                if len(lmList) != 0:
                    x1, y1 = lmList[8][1:]
                    x2, y2 = lmList[12][1:]

                    fingers = detector.fingersUp()

                    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                                  (255, 0, 255), 2)

                    if fingers is not None:  # Check if fingers is not None
                        if fingers[1] == 1 and fingers[2] == 0:
                            x3 = np.interp(x1, (frameR, wCam-frameR), (0, detector.wScr))
                            y3 = np.interp(y1, (frameR, hCam-frameR), (0, detector.hScr))

                            clocX = x3
                            clocY = y3

                            clocX = detector.plocX + (clocX - detector.plocX) / smoothening
                            clocY = detector.plocY + (clocY - detector.plocY) / smoothening

                            autopy.mouse.move(clocX, clocY)
                            detector.plocX, detector.plocY = clocX, clocY

                        if fingers[1] == 1 and fingers[2] == 1:
                            length, img, lineInfo = detector.findDistance(8, 12, img)
                            if length < 40:
                                autopy.mouse.click()

                        if fingers[1] == 1 and fingers[2] == 0:
                            # Find distance between fingers
                            length, img, lineInfo = detector.findDistance(4, 20, img)

                            # Click mouse if distance short
                            if length < 40:
                                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                                autopy.mouse.click(button=autopy.mouse.Button.RIGHT)

                cTime = time.time()
                fps = 1 / (cTime - pTime)
                pTime = cTime

                placeholder.image(img, channels="BGR", use_column_width=True)
                st.write(f"FPS: {int(fps)}")


if __name__ == "__main__":
    main()
