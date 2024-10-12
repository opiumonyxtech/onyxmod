import customtkinter as ctk

class MultiWidgetContainer(ctk.CTkFrame):
    def __init__(self, parent, label_text="Multi-Widget Container", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Add a label at the top
        self.label = ctk.CTkLabel(self, text=label_text, fg_color="#2B2B2B", text_color="#ADD8E6", font=("Arial", 14))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")  # Align label to the top

        # Create a frame to hold the buttons or other widgets
        self.widget_frame = ctk.CTkFrame(self, fg_color="#2B2B2B")
        self.widget_frame.grid(row=1, column=0, padx=10, pady=10)

        # Dictionary to hold the dynamically added buttons/widgets
        self.widgets = []

    def add_button(self, button_text="Button", command=None):
        """Adds a button to the container."""
        button = ctk.CTkButton(self.widget_frame, text=button_text, fg_color="#1A1A1A", text_color="#ADD8E6",
                               border_color="#F5F5F5", border_width=2, font=("Helvetica", 16, "bold"),
                               command=command, width=150, height=40)
        button.grid(row=len(self.widgets), column=0, padx=10, pady=5)
        self.widgets.append(button)

    def add_dropdown(self, values=["Option 1", "Option 2"], selected=None):
        """Adds a dropdown (ComboBox) to the container."""
        dropdown = ctk.CTkComboBox(self.widget_frame, values=values, fg_color="#1A1A1A", text_color="#ADD8E6",
                                   border_color="#F5F5F5", font=("Helvetica", 14), width=150, height=40)
        dropdown.grid(row=len(self.widgets), column=0, padx=10, pady=5)
        self.widgets.append(dropdown)

    def clear_widgets(self):
        """Clears all widgets from the container."""
        for widget in self.widgets:
            widget.grid_forget()
        self.widgets.clear()


def create_main_window():
    # Set the appearance mode and color theme
    ctk.set_appearance_mode("dark")  # "dark" or "light"
    ctk.set_default_color_theme("dark-blue")  # You can set other color themes if you prefer

    window = ctk.CTk()  # Initialize the customtkinter window
    window.title("Multi-Widget Container Example")
    window.geometry("400x400")  # Set the window size to 400x400 pixels
    window.resizable(False, False)  # Disable resizing

    # Create the multi-widget container and add it to the main window
    container = MultiWidgetContainer(window, label_text="My Widget Container")
    container.place(relx=0.5, rely=0.5, anchor="center")  # Center the container

    # Add a few buttons and dropdowns to demonstrate flexibility
    container.add_button(button_text="Button 1", command=lambda: print("Button 1 pressed"))
    container.add_button(button_text="Button 2", command=lambda: print("Button 2 pressed"))
    container.add_dropdown(values=["Option A", "Option B", "Option C"])

    window.mainloop()

if __name__ == "__main__":
    create_main_window()
