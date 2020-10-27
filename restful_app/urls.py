from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_show', views.new_show),
    path('shows', views.shows),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows_desc/<int:show_id>', views.show_desc),
    path('shows_delete/<int:show_id>/delete', views.show_delete)
]