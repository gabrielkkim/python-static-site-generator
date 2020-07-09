import re

from yaml import load, FullLoader
from collections.abc import Mapping

def Content(Mapping):
    __delimiter = "^(?:-|+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)
