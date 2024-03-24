import re   
import customtkinter as ctk
from datetime import datetime
def patient_details_errorfinder(name,dob,Phone,Address,insurance,Aadhaar,email):
    #--------------------------name-------------------------------------------
    name_str=str(name).replace(" ", "") 
    if name_str == "":
    #     print(name)
    #     print(type(name))
    #     pass
    # else:
        def close_dialog():
            dialog.destroy()

        # Create a new CTk window
        dialog = ctk.CTk()
        dialog.geometry("300x150")
        dialog.title("Error")

        # Error message
        error_message = ctk.CTkLabel(dialog, text=" Enter a valid name!", font=("Arial", 12))
        error_message.pack(pady=(20, 10))

        # OK button to close the dialog
        ok_button = ctk.CTkButton(dialog, text="OK", command=close_dialog)
        ok_button.pack(pady=(0, 20))

        dialog.mainloop()
        return  False 
    #-----------------------------Dob-------------------------------------------
    try:
    # Code that may raise an exception
        dob_obj = datetime.strptime(dob, "%Y-%m-%d") 
        dob_str = dob_obj.strftime("%Y-%m-%d")
    except Exception as e:
    # Code to handle the exception
        def close_dialog():
            dialog.destroy()

        # Create a new CTk window
        dialog = ctk.CTk()
        dialog.geometry("300x150")
        dialog.title("Error")

        # Error message
        error_message = ctk.CTkLabel(dialog, text=" Enter valid date-format!", font=("Arial", 12))
        error_message.pack(pady=(20, 10))

        # OK button to close the dialog
        ok_button = ctk.CTkButton(dialog, text="OK", command=close_dialog)
        ok_button.pack(pady=(0, 20))

        dialog.mainloop()
        return  False 
    
    #-------------------------------------------phone------------------------------------------------------
    phone_pattern = r"^\d{10}$"  
    phone_str=str(Phone)
    if re.match(phone_pattern, phone_str):
        pass
    else:
        def close_dialog():
            dialog.destroy()

        # Create a new CTk window
        dialog = ctk.CTk()
        dialog.geometry("300x150")
        dialog.title("Error Dialog")

        # Error message
        error_message = ctk.CTkLabel(dialog, text=" Enter a valid phone number!", font=("Arial", 12))
        error_message.pack(pady=(20, 10))

        # OK button to close the dialog
        ok_button = ctk.CTkButton(dialog, text="OK", command=close_dialog)
        ok_button.pack(pady=(0, 20))

        dialog.mainloop()
        return  False
    #------------------------------------------address--------------------------------------------------------------
    
    if Address.replace(" ", "") == "" :
    #     pass
    # else:
        def close_dialog():
            dialog.destroy()

        # Create a new CTk window
        dialog = ctk.CTk()
        dialog.geometry("300x150")
        dialog.title("Error")

        # Error message
        error_message = ctk.CTkLabel(dialog, text=" Enter a valid address!", font=("Arial", 12))
        error_message.pack(pady=(20, 10))

        # OK button to close the dialog
        ok_button = ctk.CTkButton(dialog, text="OK", command=close_dialog)
        ok_button.pack(pady=(0, 20))

        dialog.mainloop()
        return  False 
    
    #------------------------------------Aadhar------------------------------------------------------------

    Aadhaar_pattern = r"^\d{12}$"  
    Aadhaar_str=str(Aadhaar)
    if re.match(Aadhaar_pattern, Aadhaar_str):
        pass
    else:
        def close_dialog():
            dialog.destroy()

        # Create a new CTk window
        dialog = ctk.CTk()
        dialog.geometry("300x150")
        dialog.title("Error")

        # Error message
        error_message = ctk.CTkLabel(dialog, text=" Enter a valid aadhar number!", font=("Arial", 12))
        error_message.pack(pady=(20, 10))

        # OK button to close the dialog
        ok_button = ctk.CTkButton(dialog, text="OK", command=close_dialog)
        ok_button.pack(pady=(0, 20))

        dialog.mainloop()
        return  False





    # dob_pattern=r"^\d{4}-\d{2}-\d{2}$"
    # print(dob)
    # print(dob_str)
    # if re.match(dob_pattern, dob_str):
    #     print(True)
    # else:
    #     print(False)
        



#----------------------------------------email-----------------------------------------------------------------------------

    email_pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern,email):
        pass
    else:
        def close_dialog():
            dialog.destroy()

        # Create a new CTk window
        dialog = ctk.CTk()
        dialog.geometry("300x150")
        dialog.title("Error")

        # Error message
        error_message = ctk.CTkLabel(dialog, text=" Enter a valid email Id!", font=("Arial", 12))
        error_message.pack(pady=(20, 10))

        # OK button to close the dialog
        ok_button = ctk.CTkButton(dialog, text="OK", command=close_dialog)
        ok_button.pack(pady=(0, 20))

        dialog.mainloop()
        return False
        #-----------------------------------insurance----------------------------------------------------------

    if insurance.replace(" ", "") =="" :
    #     pass
    # else:
        def close_dialog():
            dialog.destroy()

        # Create a new CTk window
        dialog = ctk.CTk()
        dialog.geometry("300x150")
        dialog.title("Error")

        # Error message
        error_message = ctk.CTkLabel(dialog, text=" Enter a valid insurance ID!", font=("Arial", 12))
        error_message.pack(pady=(20, 10))

        # OK button to close the dialog
        ok_button = ctk.CTkButton(dialog, text="OK", command=close_dialog)
        ok_button.pack(pady=(0, 20))

        dialog.mainloop()
        return  False
    
    return  True


#----------------------------sucessfull_dialog------------------------------------------
def sucessfull_dialog():
    def close_dialog():
        dialog.destroy()

        # Create a new CTk window
        dialog = ctk.CTk()
        dialog.geometry("300x150")
        dialog.title("Error")

        # Error message
        error_message = ctk.CTkLabel(dialog, text=" Sucessfully added! ", font=("Arial", 12),text_color="green")
        error_message.pack(pady=(20, 10))

        # OK button to close the dialog
        ok_button = ctk.CTkButton(dialog, text="Close", command=close_dialog)
        ok_button.pack(pady=(0, 20))

        dialog.mainloop()
    return
#patient_details_errorfinder('1999-04-11',1234567892,898989898980,'chandan.ramesh@gmail.com')


#------------------------------------------------------------------------------------------------------------------------


# import customtkinter as ctk

# def close_dialog():
#     dialog.destroy()

# # Create a new CTk window
# dialog = ctk.CTk()
# dialog.geometry("300x150")
# dialog.title("Error Dialog")

# # Error message
# error_message = ctk.CTkLabel(dialog, text="An error has occurred!", font=("Arial", 12))
# error_message.pack(pady=(20, 10))

# # OK button to close the dialog
# ok_button = ctk.CTkButton(dialog, text="OK", command=close_dialog)
# ok_button.pack(pady=(0, 20))

# dialog.mainloop()