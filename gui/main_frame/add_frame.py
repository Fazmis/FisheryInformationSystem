import customtkinter as ctk

# TODO Авто-инкремент id
# TODO Выбор для внешних ключей
class AddFrame(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Добавить")
        self.entries = []
        for item in master.heading_names:
            self.entries.append(ctk.CTkEntry(self, placeholder_text=item))
            self.entries[-1].pack(padx=20, pady=5)


        self.button = ctk.CTkButton(self, text="Добавить", command=self.add_to_base)
        self.button.pack(padx=0, pady=10)

    def add_to_base(self) -> None:
        data_to_insert = list([entry.get() for entry in self.entries])
        self.master.app.database.insert_row_in_table(self.master.table_name, data_to_insert)
        self.destroy()
        self.master.refresh()