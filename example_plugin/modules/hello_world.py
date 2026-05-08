from ignis.widgets import Window, Label
from libexs import register


@register.event
class HelloWorld(Window):
    def __init__(self):
        self.seconds = 0
        self.label = Label(
            label=f"Hello World {self.seconds}",
            css_classes=["example-plugin-label-red"],
        )
        super().__init__("exs.plugin.hello", child=self.label)

    @register.events.poll(1_000)
    def __update_label(self):
        self.seconds += 1
        self.label.set_label(f"Hello World {self.seconds}")
        if self.seconds % 2 == 0:
            self.label.remove_css_class("example-plugin-label-green")
            self.label.add_css_class("example-plugin-label-red")
        else:
            self.label.remove_css_class("example-plugin-label-red")
            self.label.add_css_class("example-plugin-label-green")
