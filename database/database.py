import os
import sqlite3
class DataBase:
    def __init__(self) -> None:
        # Поиск базы
        self.db_path = os.path.abspath("database/data.sqlite")
        if not os.path.exists(self.db_path):
            need_init = True # Если база не найдена
        else:
            need_init = False # Если база найдена

        # Подключение к базе
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

        # Инициализация базы, если не найдена
        if need_init:
            self.create_db()

    def create_db(self) -> None:
        with open("database/schema.sql", "r", encoding="utf-8") as file:
            self.cursor.executescript(file.read())
            self.connection.commit()

    def have_users(self) -> bool:
        self.cursor.execute("SELECT EXISTS(SELECT 1 FROM Пользователи LIMIT 1)")
        return bool(self.cursor.fetchone()[0])