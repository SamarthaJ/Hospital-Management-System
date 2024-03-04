import customtkinter
from PIL import Image

class Mainboard(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 720,height:int = 600, **kwargs):
        super().__init__(master, height=height, width=width, **kwargs)
        label = customtkinter.CTkLabel(self, text="RoomList")
        label.grid(row=1,column=1,padx=100,pady=100)