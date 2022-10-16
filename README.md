# ecom
python –version
pip install pipenv
pipenv shell
to show current virtual envi: pipenv –venv
Django commands:Django-admin
Py manage.py runserver
Py mange.py run server 8000//Port number
Pip install mysqlclient
To join mysql:
Setting.py
python manage.py startapp shop

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop'
]

Create urls.py in ur app
Include connection between main urls.py
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls'))
]


Urls.py of app
from django.urls import path

urlpatterns = [
    path()
]


Create templates folder:
Create another folder and create a index.html
To load templates go to vies.py
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"shop/index.html")


then move to app urls.py
from django.urls import path
from.import views
urlpatterns = [
    path('home',views.home,name='home'),
]


To use extern:
    {% block content %}
    {% endblock content %}

    {% block scripts %}
    {% endblock scripts %}

Insert the navigation bar using bootstrap
Create nav_bar.html
Insert the nav_bar.html or include in main.html
{% include 'shop/inc/nav_bar.html' %}

Now create a model class in models.py

While uploading the new product we insert their name with the current time to avoid overriding

Create necessary columns
Python manage.py make migration(Error will be generates)
Pip install pillow
Python manage.py make migration
Python manage.py migrate
python manage.py createsuperuser
Username (leave blank to use 'rithi'): rith
Email address: rithiksuthan123@gmail.com
Password: 
Password (again): 
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

And open admin in browser and log into it

And to register open admin.py 
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Catagory)
admin.site.register(Product)

log into Django in browser what you did in previous step
 Then add categories and products
If you want  browser Django window with different style then
Pip install Django-jazzmin
In settings.py
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop'
]

Then slider window of bootsrap is used by creating slider.html

Then create a style sheet in style\css\style.css

Then go to fonts.google.com to select require font
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans&display=swap'); and put it in styles.css

Create link for each menus in navigation bar

Create collections in navbar and create a html and do necessary routing in views.py and urls.py

Make collections.html necessary coding to look good then
Add some changes in urls.py
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls'))
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


Creating link for each categories by modifying urls.py and views.py

In views.py create function
def collectionsview(request,name):
    if(Catagory.objects.filter(name=name,status=0)):
        products=Product.objects.filter(category__name=name)
        return render(request,"shop/products/index.html",{"products":products,"category_name":name})
    else:
        messages.warning(request,"No Such Catagory Found")
        return redirect('collections')



create a footer.html in inc folder:
<footer class="text-center text-lg-start bg-dark text-white">
    <section class="container d-flex justify-content-center justify-content-lg-between p-4">
      <div class="me-5 d-none d-lg-block">
        <span>Get connected with us on social networks:</span>
      </div>
      <div>
        <a href="" class="me-4 text-reset"><i class="fa fa-facebook"></i></a>
        <a href="" class="me-4 text-reset"><i class="fa fa-twitter"></i></a>
        <a href="" class="me-4 text-reset"><i class="fa fa-google"></i></a>
        <a href="" class="me-4 text-reset"><i class="fa fa-instagram"></i></a>
        <a href="" class="me-4 text-reset"><i class="fa fa-linkedin"></i></a>
        <a href="" class="me-4 text-reset"><i class="fa fa-github"></i></a>
      </div>
    </section>
  
    <section class="">
      <div class="container text-center text-md-start mt-5">
        <div class="row mt-3">
          <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
            <h6 class="text-uppercase fw-bold mb-4"><i class="fa fa-cart-plus"></i> ShopKart</h6>
            <p>
              shopkart.com is a one stop destination for your family's fashion needs.
               We give you the opportunity to give your wardrobe a makeover with the latest collections from our top brands.
            </p>
          </div>
  
          <div class="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">
            <h6 class="text-uppercase fw-bold mb-4">Make Money with Us</h6>
            <p><a href="#!" class="text-reset">Sell on ShopKart</a></p>
            <p><a href="#!" class="text-reset">Advertise Your Products</a></p>
            <p><a href="#!" class="text-reset">Become an Affiliate</a></p>
            <p><a href="#!" class="text-reset">Fulfilment by ShopKart</a></p>
          </div>
          <div class="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4">
            <h6 class="text-uppercase fw-bold mb-4">Useful links</h6>
            <p><a href="#!" class="text-reset">FAQ</a></p>
            <p><a href="#!" class="text-reset">Feedback</a></p>
            <p><a href="#!" class="text-reset">About Us</a></p>
            <p><a href="#!" class="text-reset">Contact Us</a></p>
          </div>
          
          <div class="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">
            <h6 class="text-uppercase fw-bold mb-4"> Contact</h6>
            <p><i class="fa fa-home"></i> Rithik Suthan</p>
            <p><i class="fa fa-envelope"></i> abc@gmail.com</p>
            <p><i class="fa fa-phone"></i> + 91 1234567890</p>
          </div>
  
        </div>
      </div>
    </section>
    <div class="text-center p-4">
      &copy;  2021 Copyright <a class="text-reset fw-bold" href="https://www.linkedin.com/in/rithik-suthan-a277491b8/"> rithik suthan</a>
    </div>
  </footer>


