# write a python script that adds all the numbers entered in the command line as arguments.
# Throw an error if user enters something other than number

import sys

import logging
import logging.config

logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger("sLogger")

logger.debug("This is a debug message")

for i in range(1, len(sys.argv)):
    x = int(sys.argv[i])
    if not x:
        raise ValueError("Invalisdfsdfd")


print(x)
