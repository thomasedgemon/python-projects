import numpy 
import time 
import datetime
import math

ordered_pair = math.modf((time.time()))
base = ordered_pair[0] + ordered_pair[1]
result = (base ** 5) % 100
print(result)