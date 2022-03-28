from django.shortcuts import render
import smtplib

# Create your views here.
def hello(request):
    if request.method=="POST":

        mail=request.POST['emails']
        count=request.POST['counts']
        con=request.POST['contents']
        
        obj = smtplib.SMTP('smtp.gmail.com', 587)
        obj.starttls()
        obj.login('buyitofficial8000@gmail.com', '6379808599')
        for i in range(int(count)):
            obj.sendmail('buyitofficial8000@gmail.com',mail,con )
        print("mail sent")       
        return render(request,"tem1/hello.html")
    return render(request,"tem1/hello.html")