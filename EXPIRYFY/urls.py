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
]

