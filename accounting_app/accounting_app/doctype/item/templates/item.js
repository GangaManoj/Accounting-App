frappe.ready(function(){
    $('#addToCart').on('click', function(){
        frappe.call({
            method: "accounting_app.accounting_app.doctype.item.item.add_item_to_cart",
            args: {
                "name": '{{ doc.name }}',
                "image": '{{ doc.image }}',
                "rate":  '{{ doc.rate }}',
                "route": '{{ doc.route }}'
            }
        })
    });
})