Make changes in urls.py
    path('collections/<str:name>',views.collectionsview,name='collections'),

Then if we click the mobiles all mobiles must be displayed 
So modify products/index.html(new one created)
To fetch the details of the particular mobile:
Add in urls.py
    path('collections/<str:cname>/<str:pname>',views.product_details,name='product_details'),

add product_details func in views.py
def product_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"shop/products/product_details.html",{"products":products})
        else:
            messages.error(request,"No Such Product Found")
            return redirect('collections')
    else:
        messages.error(request,"No Such Catagory Found")
        return redirect('collections')
    # return HTTPResponse("Product details")


Create a new file product_details.html in products
Then create options for add to card and out of stock

To print the  trending stocks
Print It in home page as

Index.html(main)
{% extends 'shop/layouts/main.html'%}

{% block title %}
ShopKart |online Shopping
{% endblock title %}


{% block content %}

{% include 'shop/inc/slider.html' %}

<div class="container " style="margin-top:70px;">
    <div class="row">
        <div class="col-12">
            <h4 class="mb-3"> Latest Offers</h4>
            <hr style="border-color:#b8bfc2">
        </div>
        {% for item in products %}
        <div class="col-md-4 col-lg-3">
            <div class="card my-3">
                <img src="{{item.product_image.url}}" class="card-image-top" alt="Categories">

                {% comment %} <a href="{% url 'collections'  item.name %}"> {% endcomment %}
                    <a href="{% url 'product_details' item.category.name item.name %}">

                    <div class="card-body">
                    <h5 class="card-title text-primary"> {{ item.name }} </h5>
                    <p class="card-text">
                        <span class="float-start old_price " ><s>Rs.{{ item.original_price | stringformat:'d' }}</s></span>
                        <span class="float-end new_price">Rs.{{ item.selling_price | stringformat:'d'}}</span>
                    </p>
                    
                </div>
            </a>
            </div>
        </div>
        {% endfor %}
    </div>

</div> 
{% endblock content %}



Now let us create form.py
from dataclasses import fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from .models import User
class CustomUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

now let us design the form in register.html
{% extends 'shop/layouts/main.html' %}

{% block title %}
Registration | ShopKart
{% endblock title %}

{% block content %}
<div class="container " style="margin-top:70px;">
    <div class="row">
        <div class="col-12">
            <h1>Register Page</h1>
            <hr style="border-color:#b8bfc2;">
            
        </div>
    </div>
    <section class="py-4" >
        <div class="container">
          <div class="row">
            <div class="col-6">
              <form method="post" action="">
                {% csrf_token %}
                <div class="mb-4">
                  <label for="" class="form-label">User Name</label>
                  {{form.username}}
                </div>
                <div class="mb-4">
                  <label for="" class="form-label">User Email</label>
                  {{form.email}}
                </div>
                <div class="mb-4">
                  <label for="" class="form-label">Password</label>
                  {{form.password1}}
                </div>
                <div class="mb-4">
                  <label for="" class="form-label">Confirm Password</label>
                  {{form.password2}}
                </div>
                <button type="submit" class="btn btn-primary">Register</button>
              </form>
              <p class="my-2">Already user ? <a href="{% url 'login' %}">Login Now</a> </p>
            </div>
            <div class="col-6">
              
                  {% if form.errors.username %}
                    <label class="text-danger d-block">{{ form.errors.username }}</label>
                  {% endif %}
              
                  {% if form.errors.email %}
                  <label class="text-danger d-block">{{ form.errors.email }}</label>
                  {% endif %}
                
                  {% if form.errors.password1 %}
                  <label class="text-danger d-block">{{ form.errors.password1 }}</label>
                  {% endif %}
                
                  {% if form.errors.password2 %}
                  <label class="text-danger d-block">{{ form.errors.password2 }}</label>
                  {% endif %}
                
            </div>
          </div>
        </div>
      </section>

