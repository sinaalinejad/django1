from django.shortcuts import render
from django.http.response import HttpResponse
from .models import *
# Create your views here.
current_user=None
def home(request):
    return render(request,"home.html")
def main1(request):
    if request.method=="GET":
        return HttpResponse("you should go to home page")
    if request.method=="POST":
        a = customer.objects.create(tell_num=request.POST["shomare"],address=request.POST["adres"],baz_type=request.POST["noe"],baz_num=request.POST["teedad"],price=request.POST["gheimat"])
        customers=customer.objects.all()
        context={"customers":customers,"firstname":current_user.firstname,"lastname":current_user.lastname}
        return render(request,"main1.html",context=context)



def main(request):
    if request.method=="GET":
        return HttpResponse("you should go to home page")
    global current_user
    customers=customer.objects.all()
    user=User.objects.all()
    for item in user:
        if item.email==request.POST["email"] and item.password==request.POST["password"]:
            current_user=item
            context={"firstname":item.firstname,"lastname":item.lastname,"customers":customers}
            return render(request,"main.html",context=context)
    return HttpResponse("شما هنوز عضو نشده اید یا پسورد را اشتباه وارد کرده اید")
        
                



def index(request):
    if request.method=="GET":
        return render(request,'index.html')
    if request.method=="POST":
        if request.POST["password"]==request.POST["password_rep"]:
            list=User.objects.all()
            for model in list:
                if request.POST["email"]==model.email:
                    dic={"email_warn":"this email is already used"}
                    return render(request,'index.html',context=dic)
            user = User.objects.create(firstname=request.POST["firstname"],lastname=request.POST["lastname"],email=request.POST["email"],password=request.POST["password"],password_rep=request.POST["password_rep"])
        else:
            context={"pass_warn":"password_repeatation was not the same as password"}
            return render(request,'index.html',context=context)
        name={"firstname":request.POST["firstname"],"lastname":request.POST["lastname"]}
        return render(request,"success.html",context=name)




def form(request):
    if request.method=="GET":
        return render(request,'form.html')

        
        
        
        
