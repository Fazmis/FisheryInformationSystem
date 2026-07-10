import customtkinter as ctk


class RegistrationFrame(ctk.CTkFrame):
    def __init__(self, master, grant_admin_rights=False):
        super().__init__(master)
        self.app = master
        self.grant_admin_rights = grant_admin_rights
        # label init
        self.label = ctk.CTkLabel(self, text="Информационная система рыболовного хозяйства", font=("Comic Sans MS", 14))
        self.label.pack(padx=10, pady=10)
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
        self.app.user = self.app.database.sign_up(login, password, grant_admin_rights=self.grant_admin_rights)
        self.app.show_main()