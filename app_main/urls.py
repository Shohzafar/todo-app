from django.urls import path
from app_main import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout'),
    path('new-todo/', views.new_todo, name='new_todo'),
    path('delete-todo/<int:todo_id>/', views.todo_delete, name='todo_delete'),
    path('todo_detail/<int:todo_id>/', views.todo_detail, name='todo_detail'),
    path('todo_edit/<int:todo_id>/', views.todo_edit, name='todo_edit'),
    path('register/', views.register_page, name='register_page'),
    path('send-email/', views.send_email, name='send_email'),
]

