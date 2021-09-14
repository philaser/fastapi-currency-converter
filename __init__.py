import logging


format = '[%(asctime)s]{%(pathname)s:%(lineno)d}%(levelname)s- %(message)s'
logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S",
                        handlers=[logging.FileHandler("example1.log"),
                  logging.StreamHandler()])

logger = logging.getLogger(__name__)