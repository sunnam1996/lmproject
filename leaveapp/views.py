from django.shortcuts import render
from django.http import HttpResponse
from .models import register
def home(request):
    return render(request,"home.html")
def reg(request):
    return render(request,"empreg.html")
def regi(request):

    b=request.POST["UserName"]
    c=request.POST["FirstName"]
    d=request.POST["LastName"]
    e=request.POST["Gender"]
    f=request.POST["DateOfjoin"]
    g=request.POST["Email"]
    h=request.POST["MobileNumber"]
    i=request.POST["Password"]
    j=request.POST["ConfirmPassword"]
    sa = register(UserName=b,FirstName=c,LastName=d,Gender=e,DateOfjoin=f,Email=g,MobileNumber=h,Password=i,ConfirmPassword=j)
    sa.save()
    return render(request,'login.html')
def log(request):
    if request.method == 'POST':
        user = request.POST['uname']
        pwd = request.POST['pwd']
        m=register.objects.get(UserName=user,Password=pwd)
        if m:
                return HttpResponse('<html> <body> login success</body></html>')
        else:
                return HttpResponse('invalid username/password')
    else:
        return render(request,'login.html')

