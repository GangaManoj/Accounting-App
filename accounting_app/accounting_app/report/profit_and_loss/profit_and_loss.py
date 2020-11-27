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
		"width" : 200
	},
	{
		"fieldname" : "amount",
		"label" : _("Amount"),
		"fieldtype" : "Currency",
		"width" : 200
	}]

	return columns

def get_data(filters):
	data = []
	expenses = 0
	income = 0
	indent = 0

	expense_accounts = get_descendants_of("Account", "Expenses") 
	expense_accounts.append("Expenses")
	income_accounts = get_descendants_of("Account", "Income")
	income_accounts.append("Income")

	parent_income = {
		'indent' : indent,
		'account' : "Income"
	}
	data.append(parent_income)
	indent += 1
	for ledger_entry in frappe.get_all('Ledger Entry', fields = ['sum(debit) as amount','account'], filters = {'account' : ["in", income_accounts]}, group_by = 'account'):
		report_entry = {
			'indent' : indent,
			'account' : ledger_entry.account,
			'amount' : ledger_entry.amount,
			'parent_account' : parent_income['account']
		}
		data.append(report_entry)
		income += ledger_entry.amount

	indent = 0
	parent_expense = {
		'indent' : indent,
		'account' : "Expenses"
	}
	data.append(parent_expense)
	indent += 1
	for ledger_entry in frappe.get_all('Ledger Entry', fields = ['sum(credit) as amount','account'], filters = {'account' :["in", expense_accounts]}, group_by = 'account'):
		report_entry = {
			'indent' : indent,
			'account' : ledger_entry.account,
			'amount' : -(ledger_entry.amount),
			'parent_account' : parent_expense['account']
		}
		data.append(report_entry)
		expenses += ledger_entry.amount

	if income > expenses:
		profit = income - expenses
		data.append({'account': "Net Profit", 'amount': profit})
	else:
		loss = expenses - income
		data.append({'account': "Net Loss", 'amount': loss})

	return data
