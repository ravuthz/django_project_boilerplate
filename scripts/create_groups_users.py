from admin_interface.models import Theme
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from django.core.management import BaseCommand

from users.models import User

USER = 1
ADMIN = 2
SUPER = 3

GROUP_CHOICES = (
    (USER, "user"),
    (ADMIN, "admin"),
    (SUPER, "supervisor"),
)


def create_groups_users():
    print("starting create_groups_users()")
    for index, name in GROUP_CHOICES:
        group, group_created = Group.objects.get_or_create(name=name)

        if group_created:
            print("Create new group:", group)
            superuser = True if (index == ADMIN or index == SUPER) else False
            user, user_created = User.objects.get_or_create(
                username=name, email="{}@gmail.com".format(name),
                is_active=True, is_staff=True, is_superuser=superuser)
            if user_created:
                user.groups.add(group)
                user.set_password("123123")
                user.save()
                print("Create new user:", user)
            elif user:
                print("User is existed:", user)
        elif group:
            print("Group existed:", group)
    print("finished create_groups_users()\n")


def assign_group_permissions():
    print("starting assign_group_permissions()")
    group_names = dict(GROUP_CHOICES)

    session_perms = Permission.objects.filter(content_type=ContentType.objects.get_for_model(Session))
    theme_perms = Permission.objects.filter(content_type=ContentType.objects.get_for_model(Theme))
    permission_perms = Permission.objects.filter(content_type=ContentType.objects.get_for_model(Permission))
    group_perms = Permission.objects.filter(content_type=ContentType.objects.get_for_model(Group))
    user_perms = Permission.objects.filter(content_type=ContentType.objects.get_for_model(User))

    user_group = Group.objects.get(name=group_names[USER])
    admin_group = Group.objects.get(name=group_names[ADMIN])
    super_group = Group.objects.get(name=group_names[SUPER])

    if user_group:
        permissions = Permission.objects.filter(
            content_type=ContentType.objects.get_for_model(User),
            codename__in=['view_user', 'change_user']
        )
        user_group.permissions.set(permissions)
        print("Assigned permissions to group:", user_group)

    if admin_group:
        admin_group.permissions.set(theme_perms)
        admin_group.permissions.set(session_perms)
        admin_group.permissions.set(permission_perms)
        admin_group.permissions.set(group_perms)
        admin_group.permissions.set(user_perms)
        print("Assigned permissions to group:", admin_group)

    if super_group:
        permissions = Permission.objects.all()
        super_group.permissions.set(permissions)
        print("Assigned permissions to group:", super_group)

    print("Finished assign_group_permissions()\n")


def run(*args):
    try:
        command = BaseCommand()
        command.stdout.write(command.style.SUCCESS('Executing {}\n'.format(__file__)))

        create_groups_users()
        assign_group_permissions()

    except Exception as exc:
        print(exc)
