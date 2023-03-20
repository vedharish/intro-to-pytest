import time

from testselection.config import GLOBAL_TIME_SCALE

class Helper():
    @staticmethod
    def add_sleep(current_scale):
        time.sleep(GLOBAL_TIME_SCALE * current_scale)
