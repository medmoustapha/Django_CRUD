from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('new',views.create_product, name="create_products"),
   #path('new(\w+)/?$',views.create_product, name="create_products"),
   #path('new(\w+)/(/id)/?$',views.create_product, name="create_products"),
   path('update/<int:id>/',views.update_product, name="update_product"),
   path('delete/<int:id>/',views.delete_product, name="delete_product"),
]