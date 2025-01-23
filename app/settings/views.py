from django.shortcuts import render
from app.settings.models import Settings, Newave, Good, Team, Technology
# Create your views here.
def index(request):
    settings_all = Settings.objects.latest("id")
    newave_id = Newave.objects.latest("id")
    good_id = Good.objects.latest("id")
    good_all = Good.objects.all()
    team_all = Team.objects.all()
    technology_all = Technology.objects.all()
    return render(request, "base/index.html", locals())