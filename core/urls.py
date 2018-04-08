from django.urls import path

from core import views

urlpatterns = [
    path('reporters/', views.ReporterView.as_view()),
    path('reporters/<int:pk>/', views.ReporterViewDetail.as_view()),
    path('reporters/auth/', views.ReporterAuthenticationView.as_view()),
    path('reporters/password-reset/<str:email>/', views.ReporterPasswordReset.as_view()),
    path('posts/', views.PostView.as_view()),
    path('posts/<int:pk>/', views.PostViewDetail.as_view()),
    path('posts/search/', views.PostSearchView.as_view())
]
