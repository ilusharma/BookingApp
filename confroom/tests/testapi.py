from django.test import TestCase

from confroom.models import ConferenceRoom, Reservation
from confroom.serializers import ConferenceRoomSerailizer, ReservationSerializer
from django.test import Client
c = Client()
class Case1(TestCase):
    def test_ok(self):

        print("\n\n In case 1 BOOK 15:00 16:30 2 sharing room already book but in VACANCY 15:45 16:00 your output show vacancy but it should show not available")

        book_1 = ConferenceRoom.objects.create(name='C-Contact', capacity=3)
        book_2 = ConferenceRoom.objects.create(name='S-Sharing', capacity=7)
        book_3 = ConferenceRoom.objects.create(name='T-Team', capacity=20)

        response = c.post('/', {'type': 'VACANCY', 'start_time': '10:00', 'end_time': '12:00'})
        print(response.content)
        response = c.post('/', {'type':'BOOK','person': '2', 'start_time': '11:00', 'end_time': '11:45'})
        print(response.content)
        response = c.post('/', {'type':'BOOK','person': '35', 'start_time': '11:30', 'end_time': '13:00'})
        print(response.content)
        response = c.post('/', {'type':'BOOK','person': '15', 'start_time': '11:30', 'end_time': '13:00'})
        print(response.content)
        response = c.post('/', {'type': 'VACANCY', 'start_time': '11:30', 'end_time': '12:00'})
        print(response.content)
        response = c.post('/', {'type':'BOOK','person': '3', 'start_time': '14:00', 'end_time': '15:30'})
        print(response.content)
        response = c.post('/', {'type':'BOOK','person': '2', 'start_time': '15:00', 'end_time': '16:30'})
        print(response.content)
        response = c.post('/', {'type':'BOOK','person': '12', 'start_time': '15:15', 'end_time': '12:15'})
        print(response.content)
        response = c.post('/', {'type': 'VACANCY', 'start_time': '15:30', 'end_time': '16:00'})
        print(response.content)
        response = c.post('/', {'type':'BOOK','person': '2', 'start_time': '15:30', 'end_time': '16:30'})
        print(response.content)
        response = c.post('/', {'type': 'VACANCY', 'start_time': '15:45', 'end_time': '16:00'})
        print(response.content)
        response = c.post('/', {'type':'BOOK','person': '5', 'start_time': '16:00', 'end_time': '17:00'})
        print(response.content)
        response = c.post('/', {'type': 'VACANCY', 'start_time': '18:00', 'end_time': '19:00'})
        print(response.content)

        print('--------Test____over--------')


class Case2(TestCase):
    def test_ok(self):

        print('\n \nas given Documents in rules point 6 No meetings can be scheduled during the buffer time. If the booking time overlaps with the buffer\
time NO_VACANT_ROOM should be printed. according to that the second case output data is not correct provided by you')

        book_1 = ConferenceRoom.objects.create(name='C-Contact', capacity=3)
        book_2 = ConferenceRoom.objects.create(name='S-Sharing', capacity=7)
        book_3 = ConferenceRoom.objects.create(name='T-Team', capacity=20)

        response = c.post('/', {'type':'BOOK','person': '2', 'start_time': '09:30', 'end_time': '13:15'})
        print(response.content)
        response = c.post('/', {'type':'BOOK','person': '2', 'start_time': '13:45', 'end_time': '18:45'})
        print(response.content)
        response = c.post('/', {'type':'BOOK','person': '3', 'start_time': '12:55', 'end_time': '14:00'})
        print(response.content)
        response = c.post('/', {'type':'BOOK','person': '6', 'start_time': '13:45', 'end_time': '17:15'})
        print(response.content)
        response = c.post('/', {'type': 'VACANCY', 'start_time': '13:45', 'end_time': '15:00'})
        print(response.content)
        response = c.post('/', {'type':'BOOK','person': '2', 'start_time': '14:00', 'end_time': '15:00'})
        print(response.content)
        response = c.post('/', {'type':'BOOK','person': '12', 'start_time': '17:00', 'end_time': '18:30'})
        print(response.content)
        response = c.post('/', {'type': 'VACANCY', 'start_time': '17:00', 'end_time': '18:00'})
        print(response.content)
        response = c.post('/', {'type': 'VACANCY', 'start_time': '17:30', 'end_time': '18:00'})
        print(response.content)
        response = c.post('/', {'type':'BOOK','person': '12', 'start_time': '17:00', 'end_time': '18:30'})
        print(response.content)
        response = c.post('/', {'type':'BOOK','person': '12', 'start_time': '15:35', 'end_time': '16:35'})
        print(response.content)

        print('--------Test____over--------')





