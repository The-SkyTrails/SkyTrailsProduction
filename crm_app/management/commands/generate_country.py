from django.core.management.base import BaseCommand
from crm_app.models import VisaCountry  # Replace 'app' with your app name
from faker import Faker

class Command(BaseCommand):

    help = 'Generate and insert fake data into the Student model'

    def handle(self, *args, **kwargs):
        fake = Faker()

        self.stdout.write(self.style.SUCCESS('Generating fake student data...'))

        for _ in range(10):  # Generate 10 fake records, adjust as needed
            fake_country = fake.country()
            fake_status = fake.boolean()
            

            # Create an instance of Student with fake data and save it
            new_student = VisaCountry(country=fake_country, status=fake_status)
            new_student.save()

        self.stdout.write(self.style.SUCCESS('Fake student data generated and inserted successfully.'))
