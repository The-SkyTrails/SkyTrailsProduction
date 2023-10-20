from django.core.management.base import BaseCommand
from crm_app.models import Enquiry  # Replace 'app' with your app name
from faker import Faker

class Command(BaseCommand):

    help = 'Generate and insert fake data into the Student model'

    def handle(self, *args, **kwargs):
        fake = Faker()

        self.stdout.write(self.style.SUCCESS('Generating fake student data...'))

        for _ in range(10):  # Generate 10 fake records, adjust as needed
            fake_email = fake.email()
            fake_contact = fake.contact()
            faker_Salutation = fake.Salutation()
            faker_FirstName = fake.firstname()
            faker_lastName = fake.lastname()
            faker_Dob = fake.dob()
            faker_Gender = fake.gender()
            faker_Country = fake.Country()
            faker_Visa_country = fake.Visa_country()
            faker_Visa_category = fake.Visa_category()
            faker_Visa_subcategory = fake.Visa_subcategory()
            faker_Visa_type = fake.Visa_type()
            faker_Package = fake.Package()
            faker_Source = fake.Source()
            faker_Reference = fake.Reference()

            

            # Create an instance of Student with fake data and save it
            new_student = Enquiry(country=fake_country, status=fake_status)
            new_student.save()

        self.stdout.write(self.style.SUCCESS('Fake student data generated and inserted successfully.'))
