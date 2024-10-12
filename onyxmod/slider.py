import customtkinter as ctk

def create_slider():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    window = ctk.CTk()
    window.geometry("300x200")

    # Slider with custom theme
    slider = ctk.CTkSlider(window, from_=0, to=100, fg_color="#1A1A1A", progress_color="#ADD8E6", 
                           button_color="#ADD8E6", button_hover_color="#FFFFFF", width=250)
    slider.place(relx=0.5, rely=0.5, anchor="center")

    window.mainloop()

if __name__ == "__main__":
    create_slider()