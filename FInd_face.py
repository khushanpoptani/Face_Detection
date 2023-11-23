import base64
import cv2
import face_recognition
import mysql.connector as sql
import os

def create_db(cursor):
    cursor.execute("CREATE DATABASE IF NOT EXISTS Face_Detection")
    cursor.execute("USE face_detection")
    cursor.execute("CREATE TABLE IF NOT EXISTS Face_data(S_No INT UNIQUE, Person_Name VARCHAR(30) NOT NULL, Age INT NOT NULL, Face_info LONGTEXT NOT NULL)")
    mydb.commit()

def get_face(cursor):
    cmd = "SELECT * FROM face_data"
    cursor.execute(cmd)
    db_face_data = cursor.fetchall()
    return db_face_data

def find_face(face_cascade, db_face, skip_interval):
    video_capture = cv2.VideoCapture(0)

    frame_count = 0

    while True:
        ret, frame = video_capture.read()

        if frame_count % skip_interval == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_coord = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

            for num, (x, y, w, h) in enumerate(face_coord):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)
                crop_face = frame[y:y + h, x:x + w]

                test_face_encoding = face_recognition.face_encodings(crop_face)

                for i, db_entry in enumerate(db_face):
                    img = db_entry[3]
                    binary_data = base64.b64decode(img)
                    open("db.jpg", "wb").write(binary_data)

                    known_face_encoding = face_recognition.face_encodings(cv2.imread("db.jpg"))

                    try:
                        os.remove("db.jpg")
                    except OSError as e:
                        print(f"Error: {e}")

                    if known_face_encoding and test_face_encoding:
                        is_same = face_recognition.compare_faces([known_face_encoding[0]], test_face_encoding[0])

                        if is_same:
                            distance = face_recognition.face_distance([known_face_encoding[0]], test_face_encoding[0])
                            distance = round(distance[0] * 100)

                            accuracy = 100 - round(distance)

                            if accuracy >= 60:
                                cv2.putText(frame, db_entry[1], (x, y + h + 15),
                                            cv2.FONT_HERSHEY_SIMPLEX,
                                            0.75, (2, 2, 2), 2)
                                print("Accuracy:", accuracy)
                        else:
                            print("No match")

            cv2.imshow("frame", frame)

        frame_count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    mydb = sql.connect(host="localhost", user="root", passwd="toor")
    face_cascade = cv2.CascadeClassifier('P:\Projects\Project_P\Projects\Face_recog\Open_CV\haarcascade_frontalface_default.xml')
    cursor = mydb.cursor()

    create_db(cursor)
    db_face = get_face(cursor)

    skip_interval = 7

    find_face(face_cascade, db_face, skip_interval)
