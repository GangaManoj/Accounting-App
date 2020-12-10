frappe.ready(function(){
    $('#addToCart').on('click', async function(){
        let cart_doc = await frappe.get_doc({doctype:'Cart', item:'{{ doc }}'});
        await cart_doc.insert();
        console.log('Hello?');
    });
    console.log('{{ doc.name }}');
    console.log('{{ doc }}');
})