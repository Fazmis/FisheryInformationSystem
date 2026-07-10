import customtkinter as ctk
from tkinter import ttk


class ReportsFrame(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)

        self.app = app
        self.database = app.database

        self.reports = {
            "Все виды рыб": "all_fish",
            "Все озёра": "all_lakes",
            "Рыбалка по озёрам": "fishing_in_lakes",
            "Рыба в озёрах": "fish_in_every_lake",
            "Средняя стоимость рыбалки": "avg_fishing_cost",
            "Самая дорогая рыба": "richest_fish",
            "Самое большое озеро": "biggest_lake",
            "Общее количество рыбы": "population",
        }

        top = ctk.CTkFrame(self)
        top.pack(fill="x", padx=10, pady=10)

        self.combo = ctk.CTkComboBox(
            top,
            values=list(self.reports.keys()),
            width=250
        )
        self.combo.pack(side="left", padx=10)

        self.combo.set("Все виды рыб")

        ctk.CTkButton(
            top,
            text="Сформировать",
            command=self.build_report
        ).pack(side="left")

        self.tree = None
        self.scrollbar = None

    def build_report(self):
        if self.tree is not None:
            self.tree.destroy()

        if self.scrollbar is not None:
            self.scrollbar.destroy()

        report_name = self.reports[self.combo.get()]

        headings = self.database.get_report_headings(report_name)
        rows = self.database.get_report(report_name)

        self.tree = ttk.Treeview(
            self,
            columns=headings,
            show="headings"
        )

        for heading in headings:
            self.tree.heading(heading, text=heading)
            self.tree.column(heading, anchor="center", width=150)

        for row in rows:
            self.tree.insert("", "end", values=row)

        self.scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.tree.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(10, 0),
            pady=(0, 10)
        )

        self.scrollbar.pack(
            side="right",
            fill="y",
            padx=(0, 10),
            pady=(0, 10)
        )