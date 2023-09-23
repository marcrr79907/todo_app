from django.urls import path
from .import views

urlpatterns = [
    path('', views.getRoute),
    path('notes/', views.getNotes),
    path('notes/<str:pk>/', views.getNote),
    path('note/create/', views.createNote),
    path('note/<str:pk>/update/', views.updateNote),
    path('note/<str:pk>/delete/', views.deleteNote),
]
