$(document).on("ready", function(){
    //adding default value to short_url field
    var curr_addr = window.location.href
    var len = curr_addr.length
    if (curr_addr[len-1] == '?'){
        len -= 1;
        curr_addr = curr_addr.substr(0, len)
    }
    $("#short_url").val(curr_addr);
    $("#long_url").val("http://");

    //operating copy_button
    $('#copy_button').click(function(event) {
        // Выборка ссылки с электронной почтой
        $('.short_url').select();

        try {
          // Теперь, когда мы выбрали текст ссылки, выполним команду копирования
          var successful = document.execCommand('copy');
          var msg = successful ? 'successful' : 'unsuccessful';
          console.log('Copy email command was ' + msg);
        } catch(err) {
          console.log('Oops, unable to copy');
        }

        // Снятие выделения

        if (window.getSelection) {
            if (window.getSelection().empty) { // Chrome
                window.getSelection().empty();
            } else if (window.getSelection().removeAllRanges) { // Firefox
                window.getSelection().removeAllRanges();
            }
        } else if (document.selection) { // IE?
            document.selection.empty();
        }
    });
});