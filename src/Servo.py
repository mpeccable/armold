"""
Mpeccable Servo Control
5-14-2026

Script contains a servo class useful for prototyping robotics at home. 
Great for controlling hobby servos on a PCA 9685 driver board. 
"""

from PCA9685 import PCA9685
import time 

class Servo:
    def __init__(self, angleMin, angleMax, PWMmin, PWMmax):
        """
        Creates a servo object for use with hobby grade servos. It is quite 
        convenient to use a PCA9685 module with this code.
        
        Arguments:
            angleMin (float): Minimum angle of output shaft on servo measured 
                in degrees
            angleMax (float): Maximum angle of output shaft on servo measured
                in degrees
            PWMmin (int): The minimum operating pulse width modulation value 
                for the servo as reported by the manufacturer in microseconds
            PWMmax (int): The maximum operating pulse width modulation value
                for the servo as reported by the manufacturer in microseconds
        Returns:
            None - but there is some terminal debugging
        """


        print("Initializing Hardware...")
        self.angleMin=angleMin   # Angle of servo output shaft
        self.angleMax=angleMax     
        # PWMmin and PWMmax are measured in seconds, 
        self.PWMmin=PWMmin/(10**6)
        self.PWMmax=PWMmax/(10**6) 
        
        self.pwm = PCA9685(address=0x40, debug=True)   
        self.pwm.setPWMFreq(50)               # Set the cycle frequency of PWM
        print("Hardware initialized.")
    
    # Convert the input angle to the corresponding value on pca9685
    def map(self,value,fromLow,fromHigh,toLow,toHigh):
        return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow
    
    def shutdown(self):
        print("\nCutting servo power...")
        for i in range(16):
            self.pwm.setServoPulse(i, 0)
        print("\nServos powered off.\n")
        
    def setServoAngle(self, channel, angle):
        if angle < self.angleMin:
            angle = self.angleMin
        elif angle > self.angleMax:
            angle = self.angleMax

        pulsewidth=self.map(angle,self.angleMin,self.angleMax,self.PWMmin,
                      self.PWMmax) 
        
        # pulsewidth is an element of [600 us, 2400 us] for most cheapo servos
        # 0.0006 seconds < pulswidth < 0.0024 seconds
        self.pwm.setServoPulse(channel, int(pulsewidth))
 

# Main program logic follows:
if __name__ == '__main__':
    try:
        while(True): 
            S=Servo(0, 180, 600, 2400)
            for i in range(16):            # Iterate through all 16 servo ports
                print(f"Moving servo #{i}")
                S.setServoAngle(i, 90)          # Send to zero pos
                print(f"Done moving servo #{i}")
            
            end = str(input("Enter \'y\' to end program: "))
            if end == "y":
                break

    except BaseException as ex:
        print(f"Exception {ex} in code")

    finally:
        S.shutdown()
        print("Shutting down...")


           
        
        


        
        
        
        
