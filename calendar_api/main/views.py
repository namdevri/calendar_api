from django.shortcuts import render
from .serializers import EventSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import CreateAPIView
from .models import Event
from django.views import generic


def calendar(request):
    events = Event.objects.all()
    return render(request, "calendar.html", {"events": events})

def event_detail(request, id):
    return render(request, "event_detail.html", {"event": Event.objects.get(id=id)})

class EventDetailView(generic.DetailView):
    model = Event
    template_name = "event_detail.html"

class EventListView(generic.ListView):
    model = Event
    paginate_by = 10
    template_name = "event_list.html"

class EventView(CreateAPIView):
    model = Event
    serializer_class = EventSerializer
    #CSRF currently disabled
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(ScriptRunView, self).dispatch(*args, **kwargs)
