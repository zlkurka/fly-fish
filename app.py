from textual.app import App
from textual.widgets import Label, Static

class HelloTextualApp(App):
    def compose(self):
        self.static = Static("Welcome to [red]FLY FISHING SIM[\red]!")
        yield self.static

        self.label = Label("Click here to go fishing.")
        yield self.label

if __name__ == "__main__":
    app = HelloTextualApp()
    app.run()