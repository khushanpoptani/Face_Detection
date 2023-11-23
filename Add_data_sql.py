import base64, cv2
import os

import mysql.connector as sql


mydb = sql.connect(host="localhost",user="root",passwd="toor")
face_cascade = cv2.CascadeClassifier('P:\Projects\Project_P\Projects\Face_recog\Open_CV\haarcascade_frontalface_default.xml')


cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS Face_Detection")
cursor.execute("use face_detection")
cursor.execute("create table if not exists Face_data(S_No int unique ,Person_Name varchar(30) not null ,Age int NOT NULL, Face_info longblob not null)")
mydb.commit()


def db_input(serial_number ,name ,age ,face_data):
    arg = (serial_number, name, age, face_data)
    Data = "insert into Face_data values(%s, %s, %s, %s)"
    cursor.execute(Data, arg)
    mydb.commit()

def get_face():
    cmd = "select * from face_data"
    cursor.execute(cmd)
    data = cursor.fetchall()

    img = data[0][3]
    binary_data = base64.b64decode(img)
    img = open("try2.png", "wb").write(binary_data)
    return data



def upload_face(face_cascade):
    name = input("Enter your name -: ")
    age = int(input("enter your age -: "))
    photo = input("Enter location of your photo with name and extension-: ")

    face_photo = cv2.imread(photo)
    gray = cv2.cvtColor(face_photo, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(faces)
    for (x, y, w, h) in faces:
        cv2.imwrite("try.png", face_photo[y:y+h, x:x+w])

        crop_img = open("try.png", 'rb').read()
        crop_img = base64.b64encode(crop_img)



        db_input(len(get_face())+1, name, age, crop_img)
        os.remove("try.png")





#print(get_face()[2])


upload_face(face_cascade)

