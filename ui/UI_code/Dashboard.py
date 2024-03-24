import customtkinter
import querr as q
class noofpatient(customtkinter.CTkFrame):
    def __init__(self, master, text,text2,value:int,width:int = 150,height:int = 30, **kwargs):
        super().__init__(master, height=height, width=width,  fg_color="white",bg_color="#F1F1F1",border_color="black",border_width=2,**kwargs)
        self.grid_rowconfigure((0,1),weight=1)
        self.grid_columnconfigure((0,1),weight=10)

        # Left justify this!!!
        label = customtkinter.CTkLabel(self,justify="left",height=5,text=text,text_color="black",font=customtkinter.CTkFont(size=8))
        label1 = customtkinter.CTkLabel(self, text=text2,text_color="black",font=customtkinter.CTkFont(size=12))
        Blank = customtkinter.CTkLabel(self, width=50, height=30, text=" ",text_color="black")
        label2 = customtkinter.CTkLabel(self, text=value,text_color="black", font=customtkinter.CTkFont(size=18))
        label.grid(row=0,column=0,padx=5, pady=0)
        label1.grid(row=1,column=0,padx=5, pady=3)
        label2.grid(row=1,column=1,padx=5,pady=3)
        Blank.grid(row=0,column=1,padx=5,pady=3)



class grid1(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 460,height:int = 113, **kwargs):
        super().__init__(master, height=height, width=width, fg_color="#F1F1F1",bg_color="white", **kwargs)
        self.grid_rowconfigure(0,weight=10)
        self.grid_columnconfigure((0,1,2),weight=10)

        noOfPatient = noofpatient(self, text="Today",text2="No of Patient:",value=q.curr_patients())
        noOfDoctors = noofpatient(self, text="Today",text2="No of Doctor:",value=q.doc_count())
        revenue = noofpatient(self, text="Today",text2="Revenue:", value=" $"+str(q.revenue()))
        noOfPatient.grid(row=0,column=0,padx=10, pady=10)
        noOfDoctors.grid(row=0,column=1,padx=10, pady=10)
        revenue.grid(row=0,column=2,padx=10, pady=10)
        

class patientlistclass(customtkinter.CTkFrame):
    def __init__(self, master,value1, value2:int,width:int = 255,height:int = 44, **kwargs):
        super().__init__(master, height=height, width=width, fg_color="white",bg_color="#F1F1F1",border_color="black",border_width=2,**kwargs)
        label = customtkinter.CTkLabel(self, text=value1+"\nPatients",text_color='black')
        res = customtkinter.CTkLabel(self, text=value2,text_color='black')
        label.grid(row=0,column=0, padx=18, pady=10)
        res.grid(row=0,column=1, padx=18, pady=10)

        
class grid2(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 388,height:int = 113, **kwargs):
        super().__init__(master, height=height, width=width, bg_color='transparent',fg_color="#F1F1F1",**kwargs)
        self.grid_rowconfigure((0,1), weight=0)
        self.grid_columnconfigure((0,1), weight=0)

        activePatient = patientlistclass(self, "active", q.no_of_patients())
        deceasedPatient = patientlistclass(self, "Deceased", q.deceased_patients())
        RecoveredPatient = patientlistclass(self, "recovered", q.discharged_patients())
        ICUPatient = patientlistclass(self, "ICU", q.icu_patients())

        # activePatient = patientlistclass(self, "active", querry.no_of_patients())
        # deceasedPatient = patientlistclass(self, "Deceased", querry.deceased_patients())
        # RecoveredPatient = patientlistclass(self, "recovered", querry.discharged_patients())
        # ICUPatient = patientlistclass(self, "ICU", "10")

        activePatient.grid(row=0,column=0,padx=10,pady=10)
        deceasedPatient.grid(row=0,column=1,padx=10,pady=10)
        RecoveredPatient.grid(row=1,column=0,padx=10,pady=10)
        ICUPatient.grid(row=1,column=1,padx=10,pady=10)

class appointmentlist(customtkinter.CTkFrame):
    def __init__(self, master, name:str,time:str,department:str,phone:int, width:int = 450,height:int = 30,**kwargs):
        super().__init__(master, border_width=2,height=height, width=width, fg_color="white",bg_color="transparent",**kwargs) 
        self.grid_columnconfigure((0,1,2,3,4),weight=1)
        Name = customtkinter.CTkLabel(self, text="Name: "+name,text_color="black")
        Time = customtkinter.CTkLabel(self, text="Time: "+time,text_color="black")
        Department = customtkinter.CTkLabel(self, text="With: "+department,text_color="black")
        Phone = customtkinter.CTkButton(self,text="phone",width=20)
        Blank = customtkinter.CTkLabel(self, width=10, height=30, text=" ")
        Name.grid(row=0,column=0,padx=10,pady=0)
        Time.grid(row=0,column=1,padx=10,pady=0)
        Department.grid(row=0,column=2,padx=10,pady=0)
        Phone.grid(row=0,column=4,padx=10,pady=0)
        Blank.grid(row=0,column=3,padx=5,pady=10)
        


class appointment(customtkinter.CTkScrollableFrame):
    def __init__(self, 
                master,
                width:int = 500,
                height:int = 302,
                **kwargs):
        super().__init__(master, 
                        height=height,
                        width=width, 
                        border_color="black",
                        border_width=2,
                        fg_color="white",
                        bg_color="transparent",
                        **kwargs)
        aptlst=q.appointment_lst()
        x=0
        for i in aptlst:
            newAppointment = appointmentlist(self,
                                            name=i[0],
                                            time=str(i[2]).replace("{","").replace("}",""),
                                            department=i[1], 
                                            phone=1234567890)
            newAppointment.grid(row=x,column=0,padx=5,pady=2,sticky="nsew")
            x+=1


        


class grid3(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 460,height:int = 302, **kwargs):
        super().__init__(master, height=height, width=width, bg_color="transparent",fg_color="white",**kwargs)
        appoint_details = appointment(self)
        appoint_details.grid(row=0, column=0)


class grid4(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 288,height:int = 302, **kwargs):
        super().__init__(master, height=height, width=width, **kwargs)


class Mainboard(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 1280,height:int = 600, **kwargs):
        super().__init__(master, height=height, width=width, fg_color="white",bg_color="white",**kwargs)
        label = customtkinter.CTkLabel(self, text="mainBoard")
        self.grid_rowconfigure((0,1), weight=0)
        self.grid_columnconfigure((0,1), weight=10)

        grid_1 = grid1(master=self)
        grid_2 = grid2(master=self)
        grid_3 = grid3(master=self)
        grid_4 = grid4(master=self)

        grid_1.grid(row=0,column=0,padx=20, pady=20,sticky="nsew")
        grid_2.grid(row=0,column=1,padx=20, pady=20,sticky="nsew")
        grid_3.grid(row=1,column=0,padx=20, pady=20,sticky="nsew")
        grid_4.grid(row=1,column=1,padx=20, pady=20,sticky="nsew")