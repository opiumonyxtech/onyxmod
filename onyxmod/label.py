import customtkinter as ctk

def create_label():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    window = ctk.CTk()
    window.geometry("300x200")

    # Custom label
    label = ctk.CTkLabel(window, text="Custom Label", fg_color="#1A1A1A", text_color="#ADD8E6", font=("Helvetica", 16, "bold"))
    label.place(relx=0.5, rely=0.5, anchor="center")

    window.mainloop()

if __name__ == "__main__":
    create_label()