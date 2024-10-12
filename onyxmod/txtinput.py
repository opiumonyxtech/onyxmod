import customtkinter as ctk

def create_text_input(placeholder_text="Enter text...", width=300, height=50, theme="dark-blue"):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme(theme)

    window = ctk.CTk()
    window.geometry(f"{width}x{height+50}")

    input_field = ctk.CTkEntry(window, placeholder_text=placeholder_text, fg_color="#1A1A1A", text_color="#ADD8E6", width=width, height=height)
    input_field.place(relx=0.5, rely=0.5, anchor="center")

    window.mainloop()

    return input_field

if __name__ == "__main__":
    create_text_input(placeholder_text="Type something here...", width=350, height=50)