$(document).ready(function()
{
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function(e)
    {
        e.preventDefault();
        var nmb = $('#number').val();
        var submit_btn = $('#submit_btn');
        var product_id =  submit_btn.data("product_id");
        var name = submit_btn.data("name");
        var price = submit_btn.data("price");
        console.log(nmb);
        console.log(product_id );
        console.log(name);
        console.log(price);

        $('.basket-items ul').append('<li>'+name+', ' + nmb + 'шт. ' + 'по ' + price + 'грн  ' +
            '<a class="delete-item" href="">x</a>'+
            '</li>');

    })
});

