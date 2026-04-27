"""
Servo module courtesy of Freenove Robot Dog Kit for Raspberry Pi

Modifed by Maxx Ibarra
8-29-2025
"""
from PCA9685 import PCA9685
import time 

class Servo:
    def __init__(self, angleMin, angleMax, PWMmin, PWMmax):
        print("Initializing Hardware...")
        self.angleMin=angleMin
        self.angleMax=angleMax
        self.PWMmin=PWMmin
        self.PWMmax=PWMmax
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

    def setServoAngle(self,channel, angle):
        if angle < self.angleMin:
            angle = self.angleMin
        elif angle > self.angleMax:
            angle = self.angleMax


        # Prev values 102 - 512 probably corresponds to the correct values for the HS645MG servos and other 
        # digital 5V servos of that size which operate on 50 Hz and has a 

        # 
        date=self.map(angle,self.angleMin,self.angleMax,self.PWMmin, self.PWMmax) 
        # Map data from angles to PWM values
        # print(date,date/4096*0.02) # FIXME! 

        # For 
        # pulse is an element of [600 us, 2400 us]
        self.pwm.setServoPulse(channel, int(date))
 

# Main program logic follows:
if __name__ == '__main__':
    try:
        while(True): 
            S=Servo(0, 180)
            for i in range(16):                 # Iterate through all 16 servo ports
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


           
        
        


        
        
        
        
