var constantsURL = $("#constantsURL").text();
var categoryID = $("#category").val();

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


$(function() {
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


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
