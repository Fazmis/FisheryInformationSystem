from database import DataBase
from gui import App


def main():
    db = DataBase()
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()