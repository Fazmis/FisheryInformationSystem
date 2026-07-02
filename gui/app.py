import customtkinter as ctk
from .main_frame import MainFrame
from .login_frame import LoginFrame
from .registration_frame import RegistrationFrame

class App(ctk.CTk):
    def __init__(self, database):
        super().__init__()
        self.geometry("720, 360")
        self.resizable(False, False)
        self.title("ИСРХ")
        self.database = database
        self.is_admin = None

        if self.database.have_users():
            self.show_login()
        else:
            self.is_admin = True
            self.show_registration(grant_admin_rights=True)

    def show_login(self):
            self.clear()

            self.current = LoginFrame(self)
            self.current.pack(fill="both", expand=True)

    def show_registration(self, grant_admin_rights=False):
            self.clear()

            self.current = RegistrationFrame(self, grant_admin_rights=grant_admin_rights)
            self.current.pack(fill="both", expand=True)

    def show_main(self):
            self.clear()

            self.current = MainFrame(self)
            self.current.pack(fill="both", expand=True)

    def clear(self):
            for widget in self.winfo_children():
                widget.destroy()