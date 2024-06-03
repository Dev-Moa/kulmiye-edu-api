from django.core.management.base import BaseCommand
from ...models import Program, Degree
from uuid import uuid4

class Command(BaseCommand):
    help = 'Adds programs to the Program model'

    def handle(self, *args, **options):
        degree = Degree.objects.get(degree_name='Bachelor')  # Replace with the appropriate degree object
        # print(degree)
        programs = [
            'Biology and Chemistry',
            'Education Management',
            'Mathematics and Chemistry',
            'Arabic Language Islamic Studies',
            'History & Geography',
            'English & History',
            'English & Geography',
            'Geographic Information System',
            'Social Work',
            'Math & Physics',
            'Somalia',
            'Mathematics',
            'Biology/Chemistry',
            'Math/Physics',
            'English and Literature',
            'Agriculture',
            'Veterinary'
        ]
        for program_name in programs:
            program = Program.objects.create(
                program_name=program_name,
                degree=degree,
                year=4  # Replace with the appropriate year
            )
            program.save()
        self.stdout.write(self.style.SUCCESS('Successfully added programs'))


