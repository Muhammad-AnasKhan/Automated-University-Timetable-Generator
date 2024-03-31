# myapp/management/commands/setup_roles.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User

"""
Custom commands Setup roles

execute this using: 

python manage.py setup_roles
"""
class Command(BaseCommand):
    help = 'Creates the initial admin and teacher groups'

    def handle(self, *args, **options):
        Group.objects.get_or_create(name='admin')
        Group.objects.get_or_create(name='teacher')
        self.stdout.write(self.style.SUCCESS('Admin and Teacher groups created'))

        # user = User.objects.create_user(username='admin123', password='admin123',first_name='admin123', last_name='admin123')
        # teacher_group = Group.objects.get(name='admin')
        # teacher_group.user_set.add(user)
