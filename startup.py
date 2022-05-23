# -*- coding: UTF-8 -*-

# auto update at startup
import os
os.system('cmd /c "pyrevit extensions update pyBiltNA"'))

# grab today's date
from pyrevit import script
from datetime import datetime
output = script.get_output()

if datetime.today().strftime('%A') == 'Thursday':
    output.print_md("# Welcome to BILT NA 2022 ")
    output.self_destruct(10)
elif datetime.today().strftime("%m/%d") == "04/01":
    # well, if it is april's fool day, then we'll do something special
    output.center()
    output.resize(width=498, height=350)
    output.print_image("C:\pyRevit\pyBiltNA.extension\\0104.gif")
    output.self_destruct(100)
else:
    pass