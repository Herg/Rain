
from RPi import GPIO
import time

#################################

GPIO_PIN_OUT = 11
DEFAULT_LIGHT_TIME = 15

#################################

class led_service(object):

    def light_em_up(self, LIGHT_TIME = DEFAULT_LIGHT_TIME):
        # setup
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(GPIO_PIN_OUT, GPIO.OUT)

        # output
        GPIO.output(GPIO_PIN_OUT, True)
        time.sleep(LIGHT_TIME)
        GPIO.output(GPIO_PIN_OUT, False)

        # cleanup
        GPIO.cleanup()
