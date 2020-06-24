from pathlib import Path # step 1

class Site: # step 2, create a class object
    """docstring for site."""

    def __init__(self, source, dest): # this is the Site class constructor
        self.source = Path(source) # convert source to a Path() object
        self.dest = Path(dest) # repeat for dest

    def create_dir(self, path): # create a method called create_dir()
        directory = self.dest / path.relative_to(self.source)
        # self.dest is first / relative_to() is second
        """variable directory needs to contain full path
           to the destination folder."""

        directory.mkdir(parents=True, exist_ok=True) # make a directory
        """call mkdir() method on directory"""

    def build(self): # make the destination directory
        self.dest.mkdir(parents=True, exist_ok=True)

        for path in self.source.rglob("*"): # recreate all paths
            """call the current iteration path """
            if path.is_dir(): # test if current path is a directory
                self.create_dir(path) # if it's a directory call create_dir()
