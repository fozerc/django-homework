from django.urls import path
from django_app.views import about, comments, update, delete

urlpatterns = [
    path('', about),
    path('comments/', comments),
    path('update', update),
    path('delete', delete)
]
