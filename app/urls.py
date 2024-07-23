from django.urls import path
from app import views

urlpatterns =[
    # inicio
    path('', views.inicio, name="inicio"),
    path('all-tools/', views.tools, name="tools"),
    # services
    path('all-tools/converter/', views.converter, name="converter"),
    path('all-tools/converter_txt/', views.converter_txt, name="converter_txt"),
    path('all-tools/converter_jpg/', views.converter_jpg, name="converter_jpg"),
    path('all-tools/compress/', views.compress, name="compress"),
    path('all-tools/compress_img/', views.compress_img, name="compress_img"),

    # files management
    path('all-tools/download/', views.download, name="download"),
    path('all-tools/download/<str:token>/', views.download, name="download"),
    path('all-tools/download/<str:token>/<str:format>', views.download, name="download"),

    
    path('all-tools/delete_file/', views.delete_file, name="delete_file"),


    #login url's
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
]