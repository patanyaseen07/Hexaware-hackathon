from django.core.management.base import BaseCommand
from batch_allocation.models import Batch

class Command(BaseCommand):
    help = 'Insert predefined batches into the Batch table'

    def handle(self, *args, **kwargs):
        # Define the batches
        batches = [
            {"id": 1, "name": "Java Batch", "programming_languages": "Java", "max_candidates": 30, "current_candidates": 0, "min_candidates": 25},
            {"id": 2, "name": ".NET Batch", "programming_languages": ".NET", "max_candidates": 30, "current_candidates": 0, "min_candidates": 25},
            {"id": 3, "name": "Data Engineering Batch", "programming_languages": "Python, SQL", "max_candidates": 30, "current_candidates": 0, "min_candidates": 25},
        ]

        # Insert or update each batch
        for batch_data in batches:
            batch, created = Batch.objects.update_or_create(
                id=batch_data["id"],
                defaults=batch_data
            )
            action = "Inserted" if created else "Updated"
            self.stdout.write(self.style.SUCCESS(f"{action} batch: {batch.name}"))

        self.stdout.write(self.style.SUCCESS('Successfully inserted/updated all batches in the Batch table.'))
