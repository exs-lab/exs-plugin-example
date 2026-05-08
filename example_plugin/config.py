import os
from ignis.options_manager import OptionsGroup, OptionsManager

from example_plugin.path import Paths


# WARNING: dont write ~/.config/exs-shell/config.jsonc !!!
USER_OPTIONS_FILE = f"{Paths.root}/config.jsonc"
OLD_USER_OPTIONS_FILE = f"{Paths.root}/old_config.jsonc"


def _migrate_old_options_file() -> None:
    with open(OLD_USER_OPTIONS_FILE) as f:
        data = f.read()

    with open(USER_OPTIONS_FILE, "w") as f:
        f.write(data)


class UserOptions(OptionsManager):
    def __init__(self):
        if not os.path.exists(USER_OPTIONS_FILE) and os.path.exists(
            OLD_USER_OPTIONS_FILE
        ):
            _migrate_old_options_file()

        try:
            super().__init__(file=USER_OPTIONS_FILE)
        except FileNotFoundError:
            pass

    class MainConfig(OptionsGroup):
        test: bool = False

    _main_config = MainConfig()

    @property
    def main_config(self) -> MainConfig:
        return self._main_config


options = UserOptions()
