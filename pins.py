import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

GPIO.setup(14,GPIO.OUT)

GPIO.setup(15,GPIO.OUT)


# Define
# Turn all off 
def reset():
    GPIO.output(4,GPIO.LOW)
    GPIO.output(17,GPIO.LOW)
    GPIO.output(18,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(22,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(24,GPIO.LOW)
    GPIO.output(25,GPIO.LOW)
    GPIO.output(5,GPIO.LOW)
    GPIO.output(6,GPIO.LOW)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(16,GPIO.LOW)
    GPIO.output(26,GPIO.LOW)
    
    GPIO.output(14,GPIO.LOW)
    
def error():
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(27,GPIO.HIGH)  

def dot():
    GPIO.output(14,GPIO.HIGH)
    
def red():
    GPIO.output(15,GPIO.HIGH)

def redoff():
    GPIO.output(15,GPIO.LOW)
    
# First Digit
def one():
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)

def two():
    GPIO.output(4,GPIO.HIGH)
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(24,GPIO.HIGH)

def three():
    GPIO.output(4,GPIO.HIGH)
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(24,GPIO.HIGH)
    
def four():
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    
def five():
    GPIO.output(4,GPIO.HIGH)
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(24,GPIO.HIGH)
    
def six():
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(24,GPIO.HIGH)
    
def seven():
    GPIO.output(4,GPIO.HIGH)
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    
def eight():
    GPIO.output(4,GPIO.HIGH)
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(24,GPIO.HIGH)
    
def nine():
    GPIO.output(4,GPIO.HIGH)
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(24,GPIO.HIGH)
    
def zero():
    GPIO.output(4,GPIO.HIGH)
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(24,GPIO.HIGH)

# Second Digit

def oneD():
    GPIO.output(6,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)

def twoD():
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(6,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(26,GPIO.HIGH)

def threeD():
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(6,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(26,GPIO.HIGH)
    
def fourD():
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(6,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    
def fiveD():
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(26,GPIO.HIGH)
    
def sixD():
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(26,GPIO.HIGH)
    
def sevenD():
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(6,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    
def eightD():
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(6,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(26,GPIO.HIGH)
    
def nineD():
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(6,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(26,GPIO.HIGH)
    
def zeroD():
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(6,GPIO.HIGH)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(26,GPIO.HIGH)