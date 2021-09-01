"""POST gen hook
"""
import logging
import os
import shutil
import sys

_logger = logging.getLogger()

def post_hook():
    """Flag the POST gen HOOK execution"""
    _logger.warning("POST Gen hook executed")

    # Exit with success     
    sys.exit(0)

if __name__ == "__main__":
    post_hook()
