import customtkinter
from PIL import Image
import querr as q

class DeptSelect(customtkinter.CTkFrame):
    def __init__(self, master, width: int = 350, height: int = 100, **kwargs):
        super().__init__(master, height=height, width=width, border_color="black", border_width=2, fg_color="white", bg_color="transparent", **kwargs)
        label1 = customtkinter.CTkLabel(self, text="Department", text_color="black")
        label1.grid(row=0, column=0, padx=2, pady=2)

        self.selected_value = "--Please-Select--"  # Initialize selected_value with a default value

        self.select = customtkinter.CTkOptionMenu(self, command=self.get_select, width=350, height=50, button_color="#e4e4e4", button_hover_color="#e4e4e4", dynamic_resizing=False, text_color="black", fg_color="#e4e4e4", bg_color="transparent")
        self.select.configure(values=q.dept_list())
        self.select.set(self.selected_value)  # Set the initial value
        print(self.selected_value)
        self.select.grid(row=1, column=0, padx=10, pady=10)

    def get_select(self, get):
        # Stores the selected value from the option menu from dept_select class
        self.selected_value = get
        print(self.selected_value)  # Print the selected value


class fetchemp(customtkinter.CTkButton):
    def __init__(self, master, name,ID,Role, width:int = 350,height:int = 50, **kwargs):
        super().__init__(master, anchor="right", height=height, width=width, border_color="black",border_width=2,fg_color="white",bg_color="transparent",text="name: " + name +"\tID: "+str(ID)+"\tRole:"+ Role,text_color="black",font=customtkinter.CTkFont(size=10),**kwargs)


class listofemp(customtkinter.CTkScrollableFrame):
    def __init__(self, master, width:int = 350,height:int = 300, **kwargs):
        super().__init__(master, height=height, width=width, border_color="black",border_width=2,fg_color="white",bg_color="transparent",**kwargs)
        a=q.doctors_list_by_dept()
        x=0
        for i in a:
            emp = fetchemp(self,
                                            name=i[0],
                                            ID=i[1],
                                            Role=i[2]
                                    )
            emp.grid(row=x,column=0,padx=2,pady=2,sticky="nsew")
            x+=1


class listofdoc(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 320,height:int = 400, **kwargs):
        super().__init__(master, height=height, width=width, border_color="black",border_width=2,fg_color="white",bg_color="transparent",**kwargs)
        self.grid_columnconfigure((0,1),weight=1)
        doc = customtkinter.CTkLabel(self,text="Doctor: "+q.doc_count(),text_color="black")
        Nur = customtkinter.CTkLabel(self,text="Nurse: "+"0",text_color="black")
        doc.grid(row=0,column=0,padx=60,pady=10,sticky="ew")
        Nur.grid(row=0,column=1,padx=60,pady=10,sticky="ew")

        

        




class grid1(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 320,height:int = 500, **kwargs):
        super().__init__(master, height=height, width=width, fg_color="white",**kwargs)
        self.grid_rowconfigure((0,1),weight=0)
        self.grid_rowconfigure(2,weight=10)
        sel_department = DeptSelect(self)
        sel_department.grid(row=0,column=0,padx=2,pady=2)

        Listofdoc_nurse = listofdoc(self)
        Listofdoc_nurse.grid(row=1,column=0,padx=1,pady=10)
        emp = listofemp(self)
        emp.grid(row=2,column=0,padx=10,pady=10,sticky="nsew")


class grid2(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 720,height:int = 500, **kwargs):
        super().__init__(master, height=height, width=width, **kwargs)
        self.grid_rowconfigure((0,1),weight=0)
        self.grid_rowconfigure(2,weight=10)


class Mainboard(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 720,height:int = 400, **kwargs):
        super().__init__(master, height=height, width=width, fg_color="white",**kwargs)
        self.grid_columnconfigure(0,weight=0)
        self.grid_columnconfigure(1,weight=10)
        grid_1 = grid1(self)
        grid_1.grid(row=0,column=0,padx=10,pady=10)
        grid_2 = grid2(self)
        grid_2.grid(row=0,column=2,padx=10,pady=10)

