import logging
logging.basicConfig(format='%(message)s')
errorHandle = []

# server authorisation check
def infoLogger(origin, info):
    print(f"##\nInfo Logger for {origin}\nMessage:{info}\n##")
    return 0

# server authorisation check
def errorLogger(origin, error):
    errorHandle.append(f'##\nLocation:{origin}\nError:{error}\n##')

def errorTrigger():
    global errorHandle
    if(len(errorHandle) > 0):
        logging.error(errorHandle[0])
