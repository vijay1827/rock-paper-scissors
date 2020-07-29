import os
import cv2
cam = cv2.VideoCapture(0)

a = int(input("Enter \n1 stone\n2 empty\n3 scissor\n4 paper\n------"))

cv2.namedWindow("img")
img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow('img', frame)
    if not ret:
        print("failed to grab frame")
        break

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("closing...")
        break


    elif k%256 == 32:
        # SPACE pressed
        if a == 1:
            for i in range(100):
                img_name = "stone_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1
                i+=1

        elif a == 2:
            for i in range(100):
                img_name = "empty_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1
                i+=1

        elif a == 3:
            for i in range(100):
                img_name = "scissor_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1
                i+=1

        else:
            for i in range(100):
                img_name = "papaer_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1
                i+=1


cam.release()

cv2.destroyAllWindows()
# write your code here to open your laptop's camera
# and store images for rock paper scissors

# I would highly recommend storing these images in folders stucture like below:
# training_data\
#           |-- empty\
#           |-- rock\
#           |-- paper\
#           |-- scissors\
# having a folder structure like this will make it easy for you to read the images while pre-processing
