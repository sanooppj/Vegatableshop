from django.urls import path
from nameapp import views
urlpatterns=[
    path('main_page/', views.main_page, name="main_page"),
    path('manager_page/', views.manager_page, name="manager_page"),
    path('manager_post/', views.manager_post, name="manager_post"),
    path('manager_table/', views.manager_table, name="manager_table"),
    path('manager_edit/<int:c_id>', views.manager_edit, name="manager_edit"),
    path('manager_update/<int:c_id>', views.manager_update, name="manager_update"),
    path('manager_delete/<int:c_id>', views.manager_delete, name="manager_delete"),
    path('product_page/', views.product_page, name="product_page"),
    path('product_post/', views.product_post, name="product_post"),
    path('product_table/', views.product_table, name="product_table"),
    path('product_edit/<int:p_id>', views.product_edit, name="product_edit"),
    path('product_update/<int:p_id>', views.product_update, name="product_update"),
    path('product_delete/<int:p_id>', views.product_delete, name="product_delete"),
    path('Adminlogin/', views.Adminlogin, name="Adminlogin"),
    path('AdminLogout/', views.AdminLogout, name="AdminLogout"),
    path('login_page/', views.login_page, name="login_page"),
    path('contact_table/', views.contact_table, name="contact_table"),
    path('contact_delete/<int:c_id>', views.contact_delete, name="contact_delete"),


]