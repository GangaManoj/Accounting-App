import frappe

def get_context(context):
    context.cart_items = frappe.get_all('Cart', fields = ['image', 'name', 'rate', 'description', 'route'])
    context.sum = frappe.get_all('Cart', fields = ['sum(rate) as sum'])
    return context