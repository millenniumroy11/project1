
from django.shortcuts import render,HttpResponseRedirect, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm , SetPasswordForm
from django.contrib import messages
from .models.category import Category
from .models.product import Product
from django.contrib.auth import authenticate, login , logout , update_session_auth_hash
from django.views import View

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def signup(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
                fm.save()
                messages.success(request,'Account Created Successfully !!')
                return redirect("signup.html")
        #if SignUpForm().isExists():
            #messages.warning(request, "Email already exists")
        #return redirect ("signup.html")
        #else:
            
            
    else:
        fm = SignUpForm()
    return render(request,'signup.html',{'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request , data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'Logged in Successfully !!')
                    return HttpResponseRedirect('profile.html')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form':fm})

    else:
        return HttpResponseRedirect('profile.html')

def profile(request):
    if request.user.is_authenticated:
        return render(request , 'profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('login.html')


def changepass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user , data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request , fm.user)
                messages.success(request,'Password Changed Successfully!!')
                return HttpResponseRedirect('profile.html')
        else:        
            fm = SetPasswordForm(user=request.user)
        return render(request, 'changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('login.html')

class Category_list(View):
    
    def post(self ,request):
        product = request.POST.get('product')
        print(product)
        


    def get(self ,request):
        products = None
        categories = Category.get_all_categories()
        categoryId = request.GET.get('category')
        if categoryId:
            products = Product.get_all_products_by_categoryid(categoryId)
        else:
            products = Product.get_all_products()
        context = {'products':products , 'categories':categories}
        return render(request , 'categories.html' , context)



