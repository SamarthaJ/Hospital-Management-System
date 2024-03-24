import customtkinter
from PIL import Image
import querr as q




class DeptSelect(customtkinter.CTkFrame):
    def __init__(self, master, width: int = 350, height: int = 500, **kwargs):
        super().__init__(master, height=height, width=width, border_color="black", border_width=2, fg_color="white", bg_color="transparent", **kwargs)
        label1 = customtkinter.CTkLabel(self, text="Department", text_color="black")
        label1.grid(row=0, column=0, padx=2, pady=2)

        # new = listofemp(self, dept="Cardiology")
        self.selected_value = "Cardiology"  # Initialize selected_value with a default value

        self.select = customtkinter.CTkOptionMenu(self, command=self.get_select, width=350, height=50, button_color="#e4e4e4", button_hover_color="#e4e4e4", dynamic_resizing=False, text_color="black", fg_color="#e4e4e4", bg_color="transparent")
        self.select.configure(values=q.dept_list())
        self.select.set(self.selected_value)  # Set the initial value
        print(self.selected_value)
        self.select.grid(row=1, column=0, padx=10, pady=10)

    def get_select(self, get):
        # Stores the selected value from the option menu from dept_select class
        self.selected_value = get
        new = listofemp(self, dept=self.selected_value)
        new.grid(row=2, column=0, padx=2, pady=2, sticky="nsew")
        # self.a=q.doctors_list_by_dept(self.selected_value)
        
        # try:
        #     self.emp.grid_forget()
        # except AttributeError:
        #     pass
        # x=4
        # for i in self.a:
        #     self.emp = fetchemp(self,name=i[0], ID=i[1], Role=i[2])
        #     self.emp.grid(row=x,column=0,padx=2,pady=2,sticky="nsew")
        #     x+=1
        # print(self.selected_value)  # Print the selected value


class fetchemp(customtkinter.CTkButton):
    def __init__(self, master, name,ID,Role, width:int = 350,height:int = 50, **kwargs):
        super().__init__(master, anchor="right", height=height, width=width, border_color="black",border_width=2,fg_color="white",bg_color="transparent",text="name: " + name +"\tID: "+str(ID)+"\tRole:"+ Role,text_color="black",font=customtkinter.CTkFont(size=10),command=lambda:[self.view(ID = ID)],**kwargs)
        self.toplevel_window2 = None
    def view(self,ID):
        a = q.getDoctorDetails(ID=ID)
        print(a)
        if self.toplevel_window2 is None or not self.toplevel_window2.winfo_exists():
            self.toplevel_window2 = grid2(arr=a)
             # create window if its None or destroyed
        else:
            self.toplevel_window2.focus()  # if window exists focus it
        pass

class listofemp(customtkinter.CTkScrollableFrame):
    def __init__(self, master, dept:str   ,width:int = 350,height:int = 300, **kwargs):
        super().__init__(master, height=height, width=width, border_color="black",border_width=2,fg_color="white",bg_color="transparent",**kwargs)
        self.a=q.doc(dept)
        
        try:
            self.emp.grid_forget()
        except AttributeError:
            pass
        x=4
        for i in self.a:
            self.emp = fetchemp(self,name=i[0], ID=i[1], Role=i[2])
            self.emp.grid(row=x,column=0,padx=2,pady=2,sticky="nsew")
            x+=1  # Print the selected value

class listofdoc(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 320,height:int = 400, **kwargs):
        super().__init__(master, height=height, width=width, border_color="black",border_width=2,fg_color="white",bg_color="transparent",**kwargs)
        self.grid_columnconfigure((0,1),weight=1)
        doc = customtkinter.CTkLabel(self,text="Doctor: "+q.doc_count(),text_color="black")
        Nur = customtkinter.CTkLabel(self,text="Nurse: "+q.nurse_count(),text_color="black")
        doc.grid(row=0,column=0,padx=60,pady=10,sticky="ew")
        Nur.grid(row=0,column=1,padx=60,pady=10,sticky="ew")

        

        




