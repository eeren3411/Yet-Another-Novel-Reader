from textual.screen import Screen


class NavigatableBase(Screen):
    BINDINGS = [
        ("up", "move_up"),
        ("down", "move_down"),
    ]

    def on_mount(self) -> None:
        self.query_one(".focusable").focus()

    def action_move_up(self) -> None:
        self.focus_previous(".focusable")

    def action_move_down(self) -> None:
        self.focus_next(".focusable")
