from ulogging import Logger

logger = Logger("logger.log")

@logger.log_it_low_importance
def func1(a):
    return a

@logger.log_it_low_importance
def func2(a):
    return a / 0

@logger.log_it_high_importance
def func3(a):
    return a / 0

logger.log_here("TEST")

func1(1)
func2(1)
func3(1)

logger.file.close()

"""
Output:
WORKING STARTED: 2022-06-03 16:32:56
1. 2022-06-03 16:32:56 <TEST>
2. 2022-06-03 16:32:56 [ALL OK] <func1>(1){1} ~NO ERRORS~
3. 2022-06-03 16:32:56 [ERROR (LOW IMPORTANCE)] <func2>(1) ~ERROR: division by zero~
4. 2022-06-03 16:32:56 [ERROR (!!!HIGH IMPORTANCE!!!)] <func3>(1) ~ERROR: division by zero~
"""