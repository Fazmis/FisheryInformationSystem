import customtkinter as ctk


class RegistrationWindow(ctk.CTk):
    def __init__(self):
        # window init
        super().__init__()
        self.geometry("400x150")
        self.resizable(False, False)
        self.title("ИСРХ")
        self.user = None
        # label init
        self.label = ctk.CTkLabel(self, text="Информационная система рыболовного хозяйства", font=("Comic Sans MS", 14))
        self.label.pack(padx=0, pady=10)
        # entry init
        self.login_entry = ctk.CTkEntry(self, placeholder_text="Логин")
        self.login_entry.pack(padx=0, pady=0)
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Пароль")
        self.password_entry.pack(padx=0, pady=0)
        # button init
        self.button = ctk.CTkButton(self, text="Зарегистрироваться", command=self.button_callback)
        self.button.pack(padx=0, pady=10)

    def button_callback(self):
        return self.user
