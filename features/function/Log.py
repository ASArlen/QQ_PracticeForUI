
import logging

def Log():


    logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    logger = logging.getLogger('automation')
    return logger


# 提供单例使用
logger = Log()

if __name__ == '__main__':
    logger = Log()
    n = 'abc'
    logger.info('automation test log:%s' % n)

