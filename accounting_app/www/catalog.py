import frappe

def get_context(context):
    context.items = frappe.get_all('Item', fields = ['image', 'name', 'rate', 'description', 'route'])
    return context