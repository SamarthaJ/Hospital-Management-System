import customtkinter
from PIL import Image
import querr as q
class patientlist(customtkinter.CTkFrame):
    def __init__(self, master, name:str,time:str,department:str,phone:int, width:int = 320,height:int = 30,**kwargs):
        super().__init__(master, border_width=2,height=height, width=width, fg_color="white",bg_color="transparent",**kwargs) 
        self.grid_columnconfigure((0,1,2,3,4),weight=1)
        Name = customtkinter.CTkLabel(self, text="Name: "+name,text_color="black")
        Time = customtkinter.CTkLabel(self, text="ID: "+time,text_color="black")
        Department = customtkinter.CTkLabel(self, text="Ins_ID: "+department,text_color="black")
        Edit = customtkinter.CTkButton(self,text="Edit",width=20)
        Del = customtkinter.CTkButton(self,text="Delete",width=20)
        Blank = customtkinter.CTkLabel(self, width=30, height=30, text=" ")
        Name.grid(row=0,column=0,padx=10,pady=0)
        Time.grid(row=0,column=1,padx=10,pady=0)
        Department.grid(row=0,column=2,padx=10,pady=0)
        Edit.grid(row=0,column=4,padx=10,pady=0)
        Del.grid(row=0,column=5,padx=10,pady=0)
        Blank.grid(row=0,column=3,padx=30,pady=10)


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
    def __init__(self, master, width:int = 320,height:int = 500, **kwargs):
        super().__init__(master, height=height, width=width,fg_color="#F1F1F1",bg_color="transparent",**kwargs)
        label = customtkinter.CTkLabel(self, text_color="Black",text="Patient Details\n____________________________________________________________________________")
        label.grid(row=0,column=0,padx=10,pady=10)

        patientList = listofpatient(self)
        patientList.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")


class patientcardaction(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 120,height:int = 100, **kwargs):
        super().__init__(master, height=height, width=width, bg_color="transparent",fg_color="#F1f1f1",**kwargs)
        statement = customtkinter.CTkButton(self, height=30,width=320,text="Statement")
        transfer = customtkinter.CTkButton(self, height=30,width=320,text="Transfer Details")
        statement.grid(row=0,column=0,padx=0,pady=10,sticky="nsew")
        transfer.grid(row=1,column=0,padx=0,pady=10,sticky="nsew")
        

class patientcard(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 320,height:int = 400, **kwargs):
        super().__init__(master, height=height, width=width, bg_color="transparent",border_color="black",border_width=2,fg_color="white",**kwargs)
        self.grid_columnconfigure(0,weight=1)
        Age=20
        Sex = "Male"
        Address = "xxx,xxx,x,x,x,x,x,x 444444"
        ID = "PAB123"
        patient_card_label = customtkinter.CTkLabel(self, text="Patient Card",text_color="black", font=customtkinter.CTkFont(size=20))
        patient_image = customtkinter.CTkLabel(self,text="",width=100,height=100,image=customtkinter.CTkImage(Image.open("image/Logo.png"),size=(100,150)))
        patient_name_label = customtkinter.CTkLabel(self, text="Samartha", text_color="black", font=customtkinter.CTkFont(size=20))
        patient_age_label = customtkinter.CTkLabel(self, text=f"Age: {Age}", text_color="black", font=customtkinter.CTkFont(size=20))
        patient_sex_label = customtkinter.CTkLabel(self, text=f"Age: {Sex}", text_color="black", font=customtkinter.CTkFont(size=20))
        patient_address_label = customtkinter.CTkLabel(self, text=f"Address: {Address}", text_color="black", font=customtkinter.CTkFont(size=12))
        patient_ID_label = customtkinter.CTkLabel(self, text=f"Patient ID: {ID}", text_color="black", font=customtkinter.CTkFont(size=16))


        patient_card_label.grid(row=0,column=0, padx=10, pady=5,sticky='nsew')
        patient_image.grid(row=1,column=0, padx=10, pady=10,sticky='nsew')
        patient_name_label.grid(row=2,column=0, padx=10, pady=5,sticky='nsew')
        patient_age_label.grid(row=3,column=0, padx=10, pady=2,sticky='nsew')
        patient_sex_label.grid(row=4,column=0, padx=10, pady=2,sticky='nsew')
        patient_address_label.grid(row=5,column=0, padx=10, pady=2,sticky='nsew')
        patient_ID_label.grid(row=6,column=0, padx=10, pady=10,sticky='nsew')

class grid2(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 320,height:int = 600, **kwargs):
        super().__init__(master, height=height, width=width, fg_color="#F1F1F1",bg_color="transparent",**kwargs)

        card = patientcard(self)
        card.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
        card_act = patientcardaction(self)
        card_act.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")


class Mainboard(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 720,height:int = 600, **kwargs):
        super().__init__(master, height=height, width=width, bg_color="transparent",fg_color="white",**kwargs)
        grid_1 = grid1(self)
        grid_1.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
        grid_2 = grid2(self)
        grid_2.grid(row=0,column=1,padx=10,pady=10)