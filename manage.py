#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import re
import socket
import sys


def main():
    """Run administrative tasks."""
    if re.match(r"Kaysons-MacBook-Pro", socket.gethostname()):
        settings_name = "development"
    else:
        settings_name = "production"

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "project.settings." + settings_name)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
