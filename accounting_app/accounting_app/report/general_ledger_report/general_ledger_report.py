# Copyright (c) 2013, Ganga Manoj and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate

def execute(filters=None):
	columns = get_columns(filters)
	data = get_data(filters)
	
	return columns, data

def get_columns(filters):
	columns = [{
		"fieldname" : "posting_date",
		"label" : _("Posting Date"),
		"fieldtype" : "Date",
		"width" : 120
	},
	{
		"fieldname" : "fiscal_year",
		"label" : _("Fiscal Year"),
		"fieldtype" : "Data",
		"width" : 120
	},
	{
		"fieldname" : "account",
		"label" : _("Account"),
		"fieldtype" : "Link",
		"options" : "Account",
		"width" : 120
	},
	{
		"fieldname" : "debit",
		"label" : _("Debit"),
		"fieldtype" : "Currency",
		"width" : 120
	},
	{
		"fieldname" : "credit",
		"label" : _("Credit"),
		"fieldtype" : "Currency",
		"width" : 120
	},
	{
		"fieldname" : "voucher_type",
		"label" : _("Voucher Type"),
		"fieldtype" : "Link",
		"options" : "DocType",
		"width" : 120
	},
	{
		"fieldname" : "voucher_number",
		"label" : _("Voucher Number"),
		"fieldtype" : "Dynamic Link",
		"options" : "voucher_type",
		"width" : 120
	},
	{
		"fieldname" : "against_account",
		"label" : _("Against Account"),
		"fieldtype" : "Text",
		"width" : 120
	},
	{
		"fieldname" : "balance",
		"label" : _("Balance"),
		"fieldtype" : "Currency",
		"width" : 258
	}]

	return columns

def get_data(filters):
	data = []
	accounts = []
	for ledger_entry in frappe.get_all('Ledger Entry', fields = ['account']):
		accounts.append(ledger_entry.account)

	c = 0
	if "from" in filters and "to" in filters:
		filter = {'posting_date' : ["between", (filters["from"], filters["to"])]}
	elif "from" in filters:	
		filter = {'posting_date' : ['>=', filters["from"]]}
	elif "to" in filters:
		filter = {'posting_date' : ['<=', filters["to"]]}
	else:
		filter = {}

	for ledger_entry in frappe.get_all('Ledger Entry', filters = filter, fields = ['posting_date','account','debit','credit','voucher_type','voucher_number']):
		c += 1

		# to find the against account
		if c % 2 == 0:
			against_account = accounts[c - 2] # the account of the ledger entry right before it
		else:
			against_account = accounts[c] # the account of the ledger entry right after it

		report_entry = {
			"posting_date" : ledger_entry.posting_date,
			"fiscal_year" : ledger_entry.fiscal_year,
			"account" : ledger_entry.account,
			"debit" : ledger_entry.debit,
			"credit" : ledger_entry.credit,
			"voucher_type" : ledger_entry.voucher_type,
			"voucher_number" : ledger_entry.voucher_number,
			"against_account" : against_account,
			"balance" : ledger_entry.debit - ledger_entry.credit
		}
		data.append(report_entry)
		
	return data