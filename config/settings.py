from dotenv import load_dotenv
import os

try:
    if os.environ['PYTHON_ENV'] == 'DEV':
        load_dotenv()
except KeyError:
    load_dotenv()


SERVER_WHATS_FINANCE_ROBOT_PORT = os.environ.get('SERVER_WHATS_FINANCE_ROBOT_PORT')

NUMBER_WHATSAPP = os.environ.get('NUMBER_WHATSAPP')

LOG_PATH = os.environ.get('LOG_PATH')