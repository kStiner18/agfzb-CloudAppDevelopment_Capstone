from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Other paths...
    path('contact/', views.contact, name='contact'),
    path('', views.get_dealerships, name='index'),
    path('my_view/', views.my_view, name='my_view'),
    path('about/', views.about_view, name='about'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('register/', views.registration_request, name='register'),
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),
    path('dealer/<int:dealer_id>/add_review/', views.add_review, name='add_review'),
    # Other paths...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)