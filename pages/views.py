from django.shortcuts import render, redirect 
from .models import Signup, Product1, Product2
from .forms import LogInForm 
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def Home(request):
    return render(request, "pages/home.html")


def Shopnow(request):
    scarfs = Product1.objects.all()
    # print(scarfs[0])
    context = {"scarfs": scarfs }
    return render(request, "pages/shopnow.html", context)


# def Login(request):
#     return render(request, "pages/login.html")
def Login(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            Email = form.cleaned_data["Email"]
            Password = form.cleaned_data["Password"]
            user = Signup.objects.filter(Email=Email, Password=Password).first()
            if user:
                # set user session
                request.session["user_id"] = user.id
                return redirect("hali")
            else:
                # invalid login
                return render(
                    request,
                    "pages/login.html",
                    {"form": form, "error": "Invalid login credentials."},
                )
    else:
        form = LogInForm()
        return render(request, "pages/login.html", {"form": form})


def signup(request):
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    address = request.POST.get("address")
    password = request.POST.get("password")
    username = request.POST.get("username")
    data = Signup(
        Email=email, Phone=phone, Address=address, Password=password, Username=username
    )
    
    data.save()
    return render(request, "pages/signup.html")

def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('login')
    

def cart(request):
       # Get the user's cart and all products associated with it
    try:
        
        products = cart.products.all()
        return render(request, "pages/cart.html" , {'cart': cart, 'products': products})
    except : # Cart.ObjectDoesNotExist:
        cart = None
        products = []

    # Render the cart template with the user's cart and products
   
        return render(request, "pages/cart.html" , {'cart': cart, 'products': products})


def Pro(request):
    user_id = request.session.get("user_id")
    user = Signup.objects.get(id=user_id)

    return render(request, "pages/pro.html", {"user": user})


def Hijab(request):
    prayer = Product2.objects.all()
    # print(scarfs[0])
    dresses = {"prayer": prayer}
    return render(request, "pages/hijab.html" , dresses)


def HALI(request):
    return render(request, "pages/hali.html")




# def Add_to_cart(request, product_id):
    # Get the product object by its ID
    product = Product1.objects.get(id=product_id)

    # Check if the user has a cart
    try:
        cart = Cart.objects.get(user=request.user)
        cart.products.add(product)

         # Redirect the user to the cart page
        return redirect('cart')
    except :#Cart.ObjectDoesNotExist:
        # If the user doesn't have a cart, create one
        cart = Cart.objects.create(user=request.user)
        cart.products.add(product)

    # Redirect the user to the cart page
        return redirect('cart')
    # Add the product to the user's cart
    #cart.products.add(product)

    # Redirect the user to the cart page
    #return redirect('cart')