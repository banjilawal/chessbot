import logging
import logging.config
from logging.handlers import RotatingFileHandler
import os

# Configuration stays ready but doesn't auto-execute
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'detailed': {
            'format': '%(asctime)s - %(levelname)-8s - %(filename)s:%(lineno)d (%(funcName)s) - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)-8s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'INFO',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            '()': lambda: RotatingFileHandler(
                'logs/app.log',
                maxBytes=5*1024*1024,
                backupCount=3,
                encoding='utf-8'
            ),
            'formatter': 'detailed',
            'level': 'DEBUG'
        }
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'DEBUG'
    }
}

def init_logging():
    """Call this to explicitly start logging"""
    os.makedirs('logs', exist_ok=True)
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(__name__)
    logger.info("Logging operation ready")
    return logger