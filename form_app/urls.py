from . import views
from django.urls import path

#Step 3: Define URLs for Profile Edit and Update
urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('user/<int:user_id>/edit/', views.edit_profile, name='edit-profile'),
    path('user/<int:user_id>/', views.update_profile, name='update-profile'),
]