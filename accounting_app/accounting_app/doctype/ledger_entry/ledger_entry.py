# -*- coding: utf-8 -*-
# Copyright (c) 2020, Ganga Manoj and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LedgerEntry(Document):
	# for ledger_entry in frappe.get_all('Ledger Entry', fields = ['posting_date', 'fiscal_year', 'name']):
	# 	fiscal_year = frappe.get_all('Fiscal Year', filters = {'from_date' : ['<=', ledger_entry.posting_date], 'to_date' : ['>=', ledger_entry.posting_date]}, pluck = 'name')
	# 	ledger_entry.fiscal_year = fiscal_year[0]
	# 	print("*" * 25)
	# 	print(ledger_entry.name)

	# 	doc = frappe.get_doc('Ledger Entry', ledger_entry.name)
	# 	doc.fiscal_year = fiscal_year[0]
	# 	doc.save()
	pass
