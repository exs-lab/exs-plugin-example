from pathlib import Path


class Paths:
    root = Path(__file__).parent.parent
    project = Path(__file__).parent
    styles = project / 'styles'
