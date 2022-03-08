import time

from Common_Function.logger import Logger

logger = Logger(logger="test").getlogger()
logger.info("sssssss")
logger.debug("debug")
time1 = time.strftime("%H", time.localtime())
print(time1)
while 1:
    if time.strftime("%H", time.localtime()) == 12:
        break
    time.sleep(2)
    logger.info('现在是{0}'.format(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(time.time()))))
    logger.debug("debug")
