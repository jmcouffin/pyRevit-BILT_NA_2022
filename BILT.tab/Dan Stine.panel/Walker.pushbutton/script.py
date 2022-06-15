from socket import fromshare
from pyrevit import revit, DB, script, forms

# subcategory walker

# list subcategorys of spaces
spaces = DB.FilteredElementCollector(revit.doc).OfCategory(DB.BuiltInCategory.OST_MEPSpaces).WhereElementIsNotElementType().ToElements()
subcats = []

for space in spaces:
    subcats.append(space.get_Parameter(DB.BuiltInParameter.SPACE_SUB_CATEGORY).AsString())

print (subcats)


# isolate that first subcategory
# on + key stroke get to the next one
# on escape, exit the script