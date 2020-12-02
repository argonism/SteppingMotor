import time 
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

class NonStopStepping:
    def __init__(self, GpioPins):
      self.step_degree = 5.625
      self.GpioPins = GpioPins
      self.motor = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")
      self.step_per_ms = 1 / (2048 / 4)
      self.reverse = False
    
    def run(self):
      while True:
        self.motor.motor_run(self.GpioPins, 0.0005, 1, reverse, False, "half", 0)

class SteppingMotor:
  def __init__(self, GpioPins):
    self.step_degree = 5.625
    self.GpioPins = GpioPins
    self.motor = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")
    self.step_per_ms = 1 / (2048 / 4)

  def rotate(self, degree, wait = 0.001, reverse=False):
    step_num = self.calc_step(degree)
    self.motor.motor_run(self.GpioPins, wait, step_num, reverse, False, "half", 0)
  
  def rotate_with_step(self, step, reverse=False, wait = 0.001):
    self.motor.motor_run(self.GpioPins, wait, step, reverse, False, "half", 0)


  def calc_step(self, degree):
    if degree <= self.step_degree:
      return 1
    else:
      return degree / self.step_degree * 8
  
  def rotate_with_ms(self, ms, wait=0.001, reverse=False):
    step = self.step_per_ms * ms
    self.motor.motor_run(self.GpioPins, wait, step, reverse, False, "half", 0)

if __name__ == "__main__":
   # GPIOピン．左からIN1, IN2, IN3, IN4に接続するピン
  GpioPins = [17, 18, 27, 22]
  motor = SteppingMotor(GpioPins)
  # 180度回転
  while True:
    motor.rotate(50)
    motor.rotate(50, reverse=True)

  GPIO.cleanup()