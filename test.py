from Autodesk.Revit import DB
from rps import doc  # перед запуском надо закомментировать

views = DB.FilteredElementCollector(doc).OfClass(DB.View3D)