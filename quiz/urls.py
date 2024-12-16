from quiz import views
from django.urls import path


urlpatterns = [
    path('', views.start, name='start'),
    path('create_session/', views.create_session, name='create_session'),
    path('play_session/<int:session_id>/', views.play_session, name='play_session'),
    path('submit_answer/<int:session_id>/', views.submit_session, name='submit_session'),
    path('show_results/<int:session_id>/', views.show_results, name='show_results'),
] 