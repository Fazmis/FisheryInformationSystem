import customtkinter as ctk


class NavigationFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        ctk.CTkButton(
            self,
            text="Рыба",
            command=lambda: self.master.show_page("Виды_Рыб")
        ).pack(fill="x")

        ctk.CTkButton(
            self,
            text="Озера",
            command=lambda: self.master.show_page("Озера")
        ).pack(fill="x")

        ctk.CTkButton(
            self,
            text="Обитание",
            command=lambda: self.master.show_page("Обитание_Видов")
        ).pack(fill="x")

        ctk.CTkButton(
            self,
            text="Рыбалка",
            command=lambda: self.master.show_page("Рыбалка_на_озерах")
        ).pack(fill="x")

        if self.master.app.user["admin_rights"]:
            ctk.CTkButton(
                self,
                text="Пользователи",
                command=lambda: self.master.show_page("Пользователи")
            ).pack(fill="x")

            ctk.CTkButton(
                self,
                text="Отчеты",
                command=lambda: self.master.show_reports()
            ).pack(fill="x")

        ctk.CTkButton(
            self,
            text="Выход",
            command=lambda: self.master.app.show_login()
        ).pack(fill="x")
