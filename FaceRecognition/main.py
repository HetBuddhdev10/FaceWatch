import pickle
import face_recognition
import cv2
import numpy as np

videoPath = 'Resources/virenvideo.mp4'
cap = cv2.VideoCapture(videoPath)

cap.set(3, 640)
cap.set(4, 480)

imgBg = cv2.imread('Resources/backgroundimage.jpg')

#Loading file

file=open('Encodefile.p','rb')
encodeListKnownwithID = pickle.load(file)
file.close()

encodeListKnown , personID = encodeListKnownwithID

# print(personID)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    resized_frame = cv2.resize(frame, (640, 480))
    imgS = cv2.resize(frame,(0,0,),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    faceCurrentFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS,faceCurrentFrame)

    # Overlay the resized video frame onto the background image
    imgBg[162:162+480, 55:55+640] = resized_frame

    for encodeFace, faceLoc, in zip(encodeCurFrame,faceCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDistance = face_recognition.face_distance(encodeListKnown,encodeFace)

        matchIndex = np.argmin(faceDistance)
        print("matches",matches)
        print("facedistance",faceDistance)

        if matches[matchIndex]:
            print("Known face detected")

    # Display the result
    cv2.imshow('Video with Background', imgBg)




cap.release()



# import cv2
#
# videoPath = 'Resources/demovideo.mp4'
# cap = cv2.VideoCapture(videoPath)
#
# cap.set(3, 640)
# cap.set(4, 480)
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     resized_frame = cv2.resize(frame, (640, 480))
#
#     # Display the result without a background image
#     cv2.imshow('Video without Background', resized_frame)
#
#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break
#
# # Release the video capture object
# cap.release()
#
# cv2.destroyAllWindows()
