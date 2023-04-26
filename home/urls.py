# from django.urls import path
# from . import views
# from . views import *

# urlpatterns = [
    # path('', views.index, name='index'),
    # path('browser', views.function in views.py file, # name=template),
    # path('', views.index, name= 'index'),
    # path('category/', views.category, name= 'category'),
    # path('product/', views.product, name= 'product'),
    # path('categories/<slug:slug>/', views.categories, name= 'categories'),
    # path('details/<slug:slug>/', views.details, name= 'details'),
    # path('signup/', views.signup, name= 'signup'),
    # path('/categories/<str:id>/', views.categories, name= 'categories'),
# ]
from django.urls import path
from . import views 
from . views import * 



urlpatterns = [
    path('', views.index, name= 'index'),    
    path('category/', views.category, name= 'category'),  
    path('product/', views.product, name= 'product'),  
    path('categories/<slug:slug>/', views.categories, name= 'categories'),    
    path('details/<slug:slug>/', views.details, name='details'),
    path('contact/', views.contact, name='contact'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('profile/', views.profile, name='profile'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('password/', views.password, name='password'),
    path('shopcart/', views.shopcart, name='shopcart'),
    path('displaycart/', views.displaycart, name='displaycart'),
    path('deleteitem/', views.deleteitem, name= 'deleteitem'),
    path('change/', views.change, name= 'change'),
    path('checkout/', views.checkout, name= 'checkout'),
    path('pay/', views.pay, name= 'pay'),
    path('callback/', views.callback, name= 'callback'),
    path('search/', views.search, name= 'search'),
    
]
