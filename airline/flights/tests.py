from django.test import TestCase,Client
from django.db.models import Max
from .models import *

# Create your tests here.
# Test olduğunu belirtik
class FlightTestCase(TestCase):
    # to define virtual db and add some data, we use setUP(self) function
    def setUp(self):
        # Create airports
        a1 = Airplane.objects.create(code="AAA", city="City A")
        a2 = Airplane.objects.create(code="BBB", city="City B")
        # Create flights
        Flights.objects.create(origin=a1, destination=a2,duration="100")
        Flights.objects.create(origin=a1, destination=a1,duration="100")

    def test_departures_count(self):
        a = Airplane.objects.get(code="AAA")
        self.assertEqual(a.departure.count(),3)

        