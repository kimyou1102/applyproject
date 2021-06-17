from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:apply_id>', views.detail, name="detail"),
    path('create', views.create, name="create"),
    path('read', views.read, name="read"),
    path('edit/<int:apply_id>', views.edit, name="edit"),
    path('update/<int:apply_id>', views.update, name="update"),
    path('delete/<int:apply_id>', views.delete, name="delete"),
]