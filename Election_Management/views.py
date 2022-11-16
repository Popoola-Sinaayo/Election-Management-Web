from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    if request.method == "GET":
        return render(request, 'index.html', {'Polling_Unit': Polling_Unit.objects.all()})
    if request.method == "POST":
        id = request.POST["id"]
        poll_array = []
        polls = Announced_Pu_Results.objects.filter(polling_unit_uniqueid=id)
        if polls.exists():
            for poll in polls:
                poll_array.append(poll)
            return render(request, 'polling-details.html', {'polls': poll_array})
        return render(request, 'index.html', {'Polling_Unit': Polling_Unit.objects.all(), 'message': "No result Available"})


def view_polling_unit(request):
    if request.method == "GET":
        return render(request, 'view-polling.html', {'Lga': Lga.objects.all()})
    if request.method == "POST":
        id = request.POST["id"]
        poll_array = []
        # poll = Announced_Pu_Results.objects.filter(polling_unit_uniqueid=id)
        poll = Polling_Unit.objects.filter(lga_id=id)
        if poll.exists():
            new_poll = Announced_Pu_Results.objects.filter(
                polling_unit_uniqueid=poll[0].polling_unit_id)
            if new_poll.exists():
                for poll in new_poll:
                    poll_array.append(poll)
            print(poll_array)
            return render(request, 'polling-total.html', {'polls': poll_array})
        return render(request, 'view-polling.html', {'message': "No score recorded", 'Lga': Lga.objects.all()})


def store_result(request):
    if request.method == "GET":
        return render(request, 'store-results.html')
    if request.method == "POST":
        poll_unit_id = request.POST["poll-unit-id"]
        ward_id = request.POST["Ward ID"]
        lga = request.POST["LGA"]
        ward = request.POST["unique-ward"]
        polling_number = request.POST["polling-number"]
        polling_name = request.POST["polling-name"]
        poll_desc = request.POST["poll-desc"]
        ip = request.POST.get("ip", "")
        date = request.POST.get("date")
        lat = request.POST.get("lat")
        long = request.POST.get("long")
        user = request.POST.get("user")
        if date == "":
            date = '2020-10-15 18:01:01'
        print(date)
        poll = Polling_Unit.objects.create(polling_unit_id=poll_unit_id, ward_id=ward_id, lga_id=lga,
                                           uniquewarsid=ward, polling_unit_number=polling_number, polling_unit_name=polling_name, polling_unit_description=poll_desc, lat=lat, long=long, entered_by_user=user, date_entered=date, user_ip_address=ip)
        poll.save()
        return render(request, 'store-results.html', {'message': "Information Creation Succesful"})
