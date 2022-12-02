import logging
import os
from datetime import datetime
import os

#log file name
LOG_FILE_NAME = f"{datetime.now().strftime('%d%m%Y__%H%M%M')}.log"

#log directory name
LOG_FILE_DTR = os.path.join(os.getcwd(),"logs")

LOG_FIle_PATH = os.path.join(LOG_FILE_DTR,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)