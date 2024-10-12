import customtkinter as ctk

def create_button(label="Click Me", on_click_function=None):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    window = ctk.CTk()
    window.geometry("400x200")
    window.resizable(False, False)

    button = ctk.CTkButton(window, text=label, fg_color="#1A1A1A", text_color="#ADD8E6",
                           border_color="#F5F5F5", border_width=2, font=("Helvetica", 16, "bold"),
                           command=on_click_function)
    button.place(relx=0.5, rely=0.5, anchor="center")

    window.mainloop()

if __name__ == "__main__":
    create_button(label="Press Me", on_click_function=lambda: print("Button pressed!"))