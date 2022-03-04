import time

from Common_Function.logger import Logger

logger = Logger(logger="test").getlogger()
logger.info("sssssss")
logger.debug("debug")
time1 = time.strftime("%H",time.localtime())
print(time1)
while 1:
    if time.strftime("%H",time.localtime())==18:
        break
    time.sleep(40)
    logger.info('现在是{0}{1}'.format(time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))))
    logger.debug("debug")