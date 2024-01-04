from django.shortcuts import render,redirect
from nameapp.models import product_Db,category_Db
from frontend.models import contact_Db,registration_Db,cart_Db,CheckoutDB
from django.contrib import messages

# Create your views here.
def homepage(req):
    pro=product_Db.objects.all()
    cat=category_Db.objects.all()
    return render(req,"homepage.html",{"pro":pro,"cat":cat})
def products(req,catname):
    cat=category_Db.objects.all()
    pro=product_Db.objects.filter(category=catname)
    return render(req,"products.html",{"pro":pro,"cat":cat})
def about_page(req):
    cat=category_Db.objects.all()
    return render(req,"about_page.html",{"cat":cat})
def blog_page(req):
    cat = category_Db.objects.all()
    return render(req, "blog_page.html", {"cat": cat})

def contact_page(req):
    cat = category_Db.objects.all()
    return render(req, "contact_page.html", {"cat": cat})
def contact_post(req):
    if req.method=="POST":
        a=req.POST.get("name")
        b=req.POST.get("email")
        c=req.POST.get("subject")
        d=req.POST.get("message")
        obj=contact_Db(name=a,email=b,subject=c,message=d)
        obj.save()
        return redirect(contact_page)
def single_product(req,p_id):
   pro=product_Db.objects.get(id=p_id)
   return render(req, "single_product.html",{"pro":pro})

def userloginpage(req):
    return render(req, "userloginpage.html")

def userloginpost(req):
    if req.method == "POST":
        a = req.POST.get("name")
        b = req.POST.get("email")
        c = req.POST.get("password")
        d = req.POST.get("cpassword")
        obj = registration_Db(NAME=a, EMAIL=b, PASSWORD=c, CPASSWORD=d)
        obj.save()
        return redirect(userloginpage)

def userlogin(request):
    if request.method == "POST":
        ab = request.POST.get("name")
        bc = request.POST.get("password")
        if registration_Db.objects.filter(NAME=ab, PASSWORD=bc).exists():
            request.session["NAME"] = ab
            request.session["PASSWORD"] = bc
            messages.success(request,"Welcome")
            return redirect(homepage)
        else:
            messages.error(request, "invalid username or password..")
            return redirect(userloginpage)
    else:
        return redirect(userloginpage)

def userlogout(request):
    del request.session['NAME']
    del request.session['PASSWORD']
    return redirect(userloginpage)
def cartpost(request):
    if request.method == "POST":
        usrnm = request.POST.get("usrname")
        productnm = request.POST.get("proname")
        productprice = request.POST.get("proprice")
        Quant = request.POST.get("qnty")
        TotalPr = request.POST.get("totalprice")
        obj = cart_Db(username=usrnm, productname=productnm, price=productprice, quantity=Quant, totalprice=TotalPr)
        obj.save()
        messages.success(request, "Added to Cart Successfully")
        return redirect(homepage)



def cartpage(request):
    data=cart_Db.objects.filter(username=request.session['NAME'])
    cat = category_Db.objects.all()

    return render(request,"mycart.html",{"data":data,"cat":cat})
def Checkout(request):
    categories =category_Db.objects.all()
    cart = cart_Db.objects.filter(username=request.session['NAME'])
    total_price = 0
    for i in cart:
        total_price = total_price + i.totalprice
    return render(request, 'Checkout.html', {'cart':cart, 'total_price':total_price, 'categories':categories})

def CheckoutDBsave(request):
    if request.method == "POST":
        nmfirst = request.POST.get('firstname')
        nmlast = request.POST.get('lastname')
        countr = request.POST.get('country')
        addr = request.POST.get('address')
        city1 = request.POST.get('city')
        pncode = request.POST.get('pincode')
        mob = request.POST.get('mobile')
        Em = request.POST.get('email')
        obj = CheckoutDB(firstnm=nmfirst, lastnm=nmlast, country=countr, address=addr, city=city1, pincode=pncode,phone=mob, email=Em)
        obj.save()
        messages.success(request, "Order Placed Successfully")
        return redirect(Checkout)

