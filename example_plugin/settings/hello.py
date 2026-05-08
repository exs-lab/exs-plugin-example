from libexs.enums.icons import Icons
from libexs.settings.base import BaseCategory
from libexs.settings.widgets import CategoryLabel, SettingsRow, SwitchRow

from example_plugin.config import options


class HelloCategory(BaseCategory):
    def __init__(self):
        super().__init__(
            [
                CategoryLabel("Hello World", Icons.ui.WIDGET),
                SettingsRow(
                    Icons.ui.TEST,
                    "Hello Test",
                    "Hello World!",
                    [
                        SwitchRow(
                            options.main_config.test,
                            lambda _: options.main_config.set_test(_),
                        )
                    ],
                ),
            ],
        )
