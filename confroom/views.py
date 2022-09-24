

from django.db.models import Case, When, Count, Avg, F, DecimalField, Sum, Q
from django.shortcuts import render,HttpResponse
from datetime import timedelta,datetime,time


from confroom.models import Reservation, ConferenceRoom

def time_in_range(start, end, current):
    return start <= current <= end

def booking(request):
    if request.method == 'POST':
        data = request.POST
        starttime = timedelta(hours=int(data['start_time'].split(':')[0]), minutes=int(data['start_time'].split(':')[1]))
        endtime = timedelta(hours=int(data['end_time'].split(':')[0]), minutes=int(data['end_time'].split(':')[1]))
        try:
            person = int(data['person'])
        except:
            person = 0

        if starttime > endtime:
            return HttpResponse('INCORRECT_INPUT')
        else:
            if int(endtime.seconds / 60)%15==0 and int(starttime.seconds / 60)%15==0:
                if (time_in_range(time(9, 0, 0), time(9, 15, 0), datetime.strptime(str(starttime), "%H:%M:%S").time())
                    or time_in_range(time(9, 0, 0), time(9, 15, 0), datetime.strptime(str(endtime), "%H:%M:%S").time())
                    or time_in_range(time(13, 15, 0), time(13, 45, 0), datetime.strptime(str(starttime), "%H:%M:%S").time())
                    or time_in_range(time(13, 15, 0), time(13, 45, 0), datetime.strptime(str(endtime), "%H:%M:%S").time())
                    or time_in_range(time(17, 45, 0), time(18, 0, 0), datetime.strptime(str(starttime), "%H:%M:%S").time())
                    or time_in_range(time(17, 45, 0), time(18, 0, 0), datetime.strptime(str(endtime), "%H:%M:%S").time())):
                    return HttpResponse('NO_VACANT_ROOM')
                else:
                    if data['type'] == 'BOOK':

                        if int(data['person']) > 0:
                            rea = Reservation.objects.filter(Q(date=datetime.now().date(), start_time__lte=datetime.strptime(str(starttime), "%H:%M:%S"), end_time__gte=datetime.strptime(str(endtime), "%H:%M:%S"))|Q(date=datetime.now().date(), start_time__gte=datetime.strptime(str(starttime), "%H:%M:%S"), end_time__lte=datetime.strptime(str(endtime), "%H:%M:%S"))|Q(date=datetime.now().date(), start_time__lte=datetime.strptime(str(starttime), "%H:%M:%S"), end_time__gte=datetime.strptime(str(starttime), "%H:%M:%S"))|Q(date=datetime.now().date(), start_time__lte=datetime.strptime(str(endtime), "%H:%M:%S"), end_time__gte=datetime.strptime(str(endtime), "%H:%M:%S"))).values('room_id')


                            room = ConferenceRoom.objects.filter(capacity__gte=int(data['person'])).annotate(
                                count=Count(Case(When(reservation__date=datetime.now().date(), reservation__start_time__lte=datetime.strptime(str(starttime), "%H:%M:%S"),
                                                     reservation__end_time__gte=datetime.strptime(str(endtime), "%H:%M:%S"), then=1)))).order_by('count').exclude(id__in=rea)

                            room  = room.first()

                            if room:
                                Reservation.objects.create(room=room,  start_time=datetime.strptime(str(starttime), "%H:%M:%S"),
                                                           end_time=datetime.strptime(str(endtime), "%H:%M:%S"))
                                return HttpResponse(room.name)
                            else:
                                return HttpResponse('NO_VACANT_ROOM')
                    elif data['type'] == 'VACANCY':
                        rea = Reservation.objects.filter(
                            Q(date=datetime.now().date(), start_time__lte=datetime.strptime(str(starttime), "%H:%M:%S"),
                              end_time__gte=datetime.strptime(str(endtime), "%H:%M:%S")) | Q(date=datetime.now().date(),
                                                                                             start_time__gte=datetime.strptime(
                                                                                                 str(starttime),
                                                                                                 "%H:%M:%S"),
                                                                                             end_time__lte=datetime.strptime(
                                                                                                 str(endtime),
                                                                                                 "%H:%M:%S")) | Q(
                                date=datetime.now().date(),
                                start_time__lte=datetime.strptime(str(starttime), "%H:%M:%S"),
                                end_time__gte=datetime.strptime(str(starttime), "%H:%M:%S")) | Q(
                                date=datetime.now().date(), start_time__lte=datetime.strptime(str(endtime), "%H:%M:%S"),
                                end_time__gte=datetime.strptime(str(endtime), "%H:%M:%S"))).values('room_id')

                        room = ConferenceRoom.objects.filter().annotate(
                            count=Count(Case(When(reservation__date=datetime.now().date(),
                                                  reservation__start_time__lte=datetime.strptime(str(starttime),
                                                                                                 "%H:%M:%S"),
                                                  reservation__end_time__gte=datetime.strptime(str(endtime),
                                                                                               "%H:%M:%S"),
                                                  then=1)))).order_by('count').exclude(id__in=rea).values('name')
                        if room:
                            ab = []
                            for i in room:
                                ab.append(i['name'] + ',')
                            return HttpResponse(ab)
                        else:
                            return HttpResponse('NO_VACANT_ROOM')

            else:
                return HttpResponse('INCORRECT_INPUT')




    return HttpResponse("Test")