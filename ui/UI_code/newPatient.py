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


        self.name = customtkinter.CTkEntry(self, placeholder_text="Your MOM'S Name")
        self.aadhar = customtkinter.CTkEntry(self, placeholder_text="Your MOM Social Security")
        self.dob = customtkinter.CTkEntry(self, placeholder_text="Your MOM non virgin date")
        self.phone = customtkinter.CTkEntry(self, placeholder_text="Your MOM's Phone number ")
        self.email = customtkinter.CTkEntry(self, placeholder_text="Your MOM's sex Mail")
        self.address = customtkinter.CTkEntry(self, placeholder_text="Your MOM's FUCK address")
        self.ins = customtkinter.CTkEntry(self, placeholder_text="Child Support ⚠️ WARNING ⚠️")
        self.pid = customtkinter.CTkEntry(self, placeholder_text="Patient ID")
        self.name = customtkinter.CTkEntry(self, placeholder_text="Name")
        self.aadhar = customtkinter.CTkEntry(self, placeholder_text="Aadhaar number")
        self.dob = customtkinter.CTkEntry(self, placeholder_text="Date of Birth")
        self.phone = customtkinter.CTkEntry(self, placeholder_text="Phone number ")
        self.email = customtkinter.CTkEntry(self, placeholder_text="Email")
        self.address = customtkinter.CTkEntry(self, placeholder_text="Address")
        self.ins = customtkinter.CTkEntry(self, placeholder_text="Insurence ID")
        self.ins = customtkinter.CTkEntry(self, placeholder_text="Sex")


        newPID = "New PID here generated automatically"

        self.pid_lab = customtkinter.CTkLabel(self, text=f"{newPID}")
        self.name_lab = customtkinter.CTkLabel(self, text="Name")
        self.aadhar_lab = customtkinter.CTkLabel(self,text="Aadhar")
        self.dob_lab = customtkinter.CTkLabel(self, text="Date of Birth")
        self.phone_lab = customtkinter.CTkLabel(self, text="Phone")
        self.email_lab = customtkinter.CTkLabel(self, text="Email")
        self.address_lab = customtkinter.CTkLabel(self,text="Address")
        self.ins_lab = customtkinter.CTkLabel(self, text="Insorence asjdjjashdjkhassd")

        self.rblock = customtkinter.CTkOptionMenu(self,command=self.room_block_sel, values=['das','asd'])
        self.rnum = customtkinter.CTkOptionMenu(self,command=self.room_num_sel, values=['1','2'])

        self.rblock_lab=customtkinter.CTkLabel(self,text="Room Block")
        self.rnum_lab=customtkinter.CTkLabel(self,text="Room Number")

        self.pid_lab.grid(row=0,column=1,padx=5,pady=5)
        self.name.grid(row=1,column=1,padx=5,pady=5)
        self.aadhar.grid(row=2,column=1,padx=5,pady=5)
        self.dob.grid(row=3,column=1,padx=5,pady=5)
        self.phone.grid(row=4,column=1,padx=5,pady=5)
        self.email.grid(row=5,column=1,padx=5,pady=5)
        self.address.grid(row=6,column=1,padx=5,pady=5)
        self.ins.grid(row=7,column=1,padx=5,pady=5)

        self.sel_rblock = '--Please-Select--'
        self.sel_rnum = '--Please-Select--'

        self.name_lab.grid(row=1,column=0,padx=5,pady=5)
        self.aadhar_lab.grid(row=2,column=0,padx=5,pady=5)
        self.dob_lab.grid(row=3,column=0,padx=5,pady=5)
        self.phone_lab.grid(row=4,column=0,padx=5,pady=5)
        self.email_lab.grid(row=5,column=0,padx=5,pady=5)
        self.address_lab.grid(row=6,column=0,padx=5,pady=5)
        self.ins_lab.grid(row=7,column=0,padx=5,pady=5)

        self.rblock.grid(row=8, column=1,padx=5,pady=5)
        self.rnum.grid(row=9, column=1,padx=5,pady=5)

        self.rblock_lab.grid(row=8, column=0,padx=5,pady=5)
        self.rnum_lab.grid(row=9, column=0,padx=5,pady=5)

        self.rblock.set(self.sel_rblock)
        self.rnum.set(self.sel_rnum)


        self.addbtn = customtkinter.CTkButton(self, text="Add New Patient",command=self.addnew)

    def addnew():
        pass

    def room_block_sel(self,get):
        self.sel_rblock=get
        print(self.sel_rblock)
    
    def room_num_sel(self,get):
        self.sel_rnum=get
        print(self.sel_rnum)