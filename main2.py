import time 
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib  
import math
import numpy as np

# GpioPins = [17, 18, 27, 22]

# T = 2  # Period [s]
# N_period = 2  # No. of periods
# amp = 72
# unit_angle = 7.2
# s_angle = 1.8  # [deg]
# N = int(4*amp/unit_angle)

# theta = amp*np.sin(np.linspace(0, 2*math.pi, N))  # Angle time history [deg]
# dt = T/len(theta)  # time-step [s]
# omega = np.gradient(theta, dt)/360  # [Hz]
# omega_pos = abs(omega)
# pm = omega < 0  # boolean for CW/CCW 
# wait = (1/omega_pos)*(s_angle/360)/2

# mymotortest = RpiMotorLib.BYJMotor('MyMotorOne', 'Nema')
# time.sleep(0.002)

# for _ in np.arange(N_period):
#     for k in np.arange(N):
#         mymotortest.motor_run(GpioPins, wait[k], 2048, pm[k], False, "half", 0)

GPIO.cleanup()
