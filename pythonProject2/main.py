
import matplotlib.pyplot as plt

import  pyrebase

firebaseConfig = {"apiKey": "AIzaSyCfuQ46q09FozGesUxT3ZakA_7XhGrnrUM",
  "authDomain": "fir-course-56a13.firebaseapp.com",
  "projectId": "fir-course-56a13",
  "storageBucket": "fir-course-56a13.appspot.com",
  "messagingSenderId": "447378702514",
  "appId": "1:447378702514:web:f15e3623cec16a1d3949ab",
  "databaseURL": "https://fir-course-56a13-default-rtdb.firebaseio.com/"
  }

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

elapsedtime = db.child("ECG1").child("Elapsed time").get()
abdomenlist = db.child("ECG1").child("Abdomen_1").get()

plt.title("ECG graph")
plt.xlabel("Elapsed Time")
plt.ylabel("Abdomen")
plt.plot(elapsedtime.val(), abdomenlist.val(), color="blue")
plt.show()



