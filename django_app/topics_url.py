from django.urls import path
from django_app.views import add_topic, remove_topic, subscribe, unsubscribe


urlpatterns = [
    path('topic/add/', add_topic),
    path('topic/remove/', remove_topic),
    path('topic/subscribe/', subscribe),
    path('topic/unsubscribe/', unsubscribe)
]
