from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register', views.register, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('ask', views.ask_question, name='ask_question'),
    path('profile/<user_name>', views.view_profile, name='view_profile'),
    path('edit', views.edit_profile, name='edit_profile'),
    path('<single_slug>/delete_ques', views.delete_ques, name='delete_ques'),
    path('<single_slug>/ans_question', views.ans_question, name='ans_question'),
    path('<single_slug>', views.single_slug, name='single_slug'),
]
