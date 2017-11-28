import logging
import logging.config
import time
import os

def setup_logging():
    """
    Setup logging configuration

    Returns
    -------

    """

    logging.Formatter.converter = time.gmtime
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "%(asctime)s - %(name)s - %(funcName)s():%(lineno)i -  %(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "stream": "ext://sys.stdout",

            },
            "file": {
                "class": "logging.FileHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "filename": "logconfig.log"

            }

        },
        "loggers": {
            "ts_core": {
                "level": "INFO",
                "handlers": ['console'],
                "propagate": False,
            },
            'requests.packages.urllib3': {
                'handlers': ['console'],
                'level': logging.WARNING
            }
        },
        "root": {
            "level": "INFO",
            "handlers": ['console']
        }
    }

    logging.config.dictConfig(config)
    return
