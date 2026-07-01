from database import DataBase
from gui import App, AuthorizationWindow, RegistrationWindow


def main():
    db = DataBase()

    if db.have_users():
        auth = AuthorizationWindow()
    else:
        auth = RegistrationWindow()
    auth.mainloop()

    if auth.user is None:
        return

    app = App(db, auth.user)
    app.mainloop()

if __name__ == '__main__':
    main()