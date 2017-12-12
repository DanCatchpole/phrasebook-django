var constantsURL = $("#constantsURL").text();
var categoryID = $("#category").val();




$(function() {



    $(".allWords").on('click', ".wordBlock .starred i.star-on", function() {
        var wordID = $(this).parent().parent().children(".word_id").val();
        var $obj = $(this);
        // console.log(wordID);
        $.post(constantsURL + "../../word/star/", {categoryID: categoryID, starred: false, wordID: wordID}, function(data, status, jqXHR) {
            console.log(data);
            if (data) {
                console.log($obj);
                $obj.removeClass('star-on');
                $obj.addClass('star-off');
                $obj.parent().attr("title", "Star")
            }
        })
    });

    $(".allWords").on('click', ".wordBlock .starred i.star-off", function() {
        var wordID = $(this).parent().parent().children(".word_id").val();
        var $obj = $(this);
        // console.log(wordID);
        $.post(constantsURL + "../../word/star/", {categoryID: categoryID, starred: true, wordID: wordID}, function(data, status, jqXHR) {
            console.log(data);
            if (data) {
                console.log($obj);
                $obj.removeClass('star-off');
                $obj.addClass('star-on');
                $obj.parent().attr("title", "Unstar")
            }
        })
    });
});
