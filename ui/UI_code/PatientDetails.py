import customtkinter
from PIL import Image
import querr as q
import dialogbox as d


class NewToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, arr, **kwargs):
        super().__init__(*args, fg_color="#F1F1F1", **kwargs)

        # PID [*] []
        # Name [*] []
        # dob [*] []
        # Sex [*] []
        # Mobile [*] []
        # address [*] []
        # Aadhaar [*] []
        # email [] []
        # Insurance [] []


        self.label = customtkinter.CTkLabel(self, text="Edit Patient Details",font= customtkinter.CTkFont(weight="bold", size=20),text_color="black",width=100)
        self.label.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky="nsew")

        self.PID_lab = customtkinter.CTkLabel(self, text="PID: "+arr[0],text_color="black",font= customtkinter.CTkFont(weight="bold", size=15),anchor="w",width=100)
        self.PID_lab.grid(row=1,column=0,columnspan=2,padx=5,pady=5,sticky="nsew")

        self.Name_lab = customtkinter.CTkLabel(self, text="Name: ",text_color="black",font= customtkinter.CTkFont(weight="bold", size=15),anchor="w",width=100)
        self.Name_lab.grid(row=2,column=0,padx=5,pady=5,sticky="nsew")

        self.dob_lab = customtkinter.CTkLabel(self, text="DOB: ",text_color="black",font= customtkinter.CTkFont(weight="bold", size=15),anchor="w",width=100)
        self.dob_lab.grid(row=3,column=0,padx=5,pady=5,sticky="nsew")

        self.Sex_lab = customtkinter.CTkLabel(self, text="Sex: ",text_color="black",font= customtkinter.CTkFont(weight="bold", size=15),anchor="w",width=100)                                                             
        self.Sex_lab.grid(row=4,column=0,padx=5,pady=5,sticky="nsew")

        self.Phone_lab = customtkinter.CTkLabel(self, text="Phone: ",text_color="black",font= customtkinter.CTkFont(weight="bold", size=15),anchor="w",width=100)
        self.Phone_lab.grid(row=5,column=0,padx=5,pady=5,sticky="nsew")

        self.Address_lab = customtkinter.CTkLabel(self, text="Address: ",text_color="black",font= customtkinter.CTkFont(weight="bold", size=15),anchor="w",width=100)
        self.Address_lab.grid(row=6,column=0,padx=5,pady=5,sticky="nsew")

        self.Aadhaar_lab = customtkinter.CTkLabel(self, text="Aadhaar: ",text_color="black",font= customtkinter.CTkFont(weight="bold", size=15),anchor="w",width=100)
        self.Aadhaar_lab.grid(row=7,column=0,padx=5,pady=5,sticky="nsew")

        self.email_lab = customtkinter.CTkLabel(self, text="Email: ",text_color="black",font= customtkinter.CTkFont(weight="bold", size=15),anchor="w",width=100)
        self.email_lab.grid(row=8,column=0,padx=5,pady=5,sticky="nsew")

        self.insurance_lab = customtkinter.CTkLabel(self, text="Insurance: ",text_color="black",font= customtkinter.CTkFont(weight="bold", size=15),anchor="w",width=100)
        self.insurance_lab.grid(row=9,column=0,padx=5,pady=5,sticky="nsew")


        self.Name = customtkinter.CTkEntry(self,placeholder_text="Enter Name")
        self.Name.grid(row=2,column=1,padx=5,pady=5,sticky="nsew")

        self.dob = customtkinter.CTkEntry(self,placeholder_text="Enter DOB")
        self.dob.grid(row=3,column=1,padx=5,pady=5,sticky="nsew")

        self.Sex = customtkinter.CTkOptionMenu(self,values=["M","F"])
        self.Sex.grid(row=4,column=1,padx=5,pady=5,sticky="nsew")

        self.Phone = customtkinter.CTkEntry(self,placeholder_text="Enter Phone")
        self.Phone.grid(row=5,column=1,padx=5,pady=5,sticky="nsew")

        self.Address = customtkinter.CTkEntry(self,placeholder_text="Enter Address")
        self.Address.grid(row=6,column=1,padx=5,pady=5,sticky="nsew")

        self.Aadhaar = customtkinter.CTkEntry(self,placeholder_text="Enter Aadhaar")
        self.Aadhaar.grid(row=7,column=1,padx=5,pady=5,sticky="nsew")

        self.email = customtkinter.CTkEntry(self,placeholder_text="Enter Email")
        self.email.grid(row=8,column=1,padx=5,pady=5,sticky="nsew")

        self.insurance = customtkinter.CTkEntry(self,placeholder_text="Enter Insurance")
        self.insurance.grid(row=9,column=1,padx=5,pady=5,sticky="nsew")

        self.Name.insert(0,arr[1])
        self.Aadhaar.insert(0,arr[2])
        self.dob.insert(0,arr[3])
        print(arr[4])
        self.Phone.insert(0,arr[4])
        print(arr[5])
        self.email.insert(0,arr[5])
        print(arr[6])
        self.Address.insert(0,arr[6])
        print(arr[7])
        self.insurance.insert(0,arr[7])
        print(arr[8])
        self.Sex.set(arr[8])

        # PID--Name--aadhaar--dob--mobile--email--addres--insurencewId--sex

        self.submit = customtkinter.CTkButton(self, text="Submit",command=self.details_validation)
        self.submit.grid(row=10,column=0,padx=5,pady=5,sticky="nsew",columnspan=2)



        # self.geometry("350x540")
        self.p_id = arr[0]
        #name--aadhaar--dob--mobile--email--addres--insurencewId--sex
    def details_validation(self):
        validate=d.patient_details_errorfinder(self.Name.get(),self.dob.get(),self.Phone.get(),self.Address.get(), self.insurance.get(),self.Aadhaar.get(),self.email.get())
        if validate!=False:
            q.edit_patient(p_id=self.p_id,name=self.Name.get(),aadhaar=self.Aadhaar.get(),dob=self.dob.get(),mobile=self.Phone.get(),email=self.email.get(),addres=self.Address.get(),insurencewId=self.insurance.get(),sex=self.Sex.get())
            def close_dialog():
                dialog.destroy()

            # Create a new CTk window
            dialog = customtkinter.CTk()
            dialog.geometry("180x120")
            dialog.title("status")

            # Error message
            error_message = customtkinter.CTkLabel(dialog, text=" Sucessfully edited! ", font=("Arial", 12),text_color="green")
            error_message.pack(pady=(20, 10))

            # OK button to close the dialog
            ok_button = customtkinter.CTkButton(dialog, text="Close", command=close_dialog)
            ok_button.pack(pady=(0, 20))
            dialog.mainloop()
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
        Blank.grid(row=0,column=3,padx=160,pady=10)
        edit.grid(row=0,column=4,padx=10,pady=0)
        self.toplevel_window = None
        self.toplevel_window2 = None
    
    def edit_patient(self,p_id):
        val=q.patient66(name=p_id)
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
        patient_sex_label = customtkinter.CTkLabel(self, text=f"Sex: {self.Sex}", text_color="black", font=customtkinter.CTkFont(size=20))
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