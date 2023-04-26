# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


import frappe
from frappe import _


def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data


def get_columns():
	columns = [
		{
			"label": _("Lead"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "Lead",
			"width": 150,
		},
  		{
			"label": _("Created On"),
			"fieldname": "date",
			"fieldtype": "Date",
   			"width": 150,
		},
		{
			"label": _("Sales Completed Date"),
			"fieldname": "sales_completed_date",
			"fieldtype": "Date",
			"width": 150,
		},
		{"label": _("Lead Name"), "fieldname": "lead_name", "fieldtype": "Data", "width": 120},
		{"fieldname": "workflow_state", "label": _("Status"), "fieldtype": "Data", "width": 100},
		{"fieldname": "lead_status", "label": _("Lead Status"), "fieldtype": "Data", "width": 100},
		{
			"fieldname": "lead_owner",
			"label": _("Lead Owner"),
			"fieldtype": "Link",
			"options": "User",
			"width": 100,
		},
		{
			"label": _("Territory"),
			"fieldname": "territory",
			"fieldtype": "Link",
			"options": "Territory",
			"width": 100,
		},
		{"label": _("Source"), "fieldname": "source", "fieldtype": "Data", "width": 120},
		{"label": _("Team User Code"), "fieldname": "team_user_code", "fieldtype": "Data", "width": 120},
		{"label": _("Introducer"), "fieldname": "introducer", "fieldtype": "Data", "width": 120},
		{"label": _("Advertisement"), "fieldname": "advertisement", "fieldtype": "Data", "width": 120},
		{"label": _("Email"), "fieldname": "email_id", "fieldtype": "Data", "width": 120},
		{"label": _("Mobile"), "fieldname": "mobile_no", "fieldtype": "Data", "width": 120},
		{"label": _("Phone"), "fieldname": "phone", "fieldtype": "Data", "width": 120},
		{
			"label": _("Owner"),
			"fieldname": "owner",
			"fieldtype": "Link",
			"options": "user",
			"width": 120,
		},
		{
			"label": _("Company"),
			"fieldname": "company",
			"fieldtype": "Link",
			"options": "Company",
			"width": 120,
		},
		{"fieldname": "address", "label": _("Address"), "fieldtype": "Data", "width": 130},
		{"fieldname": "state", "label": _("State"), "fieldtype": "Data", "width": 100},
		{"fieldname": "pincode", "label": _("Postal Code"), "fieldtype": "Data", "width": 90},
		{
			"fieldname": "country",
			"label": _("Country"),
			"fieldtype": "Link",
			"options": "Country",
			"width": 100,
		},
	]
	return columns


def get_data(filters):
	return frappe.db.sql(
		"""
		SELECT
			`tabLead`.name,
			`tabLead`.date,
			`tabLead`.sales_completed_date,
			`tabLead`.lead_name,
			`tabLead`.workflow_state,
			`tabLead`.lead_status,
			`tabLead`.lead_owner,
			`tabLead`.territory,
			`tabLead`.source,
			`tabLead`.team_user_code,
			`tabLead`.introducer,
			`tabLead`.email_id,
			`tabLead`.mobile_no,
			`tabLead`.phone,
			`tabLead`.owner,
			`tabLead`.company,
			concat_ws(', ',
				trim(',' from `tabAddress`.address_line1),
				trim(',' from tabAddress.address_line2)
			) AS address,
			`tabAddress`.state,
			`tabAddress`.pincode,
			`tabAddress`.country
		FROM
			`tabLead` left join `tabDynamic Link` on (
			`tabLead`.name = `tabDynamic Link`.link_name and
			`tabDynamic Link`.parenttype = 'Address')
			left join `tabAddress` on (
			`tabAddress`.name=`tabDynamic Link`.parent)
		WHERE
			company = %(company)s {conditions}
		ORDER BY
			`tabLead`.creation asc """.format(
			conditions=get_conditions(filters)
		),
		filters,
		as_dict=1,
	)


def get_conditions(filters):
	conditions = []
	base_date = filters.get("based_date")
    
 
	if filters.get("lead_status"):
		conditions.append(" and `tabLead`.lead_status=%(lead_status)s")
  
	if filters.get("team_user_code"):
		conditions.append(" and `tabLead`.team_user_code=%(team_user_code)s")
	if filters.get("source"):
		conditions.append(" and `tabLead`.source=%(source)s")
	if filters.get("introducer"):
		conditions.append(" and `tabLead`.introducer=%(introducer)s")
	if base_date ==  "Created":
		conditions.append(" AND `tabLead`.date BETWEEN %(from_date)s AND %(to_date)s")
	if base_date ==  "Sales Completed":
		conditions.append(" AND `tabLead`.sales_completed_date BETWEEN %(from_date)s AND %(to_date)s")

	if filters.get("territory"):
		conditions.append(" and `tabLead`.territory=%(territory)s")

	if filters.get("status"):
		conditions.append(" and `tabLead`.workflow_state=%(status)s")

	return " ".join(conditions) if conditions else ""