import sys

from rich import print as rprint

import gendocs
from scratch import Project

proj = Project(sys.argv[1])
doc = gendocs.from_project(proj)
rprint(doc)
