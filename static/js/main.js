jQuery(document).ready(function($) {


	var mastheadheight = $('.ds-header').outerHeight();
	//console.log(mastheadheight);
	$(".ds-banner,.ds-main-section").css("margin-top" , mastheadheight);

	$(window).scroll(function(){
	    if ($(window).scrollTop() >= 10) {
	        $('.ds-header').addClass('ds-fixed-header');
	    }
	    else {
	        $('.ds-header').removeClass('ds-fixed-header');
	    }
	}).scroll();


    // Ajax
    function server(form){
            // Функция для отправки формы и номера подарка
            // и получения ссылки на подарок и текста предскаания
            var url = form.attr("action");
            var data = form.serialize(); // Отправка формы в виде словаря
            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                cache: true,
                success: function (data) {
                    // Операция успешно выполнена
                    $('#comment').text("Спасибо за отзыв!");  // Поблагодарить
                },
            });
    }

    // Отправление отзыва
    $("#send").on('click', function(e){
        if ($('#message').val().trim()) {
            // Чтоб содержимое не было пустым
             server($('#form_save_mess'))
        }
    });

});