</div>
 
{% endblock content %}


now create a login.html
to perform validation dialog box appears to print it create message.html in inc folder
include messages.html in register,login ,collection page,product_details.html and products/index.html.

in views.py
create a function for login
def login_page(request):
  if request.user.is_authenticated:
    return redirect("/")
  else:
    if request.method=='POST':
      name=request.POST.get('username')
      pwd=request.POST.get('password')
      user=authenticate(request,username=name,password=pwd)
      if user is not None:
        login(request,user)#inbuilt function
        messages.success(request,"Logged in Successfully")
        return redirect("/")
      else:
        messages.error(request,"Invalid User Name or Password")
        return redirect("/login")
    return render(request,"shop/login.html")


Then create logout page :
def logout_page(request):
  if request.user.is_authenticated:#check whether user is logged in
    logout(request)
    messages.success(request,"Logged out Successfully")
  return redirect("/")

Then make some changes in nav_bar.html
Change nav_bar links to
        <a class="nav-link" aria-current="page" href="{% url 'home' %}"><i class="fa fa-home"></i> Home</a>
        {% if request.user.is_authenticated %}
          <a class="nav-link" aria-current="page" href="#"><i class="fa fa-user"></i> {{request.user}}</a>
          <a class="nav-link" aria-current="page" href="{% url 'logout' %}"><i class="fa fa-sign-out"></i> Logout</a>
        {% else %}
          <a class="nav-link" href="{% url 'login' %}"><i class="fa fa-sign-in"></i> Login</a>
          <a class="nav-link" href="{% url 'register' %}"><i class="fa fa-users"></i> Register</a>
        {% endif %}
          <a class="nav-link" href="{% url 'collections' %}"><i class="fa fa-cubes"></i> Collections</a>


Now we can create add to cart in product_view.file:
Now we have to create a quantity box
Now let us create script tag which  for js  functions for adding the quantity etc so they have to placed down the <section tag> <script tag>  must be loaded after loading page
Update in urls.py and create a fuction In views.py

Urls.py
 path('addtocart',views.add_to_cart,name="addtocart"),

