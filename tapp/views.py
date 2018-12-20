from django.shortcuts import *
from tapp.views import *
from .forms import *
from .models import *
from django.contrib import auth
from django.http import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'index.html')
def gallery(request):
    return render(request,'gallery.html')
def gallery2(request):
    return render(request,'gallery2.html')
def gallery3(request):
    return render(request,'gallery3.html')
def gallery4(request):
    return render(request,'gallery4.html')
def gallery5(request):
    return render(request,'gallery5.html')
def gallery6(request):
    return render(request,'gallery6.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def menu(request):
    category1=Categories.objects.all()
    default_category='cakes'
    all_products=Products.objects.filter(category__slug=default_category)

    return render(request,'menu.html',{'cat':category1,'pro':all_products,'p':default_category})
def item2(request,slug):
    print(slug)
    category1=Categories.objects.all()
    all_products=Products.objects.filter(category__slug=slug)
    #return HttpResponse('hello')
    return render(request,'menu1.html',{'cat':category1,'pro':all_products,'p':slug})

def carts(request):
    all_items=Cart.objects.all()
    total=[]
    for i in all_items:
        total.append(i.total_price)
    return render(request,'cart.html',{'all':all_items,
                                       'total':sum(total)})


def detail(request,s):
    all_items = Products.objects.get(id=s)
    if request.method == 'POST':
        form = cart(request.POST)
        all_it=Cart.objects.all()
        cart_data={}
        for i in all_it:
            cart_data[i.product.id]={'about':i.product,
                                       'quantity':i.quantity}
        q=request.POST['quantity']
        a=request.POST['about']
        if int(q)>0:
            if form.is_valid():
                if int(s) in cart_data.keys():
                    c=Cart.objects.get(product__id=s)
                    c.quantity +=int(q)
                    c.total_price += float(c.product.price) * float(q)
                    c.save()
                else:
                    f=form.save(commit=False)
                    f.product=all_items
                    f.quantity=q
                    f.about=a
                    f.total_price=float(all_items.price) * float(q)
                    f.save()
                return HttpResponseRedirect('/cart/')
        else:
            return HttpResponseRedirect('/INVALID/')
    else:
        form=cart()
    return render(request,'detail.html',{'d':all_items,'form':form})


def Delete(request,d):
    item=Cart.objects.get(id=d)
    item.delete()
    return HttpResponseRedirect('/cart/')


def bloghome(request):
    return render(request,'blog-home.html')
def blogsingle(request):
    return render(request,'blog-single.html')
def login(request):
    return render(request,"login.html")
def logout(request):
    return HttpResponseRedirect("/")
def sign_up(request):
    if request.method=="POST":
        form=Reg_form(request.POST,request.FILES)
        if form.is_valid():
            cd=form.cleaned_data
            print(cd)
            u=User.objects.create_user(username=cd['username'],email=cd['email'],
                                     password=cd['password'])

            u.save()
            return HttpResponseRedirect('/login/')
    else:
        form=Reg_form()
    return render(request,"login.html",{'form':form})

def order(request):
    print('hi')
    if request.method=="POST":
        form=ord(request.POST)
        print('1')
        if form.is_valid():

            cd=form.cleaned_data
            subject='sagar bakery'
            msg='thanks for ordering order confirmed'
            send_mail(subject,msg,'soni.ankita2004@gmail.com',[cd['e']]) #email is fetched from the checkout form that customer is submited

            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/last/')
    else:
        form=ord()
    return render(request,'order.html',{'form':form})

def last(request):
    return render(request,'last.html')

def auth_view(request):
    #print request.POST,type(request)
    username=request.POST['username']
    password=request.POST['password']
    #match username & password
    #if not match,authenticate() will return None
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/')
    else:
        return render(request,'login.html',{'msg':'invalid password'})
def customize(request):
    print('hi')
    if request.method =="POST":
        form=cust(request.POST)
        print('1')
        if form.is_valid():
            print(4)

            cd=form.cleaned_data
            subject='sagar bakery'
            msg='your enquiry has been received,we will reply you soon'
            send_mail(subject,msg,'sonianki2004@gmail.com',[cd['em']])
            #subject='sagar bakery'
            #msg='your enquiry has been received,we will reply you soon'
            #send_mail(subject,msg,'sonianki2004@gmail.com',[cd['em']]) #email is fetched from the checkout form that customer is submited

            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=cust()
        print('invalid details')
    return render(request,'customize.html',{'form':form})



def faq(request):
    return render(request,'faq.html')
