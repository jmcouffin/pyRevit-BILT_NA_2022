# -*- coding: UTF-8 -*-

import datetime
from pyrevit import script
from pyrevit import revit

output = script.get_output()
output.close_others(True)
output.center()
output.set_title('Models Checker')


doc = revit.doc

# Series of queries


def name(doc):
    """returns file name - everything in path from "\\" or "/" to the end"""
    name = doc.PathName
    return name


def project_number(doc):
    project_number = doc.ProjectInformation.Number
    return project_number


def project_name(doc):
    project_name = doc.ProjectInformation.Name
    return project_name


def project_client_name(doc):
    project_client_name = doc.ProjectInformation.ClientName
    return project_client_name


def project_organization_name(doc):
    project_organization_name = doc.ProjectInformation.OrganizationName
    return project_organization_name


def project_organization_description(doc):
    project_organization_description = doc.ProjectInformation.OrganizationDescription
    return project_organization_description


def project_building_name(doc):
    project_building_name = doc.ProjectInformation.BuildingName
    return project_building_name


def project_author(doc):
    project_author = doc.ProjectInformation.Author
    return project_author


def project_issue_date(doc):
    project_issue_date = doc.ProjectInformation.IssueDate
    return project_issue_date


def project_status(doc):
    project_status = doc.ProjectInformation.Status
    return project_status


def project_address(doc):
    project_address = doc.ProjectInformation.Address
    return project_address


#  date and time
timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Grab data from config
my_config = script.get_config()
tests = getattr(my_config, "BILT_tests")

# set minimal value to empty string
pname, pnumber, p_client_name, p_organization_name, p_organization_description, p_building_name, p_author, p_issue_date, p_status, p_address = "", "", "", "", "", "", "", "", "", ""

# check if queries requested in config file
if tests == [] or tests == None:
    pname = project_name(doc)
    pnumber = project_number(doc)
    p_client_name = project_client_name(doc)
    p_organization_name = project_organization_name(doc)
    p_organization_description = project_organization_description(doc)
    p_building_name = project_building_name(doc)
    p_author = project_author(doc)
    p_issue_date = project_issue_date(doc)
    p_status = project_status(doc)
    p_address = project_address(doc)
if "Project Name" in tests:
    pname = project_name(doc)
if "Project Number" in tests:
    pnumber = project_number(doc)
if "Project Client Name" in tests:
    p_client_name = project_client_name(doc)
if "Project Organization Name" in tests:
    p_organization_name = project_organization_name(doc)
if "Project Organization Description" in tests:
    p_organization_description = project_organization_description(doc)
if "Project Building Name" in tests:
    p_building_name = project_building_name(doc)
if "Project Author" in tests:
    p_author = project_author(doc)
if "Project Issue Date" in tests:
    p_issue_date = project_issue_date(doc)
if "Project Status" in tests:
    p_status = project_status(doc)
if "Project Address" in tests:
    p_address = project_address(doc)

# print the whole thing
output.print_md(pname + "\n\n" + pnumber + "\n\n" + p_client_name + "\n\n" + p_organization_name + "\n\n" + p_organization_description +
                "\n\n" + p_building_name + "\n\n" + p_author + "\n\n" + p_issue_date + "\n\n" + p_status + "\n\n" + p_address)
