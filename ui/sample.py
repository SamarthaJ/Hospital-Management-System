# import customtkinter as ctk

# # Create a new instance of the CTkInputDialog class
# dialog = ctk.CTkInputDialog(title="Input", text="Enter your name:")

# # Display the dialog box and get the user's input
# name = dialog.get_input()

# # Print the user's input
# print(name)






# import customtkinter as ctk

# # Create a new instance of the CTkInputDialog class
# label = ctk.CTkLabel(dialog, text="This is a dialog box.")
                           
                        
# # Add a button to the dialog box
# button = ctk.CTkButton(dialog, text="Submit")

# # Add a text box to the dialog box
# text_box = ctk.CTkTextbox(dialog)

# # Display the dialog box and get the user's input
# name = dialog.get_input()
# address = text_box.get_text()

# # Print the user's input
# print(name)
# print(address)

# import customtkinter as ctk
# import tkinter as tk
# from tkinter import messagebox

# # Basic parameters and initializations
# ctk.set_appearance_mode("System")
# ctk.set_default_color_theme("green")
# appWidth, appHeight = 600, 700

# App Class
# class App(ctk.CTk):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.title("GUI Application")
#         self.geometry(f"{appWidth}x{appHeight}")

#         # Name Label
#         # (Code for other GUI elements remains the same)

#         # Generate Button
#         self.generateResultsButton = ctk.CTkButton(self, text="Generate Results", command=self.show_dialog)
#         self.generateResultsButton.grid(row=5, column=1, columnspan=2, padx=20, pady=20, sticky="ew")

#     def show_dialog(self):
#         message = "Results Generated Successfully!"
#         messagebox.showinfo("Results", message)

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

# # Basic parameters and initializations
# ctk.set_appearance_mode("System")
# ctk.set_default_color_theme("green")
# appWidth, appHeight = 600, 700

# # App Class
# class App(ctk.CTk):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.title("GUI Application")
#         self.geometry(f"{appWidth}x{appHeight}")

#         # Name Label
#         # (Code for other GUI elements remains the same)

#         # Generate Button
#         self.generateResultsButton = ctk.CTkButton(self, text="Generate Results", command=self.show_error)
#         self.generateResultsButton.grid(row=5, column=1, columnspan=2, padx=20, pady=20, sticky="ew")

# def show_error():
#     message = "Error: Results could not be generated!"
#     messagebox.showerror("Error", message)

# # if __name__ == "__main__":
# #     app = App()
# #     app.mainloop()
# show_error()

#----------------------------------------------------------------------------------------------------------------------------------------------------

# import customtkinter as ctk

# class App(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         self.title("CustomTKinter App")
#         self.geometry("400x300")

#         # Button to open the dialog
#         self.open_dialog_btn = ctk.CTkButton(self, text="Open Dialog", command=self.open_dialog)
#         self.open_dialog_btn.pack(pady=20)

#     def open_dialog(self):
#         self.dialog = ctk.CTkToplevel(self)
#         self.dialog.geometry("200x100")
#         self.dialog.title("Dialog")

#         # Dialog message
#         self.dialog_msg = ctk.CTkLabel(self.dialog, text="An error occurred!", width=100, height=25)
#         self.dialog_msg.pack(pady=10)

#         # OK button in the dialog
#         self.ok_btn = ctk.CTkButton(self.dialog, text="OK", command=self.close_dialog)
#         self.ok_btn.pack()

#     def close_dialog(self):
#         self.dialog.destroy()

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

import customtkinter
from customtkinter import CTkLabel, CTkButton, CTkFrame

class SubmitMessagePopup(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = CTkLabel(self, text="Your submission was successful!")
        self.button = CTkButton(self, text="OK", command=self.destroy)

        self.label.pack(pady=10)
        self.button.pack(pady=10)

def show_submit_message_popup():
    root = customtkinter.CTk()
    popup = SubmitMessagePopup(root)
    popup.pack()
    root.mainloop()

# Example usage:
show_submit_message_popup()


