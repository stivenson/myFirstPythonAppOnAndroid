"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class MyFirstBriefcaseApp(toga.App):

    def __init__(
            self,
            formal_name=None,
            app_id=None,
            app_name=None,
            id=None,
            icon=None,
            author=None,
            version=None,
            home_page=None,
            description=None,
            startup=None,
            windows=None,
            on_exit=None,
            factory=None,
    ):
        super().__init__(
            formal_name,
            app_id,
            app_name,
            id,
            icon,
            author,
            version,
            home_page,
            description,
            startup,
            windows,
            on_exit,
            factory)
        self.name_input = toga.TextInput(style=Pack(flex=1))

    def startup(self):

        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            'Please, your name: ',
            style=Pack(padding=(0, 5))
        )

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            'Decir Hola!',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        self.main_window.info_dialog(
            'Hola, {}'.format(self.name_input.value),
            '¿Como estas?'
        )


def main():
    return MyFirstBriefcaseApp()
