from firebase import firebase
from dotenv import load_dotenv
import request
import os
load_dotenv()
firebaseInfo = os.getenv("FIREBASE_DB")
firebase = firebase.FirebaseApplication(firebaseInfo, None)
