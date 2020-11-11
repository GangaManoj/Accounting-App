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

	def on_submit(self):
		sum = 0
		for item in self.get('items'):
			sum += item.amount
		ledger_entry_doc1 = frappe.get_doc({
			"doctype": "Ledger Entry",
			"posting_date": frappe.utils.nowdate(),
			"account": "Sales" ,
			"debit": sum,
			"credit": 0,
			"voucher_type": "Sales Invoice",
			"voucher_number": self.name
		})
		ledger_entry_doc2 = frappe.get_doc({
			"doctype": "Ledger Entry",
			"posting_date": frappe.utils.nowdate(),
			"account": "Debtors" ,
			"debit": 0,
			"credit": sum,
			"voucher_type": "Sales Invoice",
			"voucher_number": self.name
		})
		ledger_entry_doc1.insert()
		ledger_entry_doc2.insert()