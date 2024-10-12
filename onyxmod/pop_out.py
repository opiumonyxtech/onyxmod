import customtkinter as ctk

def create_button_with_popout(
        button_text="Open Pop-out",
        button_command=None,
        window_title="Button with Pop-Out",
        window_size="400x300",
        pop_out_size="400x300",
        theme="dark-blue"
    ):
    """
    Creates a main window with a button that opens a pop-out window when clicked.

    Args:
        button_text (str): Text on the main button.
        button_command (callable): Command to execute when the button is clicked. Defaults to create_pop_out().
        window_title (str): Title of the main window.
        window_size (str): Size of the main window in "widthxheight" format.
        pop_out_size (str): Size of the pop-out window in "widthxheight" format.
        theme (str): CustomTkinter theme for appearance.
    """

    ctk.set_appearance_mode("dark")  # "dark" or "light"
    ctk.set_default_color_theme(theme)

    window = ctk.CTk()  # Initialize the customtkinter window
    window.title(window_title)
    window.geometry(window_size)  # Set window size
    window.resizable(False, False)  # Disable resizing

    # Create the pop-out window
    if not button_command:
        button_command = lambda: create_pop_out(size=pop_out_size, theme=theme)

    button = ctk.CTkButton(window, text=button_text, fg_color="#1A1A1A", text_color="#ADD8E6",
                           border_color="#F5F5F5", border_width=2, font=("Helvetica", 16, "bold"),
                           command=button_command, width=150, height=40)
    button.place(relx=0.5, rely=0.5, anchor="center")  # Center the button in the main window

    window.mainloop()
    return window, button


def create_pop_out(size="400x300", theme="dark-blue"):
    """
    Creates a pop-out window with a close button.

    Args:
        size (str): Size of the pop-out window in "widthxheight" format.
        theme (str): CustomTkinter theme for appearance.
    """
    pop_out = ctk.CTkToplevel()  # Create a new top-level window (pop-out)
    pop_out.title("Pop-Out Window")
    pop_out.geometry(size)  # Set the size of the pop-out window

    # Custom inner frame with the same background as the main window
    inner_frame = ctk.CTkFrame(pop_out, fg_color="#2B2B2B", width=380, height=280)
    inner_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the inner frame

    # Custom button inside the pop-out window
    pop_out_button = ctk.CTkButton(inner_frame, text="Close Pop-out", fg_color="#1A1A1A", text_color="#ADD8E6",
                                   border_color="#F5F5F5", border_width=2, font=("Helvetica", 16, "bold"),
                                   command=pop_out.destroy, width=150, height=40)
    pop_out_button.place(relx=0.5, rely=0.5, anchor="center")  # Center the button in the pop-out

    return pop_out, pop_out_button


if __name__ == "__main__":
    # Example usage with default settings
    create_button_with_popout()
