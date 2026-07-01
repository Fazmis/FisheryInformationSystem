import os
import sqlite3
class DataBase:
    def __init__(self) -> None:
        # Поиск и подключение к базе
        self.db_path = os.path.abspath("database/data.sqlite")
        if os.path.exists(self.db_path):
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
        # Если база не найдена
        else:
            pass
