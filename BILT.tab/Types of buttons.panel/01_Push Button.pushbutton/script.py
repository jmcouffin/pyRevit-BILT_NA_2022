from pyrevit import script

# grab existing windows
output = script.get_output()
# close them
output.close_others()
# center the new window
output.center()

# print a picture in a window
output.print_md('# No Revit was hurt in the process!')
output.print_image("C:\pyRevit\pyBiltNA.extension\BILT.tab\Types of buttons.panel\Push Button.pushbutton\meme.jpg")

# automatically close the window
output.self_destruct(15)