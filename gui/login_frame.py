import customtkinter as ctk


class LoginFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.app = master
        # label init
        self.label = ctk.CTkLabel(self, text="Информационная система рыболовного хозяйства", font=("Comic Sans MS", 14))
        self.label.pack(padx=10, pady=10)
        # entry init
        self.login_entry = ctk.CTkEntry(self, placeholder_text="Логин")
        self.login_entry.pack(padx=0, pady=0)
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Пароль")
        self.password_entry.pack(padx=0, pady=0)
        # error_label init
        self.error_label = ctk.CTkLabel(self, text="", text_color="red", font=("Comic Sans MS", 12))
        self.error_label.pack(padx=0, pady=0)
        # button init
        self.button = ctk.CTkButton(self, text="Войти", command=self.button_callback)
        self.button.pack(padx=0, pady=10)

    def button_callback(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        user = self.app.database.login(login, password)
        if user is None:
            self.error_label.configure(text="Неверно указан логин или пароль")
        else:
            user_id, user_login, user_is_admin = user
            self.app.is_admin = user_is_admin
            self.app.show_main()

