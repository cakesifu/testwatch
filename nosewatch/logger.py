import os
import sys
import logging

logger = logging.getLogger("nosewatch")
if os.environ.get('DEBUG', False):
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(name)s - %(message)s')
log_handler = logging.StreamHandler(sys.stdout)
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)
