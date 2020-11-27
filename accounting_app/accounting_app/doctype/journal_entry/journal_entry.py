# -*- coding: utf-8 -*-
# Copyright (c) 2020, Ganga Manoj and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

class JournalEntry(Document):
	def before_save(self):
		self.total_debit = 0
		self.total_credit = 0
		for accounting_entry in self.get('accounting_entries'):
			self.total_debit += accounting_entry.debit
			self.total_credit += accounting_entry.credit

		if self.total_credit != self.total_debit:
			frappe.throw(_('Total credit should be equal to total debit.'))

	def on_submit(self):
		for accounting_entry in self.get('accounting_entries'):
			fiscal_year = frappe.get_all('Fiscal Year', filters = {'from_date' : ['<=', self.posting_date], 'to_date' : ['>=', self.posting_date]}, pluck = 'name')
			ledger_entry_doc = frappe.get_doc({
				"doctype": "Ledger Entry",
				"posting_date": self.posting_date,
				"account": accounting_entry.account ,
				"debit": accounting_entry.debit,
				"credit": accounting_entry.credit,
				"voucher_type": "Journal Entry",
				"voucher_number": self.name,
				"fiscal_year" : fiscal_year[0],
				"company" : self.company
			})
			ledger_entry_doc.insert()