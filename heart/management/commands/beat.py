from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help = 'Heart beat - runs scheduled tasks'
    
    def handle(self, *args, **options):
        self.stdout.write(f"[{timezone.now()}] ❤️ Heart beating...")
        self.stdout.write(f"[{timezone.now()}] ✅ Heart beat complete")
