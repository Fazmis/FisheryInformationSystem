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
            self._create_db()

    def _create_db(self) -> None:
        with open("database/schema.sql", "r", encoding="utf-8") as file:
            self.cursor.executescript(file.read())
            self.connection.commit()

    def have_users(self) -> bool:
        self.cursor.execute("SELECT EXISTS(SELECT 1 FROM Пользователи LIMIT 1)")
        return bool(self.cursor.fetchone()[0])

    def login(self, login: str, password: str):
        self.cursor.execute(
            """
            SELECT ID, Логин, Права_администратора
            FROM Пользователи
            WHERE Логин = ? AND Пароль = ?
            LIMIT 1
            """,
            (login, password)
        )
        return self.cursor.fetchone()


    def sign_up(self, login: str, password: str, is_admin=False):
        self.cursor.execute(
            """
            INSERT INTO Пользователи
            (Логин, Пароль, Права_администратора)
            VALUES (?, ?, ?)
            """,
            (login, password, is_admin)
        )
        self.connection.commit()

        return self.login(login, password)