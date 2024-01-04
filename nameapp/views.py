from django.shortcuts import render,redirect
from nameapp.models import category_Db,product_Db
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from frontend.models import contact_Db
from django.contrib import messages



# Create your views here.
def main_page(request):
    return render(request,"main_page.html")
def manager_page(req):
    return render(req,"manager_page.html")
def manager_post(request):
    if request.method=="POST":
        a=request.POST.get("name")
        b=request.POST.get("description")
        c=request.FILES["image"]
        obj=category_Db(name=a,description=b,image=c)
        obj.save()
        messages.success(request,"Added successfully..")
        return redirect(manager_page)
def manager_table(req):
    data=category_Db.objects.all()
    return render(req,"manager_table.html",{"data":data})

def manager_edit(req,c_id):
    category=category_Db.objects.get(id=c_id)
    return render(req,"manager_edit.html",{"category":category})


def manager_update(req,c_id):
    if req.method=="POST":
        a=req.POST.get("name")
        b=req.POST.get("description")
        try:
            img=req.FILES["image"]
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = category_Db.objects.get(id=c_id).image
    category_Db.objects.filter(id=c_id).update(name=a,description=b,image=file)
    return redirect(manager_table)
def manager_delete(req,c_id):
    data=category_Db.objects.get(id=c_id)
    data.delete()
    messages.error(req, "deleted  Successfully")

    return redirect(manager_table)
def product_page(req):
    data=category_Db.objects.all()
    return render(req,"product_page.html",{"data":data})
def product_post(req):
    if req.method=="POST":
        a=req.POST.get("category")
        b=req.POST.get("name")
        c=req.POST.get("price")
        d=req.POST.get("description")
        e=req.FILES["image"]
        obj=product_Db(category=a,name=b,price=c,description=d,image=e)
        obj.save()
        messages.success(req, "Added successfully..")
        return redirect(product_page)
def product_table(req):
    data=product_Db.objects.all()
    return render(req,"product_table.html",{"data":data})

def product_edit(req,p_id):
    cat=category_Db.objects.all()
    product=product_Db.objects.get(id=p_id)
    return render(req,"product_edit.html",{"cat":cat,"product":product})



def product_update(req,p_id):
    if req.method == "POST":
        a = req.POST.get("category")
        b = req.POST.get("name")
        c = req.POST.get("price")
        d = req.POST.get("description")
        try:
            img=req.FILES["image"]
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = product_Db.objects.get(id=p_id).image
    product_Db.objects.filter(id=p_id).update(category=a,name=b,price=c,description=d,image=file)
    return redirect(product_table)
def product_delete(req,p_id):
    data=product_Db.objects.get(id=p_id)
    data.delete()
    messages.error(req, "deleted  Successfully")
    return redirect(product_table)
def login_page(req):
    return render(req,"login_page.html")
def Adminlogin(request):
    if request.method=="POST":
        ab=request.POST.get('name')
        bc=request.POST.get('password')

        if User.objects.filter(username__contains=ab).exists():
            x=authenticate(username=ab,password=bc)
            if x is not None:
                login(request,x)
                messages.success(request,"loged in successfully..")
                request.session['username']=ab
                request.session['password']=bc
                return redirect(main_page)
            else:
                messages.error(request, "invalid username or password..")
                return redirect(login_page)
        else:
            return redirect(login_page)

def AdminLogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_page)
def contact_table(req):
    data=contact_Db.objects.all()
    return render(req,"contact_table.html",{"data":data})
def contact_delete(req,c_id):
    data=contact_Db.objects.get(id=c_id)
    data.delete()
    return redirect(contact_table)

