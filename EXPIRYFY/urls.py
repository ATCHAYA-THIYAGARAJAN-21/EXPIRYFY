from django.urls import path
from . import views
 
urlpatterns = [ 
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path("add/", views.add_product, name="add"),
    path("update/<int:pk>/", views.update, name="update"),
    path("delete/<int:pk>/", views.delete_product, name="delete"),
    path("view/", views.view_product, name="view"),
]

