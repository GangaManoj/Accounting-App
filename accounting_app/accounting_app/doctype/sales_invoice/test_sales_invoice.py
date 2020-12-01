# -*- coding: utf-8 -*-
# Copyright (c) 2020, Ganga Manoj and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestSalesInvoice(unittest.TestCase):
	def tearDown(self):
		frappe.db.rollback()

	def test_ledger_entry_creation(self):
		before_sales_invoice = frappe.db.count('Ledger Entry')
		doc = frappe.get_doc({
			"doctype": "Sales Invoice",
			"customer": "Dhanya Aleena",
			"company": "Gada Electronics",
			"posting_date": "2020-11-20",
			"items" : [{
				"item": "xyz",
				"quantity": 2,
			}]
		})
		doc.insert()
		doc.submit()
		after_sales_invoice = frappe.db.count('Ledger Entry')
		difference = after_sales_invoice - before_sales_invoice
		self.assertEqual(difference, 2, "Creation of sales invoice does not result in the creation of two corresponding ledger entries.")

	def test_total(self):
		doc = frappe.get_doc({
			"doctype": "Sales Invoice",
			"customer": "Dhanya Aleena",
			"company": "Gada Electronics",
			"posting_date": "2020-11-20",
			"items" : [{
				"item": "xyz",
				"quantity": 2,
			},
			{
				"item": "abc",
				"quantity": 3,
			}]
		})
		doc.insert()
		total = 0
		for item in doc.get('items'):
			total += item.amount

		self.assertEqual(doc.grand_total, total, "Grand Total is incorrect.")

		