# yourapp/management/commands/load_initial_data.py
from django.core.management.base import BaseCommand
from task.models import Task  # Update this import statement to import your Task model
from core.utils import load_data  # Remove this line if it's not relevant

class Command(BaseCommand):
    help = 'Load initial data into the database'

    def handle(self, *args, **options):

        # Here you might load data from a CSV file if necessary
        # If you're not loading from a CSV, you can remove this loop
        for i, task_data in enumerate(load_data()):
            task = Task.objects.create(
                title=task_data['title'],
                completed=task_data['completed'],
                date=task_data['date']
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data'))
