frappe.ready(function(){
    $('#removeFromCart').on('click', function(){
        frappe.call({
            method: "accounting_app.www.cart.remove_item_from_cart",
            args: {
                "name": '{{ doc.name }}',
            }
        })
        console.log('Hello?');
        console.log(name);
    });
})