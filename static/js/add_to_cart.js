function add_to_cart(el) {
    let item_id = el.dataset.item_id
    let item_image = el.dataset.item_image
     let item_name = el.dataset.item_name
    let csrf_token = $('#dummy_form [name="csrfmiddlewaretoken"]').val();
    let data = {};
    data.item_id = item_id;
    data['csrfmiddlewaretoken'] = csrf_token;
    let url = '/cart/add_to_cart/';
    console.log(data);
    $.ajax({
        url:url,
        type:'POST',
        data: data,
        cache:true,
        success: function (data) {
            console.log('OK');
            // console.log(data.total_items_in_cart);
            // console.log(data.all_items);


            $('.cart-items').css('display','inline-block')
            $('#cart_count').text(data.total_items_in_cart)
             $('#cart_count1').text(data.total_items_in_cart)



            $.amaran({
                'theme'     :'user blue',
                'content'   :{
                    img: item_image,
                    user:'Добавлено в корзину:',
                    message:`${item_name}`
                },

                'position'  :'bottom right',
                'outEffect' :'slideRight'
            });
        },
        error: function () {
            console.log('ERROR')
        }
    })
}