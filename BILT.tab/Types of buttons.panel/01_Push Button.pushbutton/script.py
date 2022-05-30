from pyrevit import script
from pyrevit import revit

# grab existing windows
output = script.get_output()
# close them
output.close_others()
# center the new window
output.center()

# print a picture in a window
output.print_md('# No Revit was hurt in the process!')
output.print_image("C:\pyRevit\pyBiltNA.extension\BILT.tab\Types of buttons.panel\\01_Push Button.pushbutton\meme.jpg")

# let's do something with revit at the Application Level
output.print_md('You are using the following revit build {}'.format(revit.HOST_APP.build))

# automatically close the window
output.self_destruct(15)