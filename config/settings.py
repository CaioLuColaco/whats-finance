from dotenv import load_dotenv
import os

try:
    if os.environ['PYTHON_ENV'] == 'DEV':
        load_dotenv()
except KeyError:
    load_dotenv()


SERVER_SALES_ORDER_ROBOT_PORT = os.environ.get('SERVER_SALES_ORDER_ROBOT_PORT')

