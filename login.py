from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):
    def login(self):
        username = self.ids.username.text
        password = self.ids.password.text

        if username == "admin" and password == "1234":
            self.manager.current = "dashboard"
        else:
            print("Wrong login")
