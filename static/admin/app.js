

$(document).ready(function(){
    $('a').each(function(){
        console.log($(this))
        var newHref = $(this).attr('href').replace('https://eventmie-pro-demo.classiebit.com/', '/');
        $(this).attr('href', newHref);
    });
});