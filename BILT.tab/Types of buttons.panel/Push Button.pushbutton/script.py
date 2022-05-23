from pyrevit import revit, DB, script

output = script.get_output()
output.close_others()
output.center()

output.print_image(r'meme.jpg')

output.self_destruct(15)