import RPi.GPIO as GPIO
import time
import signal
import sys

pinS = 16
pinB = 23
count = 0
sleeptime = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinS, GPIO.OUT)
GPIO.setup(pinB, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def signal_handler(signal, frame):
	GPIO.cleanup()
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

while True:
	input_state = GPIO.input(pinB)
	GPIO.output(pinS, False)
	if (input_state == False) & (count < 3):
		count+=1
		time.sleep(sleeptime)
		print('snooze: ' + str(count))

	if count > 2:
		GPIO.output(pinS, True)
		time.sleep(0.05)
		GPIO.output(pinS,False)
		time.sleep(0.05)
		input_state = False