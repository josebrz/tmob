#!/usr/bin/env python
import os
import sys

env_to_print = [
    ("DB select:", "PG_NAME"),
    ("Debug mode:", "DEBUG"),
    ("Stage:", "STAGE")
]


def print_enviroments(env_list):
    for env in env_list:
        print(env[0], os.getenv(env[1]))


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line

        if os.getenv("DEBUG"):
            print_enviroments(env_to_print)

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
