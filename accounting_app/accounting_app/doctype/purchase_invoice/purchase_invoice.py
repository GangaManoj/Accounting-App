# -*- coding: utf-8 -*-
# Copyright (c) 2020, Ganga Manoj and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class PurchaseInvoice(Document):
	def before_save(self):
		for item in self.get('items'):
			item.amount = item.rate * item.quantity
