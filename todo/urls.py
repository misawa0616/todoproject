from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.TodoList.as_view(), name='list'),
    path('detail/<int:pk>', views.TodoDetail.as_view(), name='detail'),
    path('create/', views.TodoCreate.as_view(), name='create'),
    path('delete/<int:pk>', views.TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>', views.TodoUpdate.as_view(), name='update'),
]