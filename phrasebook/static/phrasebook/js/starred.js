var constantsURL = $("#constantsURL").text();
var categoryID = $("#category").val();

$(function() {
    $(".allWords").on('click', ".wordBlock .starred i.star-on", function() {
        var word = $(this).parent().parent().children(".lang").text();
        var $obj = $(this);
        console.log(word);
        $.post(constantsURL + "/words/star", {categoryID: categoryID, starred: false, word: word}, function(data, status, jqXHR) {
            console.log(data);
            if (data) {
                console.log($obj);
                $obj.removeClass('star-on');
                $obj.addClass('star-off');
            }
        })
    });

    $(".allWords").on('click', ".wordBlock .starred i.star-off", function() {
        var word = $(this).parent().parent().children(".lang").text();
        var $obj = $(this);
        console.log(word);
        $.post(constantsURL + "/words/star", {categoryID: categoryID, starred: true, word: word}, function(data, status, jqXHR) {
            console.log(data);
            if (data) {
                console.log($obj);
                $obj.removeClass('star-off');
                $obj.addClass('star-on');
            }
        })
    });
});
