# -*- coding: utf-8 -*-
# Copyright (c) 2020, Ganga Manoj and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class Item(WebsiteGenerator):
	pass


@frappe.whitelist(allow_guest=True)
def add_item_to_cart(name,image,rate,route):
	cart_item = frappe.get_doc({
		'doctype': 'Cart',
		'item_name': name,
		'image': image,
		'rate': rate,
		'route': route
	}).insert()