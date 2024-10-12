import customtkinter as ctk

def create_dropdown(options, width=300, height=200, theme="dark-blue", default_value=None):
    """
    Creates a dropdown menu for a list of options.

    Args:
        options (list): A list of option strings for the dropdown.
        width (int): Width of the window.
        height (int): Height of the window.
        theme (str): CustomTkinter theme for appearance.
        default_value (str): The default selected value (optional).
    """
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme(theme)

    window = ctk.CTk()  # Initialize window
    window.geometry(f"{width}x{height}")
    window.resizable(False, False)  # Disable window resizing

    # Create and display dropdown
    dropdown_var = ctk.StringVar(value=default_value if default_value else options[0])
    dropdown = ctk.CTkComboBox(window, variable=dropdown_var, values=options)
    dropdown.place(relx=0.5, rely=0.5, anchor="center")  # Center the dropdown

    window.mainloop()

    return dropdown_var

# Example usage
if __name__ == "__main__":
    options = ["Option 1", "Option 2", "Option 3"]
    create_dropdown(options, width=300, height=300)
