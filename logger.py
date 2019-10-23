import logging, json
from logging.handlers import RotatingFileHandler

log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

with open('config.json', 'r') as f:
    config = json.load(f)

logFile = config['DEV']['LogFileName']
logFileCount = config['DEV']['LogFileCount']


my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=10*1024*1024,backupCount=logFileCount, encoding=None, delay=0)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.INFO)
app_log = logging.getLogger('root')
app_log.setLevel(logging.INFO)
app_log.addHandler(my_handler)