$(document).ready(function () {

    $('#click1, #click2, #click3, #click4, #click5, #click6, #click7, #click8').click(function () {
        $(this).css('visibility','hidden');
    });

    $('#reset').click(function () {
        $('img').css('visibility','visible');
    });
    
});