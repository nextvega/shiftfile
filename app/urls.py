from django.urls import path
from app import views

urlpatterns =[
    # inicio
    path('', views.inicio, name="inicio"),
    path('all-tools/', views.tools, name="tools"),
    path('all-tools/converter/', views.converter, name="converter"),
    path('all-tools/compress/', views.compress, name="compress"),
    path('all-tools/download/', views.download, name="download"),
    path('all-tools/download/<str:token>/', views.download, name="download"),
    #login url's
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
]