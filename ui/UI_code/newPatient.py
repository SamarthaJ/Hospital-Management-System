import customtkinter
from PIL import Image

class Mainboard(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 720,height:int = 600, **kwargs):
        super().__init__(master, height=height, width=width, **kwargs)
        # PID varchar | Aphanumeric
        # Name varchar 
        # Aadhar BIGINT(12)
        # DOB DATE
        # Phone BIGINT(10)
        # Email Aphanumeric with Symboool
        # Address text
        # Ins_id varcha | Aphanumaric
        # sex char(1) : M||F

        # Room_block varchar | Aphanumeric
        # Room_number varchar | Aphanumeric


        self.pid = customtkinter.CTkEntry(self, placeholder_text="Your MOM's Walmart ID")
        self.name = customtkinter.CTkEntry(self, placeholder_text="Your MOM'S Name")
        self.aadhar = customtkinter.CTkEntry(self, placeholder_text="Your MOM Social Security")
        self.dob = customtkinter.CTkEntry(self, placeholder_text="Your MOM non virgin date")
        self.phone = customtkinter.CTkEntry(self, placeholder_text="Your MOM's Phone number ")
        self.email = customtkinter.CTkEntry(self, placeholder_text="Your MOM's sex Mail")
        self.address = customtkinter.CTkEntry(self, placeholder_text="Your MOM's FUCK address")
        self.ins = customtkinter.CTkEntry(self, placeholder_text="Child Support ⚠️ WARNING ⚠️")

        

        self.pid.grid()
