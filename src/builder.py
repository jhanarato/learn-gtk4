import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

UI_XML = """
<?xml version='1.0' encoding='UTF-8'?>
<interface>
  <requires lib="gtk" version="4.6"/>
  <object class="GtkApplicationWindow" id="main_window">
    <property name="default-height">200</property>
    <property name="default-width">400</property>
    <property name="title">Builder Example</property>
    <child>
      <object class="GtkBox">
        <child>
          <object class="GtkBox">
            <property name="margin-bottom">5</property>
            <property name="margin-end">5</property>
            <property name="margin-start">5</property>
            <property name="margin-top">5</property>
            <property name="orientation">vertical</property>
            <child>
              <object class="GtkButton" id="button1">
                <property name="halign">start</property>
                <property name="hexpand">True</property>
                <property name="label">Test button</property>
              </object>
            </child>
          </object>
        </child>
      </object>
    </child>
  </object>
</interface>
"""


class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, application):
        builder = Gtk.Builder()
        builder.add_from_string(UI_XML)

        button = builder.get_object("button1")
        button.connect("clicked", self.hello)

        self.win = builder.get_object("main_window")
        self.win.set_application(self)  # Application will close once it no longer has active windows attached to it
        self.win.present()

    def hello(self, button):
        print("Hello")


app = MyApp(application_id="org.bswa.jhanarato.BuilderExample_01")
app.run(None)
