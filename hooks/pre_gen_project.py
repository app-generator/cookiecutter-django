"""PRE gen hook
"""
import logging
import os
import shutil
import sys
import git 

_logger = logging.getLogger()
TMP_DIR = './tmp/' 

def pre_hook():
    """Flag the PRE gen HOOK execution"""
    _logger.warning("PRE Gen hook executed")

    try:

        # Default value = Volt
        theme = "{{cookiecutter.theme}}"
        repo  = 'https://github.com/app-generator/django-dashboard-volt.git'

        if 'material-dashboard' == theme:
            repo  = 'https://github.com/app-generator/django-dashboard-material.git'

        if 'soft-ui' == theme:
            repo  = 'https://github.com/app-generator/django-soft-ui-dashboard.git'

        if 'datta-able' == theme:
            repo  = 'https://github.com/app-generator/django-datta-able.git'

        if 'star-admin' == theme:
            repo  = 'https://github.com/app-generator/django-star-admin.git'

        print(' Cloning theme: <' + theme + '>, REPO: ' + repo )

        repo = git.Repo.clone_from( repo, TMP_DIR, branch='master')
        print(' ...done')
               
    except OSError as e:
        _logger.warning(f"Error: {e}")
        sys.exit(0)

    # Exit with success
    sys.exit(0)

if __name__ == "__main__":
    pre_hook()
