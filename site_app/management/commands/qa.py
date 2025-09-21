import subprocess
from io import StringIO

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):
    help = 'Initialize app data'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '--apply',
            action='store_true',
            help='Reset',
        )

    def _print(self, msg: str, is_ok: bool = True) -> None:
        if is_ok:
            self.stdout.write(
                self.style.SUCCESS(msg)
            )
        else:
            self.stdout.write(
                self.style.ERROR(msg)
            )

    def handle(self, *args, **options) -> None:  # noqa: ARG002
        apply_changes: bool = bool(options.get('apply', False))
        output = StringIO()
        ruff_items = ['ruff', 'check', '.']

        call_command('check', stdout=output)
        msg = output.getvalue()
        self._print(msg, 'no issues' in msg)

        if apply_changes:
            ruff_items.append('--fix')

        subprocess.run(ruff_items)
