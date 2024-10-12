import customtkinter as ctk

def create_checkboxes(options, width=300, height=200, theme="dark-blue"):
    """
    Creates a set of checkboxes for a list of options.
    """
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme(theme)

    window = ctk.CTk()
    window.geometry(f"{width}x{height}")
    window.resizable(False, False)

    variables = []
    for i, option in enumerate(options):
        var = ctk.StringVar(value="unchecked")
        checkbox = ctk.CTkCheckBox(window, text=option, variable=var, onvalue="checked", offvalue="unchecked", fg_color="#1A1A1A", text_color="#ADD8E6")
        checkbox.place(relx=0.5, rely=0.1 * (i + 1), anchor="center")
        variables.append(var)

    window.mainloop()

    return variables

if __name__ == "__main__":
    options = ["Option 1", "Option 2", "Option 3"]
    create_checkboxes(options, width=300, height=300)