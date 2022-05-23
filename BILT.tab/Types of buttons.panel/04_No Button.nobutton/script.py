

from pyrevit import script, revit, DB, forms 

output = script.get_output()
doc = revit.doc

# Here we use the Built In Parameter method to choose the parameter (yes/no tickbox) 
# of 'Enable Analytical Model' across all Elements inside of the Revit Document
param = DB.BuiltInParameter.STRUCTURAL_ANALYTICAL_MODEL
# Once we have our BuiltInParameter, we need to get it's Element Id and convert it 
# to a Parameter Value Provider in order to use it inside of our filter
provider = DB.ParameterValueProvider( DB.ElementId( param ) )

# We then set up an empty instance of a Filter Numeric Equals to test against a set 
# value (In this case - whether or not the Element has the box ticked for 'Enable 
# Analytical Model'
evaluator = DB.FilterNumericEquals()
# After we have the empty instance set up as our evaluator, we run a Filter Integer 
# Rule that checks the chosen parameter (Enable Anyalytical Model), runs against the 
# evaluator (Does this Number equal) and our value (1 which correlates to the tick 
# inside of our yes/no tickbox)
rule = DB.FilterIntegerRule( provider, evaluator, 1 )
# After we have generated our Rule, we can generate a filter based off this rule
filter = DB.ElementParameterFilter( rule )

# Now we have a valid rule to run against our Filtered Element Collector. So in this 
# case we pull everything inside the document - but only if it passes our filter (i.e 
# has the box ticked on for 'Enable Analytical Model') then make sure we return the 
# elements themselves. 
analyticalCollector = DB.FilteredElementCollector( doc ).WherePasses( filter ).ToElements()

processed_list = 0

with revit.Transaction('Set Analytical Model 2'):
    for i in analyticalCollector:
        object_param_AnalyticalModel = i.get_Parameter(DB.BuiltInParameter.STRUCTURAL_ANALYTICAL_MODEL)
        new_value = False
        # try when structure model is not activated (usually for architectural walls)
        try: 
            object_param_AnalyticalModel.Set(new_value)
            # increment list of elements processed
            processed_list += 1
        except:
            pass 

#takes care of remaining windows
output.close_others(all_open_outputs=True)

# feedback output message
msg = str(processed_list) + ' processed elements'
forms.alert(msg, title='Turn of analytical model property', ok=True)