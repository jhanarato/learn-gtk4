import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gtk


class ToolbarWindow(Adw.ApplicationWindow):
    def __init__(self, **kargs):
        super().__init__(**kargs, title="Toolbar View")
        self.props.width_request = 500
        self.props.height_request = 500

        self.header_bar = Adw.HeaderBar()
        self.set_content(self.header_bar)


def on_activate(app):
    win = ToolbarWindow(application=app)
    win.present()


app = Gtk.Application(application_id="org.bswa.jhanarato.ToolbarWindow")
app.connect("activate", on_activate)

app.run(None)