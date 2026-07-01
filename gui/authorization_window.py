import customtkinter as ctk


class AuthorizationWindow(ctk.CTk):
    def __init__(self):
        # window init
        super().__init__()
        self.geometry("400x150")
        self.resizable(False, False)
        self.title("ИСРХ")
        # label init
        self.label = ctk.CTkLabel(self, text="Информационная система рыболовного хозяйства", font=("Comic Sans MS", 14))
        self.label.pack(padx=0, pady=10)
        # entry init
        self.login_entry = ctk.CTkEntry(self, placeholder_text="Логин")
        self.login_entry.pack(padx=0, pady=0)
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Пароль")
        self.password_entry.pack(padx=0, pady=0)
        # button init
        self.button = ctk.CTkButton(self, text="Войти", command=self.button_callbck)
        self.button.pack(padx=0, pady=10)

    def button_callbck(self):
        print(f"Логин >> {self.login_entry.get()}")
        print(f"Пароль >> {self.password_entry.get()}")
