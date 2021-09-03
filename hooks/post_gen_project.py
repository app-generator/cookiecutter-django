"""POST gen hook
"""
import logging
import os
import shutil
import sys
from distutils.dir_util import copy_tree

_logger = logging.getLogger()
TMP_DIR = './tmp/' 

def post_hook():
    """Flag the POST gen HOOK execution"""
    _logger.warning("POST Gen hook executed")

    try:

        print(' *** Copy assets') 
        fromDirectory = TMP_DIR + "core/static"
        toDirectory   = "./core/static"

        copy_tree(fromDirectory, toDirectory)
        print(' ...done')

        print(' *** Copy templates') 
        fromDirectory = TMP_DIR + "core/templates"
        toDirectory   = "./core/templates"

        copy_tree(fromDirectory, toDirectory)
        print(' ...done')

        shutil.copy( TMP_DIR + "CHANGELOG.md", "CHANGELOG.md")
        shutil.copy( TMP_DIR + "LICENSE.md"  , "LICENSE.md")

        print('Remove `tmp` dir')
        shutil.rmtree( TMP_DIR )
        print(' ...done')

    except OSError as e:
        #_logger.warning("While attempting to remove file(s) an error occurred")
        _logger.warning(f"Error: {e}")
        sys.exit(0)

    # Exit with success     
    sys.exit(0)

if __name__ == "__main__":
    post_hook()