views.py
def add_to_cart(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_qty=data['product_qty']
      product_id=data['pid']
      #print(request.user.id)
      product_status=Product.objects.get(id=product_id)
      if product_status:
        if Cart.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Cart'}, status=200)
        else:
          if product_status.quantity>=product_qty:
            Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
            return JsonResponse({'status':'Product Added to Cart'}, status=200)
          else:
            return JsonResponse({'status':'Product Stock Not Available'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Cart'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)


Create a page for cart.html
Urls.py
path('cart',views.cart_page,name="cart"),

view.py
def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,"shop/cart.html",{"cart":cart})
    else:
        return redirect("/")

cart.html
{% extends 'shop/layouts/main.html' %}
{% block title %}
  Registration | ShopKart
{% endblock title %}
{% block content %}
  <section class="bg-light py-4 my-5" style="min-height:600px;">
    <div class="container">
      <div class="row">
        <div class="col-12">
          <h4 class="mb-3">Cart  Items</h4>
          <hr style="border-color:#b8bfc2;">
        </div>
      
        <table>
            <tr>
                <th>Image</th>
                <th>Product Name</th>
                <th>Unit</th>
                <th>Quantity</th>
                <th>Amount</th>
                <th>Remove</th>
            </tr>
          

            {% for item in cart %}
           <tr>
              <td><img src="{{item.product.product_image.url}}" height="75px" alt="{{item.product.name}}"></td>
              <td>{{item.product.name}}</td>
              <td>{{item.product.selling_price | stringformat:'d'}}</td>
              <td>{{item.product_qty}}</td>
              <td class="amt">{{item.total_cost | stringformat:'d'}}</td>
              {% comment %} <td><a href="{% url 'remove_cart' item.id %}"  onclick="return confirm('Are you sure? to Remove')"  class="btn btn-danger btn-sm"><i class="fa fa-trash"></i> Remove</a></td>
            </tr> {% endcomment %}
            {% endfor %}
            <tr>
              <td></td>
              <td></td>
              <td colspan="2"><b>Total Amount</b></td>
              <th id="net">0</th>
              <td><button class="btn btn-primary btn-sm">
                <i class="fa fa-check-circle"></i> Check Out
              </button></td>
            </tr>
           
        </table>
       
      </div>
      </div>
  </section>

  <script>
    const nodes = document.querySelectorAll('.amt');
    const arr = Array.from(nodes);
    const res = arr.reduce((acc, curr) => {
     return acc += Number(curr.textContent)
    }, 0);
    document.getElementById("net").innerHTML="Rs : "+res;

  </script>
{% endblock content %}

Now create removing from cart:
Urls.py
path('cart',views.remove_cart,name="remove_cart"),

Views.py
def remove_cart(request,cid):
  cartitem=Cart.objects.get(id=cid)
  cartitem.delete()
  return redirect("/cart")


Let us create favouirtes:
Urls.py
 path('fav',views.fav_page,name="fav"),

views.py
def fav_page(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_id=data['pid']
      product_status=Product.objects.get(id=product_id)
      if product_status:
         if Favourite.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Favourite'}, status=200)
         else:
          Favourite.objects.create(user=request.user,product_id=product_id)
          return JsonResponse({'status':'Product Added to Favourite'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Favourite'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)

in product_details.html
btnFav.addEventListener("click", function() {
     
        let postObj = { 
            'pid': pid.value
        }
        console.log(postObj);
        fetch("/fav",{
          method: 'POST',
          credentials: 'same-origin',
          headers:{
              'Accept': 'application/json',
              'X-Requested-With': 'XMLHttpRequest',
              'X-CSRFToken': '{{ csrf_token }}',
          },
          body: JSON.stringify(postObj)
        }).then(response => {
          return response.json();
        }).then(data => {
          //console.log(data);
          alert(data['status']);
        });
      
  });

});


To see the favourites create a favourite  page and see it

Urls.py
path('favviewpage',views.favviewpage,name="favviewpage"),

Views.py


def favviewpage(request):
  if request.user.is_authenticated:
    fav=Favourite.objects.filter(user=request.user)
    return render(request,"shop/fav.html",{"fav":fav})
  else:
    return redirect("/")

Then inside shop create fav.html
{% extends 'shop/layouts/main.html' %}
{% block title %}
  Registration | ShopKart
{% endblock title %}
{% block content %}
  <section class="bg-light py-4 my-5" style="min-height:600px;">
    <div class="container">
      <div class="row">
        <div class="col-12">
          <h4 class="mb-3">Favourite Item</h4>
          <hr style="border-color:#b8bfc2;">
        </div>
      
        <table>
            <tr>
                <th>Image</th>
                <th>Product Name</th>
                <th>Unit</th>
                <th>Remove</th>
            </tr>
          

            {% for item in fav %}
           <tr>
              <td><img src="{{item.product.product_image.url}}" height="75px" alt="{{item.product.name}}"></td>
              <td>{{item.product.name}}</td>
              <td>{{item.product.selling_price | stringformat:'d'}}</td>
              <td><a href="{% url 'remove_fav' item.id %}"  onclick="return confirm('Are you sure? to Remove')"  class="btn btn-danger btn-sm"><i class="fa fa-trash"></i> Remove</a></td>
            </tr>
            {% endfor %}
            <tr>
        </table>
       
      </div>
      </div>
  </section>
{% endblock content %}

Then to remove the favourites:
Urls.py
 path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),

views.py
def remove_fav(request,fid):
  item=Favourite.objects.get(id=fid)
  item.delete()
  return redirect("/favviewpage")

product_details.html(whole code)

{% extends 'shop/layouts/main.html' %}
{% block title %}
ShopKart | Online Shopping
{% endblock title %}

{% block content %}
<style>
    .pic-box {
        position: relative;
      }
      
      .hot {
        background-color: orangered;
        color: white;
        width: 50px;
        text-align: center;
        font-weight: bold;
        display: inline;
        border-radius: 5px;
        padding: 5px;
        position: absolute;
        top: 0;
        right: 130px;
        z-index: 10;
      }
</style>
<section class="bg-light py-4 my-5" style="min-height:600px;">
  <div class="container">
    <div class="row">
      <div class="col-12">
        <h4 class="mb-3">  {{products}} Details</h4>
        <hr style="border-color:#b8bfc2;">
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="{% url 'home' %}">Home</a></li>
            <li class="breadcrumb-item"><a href="{% url 'collections' products.category.name  %}">Collections</a></li>
            <li class="breadcrumb-item active" aria-current="page">{{products}}</li>
          </ol>
        </nav>
        {% include 'shop/inc/message.html' %}
      </div>
      <div class="col-4 my-3 pic-box">
        {% if products.trending %}
          <div class="hot">Hot</div>
          {% endif %}
          <img src="{{products.product_image.url}}" class="card-image-top" alt="{{products}}"
          style="height:300px; width:300px">
      </div>
      <div class="col-8 my-3">
          <h5 class="text-success">{{products | upper}}</h5>
          <p>{{products.vendor}}</p>
          <p>{{products.description}}</p>
          <h6 class="my-2 text-danger">Current Price : Rs. <s>{{products.original_price}}</s></h6>
          <h5 class="my-2 text-primary">Offer Price   : Rs.{{products.selling_price}}</h5>
          <div class="my-3">
            {% if products.quantity > 0 %}
            <input type="hidden" value="{{products.id}}" id="pid">
            
              <p>
                <div class="input-group" style="width:150px">
                  <button class="input-group-text bg-success text-light" id="btnMinus" ><i class="fa fa-minus"></i></button>
                    <input type="text" name="qty" id="txtQty" value="1" class="form-control text-center">
                  <button class="input-group-text bg-success text-light" id="btnPlus"><i class="fa fa-plus"></i></button>
                </div>
              </p>
             <button class="btn btn-primary" id="btnCart"><i class="fa fa-shopping-cart"></i> Add to Cart</button>
            {% else %}
            <button class="btn btn-secondary"><i class="fa fa-minus"></i> Out of Stock</button>
            {% endif %}
            <button class="btn btn-danger" id="btnFav"><i class="fa fa-heart"></i></button>
          </div>
      </div>
    </div>
  </div>
</section>
 <script>
document.addEventListener("DOMContentLoaded", function(event) {
  const btnPlus = document.getElementById("btnPlus");
  const btnMinus = document.getElementById("btnMinus");
  const txtQty = document.getElementById("txtQty");
  const pid = document.getElementById("pid");
  const btnCart = document.getElementById("btnCart");
  const btnFav = document.getElementById("btnFav");

  btnPlus.addEventListener("click", function() {
    let qty=parseInt(txtQty.value,10);
    qty=isNaN(qty)?0:qty;
    //console.log(qty);
    if(qty<10){
      qty++;
      txtQty.value=qty;
    }
  });

  btnMinus.addEventListener("click", function() {
      let qty=parseInt(txtQty.value,10);
      qty=isNaN(qty)?0:qty;
      //console.log(qty);
      if(qty>1){
        qty--;
        txtQty.value=qty;
      }
  });

  btnCart.addEventListener("click", function() {
      let qty=parseInt(txtQty.value,10);
      qty=isNaN(qty)?0:qty;
      
      if(qty>0){
        let postObj = { 
            'product_qty': qty, 
            'pid': pid.value
        }
        //console.log(postObj);
        fetch("/addtocart",{
          method: 'POST',
          credentials: 'same-origin',
          headers:{
              'Accept': 'application/json',
              'X-Requested-With': 'XMLHttpRequest',
              'X-CSRFToken': '{{ csrf_token }}',
          },
          body: JSON.stringify(postObj)
        }).then(response => {
          return response.json();
        }).then(data => {
          //console.log(data);
          alert(data['status']);
        });
 

      }else{
        alert("Please Enter The Quantity");
      }
      
  });

  btnFav.addEventListener("click", function() {
     
        let postObj = { 
            'pid': pid.value
        }
        console.log(postObj);
        fetch("/fav",{
          method: 'POST',
          credentials: 'same-origin',
          headers:{
              'Accept': 'application/json',
              'X-Requested-With': 'XMLHttpRequest',
              'X-CSRFToken': '{{ csrf_token }}',
          },
          body: JSON.stringify(postObj)
        }).then(response => {
          return response.json();
        }).then(data => {
          //console.log(data);
          alert(data['status']);
        });
      
  });

});
 </script>
{% endblock content %}

{% comment %} {% extends 'shop/layouts/main.html'%}

{% block title %}
ShopKart |online Shopping
{% endblock title %}


{% block content %}

<style>
    .pic-box {
        position: relative;
      }
      
      .hot {
        background-color: orangered;
        color: white;
        width: 50px;
        text-align: center;
        font-weight: bold;
        display: inline;
        border-radius: 5px;
        padding: 5px;
        position: absolute;
        top: 0;
        right: 130px;
        z-index: 10;
      }
</style>
<section class="bg-light py-4 my-5" style="min-height:600px">
    <div class="container">
        <div class="row">
            <div class="col-12">
                <br><br>
                <h4 class="mb-3"> {{products}} Details</h4>
                <hr style="border-color:#b8bfc2">
            </div>
            <nav aria-label="breadcrumb">
                <ol class="breadcrumb">
                  <li class="breadcrumb-item"><a href="{% url 'home' %}">Home</a></li>
                  <li class="breadcrumb-item"><a href="{% url 'collections' products.category.name  %}">Collections</a></li>
                  <li class="breadcrumb-item active" aria-current="page">{{products}}</li>
                </ol>
              </nav>
              {% include 'shop/inc/message.html' %}
            <div class="col-4 my-3 pic-box" >
                {% if products.trending %}
                <div class="hot">Hot</div>
                {% endif %}
                <img src="{{products.product_image.url}}" class="card-image-top" alt="{{products}}"
                style="height:300px; width:300px">

            </div>
        

            <div class="col-8 my-3" >
                </h5 class="test-sucess">{{products|upper}}</h>
                <p>{{products.vendor}}</p>    
                <p>
                    {{products.description}}
                </p>
                <h6 class="my-2 text-danger">Current Price : Rs.<s>{{products.original_price}}</s></h6>
                <h5 class="my-2 text-primary">Offer Price : Rs.{{products.selling_price}}</h6>
        
                <div class="my-3">

                    {% if products.quantity > 0 %}

                    <input type="hidden" value="{{products.id}}" id="pid">
            
              <p>
                <div class="input-group" style="width:150px">
                  <button class="input-group-text bg-success text-light" id="btnMinus" ><i class="fa fa-minus"></i></button>
                    <input type="text" name="qty" id="txtQty" value="1" class="form-control text-center">
                  <button class="input-group-text bg-success text-light" id="btnPlus"><i class="fa fa-plus"></i></button>
                </div>
              </p>

                    <button class="btn btn-primary"><i class="fa fa-shopping-cart"></i>Add to Cart</button>
                    
                    {% else %}
                    <button class="btn btn-secondary"><i class="fa fa-minus"></i> Out of Stock</button>
                    {% endif %}
                    <button class="btn btn-danger"><i class="fa fa-heart"></i></button>
                </div>
            </div>
        </div>
    </div>
</section>
<script>
    document.addEventListener("DOMContentLoaded", function(event) {
        const btnPlus = document.getElementById("btnPlus");
        const btnMinus = document.getElementById("btnMinus");
        const txtQty = document.getElementById("txtQty");
        const pid = document.getElementById("pid");
        const btnCart = document.getElementById("btnCart");
        const btnFav = document.getElementById("btnFav");
      
        btnPlus.addEventListener("click", function() {
          let qty=parseInt(txtQty.value,10);
          qty=isNaN(qty)?0:qty;
          //console.log(qty);
          if(qty<10){
            qty++;
            txtQty.value=qty;
          }
        });

        btnMinus.addEventListener("click", function() {
            let qty=parseInt(txtQty.value,10);
            qty=isNaN(qty)?0:qty;
            //console.log(qty);
            if(qty>1){
              qty--;
              txtQty.value=qty;
            }
        });

        
</script>
{% endblock content %} {% endcomment %}


Project is successfully completed with no errors!!!
