
import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size() # bcz the display og monitor could be greater than camera frame 
index_y = 0
while True:
    _, frame = cap.read()       
    frame = cv2.flip(frame, 1)  # flip the frame on y axis because the image in mirored so move right so pixel  will be opposite 
    frame_height, frame_width, _ = frame.shape  # _ will be for left the third argument as it is
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # separating the colors  of hands and converting into RGB
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks             #21 different points on hand
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)     # *framewidth to get an bigger number and convert it into int beause if the number is mor accurate it will only click if the point(pixels) matches exactly 
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255)) # to create circle at index
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y

                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    print('outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)
                    elif abs(index_y - thumb_y) < 100:
                        pyautogui.moveTo(index_x, index_y)
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)