import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk


@Gtk.Template(filename="templates/nested_button.ui")
class NestedButton(Gtk.Button):
    __gtype_name__ = "NestedButton"


@Gtk.Template(filename="templates/nesting_window.ui")
class NestingWindow(Adw.ApplicationWindow):
    __gtype_name__ = "NestingWindow"

    a_nested_button = Gtk.Template.Child("a-nested-button")

    @Gtk.Template.Callback()
    def button_clicked(self, button):
        self.close()


def on_activate(app):
    win = NestingWindow(application=app)
    win.present()


app = Adw.Application(application_id='org.bswa.jhanarato.FormWindow')
app.connect('activate', on_activate)

app.run(None)
