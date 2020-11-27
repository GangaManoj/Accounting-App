# Copyright (c) 2013, Ganga Manoj and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils.nestedset import get_descendants_of

def execute(filters=None):
	columns = get_columns(filters)
	data = get_data(filters)

	return columns, data

def get_columns(filters):
	columns =[{
		"fieldname" : "account",
		"label" : _("Account"),
		"fieldtype" : "Link",
		"options" : "Account",
		"width" : 150
	},
	{
		"fieldname" : "debit",
		"label" : _("Amount"),
		"fieldtype" : "Currency",
		"width" : 150
	}]

	return columns

def get_data(filters):
	data = []
	assets = get_descendants_of("Account", "Application of Funds (Assets)") 
	liabilities = get_descendants_of("Account", "Source of Funds (Liabilities)")
	assets_and_liabilities = assets + liabilities

	data = frappe.get_all('Ledger Entry', fields = ['account', 'debit'], filters = {'account' : ["in", assets_and_liabilities]})

	return data