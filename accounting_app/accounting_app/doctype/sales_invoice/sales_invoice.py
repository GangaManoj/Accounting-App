# -*- coding: utf-8 -*-
# Copyright (c) 2020, Ganga Manoj and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class SalesInvoice(Document):
	def before_save(self):
		for item in self.get('items'):
			item.amount = item.rate * item.quantity
		grand_total = 0
		for item in self.get('items'):
			grand_total += item.amount
		self.grand_total = grand_total

	def on_submit(self):
		fiscal_year = frappe.get_all('Fiscal Year', filters = {'from_date' : ['<=', self.posting_date], 'to_date' : ['>=', self.posting_date]}, pluck = 'name')
		ledger_entry_doc1 = frappe.get_doc({
			"doctype": "Ledger Entry",
			"posting_date": self.posting_date,
			"fiscal_year" : fiscal_year[0],
			"account": "Sales" ,
			"debit": self.grand_total,
			"credit": 0,
			"voucher_type": "Sales Invoice",
			"voucher_number": self.name,
			"company" : self.company
		})
		ledger_entry_doc2 = frappe.get_doc({
			"doctype": "Ledger Entry",
			"posting_date": self.posting_date,
			"fiscal_year" : fiscal_year[0],
			"account": "Debtors" ,
			"debit": 0,
			"credit": self.grand_total,
			"voucher_type": "Sales Invoice",
			"voucher_number": self.name,
			"company" : self.company
		})
		ledger_entry_doc1.insert()
		ledger_entry_doc2.insert()