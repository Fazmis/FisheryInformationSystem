from database import DataBase
from gui import App, AuthorizationWindow, RegistrationWindow


def main() -> None:
    db = DataBase()

    if db.have_users():
        auth = AuthorizationWindow(db)
    else:
        auth = RegistrationWindow(db, is_admin=True)
    auth.mainloop()

    if not auth.user:
        return

    app = App(db, auth.user)
    app.mainloop()

if __name__ == '__main__':
    main()