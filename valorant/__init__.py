__version__ = "0.0.1"

import logging
import os
import sys
import datetime as datetime

MODULE_PATH = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = os.path.dirname(MODULE_PATH)
PARENT_PATH = os.path.abspath(os.path.join(REPO_PATH, os.pardir))

# Local storage path
DATA_PATH = f"{REPO_PATH}/data/"

# Conmfiguring logs
logger = logging.getLogger(__name__)
logger.propagate = False
handler = logging.StreamHandler(stream=sys.stdout)
formatter = logging.Formatter("[%(levelname)5s] %(asctime)5s %(filename)-15.15s:%(lineno)03d - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# Get today's date
LOAD_DATE: str = datetime.now().strftime('%Y-%m-%d')