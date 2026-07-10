import customtkinter as ctk
from .navigation_frame import NavigationFrame
from .reports_frame import ReportsFrame
from .sql_frame import SQLFrame


class MainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.app = master

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.navigation = NavigationFrame(self)
        self.navigation.grid(row=0, column=0, sticky="ns")

        self.content = ctk.CTkFrame(self)
        self.content.grid(row=0, column=1, sticky="nsew")

        self.show_page("Виды_Рыб")

    def show_page(self, table_name):
        self.clear()
        page = SQLFrame(self.content, self.app, table_name)
        page.pack(fill="both", expand=True)

    def show_reports(self):
        self.clear()
        page = ReportsFrame(self.content, self.app)
        page.pack(fill="both", expand=True)

    def clear(self):
        for widget in self.content.winfo_children():
            widget.destroy()