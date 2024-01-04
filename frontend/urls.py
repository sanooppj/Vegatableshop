from django.urls import path
from frontend import views
urlpatterns=[
     path('homepage/', views.homepage, name="homepage"),
     path('products/<catname>/', views.products, name="products"),
     path('about_page/', views.about_page, name="about_page"),
     path('blog_page/', views.blog_page, name="blog_page"),
     path('contact_page/', views.contact_page, name="contact_page"),
     path('contact_post/', views.contact_post, name="contact_post"),
     path('single_product/<int:p_id>', views.single_product, name="single_product"),
     path('cartpost/', views.cartpost, name="cartpost"),
     path('cartpage/', views.cartpage, name="cartpage"),
     path('userloginpage/', views.userloginpage, name="userloginpage"),
     path('userloginpost/', views.userloginpost, name="userloginpost"),
     path('userlogin/', views.userlogin, name="userlogin"),
     path('userlogout/', views.userlogout, name="userlogout"),
     path('Checkout/', views.Checkout, name="Checkout"),
     path('CheckoutDBsave/', views.CheckoutDBsave, name="CheckoutDBsave"),

]