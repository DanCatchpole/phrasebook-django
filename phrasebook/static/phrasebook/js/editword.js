var constantsURL = $("#constantsURL").text();
var categoryID = $("#category").val();
$(function() {
    $(".allWords").on('click', ".wordBlock .edit i.fa-pencil:not(.editing)", function() {
        var $lang = $(this).parent().parent().children(".lang");
        var $eng = $(this).parent().parent().children(".english");

        var word = $lang.text();
        var english = $eng.text();

        $(".editing").each(function() {
            $(this).removeClass("editing");
            $(this).removeClass("fa-check");
            $(this).addClass("fa-pencil");

            var $l = $(this).parent().parent().children(".lang");
            var $e = $(this).parent().parent().children(".english");

            $l.text($l.children("input[type=hidden]").val());
            $e.text($e.children("input[type=hidden]").val());

        });

        var $obj = $(this);
        $obj.addClass("editing");
        $obj.addClass("fa-check");
        $obj.removeClass("fa-pencil");

        $lang.text("");
        $eng.text("");

        $lang.append($("<input>", {id: "hiddenLang", type: "hidden"}).val(word));
        $eng.append($("<input>", {id: "hiddenEng", type: "hidden"}).val(english));

        $lang.append($("<input>", {class: "langEdit", id: "langEdit", type: "text"}).val(word));
        $eng.append($("<input>", {class: "englishEdit", id: "englishEdit", type: "text"}).val(english));

        console.log(word);
        console.log(english);
    });

    $(".allWords").on('click', ".wordBlock .edit i.editing", function() {
        console.log("send");
        $(this).removeClass("editing");
        $(this).removeClass("fa-check");
        $(this).addClass("fa-pencil");

        var $lang = $(this).parent().parent().children(".lang");
        var $eng = $(this).parent().parent().children(".english");

        var wordToChange = $lang.children("input[type=hidden]").val();
        var newValue = $lang.children("input[type=text]").val();
        var newEng = $eng.children("input[type=text]").val();

        $.post(constantsURL + "/words/update", {word: wordToChange, newWord: newValue, newEnglish: newEng, category: categoryID}, function(data, status, jqXHR) {
            console.log(data);
            $lang.text($lang.children("input[type=text]").val());
            $eng.text($eng.children("input[type=text]").val());
        });
    });
});
