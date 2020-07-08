from pathlib import Path

class Site:

    def __init__(self, source, dest, parsers=None):
        self.source = Path(source) # convert source to a Path() object
        self.dest = Path(dest) # repeat for dest
        self.parsers = parsers or []

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)

    def load_parser(self, extension):
        for parser in self.parsers:
