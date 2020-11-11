# -*- coding: utf-8 -*-
# Copyright (c) 2020, Ganga Manoj and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class SalesInvoiceItem(Document):
	def before_save(self):
		self.amount = self.rate * self.quantity