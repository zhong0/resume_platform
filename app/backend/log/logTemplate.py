import logging
import os
import json
import datetime
from utils import params as const

class JSONLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        if not self.logger.hasHandlers():
            self._setup_logger()
    
    def _setup_logger(self):
        log_path = self._get_log_file_path()
        log_level = getattr(logging, const.LOG_LEVEL, logging.INFO)
        
        self.logger.setLevel(log_level)
        handler = logging.FileHandler(log_path)
        handler.setLevel(log_level)
        handler.setFormatter(self._json_formatter())
        
        self.logger.addHandler(handler)
    
    def _get_log_file_path(self):
        log_dir = "./log"
        os.makedirs(log_dir, exist_ok=True)
        return os.path.join(log_dir, f"log-{datetime.date.today().strftime('%Y%m%d')}.log")
    
    def _json_formatter(self):
        return logging.Formatter(fmt=json.dumps({
            "logger": "%(name)s",
            "timestamp": "%(asctime)s",
            "level": "%(levelname)s",
            "message": "%(message)s"
        }, ensure_ascii=False), datefmt='%Y-%m-%d %H:%M:%S')
    
    def get_logger(self):
        return self.logger