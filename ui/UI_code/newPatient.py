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


        self.pid = customtkinter.CTkEntry(self, placeholder_text="Patient ID")
        self.name = customtkinter.CTkEntry(self, placeholder_text="Name")
        self.aadhar = customtkinter.CTkEntry(self, placeholder_text="Aadhaar number")
        self.dob = customtkinter.CTkEntry(self, placeholder_text="Date of Birth")
        self.phone = customtkinter.CTkEntry(self, placeholder_text="Phone number ")
        self.email = customtkinter.CTkEntry(self, placeholder_text="Email")
        self.address = customtkinter.CTkEntry(self, placeholder_text="Address")
        self.ins = customtkinter.CTkEntry(self, placeholder_text="Insurence ID")
        self.ins = customtkinter.CTkEntry(self, placeholder_text="Sex")


        

        self.pid.grid()
