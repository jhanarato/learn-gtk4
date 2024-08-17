import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


@Gtk.Template(filename="form_window.ui")
class FormWindow(Gtk.ApplicationWindow):
    __gtype_name__ = "form-window"


def on_activate(app):
    win = FormWindow(application=app)
    win.present()


app = Gtk.Application(application_id='org.bswa.jhanarato.FormWindow')
app.connect('activate', on_activate)

app.run(None)
