$(document).ready(function() {

     // this line will add Jquery DataTable to the Task list table
     $('#to_do_table').DataTable();

    // Code for expanding to do input field on hover
    var divWidth = $(".add_item").width();
    var window_width = $(window).width()
    if(window_width > 780) {
        $("input.add_item").on("click", function(){
               $(this).animate({
                    width: "400"
                });
        }).mouseleave(function(){
            $(this).animate({
                width: divWidth
            });
        });
    }


//    $('#to_do_table th.contenteditable input').keyup(function(e){
//    if(e.keyCode == 13)
//        {
//            $.ajax({
//                  type: "POST",
//                  url: "/ajax_item_submit",
//                  data: {
//                    'item': $(this).val() // from form
//                  },
//                  success: function () {
//                  }
//                });
//            $('.nav-item .active').focus();
//        }
//
//    });
//
//function getCookie(name) {
//var cookieValue = null;
//if (document.cookie && document.cookie != '') {
//    var cookies = document.cookie.split(';');
//    for (var i = 0; i < cookies.length; i++) {
//        var cookie = jQuery.trim(cookies[i]);
//        // Does this cookie string begin with the name we want?
//        if (cookie.substring(0, name.length + 1) == (name + '=')) {
//            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//            break;
//        }
//    }
//}
//    return cookieValue;
//}
//var csrftoken = getCookie('csrftoken');
//console.log(csrftoken);
//
////Ajax call
//function csrfSafeMethod(method) {
//// these HTTP methods do not require CSRF protection
//return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//}
//$.ajaxSetup({
//    crossDomain: false, // obviates need for sameOrigin test
//    beforeSend: function(xhr, settings) {
//        if (!csrfSafeMethod(settings.type)) {
//            xhr.setRequestHeader("X-CSRFToken", csrftoken);
//        }
//    }
//});
});

