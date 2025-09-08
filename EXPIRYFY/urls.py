from django.urls import path
from . import views
 
urlpatterns = [ 
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path("add/", views.add_product, name="add_product"),
    path("update/<int:pk>/", views.update_product, name="update_product"),
    path("delete/<int:pk>/", views.delete_product, name="delete_product"),
    path("list/", views.product_list, name="product_list"),
    path("view-by-rack/", views.view_by_rack, name="view_by_rack"),

    path('rack/add/', views.rack_add, name='rack_add'),
    path('rack/update/<int:pk>/', views.rack_update, name='rack_update'),
    path('rack/delete/<int:pk>/', views.rack_delete, name='rack_delete'),
    path('rack/view/', views.rack_view, name='rack_view'),

     path("billing/", views.billing_page, name="billing"),
    path("get-product/", views.get_product_by_batch, name="get_product"),
    path("checkout/", views.checkout, name="checkout"),

    
]



