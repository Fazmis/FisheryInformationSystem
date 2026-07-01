from database import DataBase
from gui import App, AuthorizationWindow


def main():
    db = DataBase()
    app = AuthorizationWindow()
    app.mainloop()

if __name__ == '__main__':
    main()