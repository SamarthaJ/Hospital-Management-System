import customtkinter
from PIL import Image
import querr as q
class appointmentlist(customtkinter.CTkFrame):
    def __init__(self, master, name:str,time:str,department:str,phone:int, width:int = 1000,height:int = 30,**kwargs):
        super().__init__(master, border_width=2,height=height, width=width, fg_color="white",bg_color="transparent",**kwargs) 
        self.grid_columnconfigure((0,1,2,3,4),weight=1)
        Name = customtkinter.CTkLabel(self, text="Name: "+name,text_color="black")
        Time = customtkinter.CTkLabel(self, text="Time: "+time,text_color="black")
        Department = customtkinter.CTkLabel(self, text="With: "+department,text_color="black")
        Phone = customtkinter.CTkButton(self,text="phone",width=20)
        Blank = customtkinter.CTkLabel(self, width=30, height=30, text=" ")
        Name.grid(row=0,column=0,padx=30,pady=0)
        Time.grid(row=0,column=1,padx=30,pady=0)
        Department.grid(row=0,column=2,padx=30,pady=0)
        Phone.grid(row=0,column=4,padx=10,pady=0)
        Blank.grid(row=0,column=3,padx=170,pady=10)


class appointment(customtkinter.CTkScrollableFrame):
    def __init__(self, 
                master,
                width:int = 900,
                height:int = 450,
                **kwargs):
        super().__init__(master, 
                        height=height,
                        width=width, 
                        border_color="black",
                        border_width=2,
                        fg_color="white",
                        bg_color="transparent",
                        **kwargs)
        x=0
        apintlst=q.appointment_lst()
        for i in apintlst:
            newAppointment = appointmentlist(self,
                                            name=i[0],
                                            time=str(i[2]).replace("{","").replace("}",""),
                                            department=i[1], 
                                            phone=1234567890)
            newAppointment.grid(row=x,column=0,padx=0,pady=10,sticky="nsew")
            x=+1



class Mainboard(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 720,height:int = 600, **kwargs):
        super().__init__(master, height=height, width=width, **kwargs)
        appoint_details = appointment(self)
        appoint_details.grid(row=0, column=0,padx=10,pady=10)

