import customtkinter as ctk

def create_chat_window():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    window = ctk.CTk()
    window.title("Chat Application")
    window.geometry("900x750")
    window.resizable(False, False)

    # Outer frame to provide background and structure
    outer_frame = ctk.CTkFrame(window, fg_color="#2B2B2B", width=880, height=730)  # Dark gray background
    outer_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Inner frame for chat display and input
    inner_frame = ctk.CTkFrame(outer_frame, fg_color="#1A1A1A", width=850, height=700)  # Black inner frame
    inner_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Chat display area
    chat_display = ctk.CTkTextbox(inner_frame, fg_color="#1A1A1A", text_color="#ADD8E6",
                                  width=830, height=600, state="disabled")
    chat_display.place(x=10, y=10)

    # Message input field
    message_input = ctk.CTkEntry(inner_frame, width=700, height=40, fg_color="#1A1A1A", text_color="#ADD8E6")
    message_input.place(x=10, y=620)

    # Send button next to the input field
    send_button = ctk.CTkButton(inner_frame, text="Send", fg_color="#1A1A1A", text_color="#ADD8E6",
                                border_color="#F5F5F5", border_width=2, font=("Helvetica", 16, "bold"),
                                command=lambda: send_message(chat_display, message_input),
                                width=120, height=40)
    send_button.place(x=720, y=620)

    window.mainloop()

def send_message(chat_display, message_input):
    message = message_input.get()
    if message:
        chat_display.configure(state="normal")
        chat_display.insert("end", message + "\\n")
        chat_display.configure(state="disabled")
        message_input.delete(0, "end")

if __name__ == "__main__":
    create_chat_window()