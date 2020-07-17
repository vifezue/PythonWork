import logging
import datetime


class Log:
    """https://docs.python.org/2/library/logging.html
    
        This module defines functions and classes which implement a 
        flexible event logging system for applications and libraries.
    """

    logging.basicConfig(filename='/example/log.txt', level=logging.DEBUG)
    logger = logging.getLogger('log')
    handler = logging.FileHandler('/example/log.txt')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def logAction(self, logtype, message):
        if logtype.lower() == "application error":
            logging.critical(logtype.lower() + " " + message)

        if logtype.lower() == "folder created":
            logging.critical(logtype.lower() + " " + message)

        if logtype.lower() == "skipped folder":
            logging.critical(logtype.lower() + " " + message)

        if logtype.lower() == "file copied":
            logging.critical(logtype.lower() + " " + message)

        if logtype.lower() == "started application":
            logging.critical(message + " " + logtype.lower())
