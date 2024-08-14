import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


@Gtk.Template(filename="a_template.ui")
class ATemplate(Gtk.Box):
    __gtype_name__ = "example1"

    hello_button = Gtk.Template.Child()

    @Gtk.Template.Callback()
    def hello_button_clicked(self, *args):
        print("Oh my god that's the funky shit")


class WindowWithTemplate(Gtk.ApplicationWindow):
    def __init__(self, **kargs):
        super().__init__(**kargs, title='With a Template')
        a_template = ATemplate()
        a_template.props.height_request = 300
        a_template.props.width_request = 300
        self.set_child(a_template)


def on_activate(app):
    win = WindowWithTemplate(application=app)
    win.present()


app = Gtk.Application(application_id='org.bswa.jhanarato.TemplateExample')
app.connect('activate', on_activate)

app.run(None)
