import customtkinter as ctk

app = ctk.CTk()

reset_button = ctk.CTkButton(app, text="Reset Data")
reset_button.pack(padx=20, pady=20)

app.mainloop()