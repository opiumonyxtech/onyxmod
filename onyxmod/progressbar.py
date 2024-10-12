import customtkinter as ctk

def create_progress_bar(min_value=0, max_value=100, initial_value=0, width=300, height=20, theme="dark-blue"):
    """
    Creates a customizable progress bar.
    """
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme(theme)

    window = ctk.CTk()
    window.geometry(f"{width}x{height+50}")

    progress = ctk.CTkProgressBar(window, width=width, height=height, fg_color="#1A1A1A", progress_color="#ADD8E6")
    progress.set(initial_value / max_value)
    progress.place(relx=0.5, rely=0.5, anchor="center")

    window.mainloop()

    return progress

if __name__ == "__main__":
    create_progress_bar(initial_value=50)