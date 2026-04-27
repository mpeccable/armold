"""
Maxx Ibarra (ME25)
Arm Robot Control
2-1-2026
"""

import traceback
import time
import math

from Servo import *

class Arm():
    """
    Wrapper for a robotic arm with N = 6 degrees of freedom.
    \nFunctions: 
    \n\tarm.angles = [a1, a2, ..., an] update the target position
    \n\tarm.pose(): Send hardware to target position
    \n\tarm.shutdown(): Terminate hardware/software connection
    """

    def __init__(self):
        """
        Create an Arm() with N=6 degrees of freedom. 
        """
        self.N = 6      # Number corresponds to port number on a PCA9685 module
        self.joint0 = 90    # Shoulder
        self.joint1 = 90    # Waist
        self.joint2 = 100   # Wrist Elevation
        self.joint3 = 90    # Gripper
        self.joint4 = 90    # Wrist Rotation
        self.joint5 = 100   # Elbow

        # Position vector in arm space 
        self.angles = [self.joint0, self.joint1, self.joint2, self.joint3, 
                       self.joint4, self.joint5]   
        
        self.actuators = Servo()    # Main control object
        self.pose()                 # Send hardware to zero position

    def pose(self):
        """
        Poses the Arm() based upon the values of Arm().angles. Arm()  will not 
        move to an updated target position until this command has been sent.
        
        :Arguments:
            None
        :Returns:
            None
        :Related Variables:
            Arm().angles (List[float]): The ordered list of target positions for 
            each of the six actuators. Angles are measured in radians, 
            with the "zero" position labeled as `theta`_n range n[0, 6]
            Arm().joint# range #[0, 6] (float): current value for `theta`_# in 
            radians 
        """
        # print(f"Sending arm to {self.angles}")        # enable angle logging
        for i, e in enumerate(self.angles):
            self.actuators.setServoAngle(i, e)

    def shutdown(self): 
        """
        Terminates hardware/software connection and frees up computational 
        resources on RPi. 
        :Arguments:
            None
        :Returns:
            None
        """
        print("Shutting down now...")
        self.actuators.shutdown()
        print("Hardware connection terminated.")


if __name__ == "__main__":
    try:
        pass
    except BaseException as ex:
        pass
    finally:
        pass
