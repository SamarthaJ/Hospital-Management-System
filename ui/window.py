import customtkinter

class second(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 720,height:int = 600, **kwargs):
        super().__init__(master, height=height, width=width, **kwargs)
        label = customtkinter.CTkLabel(self, text="Second")
        label.grid(row=0,column=0,padx=100,pady=100)