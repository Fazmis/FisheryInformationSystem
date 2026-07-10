import customtkinter as ctk
from tkinter import ttk
from .add_frame import AddFrame
from .edit_frame import EditFrame
from .delete_frame import DeleteFrame


class SQLFrame(ctk.CTkFrame):
    def __init__(self, master, app, table_name):
        super().__init__(master)
        self.app = app
        self.database = self.app.database
        self.table_name = table_name
        self.headings_list = self.get_headings()
        self.heading_names = []
        for heading in self.headings_list:
            self.heading_names.append(heading.capitalize().replace("_", " "))
        # ---------- Верхняя панель ----------
        top_frame = ctk.CTkFrame(self)
        top_frame.pack(fill="x", padx=10, pady=10)

        self.add_button = ctk.CTkButton(
            top_frame,
            text="Добавить",
            command=self.add
        )
        self.add_button.pack(side="left", padx=5)

        self.edit_button = ctk.CTkButton(
            top_frame,
            text="Изменить",
            command=self.edit
        )
        self.edit_button.pack(side="left", padx=5)

        if self.app.user["admin_rights"]:
            self.delete_button = ctk.CTkButton(
                top_frame,
                text="Удалить",
                command=self.delete
            )
            self.delete_button.pack(side="left", padx=5)

        # ---------- Таблица ----------
        self.tree = ttk.Treeview(
            self,
            columns=tuple(self.headings_list),
            show="headings"
        )

        for i, heading in enumerate(self.headings_list):
            self.tree.heading(heading, text=self.heading_names[i])


        for heading in self.headings_list:
            self.tree.column(heading, anchor="center")

        scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=(0, 10))
        scrollbar.pack(side="right", fill="y", pady=(0, 10), padx=(0, 10))

        self.load_data()

    def get_headings(self):
        return self.database.get_headings(self.table_name)

    def load_data(self):
        """Загрузка данных из БД."""

        for item in self.tree.get_children():
            self.tree.delete(item)

        items_to_select = str(self.headings_list)[1:-1].replace("'", "")
        self.database.cursor.execute(f"""
            SELECT {items_to_select}
            FROM {self.table_name}
            ORDER BY ID
        """)

        for row in self.database.cursor.fetchall():
            self.tree.insert("", "end", values=row)

    def get_selected(self):
        item = self.tree.focus()

        if not item:
            return None

        return self.tree.item(item)["values"]

    def add(self):
        AddFrame(self)

    def edit(self):
        selected = self.get_selected()
        if selected is None:
            return
        EditFrame(self, selected)

    def delete(self):
        selected = self.get_selected()
        if selected is None:
            return
        DeleteFrame(self, selected)

    def refresh(self):
        self.master.master.show_page(self.table_name)