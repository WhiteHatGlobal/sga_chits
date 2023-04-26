// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Lead Report"] = {
	"filters": [
		{
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"default": frappe.defaults.get_user_default("Company"),
			"reqd": 1
		},
		{
			"fieldname":"based_date",
			"label": __("Based Date"),
			"fieldtype": "Select",
			"default": "Created",
			"options": "\nCreated\nSales Completed"
		},
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -12),
			"reqd": 1
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1
		},
		{
			"fieldname":"source",
			"label": __("Source"),
			"fieldtype": "Link",
			"options": "Lead Source"
		},
		{	
			"fieldname":"team_user_code",
			"label": __("Team User Code"),
			"fieldtype": "Select",
			"options": "\nKTS\nMJP\nTYN\nRUK\nPMC\nNSV\nVTN\nNAB\nSSP\nSGA"
		},
		{	
			"fieldname":"introducer",
			"label": __("Introducer"),
			"fieldtype": "Link",
			"options": "Introducer"
		},
		{
			"fieldname":"status",
			"label": __("Status"),
			"fieldtype": "Link",
			"options": "Workflow State"
			// [
			// 	{ "value": "Lead", "label": __("Lead") },
			// 	{ "value": "Open", "label": __("Open") },
			// 	{ "value": "Replied", "label": __("Replied") },
			// 	{ "value": "Opportunity", "label": __("Opportunity") },
			// 	{ "value": "Quotation", "label": __("Quotation") },
			// 	{ "value": "Lost Quotation", "label": __("Lost Quotation") },
			// 	{ "value": "Interested", "label": __("Interested") },
			// 	{ "value": "Converted", "label": __("Converted") },
			// 	{ "value": "Do Not Contact", "label": __("Do Not Contact") },
			// ],
		},
		{
			"fieldname":"lead_status",
			"label": __("Lead Status"),
			"fieldtype": "Select",
			"options": "\nHot\nCold\nWarm\nNot to Call\nDead"
		},
		{
			"fieldname":"territory",
			"label": __("Territory"),
			"fieldtype": "Link",
			"options": "Territory",
		}
	]
};
