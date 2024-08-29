import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk


@Gtk.Template(filename="templates/adwaita_toolbar_view.ui")
class FormWindow(Adw.ApplicationWindow):
    __gtype_name__ = "form-window"


def on_activate(app):
    win = FormWindow(application=app)
    win.present()


app = Adw.Application(application_id='org.bswa.jhanarato.AdwaitaToolbarViewWindow')
app.connect('activate', on_activate)

app.run(None)
