from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='loginpage'),
    path('logout/', LogoutView.as_view(next_page='loginpage'), name='logoutpage'),
    path('register/', views.RegisterView.as_view(), name='registerpage'),
    path('', views.TaskList.as_view(), name='tasklist'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='taskdetail'),
    path('create-task/', views.TaskCreate.as_view(), name='taskcreate'),
    path('update-task/<int:pk>', views.TaskUpdate.as_view(), name='taskupdate'),
    path('delete-task/<int:pk>', views.TaskDelete.as_view(), name='taskdelete'),
]