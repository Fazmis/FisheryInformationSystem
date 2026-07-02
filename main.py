from database import DataBase
from gui import App


def main() -> None:
    db = DataBase()
    app = App(db)
    app.mainloop()


if __name__ == '__main__':
    main()