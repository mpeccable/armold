"""
Maxx Ibarra
Manual control for robot arm
2-4-2026
"""

from tkinter import *
from armold import *

import customtkinter

SLIDER_WIDTH = 150
SLIDER_HEIGHT = 700
BUTTON_LENGTH = 20
BUTTON_RADIUS = 20

if __name__ == "__main__":
    """
    Main method for running gui for Armold. 

    :Arguments:
        None

    :Returns: 
        None
    """

    try:
        arm = Arm()   # Init Hardware

        customtkinter.set_appearance_mode("System")     # Set theme and color
        customtkinter.set_default_color_theme("blue")

        root = customtkinter.CTk()          # Init gui object
        root.title('4RM0LD Control Panel')   # Set gui window title
        root.geometry('1400x1200')            # Window size on init
        
        # Can add a custom app icon if you want style points 
        #root.iconbitmap('~/home/baloo/shared/B4100/Mblem.ico')
        
        # Joint 1 slider
        def j0_cmd(value):
            j0_label.configure(text=f"Joint 1 (Shoulder) \n{value:.2f} deg")
            arm.angles[0] = value
            arm.pose()
        
        j0_slide = customtkinter.CTkSlider(root,
            from_=60,
            to=100, 
            orientation='vertical',
            height=SLIDER_HEIGHT,
            width=SLIDER_WIDTH,
            command=j0_cmd, 
            button_length=BUTTON_LENGTH,
            button_corner_radius=BUTTON_RADIUS
            ) 
        j0_slide.grid(row=1, column=2)
        j0_slide.set(90)
        j0_label = customtkinter.CTkLabel(root, text='Joint 1 (Shoulder) \n100 deg',font=("Helvetica", 18))
        j0_label.grid(row=0, column = 2)


        # Joint 0 slider
        def j1_cmd(value):
            j1_label.configure(text=f"Joint 0 (Waist) \n{value:.2f} deg")
            arm.angles[1] = value
            arm.pose()

        j1_slide = customtkinter.CTkSlider(root,
            from_=120,
            to=60,
            orientation='horizontal',
            height=SLIDER_WIDTH,
            width=SLIDER_HEIGHT,
            command=j1_cmd,
            button_length=BUTTON_LENGTH,
            button_corner_radius=BUTTON_RADIUS
            ) 
        j1_slide.grid(row=0, column=1)
        j1_slide.set(90)
        j1_label = customtkinter.CTkLabel(root, text='Joint 0 (Waist) \n90 deg',font=("Helvetica", 18))
        j1_label.grid(row=0, column = 0)


        # Joint 2 slider 
        def j2_cmd(value):
            j2_label.configure(text=f"Joint 3 (Wrist Elevation) \n{value:.2f} deg")
            arm.angles[2] = value
            arm.pose()
        
        j2_slide = customtkinter.CTkSlider(root,
            from_=70,
            to=130, 
            orientation='vertical',
            height=SLIDER_HEIGHT,
            width=SLIDER_WIDTH,
            command=j2_cmd,
            button_length=BUTTON_LENGTH,
            button_corner_radius=BUTTON_RADIUS
            )
        j2_slide.grid(row=1, column=4)
        j2_slide.set(100)
        j2_label = customtkinter.CTkLabel(root, text='Joint 3 (Wrist Elevation) \n90 deg',font=("Helvetica", 18))
        j2_label.grid(row=0, column = 4)


        # Joint 5 slider 
        def j3_cmd(value):
            j3_label.configure(text=f"Joint 5 (Gripper) \n{value:.2f} deg")
            arm.angles[3] = value
            arm.pose()
        
        j3_slide = customtkinter.CTkSlider(root,
            from_=120,
            to=40, 
            orientation='horizontal',
            height=SLIDER_WIDTH,
            width=SLIDER_HEIGHT,
            command=j3_cmd,
            button_length=BUTTON_LENGTH,
            button_corner_radius=BUTTON_RADIUS
            )
        j3_slide.grid(row=2, column=1)
        j3_slide.set(90)
        j3_label = customtkinter.CTkLabel(root, text='Joint 5 (Gripper) \n90 deg',font=("Helvetica", 18))
        j3_label.grid(row=2, column = 0)


        # Joint 4 slider
        def j4_cmd(value):
            j4_label.configure(text=f"Joint 4 (Wrist Rotation) \n{value:.2f} deg")
            arm.angles[4] = value
            arm.pose()
        
        j4_slide = customtkinter.CTkSlider(root,
            from_=18,
            to=162, 
            orientation='horizontal',
            height=SLIDER_WIDTH,
            width=SLIDER_HEIGHT,
            command=j4_cmd,
            button_length=BUTTON_LENGTH,
            button_corner_radius=BUTTON_RADIUS
            )
        j4_slide.grid(row=1, column=1)
        j4_slide.set(90)
        j4_label = customtkinter.CTkLabel(root, text='Joint 4 (Wrist Rotation) \n90 deg',font=("Helvetica", 18))
        j4_label.grid(row=1, column = 0)


        # Joint 2 slider FIXME
        def j5_cmd(value):
            j5_label.configure(text=f"Joint 2 (Elbow) \n{value:.2f} deg")
            arm.angles[5] = value
            arm.pose()
        
        j5_slide = customtkinter.CTkSlider(root,
            from_=110,
            to=40, 
            orientation='vertical',
            height=SLIDER_HEIGHT,
            width=SLIDER_WIDTH,
            command=j5_cmd,
            button_length=BUTTON_LENGTH,
            button_corner_radius=BUTTON_RADIUS
            )
        j5_slide.grid(row=1, column=3)
        j5_slide.set(100)
        j5_label = customtkinter.CTkLabel(root, text='Joint 2 (Elbow) \n100 deg',font=("Helvetica", 18))
        j5_label.grid(row=0, column=3)

        root.mainloop()     # This command launches GUI thread. All lines above
            # set rules for the sliders and actuator stuff. 

    except BaseException as ex:
        print("Ending due to exception: %s" % repr(ex))
        traceback.print_exc()

    finally: 
        print("Shutting down!")
        arm.shutdown()