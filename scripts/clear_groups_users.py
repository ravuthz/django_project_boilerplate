from django.contrib.auth.models import Group
from django.core.management import BaseCommand

from users.models import User


def run(*args):
    try:
        command = BaseCommand()
        command.stdout.write(command.style.SUCCESS('Executing {}\n'.format(__file__)))

        User.objects.all().delete()
        Group.objects.all().delete()

    except Exception as exc:
        print(exc)
