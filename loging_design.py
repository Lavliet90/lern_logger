import logging
import requests
'''
NOTSET - 0
DEBUG - 10
INFO - 20
WARNING - 30
ERROR - 40
CRITICAL - 50
'''
logging.basicConfig(level='DEBUG', filename='mylog.log')
logger = logging.getLogger()
print(logger)
logger.setLevel('DEBUG')
print(logger.level)
print(logger.handlers)


logging.getLogger('urllib3').setLevel('CRITICAL')

# for key in logging.Logger.manager.loggerDict:
#     print(key)


def main(name):
    logger.debug(f'Enter in the main() function: name = {name}')

    r = requests.get('http://www.google.ru')


if __name__ == '__main__':
    main('Yan')
