#!/usr/bin/env python3

import typer
from ssg.site import Site


def main(source="content", dest="dist"):
    config: dict = {"source": source, "dest": dest}
    # Unpack the dictionary values
    Site(**config).build()


typer.run(main)
