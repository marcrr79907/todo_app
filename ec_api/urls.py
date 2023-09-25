from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from .import views

route = routers.DefaultRouter()
route.register(r'tasks', views.TaskView, 'tasks')

urlpatterns = [
    path('', include(route.urls)),
    path('docs/', include_docs_urls(title='Tasks API')),
]
