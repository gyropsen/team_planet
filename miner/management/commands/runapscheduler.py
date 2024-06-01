from django.core.management.base import BaseCommand

from miner.services import start_scheduler


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        start_scheduler()
