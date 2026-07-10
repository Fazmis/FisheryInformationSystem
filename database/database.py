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
            if True:
                self._init_data_db()

    def _create_db(self) -> None:
        with open("database/schema.sql", "r", encoding="utf-8") as file:
            self.cursor.executescript(file.read())
            self.connection.commit()

    def _init_data_db(self) -> None:
        with open("database/init_exemple_data.sql", "r", encoding="utf-8") as file:
            self.cursor.executescript(file.read())
            self.connection.commit()

    def have_users(self) -> bool:
        self.cursor.execute("SELECT EXISTS(SELECT 1 FROM Пользователи LIMIT 1)")
        return bool(self.cursor.fetchone()[0])

    def get_headings(self, table_name) -> list:
        self.cursor.execute(f"PRAGMA table_info({table_name})")
        return [row[1] for row in self.cursor.fetchall()]

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
        sqluser = self.cursor.fetchone()
        if sqluser is None:
            return None
        user = {"id": int(sqluser[0]), "login": str(sqluser[1]), "admin_rights": bool(sqluser[2])}
        return user


    def sign_up(self, login: str, password: str, grant_admin_rights=False):
        self.cursor.execute(
            """
            INSERT INTO Пользователи
            (Логин, Пароль, Права_администратора)
            VALUES (?, ?, ?)
            """,
            (login, password, grant_admin_rights)
        )
        self.connection.commit()
        return self.login(login, password)

    def get_row_from_table(self, table_name: str, row_id):
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE ID = {row_id}")
        row = self.cursor.fetchone()
        return row
    def insert_row_in_table(self, table_name: str, data_to_insert: list):
        headings = self.get_headings(table_name)
        if len(headings) != len(data_to_insert):
            return
        self.cursor.execute(f"INSERT INTO {table_name} {tuple(headings)} VALUES {tuple(data_to_insert)}")
        self.connection.commit()

    def delete_row_from_table(self, table_name, data_to_delete: list):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE ID = {data_to_delete[0]}")
        self.connection.commit()

    def get_report(self, report_name):
        reports = {
            "all_fish": "SELECT * FROM Виды_Рыб ORDER BY Вид;",
            "all_lakes": "SELECT * FROM Озера;",
            "fishing_in_lakes": """SELECT Озера.Наименование,
                                Рыбалка_на_озерах.Дата_и_время,
                                Рыбалка_на_озерах.Стоимость_рыбалки
                                FROM Рыбалка_на_озерах JOIN Озера
                                ON Озера.ID = Рыбалка_на_озерах.ID_Озера;""",
            "fish_in_every_lake": """SELECT Озера.Наименование, Виды_Рыб.Вид,
                                Обитание_Видов.Примерное_количество_особей
                                FROM Обитание_Видов JOIN Озера ON
                                Озера.ID = Обитание_Видов.ID_Озера
                                JOIN Виды_Рыб ON 
                                Виды_Рыб.ID = Обитание_Видов.ID_Вида_Рыбы;""",
            "avg_fishing_cost": "SELECT AVG(Стоимость_рыбалки) FROM Рыбалка_на_озерах;",
            "richest_fish": "SELECT Вид, Стоимость_за_килограмм FROM Виды_Рыб ORDER BY Стоимость_за_килограмм DESC LIMIT 1;",
            "biggest_lake": "SELECT * FROM Озера ORDER BY Площадь DESC LIMIT 1;",
            "population": "SELECT SUM(Примерное_количество_особей) FROM Обитание_Видов;",
        }
        self.cursor.execute(reports[report_name])
        return self.cursor.fetchall()

    def get_report_headings(self, report_name):
        headings = {
            "all_fish": [
                "ID",
                "Вид",
                "Стоимость за кг"
            ],
            "all_lakes": [
                "ID",
                "Наименование",
                "Расположение",
                "Площадь",
                "Средняя температура"
            ],
            "fishing_in_lakes": [
                "Озеро",
                "Дата",
                "Стоимость"
            ],
            "fish_in_every_lake": [
                "Озеро",
                "Вид",
                "Количество"
            ],
            "avg_fishing_cost": [
                "Средняя стоимость"
            ],
            "richest_fish": [
                "Вид",
                "Стоимость"
            ],
            "biggest_lake": [
                "ID",
                "Наименование",
                "Расположение",
                "Площадь",
                "Средняя температура"
            ],
            "population": [
                "Количество особей"
            ]
        }
        return headings[report_name]