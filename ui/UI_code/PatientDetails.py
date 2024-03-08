import customtkinter
from PIL import Image
import querr as q
class patientlist(customtkinter.CTkFrame):
    def __init__(self, master, name:str,time:str,department:str,phone:int, width:int = 320,height:int = 30,**kwargs):
        super().__init__(master, border_width=2,height=height, width=width, fg_color="white",bg_color="transparent",**kwargs) 
        p = grid2(self)
        # p = PatientCard(self,array=[name,age,sex,address,id])
        self.grid_columnconfigure((0,1,2,3,4),weight=1)
        Name = customtkinter.CTkLabel(self, text="Name: "+name,text_color="black")
        Time = customtkinter.CTkLabel(self, text="ID: "+time,text_color="black")
        Department = customtkinter.CTkLabel(self, text="Ins_ID: "+department,text_color="black")
        view = customtkinter.CTkButton(self,text=" 🔍 ",width=20, command=lambda: [self.view_details(name=name)])
        Del = customtkinter.CTkButton(self,text="Delete",width=20, command=self.delete_patient)
        Blank = customtkinter.CTkLabel(self, width=30, height=30, text=" ")
        Name.grid(row=0,column=0,padx=10,pady=0)
        Time.grid(row=0,column=1,padx=10,pady=0)
        Department.grid(row=0,column=2,padx=10,pady=0)
        view.grid(row=0,column=4,padx=10,pady=0)
        Del.grid(row=0,column=5,padx=10,pady=0)
        Blank.grid(row=0,column=3,padx=220,pady=10)
        self.toplevel_window = None
    def delete_patient():
        pass
    def view_details(self, name):
        val=q.patient_dis(name)
        print(name)
        print(val)
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(array=val)
             # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

class listofpatient(customtkinter.CTkScrollableFrame):
    def __init__(self, 
                master,
                width:int = 30,
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
        pat=q.patientInfo()
        x=0
        for i in pat:
            newAppointment = patientlist(self,
                                            name=i[0],
                                            time=i[1], 
                                            department=i[2], 
                                            phone=i[3])
            newAppointment.grid(row=x,column=0,padx=0,pady=10,sticky="nsew")
            x+=1


class grid1(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 1020,height:int = 500, **kwargs):
        super().__init__(master, height=height, width=width,fg_color="#F1F1F1",bg_color="transparent",**kwargs)
        linecolor = "#8b8b8b"
        label = customtkinter.CTkLabel(self, text_color="Black",text="Patient Details")
        progressbar = customtkinter.CTkProgressBar(self, width=920,progress_color=linecolor,orientation="horizontal",)
        progressbar.set(1)
        progressbar.grid(row=1,column=0,padx=10,pady=5, sticky="nsew")
        label.grid(row=0,column=0,padx=10,pady=10)

        patientList = listofpatient(self)
        patientList.grid(row=2,column=0,padx=10,pady=10,sticky="nsew")


class patientcardaction(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 120,height:int = 100, **kwargs):
        super().__init__(master, height=height, width=width, bg_color="transparent",fg_color="#F1f1f1",**kwargs)
        statement = customtkinter.CTkButton(self, height=30,width=320,text="Statement")
        transfer = customtkinter.CTkButton(self, height=30,width=320,text="Transfer Details")
        statement.grid(row=0,column=0,padx=0,pady=10,sticky="nsew")
        transfer.grid(row=1,column=0,padx=0,pady=10,sticky="nsew")
        

class PatientCard(customtkinter.CTkFrame):
    def __init__(self, master, array,width: int = 320, height: int = 400, **kwargs):
        super().__init__(master, height=height, width=width, bg_color="transparent", border_color="black",
                         border_width=2, fg_color="white", **kwargs)
        self.grid_columnconfigure(0,weight=1)
        print(array[0][0])
        print(array[0][1])
        print(array[0][2])
        print(array[0][3])
        print(array[0][4])
        # self.Name = array[0][0]
        # self.Age = array[0][1]
        # self.Sex = array[0][2]
        # self.Address = array[0][3]
        # self.ID = array[0][4]
        # patient_card_label = customtkinter.CTkLabel(self, text="Patient Card",text_color="black", font=customtkinter.CTkFont(size=20))
        # patient_image = customtkinter.CTkLabel(self,text="",width=100,height=100,image=customtkinter.CTkImage(Image.open("image/Logo.png"),size=(100,150)))
        # patient_name_label = customtkinter.CTkLabel(self, text=self.Name, text_color="black", font=customtkinter.CTkFont(size=20))
        # patient_age_label = customtkinter.CTkLabel(self, text=f"Age: {self.Age}", text_color="black", font=customtkinter.CTkFont(size=20))
        # patient_sex_label = customtkinter.CTkLabel(self, text=f"Age: {self.Sex}", text_color="black", font=customtkinter.CTkFont(size=20))
        # patient_address_label = customtkinter.CTkLabel(self, text=f"Address: {self.Address}", text_color="black", font=customtkinter.CTkFont(size=12))
        # patient_ID_label = customtkinter.CTkLabel(self, text=f"Patient ID: {self.ID}", text_color="black", font=customtkinter.CTkFont(size=16))


        # patient_card_label.grid(row=0,column=0, padx=10, pady=5,sticky='nsew')
        # patient_image.grid(row=1,column=0, padx=10, pady=10,sticky='nsew')
        # patient_name_label.grid(row=2,column=0, padx=10, pady=5,sticky='nsew')
        # patient_age_label.grid(row=3,column=0, padx=10, pady=2,sticky='nsew')
        # patient_sex_label.grid(row=4,column=0, padx=10, pady=2,sticky='nsew')
        # patient_address_label.grid(row=5,column=0, padx=10, pady=2,sticky='nsew')
        # patient_ID_label.grid(row=6,column=0, padx=10, pady=10,sticky='nsew')

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, array,*args, **kwargs):
        super().__init__(*args, fg_color="#F1F1F1",**kwargs)
        self.geometry("350x540")
        self.title("Patient Card")
        card = PatientCard(self,array=array)
        card.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
        card_act = patientcardaction(self)
        card_act.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
        

class grid2(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 320,height:int = 600, **kwargs):
        super().__init__(master, height=height, width=width, fg_color="#F1F1F1",bg_color="transparent",**kwargs)
        self.array = q.patient_name()
        self.card = PatientCard(self,self.array)
        self.card.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
        card_act = patientcardaction(self)
        card_act.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
    
    
        


class Mainboard(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 720,height:int = 600, **kwargs):
        super().__init__(master, height=height, width=width, bg_color="transparent",fg_color="white",**kwargs)
        grid_1 = grid1(self)
        grid_1.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
        # grid_2 = grid2(self)
        # grid_2.grid(row=0,column=1,padx=10,pady=10)