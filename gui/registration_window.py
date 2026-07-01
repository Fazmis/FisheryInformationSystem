import customtkinter as ctk


class RegistrationWindow(ctk.CTk):
    def __init__(self, database, is_admin=False):
        # window init
        super().__init__()
        self.geometry("400x150")
        self.resizable(False, False)
        self.title("ИСРХ")
        self.database = database
        self.is_admin = is_admin
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
        login = self.login_entry.get()
        password = self.password_entry.get()
        user = self.database.sign_up(login, password, is_admin=self.is_admin)
        if user is None:
            pass
        else:
            self.user = user
            self.destroy()