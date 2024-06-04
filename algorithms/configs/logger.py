# Created by        : MyWork
# Created on        : 2024-05-18
import logging
import sys
from pathlib import Path

logging.basicConfig()

BASE_PATH = Path(__file__).parent.parent.resolve()
LOG_FILE = BASE_PATH / "logfile.log"
LOG_FRMT = logging.Formatter("%(asctime)s %(filename)s [%(levelname)s] : %(message)s")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# HANDLERS
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(LOG_FRMT)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(LOG_FRMT)
logger.handlers = [file_handler, console_handler]
