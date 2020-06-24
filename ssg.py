import typer # Import typer set up the command line interface CLI

from ssg.site import Site # ./ssg/site

def main(source="content", dest="dist"): # Config options
    # dictionary called config
    config = {"source": source, "dest": dest}
    # create an instance called Site class
    Site(**config).build() # attributes are stored in config dictionary

typer.run(main)
