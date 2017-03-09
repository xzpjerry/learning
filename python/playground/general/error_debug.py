import logging
logging.basicConfig(level = logging.DEBUG)
# debug, info, warning, error
s = '0'
num_s = int(s)
logging.info('n = %d' % num_s)
print(10/num_s)