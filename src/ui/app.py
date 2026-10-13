from textual.app import App, ComposeResult
from textual.widgets import Static

from ui.screens.home import HomeScreen


class AppBase(App):
    SCREENS = {
        "home": HomeScreen,
    }

    CSS = """
    Screen {
        background: $background;
        padding: 0 2;
    }
    """

    def on_mount(self) -> None:
        self.push_screen("home")
