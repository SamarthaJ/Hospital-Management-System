import customtkinter
import home 


class App(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("1280x720")
        self._set_appearance_mode("light")
        self.wm_resizable(False,False)

        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(0,weight=10)

        self.NavFrame = home.nav(master=self)
        self.downFrame = home.down(master=self)

        self.NavFrame.grid(row=0,column=0, padx=20, pady=20)
        self.downFrame.grid(row=1,column=0, padx=20, pady=10,sticky="nsew")
app = App()
app.mainloop()