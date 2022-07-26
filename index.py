import sys
import traceback
import os

from flask import Flask
from waitress import serve
from apscheduler.schedulers.background import BackgroundScheduler

from config.settings import SERVER_WHATS_FINANCE_ROBOT_PORT

from config import routes
from service.whats_finance_robot import whats_finance_robot
from utils import errorLogger, errorTrigger, infoLogger

app = Flask(__name__)

routes(app)

scheduler = BackgroundScheduler()
scheduler.add_job(whats_finance_robot, trigger='cron', hour='10', minute='00')
scheduler.start()

try:
    infoLogger(os.path.basename(__file__), (f""" PYTHON - COLACO | ROBOT - WHATS FINANCE | listening on port - {SERVER_WHATS_FINANCE_ROBOT_PORT} """))
    serve(app, port=SERVER_WHATS_FINANCE_ROBOT_PORT)
except Exception as error:
    # Prettify Error 
    exc_type, exc_value, exc_traceback = sys.exc_info()
    errorLogger(traceback.format_tb(exc_traceback)[1], error)
finally:
    # Raise Exception if needed
    errorTrigger()
