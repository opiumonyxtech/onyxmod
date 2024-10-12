import customtkinter as ctk

def create_text_display(display_text="Hello, World!", width=400, height=200, font=("Helvetica", 16), theme="dark-blue"):
    """
    Creates a text display widget.
    """
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme(theme)

    window = ctk.CTk()
    window.geometry(f"{width}x{height}")

    label = ctk.CTkLabel(window, text=display_text, font=font, fg_color="#1A1A1A", text_color="#ADD8E6")
    label.place(relx=0.5, rely=0.5, anchor="center")

    window.mainloop()

    return label

if __name__ == "__main__":
    create_text_display(display_text="Welcome to Onyx!", width=400, height=200, font=("Helvetica", 18))