#!/usr/bin/env python3

import typer
import ssg.parsers
from ssg.site import Site


def main(source="content", dest="dist"):
    config: dict = {
        "source": source,
        "dest": dest,
        "parsers": [ssg.parsers.ResourceParser(), ],
    }
    # Unpack the dictionary values
    Site(**config).build()


typer.run(main)
