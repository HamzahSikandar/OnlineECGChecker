from django.shortcuts import render,HttpResponse
import pyrebase
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from .utils import get_plt
# Create your views here.
config={
  "apiKey": "AIzaSyDbqs8dKsNKq3HNsnC5f-XT1Z9PLaNc0AY",
  "authDomain": "ecg-demo.firebaseapp.com",
  "databaseURL": "https://ecg-demo-default-rtdb.firebaseio.com",
  "projectId": "ecg-demo",
  "storageBucket": "ecg-demo.appspot.com",
  "messagingSenderId": "775853856576",
  "appId": "1:775853856576:web:ecd9d6dd63faae36e14ca5",
  "measurementId": "G-1KWM9HTDRJ"
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def index(request):
    try:
        return render(request,'index.html')
    except:
        return HttpResponse("Erorr 404 !!")
def get_data(request):
    try:
        if request.method=="POST":
            id=request.POST['id_no']
            name=database.child('Patent').child(id).shallow().get().val()
            em_list=[]
            for i in name:
                em_list.append(database.child('Patent').child(id).child(i).get().val())
            x_axis=[]
            y_axis=[]
            i=0
            for j in em_list:
                # y=j/10
                # i+=1
                x_axis.append(j)
                # y_axis.append(y)
    except:
        return HttpResponse("Please enter Patent Id Again")
    try:

        chart=get_plt(x_axis)

        # plt.plot(y_axis,x_axis)
        # plt.show()


        context={'chart':chart}
        return render(request,'report.html',context)
    except:
        return HttpResponse("Your graph is not avalable here")
    
    