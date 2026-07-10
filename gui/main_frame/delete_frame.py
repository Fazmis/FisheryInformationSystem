import customtkinter as ctk

class DeleteFrame(ctk.CTkToplevel):
    def __init__(self, master, selected):
        super().__init__(master)
        self.master = master
        self.selected = selected
        self.title("Удаление")
        self.label = ctk.CTkLabel(
            self,
            text=f"Вы уверены, что хотите удалить запись с ID {self.selected[0]}?",
            font=("Comic Sans MS", 14)
        )
        self.label.pack(padx=10, pady=10)
        self.button = ctk.CTkButton(self, text="Подтвердить", command=self.delete_from_base)
        self.button.pack(side="left")
        self.button = ctk.CTkButton(self, text="Отмена", command=self.destroy)
        self.button.pack(side="right")

    def delete_from_base(self):
        self.master.app.database.delete_row_from_table(self.master.table_name, self.selected)
        self.destroy()
        self.master.refresh()
