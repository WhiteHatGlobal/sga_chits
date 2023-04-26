# Copyright (c) 2023, White Hat Global and contributors
# For license information, please see license.txt


import frappe
from frappe import _


def execute(filters=None):
    if not filters:
        filters={}

    columns = get_columns(filters)
    data = get_data(filters)
    
    return columns, data

def get_data(filters):
    from_date=filters.get("from_date")
    to_date=filters.get("to_date")
    company=filters.get("company")
    lead=filters.get("lead") 
    data=[]
    cus_filters={"date":["between",(from_date, to_date)]}

    if(company):
        cus_filters["company"]=company
    if(lead):
        cus_filters["lead"]=lead
    
    data = frappe.db.get_all("Telecalling SGA",filters=cus_filters,
        fields=[
            "date","company","name","lead_name","time","about"])
    return data


def get_columns(filters):
	return [
        {
            "fieldname":"company",
            "label": "Company",
            "fieldtype": "Link",
            "options": "Company",
            "width": 200
        },
		{
            "fieldname":"date",
            "label": "Date",
            "fieldtype": "Date",
            "width": 160
        },
		{
            "fieldname":"name",
            "label": "Lead",
            "fieldtype": "Link",
            "options": "Lead",
            "width": 180
        },
		{
            "fieldname":"lead_name",
            "label": "Lead Name",
            "fieldtype": "Data",
            "width": 180
        },
		{
            "fieldname":"time",
            "label": "Time",
            "fieldtype": "Time",
            "width": 130
        },
        {
            "fieldname":"about",
            "label": "About",
            "fieldtype": "Small Text",
            "width": 200
        }
    ]
 
 
 
#  import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data

# def get_columns():
# 	columns = [
# 		{
# 			"fieldname": "date",
# 			"label": ("Date"),
# 			"fieldtype": "Date",
# 			"width": 100,
# 		},
# 		{
# 			"fieldname": "company",
# 			"label": ("Company"),
# 			"fieldtype": "Link",
# 			"options": "Company",
# 			"width": 120,
# 		},
# 		{
# 			"fieldname": "name",
# 			"label": ("Lead"),
# 			"fieldtype": "Link",
# 			"options": "Lead",
# 			"width": 120,
# 		},
# 		{
# 			"fieldname": "lead_name",
# 			"label": ("Lead Name"),
# 			"fieldtype": "Data",
# 			"width": 120,
# 		},
# 		{
# 			"fieldname": "time",
# 			"label": ("Time"),
# 			"fieldtype": "Time",
# 			"width": 120,
# 		},
# 		{
# 			"fieldname": "about",
# 			"label": ("About"),
# 			"fieldtype": "Data",
# 			"width": 200
# 		}
		
# 	]
# 	return columns

# def get_data(filters):
# 	return frappe.db.sql(
# 		"""
# 		SELECT
# 			`tabTelecalling SGA`.date,
# 			`tabTelecalling SGA`.company,
# 			`tabTelecalling SGA`.name,
# 			`tabTelecalling SGA`.lead_name,
# 			`tabTelecalling SGA`.time,
# 			`tabTelecalling SGA`.about
			
# 		FROM
# 			`tabTelecalling SGA`
# 		WHERE
# 			company = %(company)s AND `tabTelecalling SGA`.date BETWEEN %(from_date)s AND %(to_date)s {conditions}
# 		ORDER BY
# 			`tabTelecalling SGA`.creation asc """.format(
# 			conditions=get_conditions(filters)
# 		),
# 		filters,
# 		as_dict=1,
# 	)

# def get_conditions(filters):
# 	conditions = []
    
 
# 	if filters.get("lead"):
# 		conditions.append(" and `tabTelecalling SGA`.lead.name=%(lead)s")

# 	return " ".join(conditions) if conditions else ""
