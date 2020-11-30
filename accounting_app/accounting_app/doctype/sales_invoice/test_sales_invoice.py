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
		customer = frappe.get_doc("Customer", "Arjun Manoj")
		company = frappe.get_doc("Company", "Gada Electronics")
		doc = frappe.get_doc({
			"doctype": "Sales Invoice",
			"customer": customer,
			"company": company,
			"posting_date": "2020-11-20"
		})
		doc.append("items",{
			"item": "xyz",
			"quantity": 2
		})
		doc.insert()
		after_sales_invoice = frappe.db.count('Ledger Entry')
		difference = after_sales_invoice - before_sales_invoice
		self.assertEqual(difference, 2, "Creation of sales invoice does not result in the creation of two corresponding ledger entries.")