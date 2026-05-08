from libexs.utils import plugin

from example_plugin.modules.hello_world import HelloWorld
from example_plugin.path import Paths
from example_plugin.services.my_service import MyService
from example_plugin.settings.hello import HelloCategory


def init():
    plugin.apply_service(MyService(), "my_service")
    plugin.apply_css(Paths.styles / "main.scss")
    HelloWorld()
    plugin.apply_settings_category(HelloCategory())
