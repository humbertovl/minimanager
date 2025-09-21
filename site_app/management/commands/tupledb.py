from django.core.management.base import BaseCommand, CommandParser

from site_app.data.custom_seeder import DataSeeder
from site_app.models.currency import Currency


class Command(BaseCommand):
    help = 'Initialize app data'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '--reset',
            action='store_true',
            help='Reset',
        )

    def handle(self, *args, **options) -> None:  # noqa: ARG002
        if options.get('reset', False):
            Currency.objects.all().delete()
            self.stdout.write(
                self.style.SUCCESS('Data reseted successfully')
            )

        for c in DataSeeder.get_currencies():
            Currency.objects.get_or_create(
                defaults={
                    'name': c.name,
                },
                label=c.label,
                kind=c.kind,
            )

        self.stdout.write(
            self.style.SUCCESS('Data successfully initialized')
        )
