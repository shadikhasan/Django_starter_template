# import necessary modules
import os
import csv
from django.conf import settings
from task.models import Task

# Define the path for your CSV files
TASK_METADATA_CSV = os.path.join(settings.DATA_DIR, "MOCK_DATA.csv")

# Define a function to load data from the CSV file into the Task model
def load_data():
    dataset = []
    with open(TASK_METADATA_CSV, newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data = {
                'title': row.get("title", None),
                'completed': False,  # You can set completed status as per your requirement
                'date': row.get("date", None),  # Adjust as per your CSV columns
            }
            # Create a Task object and save it to the database
            task = Task(**data)
            task.save()
            dataset.append(data)  # Optionally, you can append the data to the dataset list
    return dataset

print(load_data())