class grid1(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 320,height:int = 500, **kwargs):
        super().__init__(master, height=height, width=width, fg_color="white",**kwargs)
        self.grid_rowconfigure((0,1),weight=0)
        self.grid_rowconfigure(2,weight=10)
        Listofdoc_nurse = listofdoc(self)
        Listofdoc_nurse.grid(row=0,column=0,padx=1,pady=10)
        sel_department = DeptSelect(self)
        sel_department.grid(row=1,column=0,padx=2,pady=2)

        # emp = listofemp(self, dept="Cardiology")
        # emp.grid(row=2,column=0,padx=10,pady=10,sticky="nsew")


class grid2(customtkinter.CTkToplevel):
    def __init__(self,*args, arr, **kwargs):
        super().__init__(*args, fg_color="#F1F1F1", **kwargs)
        
        # ID
        # Name
        # Department
            # ==> Get the department name from the database using department ID
        # Role
        # Address
        # Aadhar
        # dept = q.dept_name(arr[2]) 

        Main_label = customtkinter.CTkLabel(self, text="Doctor Details", font=customtkinter.CTkFont(weight="bold", size=20), text_color="black")
        Main_label.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky="nsew")
        
        Id = customtkinter.CTkLabel(self, width=100,text="ID", font=customtkinter.CTkFont(weight="bold"), text_color="black", anchor="w")
        Id.grid(row=1,column=0,padx=5,pady=5,sticky="nsew")

        Name = customtkinter.CTkLabel(self, width=100,text="Name", font=customtkinter.CTkFont(weight="bold"), text_color="black", anchor="w")
        Name.grid(row=2,column=0,padx=5,pady=5,sticky="nsew")

        Department = customtkinter.CTkLabel(self, width=100,text="Department", font=customtkinter.CTkFont(weight="bold"), text_color="black", anchor="w")
        Department.grid(row=3,column=0,padx=5,pady=5,sticky="nsew")

        Role = customtkinter.CTkLabel(self, width=100,text="Role", font=customtkinter.CTkFont(weight="bold"), text_color="black", anchor="w")
        Role.grid(row=4,column=0,padx=5,pady=5,sticky="nsew")

        Address = customtkinter.CTkLabel(self, width=100,text="Address", font=customtkinter.CTkFont(weight="bold"), text_color="black", anchor="w")
        Address.grid(row=5,column=0,padx=5,pady=5,sticky="nsew")

        Aadhar = customtkinter.CTkLabel(self, width=100,text="Aadhar", font=customtkinter.CTkFont(weight="bold"), text_color="black", anchor="w")
        Aadhar.grid(row=6,column=0,padx=5,pady=5,sticky="nsew")    

        Id_Data = customtkinter.CTkLabel(self, width=100,text=arr[0][0], text_color="black", anchor="w")
        Id_Data.grid(row=1,column=1,padx=5,pady=5,sticky="nsew")

        Name_Data = customtkinter.CTkLabel(self, width=100,text=arr[0][1], text_color="black", anchor="w")
        Name_Data.grid(row=2,column=1,padx=5,pady=5,sticky="nsew")

        Department_Data = customtkinter.CTkLabel(self, width=100,text=arr[0][2], text_color="black", anchor="w")
        Department_Data.grid(row=3,column=1,padx=5,pady=5,sticky="nsew")

        Role_Data = customtkinter.CTkLabel(self, width=100,text=arr[0][3], text_color="black", anchor="w")
        Role_Data.grid(row=4,column=1,padx=5,pady=5,sticky="nsew")

        Address_Data = customtkinter.CTkLabel(self, width=100,text=arr[0][4], text_color="black", anchor="w")
        Address_Data.grid(row=5,column=1,padx=5,pady=5,sticky="nsew")

        Aadhar_Data = customtkinter.CTkLabel(self, width=100,text=arr[0][5], text_color="black", anchor="w")
        Aadhar_Data.grid(row=6,column=1,padx=5,pady=5,sticky="nsew")

        Close = customtkinter.CTkButton(self, text="Close",command=self.destroy)
        Close.grid(row=7,column=0,padx=20,pady=5,columnspan=2)




class Mainboard(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 720,height:int = 400, **kwargs):
        super().__init__(master, height=height, width=width, fg_color="white",**kwargs)
        self.grid_columnconfigure(0,weight=0)
        self.grid_columnconfigure(1,weight=10)
        grid_1 = grid1(self)
        grid_1.grid(row=0,column=0,padx=10,pady=10)

