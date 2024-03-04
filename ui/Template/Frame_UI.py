from typing import Any, Optional, Tuple, Union
import customtkinter
from PIL import Image

class nav(customtkinter.CTkFrame):
    def __init__ (self,*args,master,width:int = 720, height:int = 100,**kwargs):
        super().__init__(master,width=width, height=height, fg_color="white",bg_color="white",corner_radius=100,**kwargs)
        self.grid_columnconfigure(4,weight=1)

        entry = customtkinter.CTkEntry(self, placeholder_text="Search Patient/Patient ID",width=411,height=40)

        profile = customtkinter.CTkButton(self,text="C", width=32,height=32,corner_radius=1000)

        Logo = customtkinter.CTkImage(light_image=Image.open("image/Logo.png"),size=(191,44))
        image_label = customtkinter.CTkLabel(self, image=Logo, text="")
        
        empty = customtkinter.CTkLabel(self, text=" ")
        
        image_label.grid(row=1,column=0, padx=10, pady=5)
        empty.grid(row=1,column=2,padx=250,pady=30,sticky="nsew")
        entry.grid(row=1,column=3,padx=10,pady=10)
        profile.grid(row=1,column=4,padx=10,pady=10)

class down(customtkinter.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master,fg_color="transparent",bg_color="transparent",**kwargs)
        # Create two new frames in col 1 and col 2
        # called Sidebar and MainBoard
        # |----------------------------|
        # |  Navbar                    |
        # |----------------------------|
        # | Side|                      |
        # | bar |                      |
        # |     |      Mainboard       |
        # |     |                      |
        # |     |                      |
        # -----------------------------|

        self.grid_rowconfigure(10, weight=0)
        self.grid_columnconfigure(0, weight=0)

        SideBar = Side(master=self)
        SideBar.grid(row=0,column=0, padx=20, pady=20)

        MainBoard = MainBoard(master=self)
        MainBoard.grid(row=0,column=1, padx=20, pady=20)
        
        label = customtkinter.CTkLabel(self, text="down")
        # label.grid(row=0,column=0,padx=20,pady=20)


class Side(customtkinter.CTkFrame):
    def __init__(self, master,width:int = 170,height:int = 450,**kwargs):
        super().__init__(master,height=height,width=width,fg_color="white",bg_color="transparent",**kwargs)
        btncolor = "#F3F3F3"

        MainLabel = customtkinter.CTkLabel(self, font=customtkinter.CTkFont(size=24),text="Dashboard",text_color="#000000")
        MainLabel.grid(row=0,column=0,padx=10,pady=40)
        DashboardImage = customtkinter.CTkImage(light_image=Image.open("image/dashboard_FILL0_wght400_GRAD0_opsz24.png"))
        DoctorListImage  = customtkinter.CTkImage(light_image=Image.open("image/stethoscope_FILL0_wght400_GRAD0_opsz24.png"))
        patientListImage = customtkinter.CTkImage(light_image=Image.open("image/patient_list_FILL0_wght400_GRAD0_opsz24.png"))
        RoomListImage = customtkinter.CTkImage(light_image=Image.open("image/moving_beds_FILL0_wght400_GRAD0_opsz24.png"))
        PharmacyImage = customtkinter.CTkImage(light_image=Image.open("image/pill_FILL0_wght400_GRAD0_opsz24.png"))
        NewPatientImage = customtkinter.CTkImage(light_image=Image.open("image/add_FILL0_wght400_GRAD0_opsz24.png"))
        AppointmentImage = customtkinter.CTkImage(light_image=Image.open("image/add_call_FILL0_wght400_GRAD0_opsz24.png"))


        Dashboard= customtkinter.CTkButton(self, width=146, height=33,image=DashboardImage,text="Dashboard", fg_color=btncolor,text_color="black",border_color="black",border_width=2)
        DoctorList= customtkinter.CTkButton(self, width=146, height=33,image=DoctorListImage,text="Doctor List", fg_color=btncolor,text_color="black",border_color="black",border_width=2)
        patientList= customtkinter.CTkButton(self, width=146, height=33,image=patientListImage,text="Patient List", fg_color=btncolor,text_color="black",border_color="black",border_width=2)
        RoomList= customtkinter.CTkButton(self, width=146, height=33,image=RoomListImage,text="Room List", fg_color=btncolor,text_color="black",border_color="black",border_width=2)
        Pharmacy= customtkinter.CTkButton(self, width=146, height=33,image=PharmacyImage,text="Pharmacy", fg_color=btncolor,text_color="black",border_color="black",border_width=2)
        NewPatient= customtkinter.CTkButton(self, width=146, height=33,image=NewPatientImage,text="New Patient", fg_color=btncolor,text_color="black",border_color="black",border_width=2)
        Appointment= customtkinter.CTkButton(self, width=146, height=33,image=AppointmentImage,text="Appointment", fg_color=btncolor,text_color="black",border_color="black",border_width=2)
        Blank = customtkinter.CTkLabel(self, width=100, height=50, text=" ")
        needHelp = customtkinter.CTkButton(self, width=146, height=20,text_color="black", text="Need Help?", fg_color="transparent", bg_color="transparent",hover_color="#ffffff")
        copyright = customtkinter.CTkLabel(self, width=100, height=10,text_color="black",text="©Copyright Intruders all recived")


        Dashboard.grid(row=1,column=0,padx=10,pady=2,sticky = 'nsew')
        DoctorList.grid(row=2,column=0,padx=10,pady=2,sticky = 'nsew')
        patientList.grid(row=3,column=0,padx=10,pady=2,sticky = 'nsew')
        RoomList.grid(row=4,column=0,padx=10,pady=2,sticky = 'nsew')
        Pharmacy.grid(row=5,column=0,padx=10,pady=2,sticky = 'nsew')
        NewPatient.grid(row=6,column=0,padx=10,pady=2,sticky = 'nsew')
        Appointment.grid(row=7,column=0,padx=10,pady=2,sticky = 'nsew')
        needHelp.grid(row=9,column=0,padx=10,pady=2,sticky = 'nsew')
        Blank.grid(row=8,column=0,padx=10,pady=2,sticky = 'nsew')
        copyright.grid(row=10,column=0,padx=20,pady=10,sticky = 'nsew')

        




