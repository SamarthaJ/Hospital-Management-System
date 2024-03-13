import customtkinter
from PIL import Image
import querr as q


class NewToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, arr, **kwargs):
        super().__init__(*args, fg_color="#F1F1F1", **kwargs)

        label = customtkinter.CTkLabel(self,text="Edit Patient Details", text_color="black")
        label.grid(row=0,column=0,padx=10,pady=10)

        Name = customtkinter.CTkEntry(self, placeholder_text="Name of the Patient")
        Phone = customtkinter.CTkEntry(self, placeholder_text="Phone number")
        Age = customtkinter.CTkEntry(self, placeholder_text="Age")
        sex = customtkinter.CTkEntry(self, placeholder_text="Sex")
        Address = customtkinter.CTkEntry(self, placeholder_text="Department")

        submitbutton = customtkinter.CTkButton(self, text="Submit",command=lambda: self.submit(arr[4],Name.get(),Age.get(),sex.get(),Phone.get(),Address.get()))

        Name_lab = customtkinter.CTkLabel(self, width=100, text="Name", text_color="black", anchor="w")
        Age_lab = customtkinter.CTkLabel(self, width=100, text="Age", text_color="black", anchor="w")
        sex_lab = customtkinter.CTkLabel(self, width=100, text="Sex", text_color="black", anchor="w")
        Phone_lab = customtkinter.CTkLabel(self, width=100, text="Phone", text_color="black", anchor="w")
        Dept_lab = customtkinter.CTkLabel(self, width=100, text="Department", text_color="black", anchor="w")

        Name.insert(0,arr[0])
        sex.insert(0,arr[2])
        Age.insert(0,arr[1])
        Phone.insert(0,arr[1])
        Address.insert(0,arr[3])
        
        Name.grid(row=1,column=1,padx=10,pady=10)
        sex.grid(row=2,column=1,padx=10,pady=10)
        Age.grid(row=3,column=1,padx=10,pady=10)
        Phone.grid(row=4,column=1,padx=10,pady=10)
        Address.grid(row=5,column=1,padx=10,pady=10)

        submitbutton.grid(row=6,column=1,padx=10,pady=10)
        
        Name_lab.grid(row=1,column=0,padx=10,pady=10)
        sex_lab.grid(row=2,column=0,padx=10,pady=10)
        Age_lab.grid(row=3,column=0,padx=10,pady=10)
        Phone_lab.grid(row=4,column=0,padx=10,pady=10)
        Dept_lab.grid(row=5,column=0,padx=10,pady=10)
        # self.geometry("350x540")
        self.p_id = arr
    def submit(self,p_id,name,age,sex,phone,dept):
        print(p_id,name,age,sex,phone,dept)
        # q.edit_patient(p_id,name,age,sex,phone,dept)
        self.destroy()
class patientlist(customtkinter.CTkFrame):
    def __init__(self, master, name:str,p_id:str,department:str,phone:int, width:int = 320,height:int = 30,**kwargs):
        super().__init__(master, border_width=2,height=height, width=width, fg_color="white",bg_color="transparent",**kwargs) 
        # p = PatientCard(self,array=[name,age,sex,address,id])
        self.grid_columnconfigure((0,1,2,3,4),weight=1)
        Name = customtkinter.CTkLabel(self, text="Name: "+name,text_color="black")
        id = customtkinter.CTkLabel(self, text="ID: "+p_id,text_color="black")
        Department = customtkinter.CTkLabel(self, text="Ins_ID: "+department,text_color="black")
        edit = customtkinter.CTkButton(self,text="Edit",width=20, command=lambda: [self.edit_patient(p_id=p_id)])
        view = customtkinter.CTkButton(self,text=" 🔍 ",width=20, command=lambda: [self.view_details(name=name)])
        Del = customtkinter.CTkButton(self,text="Delete",width=20, command=lambda: [self.delete_patient(p_id=p_id)])
        Blank = customtkinter.CTkLabel(self, width=30, height=30, text=" ")
        Name.grid(row=0,column=0,padx=10,pady=0)
        id.grid(row=0,column=1,padx=10,pady=0)
        Department.grid(row=0,column=2,padx=10,pady=0)
        view.grid(row=0,column=5,padx=10,pady=0)
        Del.grid(row=0,column=6,padx=10,pady=0)
        Blank.grid(row=0,column=3,padx=200,pady=10)
        edit.grid(row=0,column=4,padx=10,pady=0)
        self.toplevel_window = None
        self.toplevel_window2 = None
    
    def edit_patient(self,p_id):
        val=q.patient_dis(name=p_id)
        print(val)
        if self.toplevel_window2 is None or not self.toplevel_window2.winfo_exists():
            self.toplevel_window2 = NewToplevelWindow(arr=val)
             # create window if its None or destroyed
        else:
            self.toplevel_window2.focus()  # if window exists focus it
    def delete_patient(self,p_id):
        q.delete_patient(p_id)
        self.destroy()

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
                                            p_id=i[1], 
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

        self.patientList = listofpatient(self)
        self.patientList.grid(row=2,column=0,padx=10,pady=10,sticky="nsew")


class patientcardaction(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 120,height:int = 150, **kwargs):
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
        
        self.Name = array[0]
        self.Age = array[1]
        self.Sex = array[2]
        self.Address = array[3]
        self.ID = array[4]
        
        patient_card_label = customtkinter.CTkLabel(self, text="Patient Card",text_color="black", font=customtkinter.CTkFont(size=20))
        patient_image = customtkinter.CTkLabel(self,text="",width=100,height=100,image=customtkinter.CTkImage(Image.open("image/Logo.png"),size=(100,150)))
        patient_name_label = customtkinter.CTkLabel(self, text=self.Name, text_color="black", font=customtkinter.CTkFont(size=20))
        patient_age_label = customtkinter.CTkLabel(self, text=f"Age: {self.Age}", text_color="black", font=customtkinter.CTkFont(size=20))
        patient_sex_label = customtkinter.CTkLabel(self, text=f"Age: {self.Sex}", text_color="black", font=customtkinter.CTkFont(size=20))
        patient_address_label = customtkinter.CTkLabel(self, text=f"Address: {self.Address}", text_color="black", font=customtkinter.CTkFont(size=12))
        patient_ID_label = customtkinter.CTkLabel(self, text=f"Patient ID: {self.ID}", text_color="black", font=customtkinter.CTkFont(size=16))


        patient_card_label.grid(row=0,column=0, padx=10, pady=5,sticky='nsew')
        patient_image.grid(row=1,column=0, padx=10, pady=10,sticky='nsew')
        patient_name_label.grid(row=2,column=0, padx=10, pady=5,sticky='nsew')
        patient_age_label.grid(row=3,column=0, padx=10, pady=2,sticky='nsew')
        patient_sex_label.grid(row=4,column=0, padx=10, pady=2,sticky='nsew')
        patient_address_label.grid(row=5,column=0, padx=10, pady=2,sticky='nsew')
        patient_ID_label.grid(row=6,column=0, padx=10, pady=10,sticky='nsew')

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, array,*args, **kwargs):
        super().__init__(*args, fg_color="#F1F1F1",**kwargs)
        self.geometry("350x540")
        self.title("Patient Card")
        card = PatientCard(self,array=array)
        card.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
        card_act = patientcardaction(self)
        card_act.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
        close = customtkinter.CTkButton(self,text="Close",command=self.destroy)
        close.grid(row=2,column=0,padx=10,pady=10,sticky="nsew")
        

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
        self.grid_1 = grid1(self)
        self.grid_1.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")