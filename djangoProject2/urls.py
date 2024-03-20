from django.contrib import admin
from django.urls import path
from sample import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test/', views.test),
    path('api/v1/product_list/', views.get_product)
]
