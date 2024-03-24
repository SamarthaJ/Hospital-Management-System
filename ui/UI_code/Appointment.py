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
        Blank.grid(row=0,column=3,padx=140,pady=10)


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
        print(apintlst)
        for i in apintlst:
            newAppointment = appointmentlist(self,
                                            name=i[0],
                                            time=str(i[2]).replace("{","").replace("}",""),
                                            department=i[1], 
                                            phone=1234567890)
            newAppointment.grid(row=x,column=0,padx=0,pady=10,sticky="nsew")
            x+=1



class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, fg_color="#F1F1F1",**kwargs)
        # Name
        # Phone
        # Date:Time
        # Doctor
        self.label = customtkinter.CTkLabel(self, text="Appointment Details",text_color="black")
        self.label.grid(row=0,column=0,padx=10,pady=10)
        self.PID = customtkinter.CTkEntry(self,placeholder_text="Patient ID")
        self.find = customtkinter.CTkButton(self, text="Find",command=self.find)
        self.find.grid(row=5,column=0,padx=20,pady=10)
        self.Name = customtkinter.CTkEntry(self,placeholder_text="Name of the Patient")
        self.Phone = customtkinter.CTkEntry(self,placeholder_text="Enter Phone number")
        self.DateTime = customtkinter.CTkEntry(self,placeholder_text="2012-11-14 14:32:30")
        self.Doc = customtkinter.CTkEntry(self,placeholder_text="Name of Doctor")
        self.submitbutton = customtkinter.CTkButton(self, text="Submit",command=self.submit)

        self.Name_lab = customtkinter.CTkLabel(self, width=100,text="Name",text_color="black",anchor="w")
        self.Phone_lab = customtkinter.CTkLabel(self, width=100 ,text="Phone",text_color="black",anchor="w")
        self.DateTime_lab = customtkinter.CTkLabel(self, width=100 ,text="Date and time",text_color="black",anchor="w")
        self.Doc_lab = customtkinter.CTkLabel(self, width=100 ,text="Doctor",text_color="black",anchor="w")

        self.Name_lab.grid(row=1,column=0,padx=10,pady=5)
        self.Phone_lab.grid(row=2,column=0,padx=10,pady=5)
        self.DateTime_lab.grid(row=3,column=0,padx=10,pady=5)
        self.Doc_lab.grid(row=4,column=0,padx=10,pady=5)
        self.label.grid(row=0,column=1,padx=10,pady=5)
        self.PID.grid(row=0,column=1,padx=10,pady=5)
        self.Name.grid(row=1,column=1,padx=10,pady=5)
        self.Phone.grid(row=2,column=1,padx=10,pady=5)
        self.DateTime.grid(row=3,column=1,padx=10,pady=5)
        self.Doc.grid(row=4,column=1,padx=10,pady=5)
        self.submitbutton.grid(row=5,column=1,padx=10,pady=5)

    def  find(self):
        a = q.patient_appoint_d(self.PID.get())
        self.Name.delete(0, 'end')
        self.Name.insert(0, a[0])
        self.Name.configure(state= "readonly")
        self.Phone.delete(0, 'end')
        self.Phone.insert(0,a[1])
        self.Phone.configure(state= "readonly")
        
        print(a)
    
    def submit(self):
        # self.getName = self.Name.get()
        

        # self.getPhone = self.Phone.get()

        # self.getDateTime = self.DateTime.get()
        # print(self.getDateTime)

        # self.getDoc = self.Doc.get()
        # print(self.getDoc)

        # print(self.getDateTime,self.getDoc,self.getPhone,self.getName)
        q.add_appoint(P_id=self.Name.get(), Phone_no=self.Phone.get(), Date=self.DateTime.get(), emp_id=self.Doc.get())
        self.destroy()

class Mainboard(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 720,height:int = 600, **kwargs):
        super().__init__(master, height=height, width=width, **kwargs)
        appoint_details = appointment(self)
        appoint_details.grid(row=0, column=0,padx=10,pady=10)
        newAppoint = customtkinter.CTkButton(self, text="Add New Appointment",command=self.appoint)
        newAppoint.grid(row=1, column=0,padx=10,pady=10)
        self.toplevel_window = None

    def appoint(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow()
             # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

