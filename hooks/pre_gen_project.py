"""PRE gen hook
"""
import logging
import os
import shutil
import sys

_logger = logging.getLogger()

def pre_hook():
    """Flag the PRE gen HOOK execution"""
    _logger.warning("PRE Gen hook executed")

    # Exit with success     
    sys.exit(0)

if __name__ == "__main__":
    pre_hook()
