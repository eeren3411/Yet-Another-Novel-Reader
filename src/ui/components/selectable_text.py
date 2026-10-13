from textual.app import RenderResult
from textual.message import Message
from textual.widgets import Static


class SelectableText(Static, can_focus=True):
    class Entered(Message):
        def __init__(self, widget: "SelectableText") -> None:
            self.widget = widget
            super().__init__()

    BINDINGS = [("enter", "enter")]

    def action_enter(self) -> None:
        self.post_message(self.Entered(self))

    @property
    def prefix(self) -> str:
        return "> " if self.has_focus else "  "

    def render(self) -> RenderResult:
        return f"{self.prefix}{self.content}"
