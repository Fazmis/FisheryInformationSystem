import customtkinter as ctk

# TODO Выбор для внешних ключей
class EditFrame(ctk.CTkToplevel):
    def __init__(self, master, selected):
        super().__init__(master)
        self.master = master
        self.selected = selected
        self.title("Изменить")
        self.data = self.get_data_from_base()
        self.entries = []
        for i, item in enumerate(master.heading_names):
            self.label = ctk.CTkLabel(self, text=item, font=("Comic Sans MS", 14))
            self.label.grid(row=i, column=0)
            self.entries.append(ctk.CTkEntry(self, placeholder_text=self.data[i]))
            self.entries[-1].grid(row=i, column=1)


        self.button = ctk.CTkButton(self, text="Изменить", command=self.edit_in_base)
        self.button.grid(row=len(self.data), column=1)

    def get_data_from_base(self) -> list:
        data = self.master.app.database.get_row_from_table(self.master.table_name, self.selected[0])
        print(data)
        return data

    def edit_in_base(self) -> None:
        new_row_in_base = []
        for i, entry in enumerate(self.entries):
            user_input = entry.get()
            if user_input:
                new_row_in_base.append(user_input)
            else:
                new_row_in_base.append(self.data[i])

        self.master.app.database.delete_row_from_table(self.master.table_name, self.data)
        self.master.app.database.insert_row_in_table(self.master.table_name, new_row_in_base)
        self.destroy()
        self.master.refresh()