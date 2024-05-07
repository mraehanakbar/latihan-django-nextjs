from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.getAllMenu, name='menu'),
    path('menu/new/', views.addMenu, name='add_new_menu'),
    path('menu/<str:pk>/', views.getMenu, name='get_menu'),
    path('menu/<str:pk>/update/', views.updateMenu, name='update_menu'),
]