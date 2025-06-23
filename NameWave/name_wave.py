import time
import numpy as np
from math import pi, sin

from ah_wrapper.ah_serial_client import AHSerialClient

client = AHSerialClient(write_thread=True, baud_rate=460800)

try:
    ### TODO: Implement your name wave code here ###
    client.set_position(0)
except KeyboardInterrupt:
    pass
finally:
    client.close()

