import customtkinter
from PIL import Image
import querr as q
import random as r
import dialogbox as d

class Mainboard(customtkinter.CTkFrame):
    def __init__(self, master, width:int = 720,height:int = 600, **kwargs):
        super().__init__(master, height=height, width=width, **kwargs)
        # PID varchar | Aphanumeric
        # Name varchar 
        # Aadhar BIGINT(12)
        # DOB DATE
        # Phone BIGINT(10)
        # Email Aphanumeric with Symboool
        # Address text
        # Ins_id varcha | Aphanumaric
        # sex char(1) : M||F

        # Room_block varchar | Aphanumeric
        # Room_number varchar | Aphanumeric





        self.name = customtkinter.CTkEntry(self, placeholder_text="Name",width=300,height=40)
        self.aadhar = customtkinter.CTkEntry(self, placeholder_text="Aadhaar number",width=300,height=40)
        self.dob = customtkinter.CTkEntry(self, placeholder_text="1999-04-11 (YYYY-MM-DD)",width=300,height=40)
        self.phone = customtkinter.CTkEntry(self, placeholder_text="Phone number ",width=300,height=40)
        self.email = customtkinter.CTkEntry(self, placeholder_text="Email",width=300,height=40)
        self.address = customtkinter.CTkEntry(self, placeholder_text="Address",width=300,height=40)
        self.ins = customtkinter.CTkEntry(self, placeholder_text="Insurence ID",width=300,height=40)
        self.sex = customtkinter.CTkOptionMenu(self,values=["M","F"],width=300,height=40)

        


        self.newPID = "New PID here generated automatically"

        self.pid_lab = customtkinter.CTkLabel(self, text=f"{self.newPID}",anchor="w",font=customtkinter.CTkFont(size=15,weight="bold"),width=100)
        self.name_lab = customtkinter.CTkLabel(self, text="Name",anchor="w",font=customtkinter.CTkFont(size=15,weight="bold"),width=100)
        self.aadhar_lab = customtkinter.CTkLabel(self,text="Aadhar",anchor="w",font=customtkinter.CTkFont(size=15,weight="bold"),width=100)
        self.dob_lab = customtkinter.CTkLabel(self, text="Date of Birth",anchor="w",font=customtkinter.CTkFont(size=15,weight="bold"),width=100)
        self.phone_lab = customtkinter.CTkLabel(self, text="Phone",anchor="w",font=customtkinter.CTkFont(size=15,weight="bold"),width=100)
        self.email_lab = customtkinter.CTkLabel(self, text="Email",anchor="w",font=customtkinter.CTkFont(size=15,weight="bold"),width=100)
        self.address_lab = customtkinter.CTkLabel(self,text="Address",anchor="w",font=customtkinter.CTkFont(size=15,weight="bold"),width=100)
        self.ins_lab = customtkinter.CTkLabel(self, text="Insurence Id",anchor="w",font=customtkinter.CTkFont(size=15,weight="bold"),width=100)

        self.rnum = customtkinter.CTkOptionMenu(self,command=self.room_num_sel, values=q.avaliable_rooms(),width=300,height=40)

        self.sex_lab=customtkinter.CTkLabel(self,text="Sex",font=customtkinter.CTkFont(size=15,weight="bold"),width=100, anchor="w")
        self.rnum_lab=customtkinter.CTkLabel(self,text="Room Number",font=customtkinter.CTkFont(size=15,weight="bold"),width=100, anchor="w")

        self.pid_lab.grid(row=0,column=1,padx=10,pady=5)
        self.name.grid(row=1,column=1,padx=10,pady=5)
        self.aadhar.grid(row=2,column=1,padx=10,pady=5)
        self.dob.grid(row=3,column=1,padx=10,pady=5)
        self.phone.grid(row=4,column=1,padx=10,pady=5)
        self.email.grid(row=5,column=1,padx=10,pady=5)
        self.address.grid(row=6,column=1,padx=10,pady=5)
        self.ins.grid(row=7,column=1,padx=10,pady=5)

        self.sel_rnum = 'Please Select'

        self.name_lab.grid(row=1,column=0,padx=10,pady=5)
        self.aadhar_lab.grid(row=2,column=0,padx=10,pady=5)
        self.dob_lab.grid(row=3,column=0,padx=10,pady=5)
        self.phone_lab.grid(row=4,column=0,padx=10,pady=5)
        self.email_lab.grid(row=5,column=0,padx=10,pady=5)
        self.address_lab.grid(row=6,column=0,padx=10,pady=5)
        self.ins_lab.grid(row=7,column=0,padx=10,pady=5)

        self.sex.grid(row=8, column=1,padx=10,pady=5)
        self.rnum.grid(row=9, column=1,padx=10,pady=5)

        self.sex_lab.grid(row=8, column=0,padx=10,pady=5)
        self.rnum_lab.grid(row=9, column=0,padx=10,pady=5)

        self.sex.set("Please select")
        self.rnum.set(self.sel_rnum)


        self.addbtn = customtkinter.CTkButton(self, text="Add New Patient",command=self.validation_newPatient, width=300,height=40)

        self.addbtn.grid(row=10, column=0,padx=10,pady=5,columnspan=2)

    def validation_newPatient(self):
        validate=d.patient_details_errorfinder(self.name.get(),self.dob.get(),self.phone.get(),self.address.get(), self.ins.get(),self.aadhar.get(),self.email.get())
        if validate!=False:
            self.name_data = self.name.get()
            self.aadhar_data = self.aadhar.get()
            self.dob_data = self.dob.get()
            self.phone_data = self.phone.get()
            self.email_data = self.email.get()
            self.address_data = self.address.get()
            self.ins_data = self.ins.get()
            # use self.sel_rblock for to get the block number from option menu
            # use self.sel_rnum for to get the room number from option menu
            pid=r.randint(50000,60001)
            q.add_patient(pid=pid,name=self.name_data,aadhar=self.aadhar_data,dob=self.dob_data,mobile=self.phone_data,email=self.email_data,address=self.address_data,insu_id=self.ins_data,sex='M')
            self.name.delete(0,'end')
            self.aadhar.delete(0,'end')
            self.dob.delete(0,'end')
            self.phone.delete(0,'end')
            self.email.delete(0,'end')
            self.address.delete(0,'end')
            self.ins.delete(0,'end')
            self.sex.set("Please select")
            self.rnum.set("Please select")
            
            def close_dialog():
                dialog.destroy()

            # Create a new CTk window
            dialog = customtkinter.CTk()
            dialog.geometry("180x120")
            dialog.title("status")

            # Error message
            error_message = customtkinter.CTkLabel(dialog, text=" Sucessfully added! ", font=("Arial", 12),text_color="green")
            error_message.pack(pady=(20, 10))

            # OK button to close the dialog
            ok_button = customtkinter.CTkButton(dialog, text="Close", command=close_dialog)
            ok_button.pack(pady=(0, 20))
            dialog.mainloop()



            

    def room_block_sel(self,get):
        self.sel_rblock=get
        print(self.sel_rblock)
    
    def room_num_sel(self,get):
        self.sel_rnum=get
        print(self.sel_rnum)