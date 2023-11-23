# Face Detection

This is a face Dtecton tool used to Detect faces.



## Technologies Used

- Python
- MySQL


## Usage

This is a raw code and can be used any where with some modification and changes. Face detection is a computer vision task that involves locating and identifying faces in images or video. It has various practical applications across different domains. Here are some common uses of face detection:

1. **Biometric Security:**
   - **Facial Recognition:** Face detection is a crucial component in facial recognition systems. It helps identify and verify individuals based on their facial features. This is widely used in security systems, access control, and authentication processes.

2. **Surveillance and Security:**
   - **CCTV Monitoring:** Face detection is used in video surveillance systems to monitor crowded places, airports, public events, and streets. It aids in identifying and tracking individuals for security purposes.

3. **User Authentication:**
   - **Smartphones and Computers:** Many modern devices use face detection for user authentication. This can replace or complement traditional methods like passwords or PINs, providing a convenient and secure way to access devices.

4. **Photography and Social Media:**
   - **Auto-Focus and Image Enhancement:** In photography, face detection helps cameras focus on human faces to ensure clear and sharp images. It is also used in smartphones for features like portrait mode and beautification.
   - **Social Media Tagging:** Platforms like Facebook and Instagram use face detection to automatically tag people in photos.

5. **Marketing and Analytics:**
   - **Customer Analysis:** In retail, face detection can be used to analyze customer demographics, track customer movements in stores, and measure the effectiveness of marketing campaigns.
   - **Digital Signage:** Face detection can be employed to tailor digital signage content based on the demographics of the audience in real-time.

6. **Healthcare:**
   - **Patient Monitoring:** Face detection can be used in healthcare for patient monitoring, ensuring that the right patient receives the right treatment by matching their identity through facial recognition.

7. **Human-Computer Interaction:**
   - **Gaming and Virtual Reality:** Face detection is used in gaming and virtual reality to track facial expressions, enabling more immersive and interactive experiences.

8. **Law Enforcement:**
   - **Criminal Identification:** Law enforcement agencies use face detection to identify and track individuals in surveillance footage. This can aid in solving crimes and locating suspects.

9. **Emotion Analysis:**
   - **Human-Computer Interaction:** Face detection can be combined with emotion analysis to understand facial expressions. This is useful in human-computer interaction scenarios, such as virtual assistants that respond to users' emotions.

10. **Education:**
    - **Attendance Tracking:** Face detection can be used in educational institutions for automated attendance tracking, making the process more efficient.

Face detection, when combined with other technologies like facial recognition and emotion analysis, opens up a wide range of possibilities in diverse fields, improving security, efficiency, and user experience. However, it also raises ethical and privacy concerns, and it's essential to implement these technologies responsibly and in compliance with privacy regulations.

### Prerequisites

- Python 3.9 (because it is hard to install face recognition in above version)
- MySQL Server

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command: `https://github.com/Thunder1409/Face_Detection.git`


### Step 2: Install Requirements

Navigate to the project directory and use pip to install all requirements for the project. Execute the following command:
`pip install MySQL-python`
`pip install opencv-python`
`pip install face-recognition`
`pip install os-sys`

### Step 3: Changing database credentials

After installing all the modules open Add_Face.py and Face_Detection.py and change the credentials for MySQL Server.


### **Working (LOGIC)** 

Add_Face.py is used to enter there face data with name, serial number and age. In server a passport size photo is upload in the form of binary (blob) data to keep he records.

Face_Detection.py is used to detect the face, mark the face and print the name of the user if users data is stored in MySQL.

Open Cv is used to find faces, mark them and print the name.Face recognition is used to compare the face and find the accuracy of the face matched from the user to the database. 

