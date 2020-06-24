from pathlib import Path # step 1

class Site: # step 2, create a class object

    def __init__(self, source, dest): # this is the Site class constructor
        self.source = Path(source) # convert source to a Path() object
        self.dest = Path(dest) # repeat for dest

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
