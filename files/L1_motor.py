from periphery import PWM
import time

# find the pwmchip that has 2 channels:
#   $ ls /sys/class/pwm
#   pwmchip0  pwmchip1  ...
#   $ cat /sys/class/pwm/pwmchipX/npwm   # look for “2”

PWM_CHIP = 1    # replace with the chip number that reports npwm=2
p0 = PWM(3, 1)   # channel 0 → header pin 32 (GPIO12/PWM0)
p1 = PWM(5, 1)   # channel 1 → header pin 33 (GPIO13/PWM1)

# configure and enable
for p in (p0,p1):
    p.frequency = 150
    p.enable()

def drive(speed):
    """speed ∈ [-1.0…+1.0]: + forward, - reverse, 0 stop"""
    if speed > 0:
        p0.duty_cycle = speed
        p1.duty_cycle = 0
    elif speed < 0:
        p0.duty_cycle = 0
        p1.duty_cycle = -speed
    else:
        p0.duty_cycle = 0
        p1.duty_cycle = 0

if __name__ == "__main__":
    try:
        drive(0.8);  time.sleep(4)   # forward
        drive(-0.8); time.sleep(4)   # reverse
        drive(0);    time.sleep(4)   # stop
    finally:
        p0.disable()
        p1.disable()
        p0.close()
        p1.close()