#!/usr/bin/env python3

from pathlib import Path


class Site:
    source = None
    dest = None

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        # Find root directory.
        directory = self.dest / path.relative_to(self.source)
        # Replace directory if it exists.
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        # Make the destination directory.
        self.dest.mkdir(parents=True, exist_ok=True)
        # Recreate all paths.
        for path in self.source.rglob(pattern="*"):
            if path.is_dir():
                self.create_dir(path=path)
