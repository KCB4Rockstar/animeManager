console.log("Hello visitors! Nice of you to check out our console...but why?");

$("body").find('img').each(function() {
    $(this).on("error", function(){
        $(this).attr("src", "/static/img/noPhoto.png").load();
    });
});