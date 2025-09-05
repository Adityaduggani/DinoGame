import cv2

from cvzone.HandTrackingModule import HandDetector 
from directkeys import PressKey, ReleaseKey
from directkeys import space_pressed
import time     
detector=HandDetector(detectionCon=0.8,maxHands=1)

space_key_pressed=space_pressed

time.sleep(2.0)
current_key_pressed=set()

video=cv2.VideoCapture(0)
while(True):
    ret,frame=video.read() 
    keyPressed=False 
    spacePressed=False 
    key_count=0 
    key_pressed=0
    
    hands,img=detector.findHands(frame)  

    cv2.rectangle(frame,(0,400),(200,480),(0,255,0),cv2.FILLED)
    cv2.rectangle(frame,(0,0),(200,80),(0,255,0),cv2.FILLED)
    if hands:
        lmList=hands[0]
        fingerUp=detector.fingersUp(lmList)
        print(fingerUp)
        if fingerUp==[0,0,0,0,0]:
            cv2.putText(frame,'FingerCount: 0',(20,460), cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame,'Dino Game',(20,50), cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),1,cv2.LINE_AA) 
            PressKey(space_key_pressed)
            spacePressed=True; 
            current_key_pressed.add(space_key_pressed)
            key_pressed=space_key_pressed
            keyPressed=True  
            key_count=key_count+1
        if fingerUp==[0,1,0,0,0]: 
            cv2.putText(frame,'FingerCount: 1',(20,460), cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),1,cv2.LINE_AA)
        if fingerUp==[0,1,1,0,0]:
            cv2.putText(frame,'FingerCount: 2',(20,460), cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),1,cv2.LINE_AA)
        if fingerUp==[0,1,1,1,0]:
            cv2.putText(frame,'FingerCount: 3',(20,460), cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),1,cv2.LINE_AA)
        if fingerUp==[0,1,1,1,1]:
            cv2.putText(frame,'FingerCount: 4',(20,460), cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),1,cv2.LINE_AA)
        if fingerUp==[1,1,1,1,1]:
            cv2.putText(frame,'FingerCount: 5',(20,460), cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),1,cv2.LINE_AA)
        if not keyPressed and len(current_key_pressed)!=0:
            for key in current_key_pressed:
                ReleaseKey(key)
            current_key_pressed=set()
        elif key_count==1 and len(current_key_pressed)==2:
            for key in current_key_pressed:
               if key!=key_pressed:
                    ReleaseKey(key)
            current_key_pressed=set()
            for key in current_key_pressed:
                ReleaseKey(key)
            current_key_pressed=set()

            
    cv2.imshow("My Video",frame)
    k=cv2.waitKey(1)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):

        break

video.release()
cv2.destroyAllWindows()
