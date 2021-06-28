#!/usr/bin/env python
import os
import sys

from django.conf import settings

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "switch.settings")

    if settings.DEBUG:
        if os.environ.get('RUN_MAIN'):
            if os.environ.get('VSC_DEBUG'):
                import ptvsd

                ptvsd.enable_attach(address=('0.0.0.0', 3000))
                ptvsd.wait_for_attach()
                print('Attached!')
            
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()

