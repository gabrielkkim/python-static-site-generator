import shutil
import sys

from typing import List
from pathlib import Path

from docutils.core import publish_parts
from markdown import markdown
from ssg.content import Content


class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path, "r") as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, "w") as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest / path.relative_to(source))

class MarkdownParser():
    extensions = [".md", ".markdown"]

    def parse(self, path, source, dest):
        content = Content.load(self.read(path))

class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path, source, dest):
        self.copy(path, source, dest)
