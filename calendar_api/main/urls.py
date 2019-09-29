from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.calendar, name='calendar'),
    path("add-event/", views.EventView.as_view(), name="add-event"),
    path("event/<slug:pk>/", views.EventDetailView.as_view(), name="event_detail_view"),
    path("events/", views.EventListView.as_view(), name="event_list_view")
]
