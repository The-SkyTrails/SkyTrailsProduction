from django.core.management.base import BaseCommand
from crm_app.models import VisaCategory,VisaCountry  # Replace 'app' with your app name
from faker import Faker

class Command(BaseCommand):
    help = 'Generate and insert fake VisaCategory data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        self.stdout.write(self.style.SUCCESS('Generating fake Category data...'))
        visa_countries = VisaCountry.objects.all()

        for _ in range(10):  # Generate 10 fake records, adjust as needed
            fake_category = fake.random_element(elements=("visitor visa", "single visa", "Tourist", "work permit", "Business Visa", "Student Visa (F1)", "PR", "holiday"))
            fake_status = fake.boolean()
            
            # Select a random VisaCountry object
            random_visa_country = fake.random_element(visa_countries)

            # Create an instance of VisaCategory with fake data and a specific VisaCountry
            new_category = VisaCategory(
                visa_country_id=random_visa_country,
                category=fake_category,
                status=fake_status
            )
            new_category.save()

        self.stdout.write(self.style.SUCCESS('Fake Category data generated and inserted successfully.'))