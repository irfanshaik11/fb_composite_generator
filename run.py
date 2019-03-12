import subprocess
import shutil
import os

source = '/Users/HabibullahShaik/Desktop/FaceGrab-master/facegrab/myfriends'
dest1 = '/Users/HabibullahShaik/Desktop/FaceGrab-master/accept'

subprocess.run(["rm", "-rf", "accept"])
subprocess.run(["mkdir", "accept"])

subprocess.run(["rm", "-rf", "facegrab/myfriends"])
subprocess.run(["mkdir", "facegrab/accept"])



subprocess.run(["python", "seleniumscraper.py"])

subprocess.run(["python", "facegrab.py"])


subprocess.run(["autocrop", "-i", "facegrab/myfriends", "-o", "accept", "-r", "reject", "-w", "400", "-H", "400", "--facePercent", "90"])

subprocess.run(["python3", "face_landmark_detection.py","shape_predictor_68_face_landmarks.dat", "accept"])

subprocess.run(["python3", "faceAverage.py"])
