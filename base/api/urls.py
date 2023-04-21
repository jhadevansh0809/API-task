from django.urls import path,include
from . import views

urlpatterns = [
     path('register/',views.Register.as_view(),name="register"),
     path('login/',views.Login.as_view(),name="login"),
     path('insertparagraphs/',views.Paragraphs.as_view(),name="insertparagraphs"),
     path('findparagraphs/',views.FindParagraphs.as_view(),name="findparagraphs")
]
