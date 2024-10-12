import customtkinter as ctk

def create_window():
    # Set the appearance mode and color theme
    ctk.set_appearance_mode("dark")  # "dark" or "light"
    ctk.set_default_color_theme("dark-blue")  # You can set other color themes if you prefer

    window = ctk.CTk()  # Initialize the customtkinter window
    window.title("App Window with Custom Theme")
    
    # Set the window size to 1200x750 pixels and disable resizing
    window.geometry("1200x750")
    window.resizable(False, False)  # Disable resizing

    # Custom inner frame with darker background
    inner_frame = ctk.CTkFrame(window, fg_color="#2B2B2B", width=1170, height=720)
    inner_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the inner frame

    window.mainloop()

if __name__ == "__main__":
    create_window()
