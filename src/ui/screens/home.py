from textual.reactive import reactive
from textual.app import ComposeResult

from ui.components.selectable_text import SelectableText
from ui.screens.navigatable_base import NavigatableBase


class HomeScreen(NavigatableBase):
    CSS = """
    Input {
        border: none;
        background: transparent;
        height: 1;
        padding: 0;
        margin: 0;
    }
    """

    search_text: str = reactive("")

    def on_selectable_text_entered(self, event: SelectableText.Entered) -> None:
        self.app.log(event)

    def compose(self) -> ComposeResult:
        yield SelectableText("Hello, world!", classes="focusable")
        yield SelectableText("Hello, world!", classes="focusable")
        yield SelectableText("Hello, world!", classes="focusable")
        yield SelectableText("Hello, world!", classes="focusable")
