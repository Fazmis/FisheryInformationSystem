CREATE TABLE "Виды_Рыб" (
	"ID"	INTEGER NOT NULL,
	"Вид"	TEXT NOT NULL UNIQUE,
	"Стоимость_за_килограмм"	REAL NOT NULL CHECK("Стоимость_за_килограмм" > 0),
	PRIMARY KEY("ID" AUTOINCREMENT)
);
CREATE TABLE "Обитание_Видов" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"ID_Вида_Рыбы"	INTEGER NOT NULL,
	"ID_Озера"	INTEGER NOT NULL,
	"Примерное_количество_особей"	INTEGER,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("ID_Вида_Рыбы") REFERENCES "Виды_Рыб"("ID"),
	FOREIGN KEY("ID_Озера") REFERENCES "Озера"("ID")
);
CREATE TABLE "Озера" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"Наименование"	TEXT,
	"Расположение"	TEXT NOT NULL UNIQUE,
	"Площадь"	REAL NOT NULL,
	"Средняя_температура_воды"	REAL,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
CREATE TABLE "Рыбалка_на_озерах" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"ID_Озера"	INTEGER NOT NULL,
	"Дата_и_время"	TEXT NOT NULL,
	"Стоимость_рыбалки"	REAL NOT NULL,
	"Максимальное_количество_рыбаков"	INTEGER NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("ID_Озера") REFERENCES "Озера"("ID")
);
CREATE TABLE "Пользователи" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"Логин"	TEXT NOT NULL UNIQUE,
	"Пароль"	TEXT NOT NULL,
	"Права_администратора"	INTEGER NOT NULL DEFAULT 0 CHECK(0 <= Права_администратора <= 1),
	PRIMARY KEY("ID" AUTOINCREMENT)
);