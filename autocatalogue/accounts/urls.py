from .views import *
from django.urls import path

urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('email-verify/',VerifyEmail.as_view(), name='email-verify'),
    path('cars/',CarsAPIView.as_view(), name='cars'),
    path('brands/',BrandsAPIView.as_view(), name='cars'),
    path('models/',ModelsAPIView.as_view(), name='models'),
    path('generations/',ModelsAPIView.as_view(), name='generations'),
    path('categories/',CategoriesAPIView.as_view(), name='categories'),
    path('parts/',PartsAPIView.as_view(), name='parts'),

]
