// Copyright (c) 2016, Ganga Manoj and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["General Ledger Report"] = {
	"filters": [
		{
			"fieldname" : "from",
			"label" : __("From"),
			"fieldtype" : "Date"
		},
		{
			"fieldname" : "to",
			"label" : __("To"),
			"fieldtype" : "Date"
		}
	]
};