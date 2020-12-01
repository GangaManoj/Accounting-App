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
		"fieldname" : "amount",
		"label" : _("Amount"),
		"fieldtype" : "Currency",
		"width" : 150
	}]

	return columns

def get_data(filters):
	data = []
	assets = get_descendants_of("Account", "Application of Funds (Assets)") 
	liabilities = get_descendants_of("Account", "Source of Funds (Liabilities)")
	indent = 0

	parent_assets = {
		'indent' : indent,
		'account' : "Assets"
	}
	data.append(parent_assets)
	indent += 1
	for ledger_entry in frappe.get_all('Ledger Entry', fields = ['sum(credit) as amount','account'], filters = {'account' : ["in", assets]}, group_by = 'account'):
		report_entry = {
			'indent' : indent,
			'account' : ledger_entry.account,
			'amount' : ledger_entry.amount,
			'parent_account' : parent_assets['account']
		}
		data.append(report_entry)

	indent = 0
	parent_liabilities = {
		'indent' : indent,
		'account' : "Liabilities"
	}
	data.append(parent_liabilities)
	indent += 1
	for ledger_entry in frappe.get_all('Ledger Entry', fields = ['sum(debit) as amount','account'], filters = {'account' :["in", liabilities]}, group_by = 'account'):
		report_entry = {
			'indent' : indent,
			'account' : ledger_entry.account,
			'amount' : ledger_entry.amount,
			'parent_account' : parent_liabilities['account']
		}
		data.append(report_entry)

	return data