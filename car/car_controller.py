import RPi.GPIO as gpio
import time

FRIGHT_1 = 24
FRIGHT_2 = 23
FRIGHT_PWM = 16
BRIGHT_1 = 17
BRIGHT_2 = 27
BRIGHT_PWM = 18
FLEFT_1 = 6
FLEFT_2 = 5
FLEFT_PWM = 13
BLEFT_1 = 20
BLEFT_2 = 21
BLEFT_PWM = 19
gpio.setmode(gpio.BCM)
gpio.setup(FRIGHT_PWM, gpio.OUT)
gpio.setup(BRIGHT_PWM, gpio.OUT)
gpio.setup(FLEFT_PWM, gpio.OUT)
gpio.setup(BLEFT_PWM, gpio.OUT)
gpio.setup(FRIGHT_1, gpio.OUT)
gpio.setup(FRIGHT_2, gpio.OUT)
gpio.setup(BRIGHT_1, gpio.OUT)
gpio.setup(BRIGHT_2, gpio.OUT)
gpio.setup(FLEFT_1, gpio.OUT)
gpio.setup(FLEFT_2, gpio.OUT)
gpio.setup(BLEFT_1, gpio.OUT)
gpio.setup(BLEFT_2, gpio.OUT)
pwmfr = gpio.PWM(FRIGHT_PWM, 100)
pwmbr = gpio.PWM(BRIGHT_PWM, 100)
pwmfl = gpio.PWM(FLEFT_PWM, 100)
pwmbl = gpio.PWM(BLEFT_PWM, 100)
pwmbr.start(0)
pwmfr.start(0)
pwmbl.start(0)
pwmfl.start(0)

def change_pwm(dc1, dc2, dc3, dc4):
    pwmbl.ChangeDutyCycle(dc1)
    pwmfl.ChangeDutyCycle(dc2)
    pwmfr.ChangeDutyCycle(dc3)
    pwmbr.ChangeDutyCycle(dc4)

def stop():
    change_pwm(0, 0, 0, 0)
    gpio.output(FRIGHT_1, gpio.HIGH)
    gpio.output(FRIGHT_2, gpio.HIGH)
    gpio.output(BRIGHT_1, gpio.HIGH)
    gpio.output(BRIGHT_2, gpio.HIGH)
    gpio.output(FLEFT_1, gpio.HIGH)
    gpio.output(FLEFT_2, gpio.HIGH)
    gpio.output(BLEFT_1, gpio.HIGH)
    gpio.output(BLEFT_2, gpio.HIGH)

def forward(tf, dc1, dc2, dc3, dc4):
    change_pwm(dc1, dc2, dc3, dc4)
    gpio.output(FRIGHT_1, gpio.HIGH)
    gpio.output(FRIGHT_2, gpio.LOW)
    gpio.output(BRIGHT_1, gpio.HIGH)
    gpio.output(BRIGHT
    gpio.output(FLEFT_1, gpio.HIGH)
    gpio.output(FLEFT_2, gpio.LOW)
    gpio.output(BLEFT_1, gpio.HIGH)
    gpio.output(BLEFT_2, gpio.LOW)
    time.sleep(tf)
    stop()

def reverse(tf, dc1, dc2, dc3, dc4):
    change_pwm(dc1, dc2, dc3, dc4)
    gpio.output(FRIGHT_1, gpio.LOW)
    gpio.output(FRIGHT_2, gpio.HIGH)
    gpio.output(BRIGHT_1, gpio.LOW)
    gpio.output(BRIGHT_2, gpio.HIGH)
    gpio.output(FLEFT_1, gpio.LOW)
    gpio.output(FLEFT_2, gpio.HIGH)
    gpio.output(BLEFT_1, gpio.LOW)
    gpio.output(BLEFT_2, gpio.HIGH)
    time.sleep(tf)
    stop()

def fullright(tf, dc1, dc2, dc3, dc4):
    change_pwm(dc1, dc2, dc3, dc4)
    gpio.output(FRIGHT_1, gpio.LOW)
    gpio.output(FRIGHT_2, gpio.HIGH)
    gpio.output(BRIGHT_1, gpio.LOW)
    gpio.output(BRIGHT_2, gpio.HIGH)
    gpio.output(FLEFT_1, gpio.HIGH)
    gpio.output(FLEFT_2, gpio.LOW)
    gpio.output(BLEFT_1, gpio.HIGH)
    gpio.output(BLEFT_2, gpio.LOW)
    time.sleep(tf)
    stop()

def fullleft(tf, dc1, dc2, dc3, dc4):
    change_pwm(dc1, dc2, dc3, dc4)
    gpio.output(FRIGHT_1, gpio.HIGH)
    gpio.output(FRIGHT_2, gpio.LOW)
    gpio.output(BRIGHT_1, gpio.HIGH)
    gpio.output(BRIGHT_2, gpio.LOW)
    gpio.output(FLEFT_1, gpio.LOW)
    gpio.output(FLEFT_2, gpio.HIGH)
    gpio.output(BLEFT_1, gpio.LOW)
    gpio.output(BLEFT_2, gpio.HIGH)
    time.sleep(tf)
    stop()
