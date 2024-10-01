from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('blog', views.post_list_BW, name='blog'),
    path('blog/<int:pk>/', views.post_detail_BW, name='post_detail_BW'),
    path('blog/new/', views.post_new_BW, name='post_new_BW'),
    path('blog/<int:pk>/edit/', views.post_edit_BW, name='post_edit_BW'),
    path('blog/<int:pk>/delete/', views.post_delete_BW, name='post_delete_BW'),
    path('blog/<int:blog_pk>/posts/new/', views.post_post_new_BW, name='post_post_new_BW'),  # Nowy post w blogu
    path('blog/<int:blog_pk>/posts/<int:pk>/edit/', views.post_post_edit_BW, name='post_post_edit_BW'),  # Edycja posta
    path('blog/<int:blog_pk>/posts/<int:pk>/delete/', views.post_post_delete_BW, name='post_post_delete_BW'),
    path('blogS', views.post_list_S, name='blogS'),
    path('blogS/<int:pk>/', views.post_detail_S, name='post_detail_S'),
    path('blogS/new/', views.post_new_S, name='post_new_S'),
    path('blogS/<int:pk>/edit/', views.post_edit_S, name='post_edit_S'),
    path('blogS/<int:pk>/delete/', views.post_delete_S, name='post_delete_S'),
    path('blogS/<int:blog_pk>/posts/new/', views.post_post_new_S, name='post_post_new_S'),  # Nowy post w blogu S
    path('blogS/<int:blog_pk>/posts/<int:pk>/edit/', views.post_post_edit_S, name='post_post_edit_S'),  # Edycja posta S
    path('blogS/<int:blog_pk>/posts/<int:pk>/delete/', views.post_post_delete_S, name='post_post_delete_S'),
    path('qualifications',views.qualifications, name='qualifications'),
    path('qualifications/new/', views.qualifications_new, name='qualifications_new'),
    path('qualifications/<int:pk>/edit/', views.qualifications_edit, name='qualifications_edit'),
    path('qualifications/<int:pk>/delete/', views.qualifications_delete, name='qualifications_delete'),
    path('services', views.services, name='services'),
    path('services/new/', views.services_new, name='services_new'),
    path('services/<int:pk>/edit/', views.services_edit, name='services_edit'),
    path('services/<int:pk>/delete/', views.services_delete, name='services_delete'),
    path('contact', views.contact, name='contact'),
    path('contact/email/', views.send_question_email_view, name='send_question_email_view'),


]