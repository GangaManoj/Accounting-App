import frappe

def get_context(context):
    context.cart_items = frappe.get_all('Cart', fields = ['image', 'name', 'rate','route'])
    context.sum = frappe.get_all('Cart', fields = ['sum(rate) as sum'])
    return context

@frappe.whitelist(allow_guest=True)
def remove_item_from_cart(name):
	frappe.delete_doc('Cart', name)

	print(name)
	print("*" * 100)