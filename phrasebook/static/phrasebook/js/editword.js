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
        convert($obj, $lang, $eng, word, english);
    });

    $(".allWords").on('click', ".wordBlock .edit i.editing", function() {
        $(this).removeClass("editing");
        $(this).removeClass("fa-check");
        $(this).addClass("fa-pencil");

        var $lang = $(this).parent().parent().children(".lang");
        var $eng = $(this).parent().parent().children(".english");

        var wordID = $(this).parent().parent().children(".word_id").val();
        var newValue = $lang.children("input[type=text]").val();
        var newEng = $eng.children("input[type=text]").val();

        $.post(constantsURL + "../word/update", {word_id: wordID, newWord: newValue, newEnglish: newEng, category: categoryID}, function(data, status, jqXHR) {
            if (data.status === "error") {
                convert($(this), $lang, $eng, newValue, newEng);
            } else {
                $lang.text($lang.children("input[type=text]").val());
                $eng.text($eng.children("input[type=text]").val());
            }
        });

    });


    // Edit notes
    $("#edit_notes").click(function() {
        // check if "edit" or "save"
        let $content = $(".content");
        if($(this).text() === "Edit") {
            // edit
            $(".description-editor").removeClass("hidden");
            $(".notes").addClass("hidden");
            $(this).removeClass("bg--deepOrange").addClass("bg--olive").text("Save");
        } else {
            // save
            let value = $(".description-editor").val();
            $.post("./notes/update/", {
                "notes": value,
                "renderonly": "false"
            }, function(data) {
                console.log(data);
                $(".description-editor").addClass("hidden");
                $(".notes").html(data.message).removeClass("hidden");
            });
            // $content.html(value.replace('<script>'));
            $(this).addClass("bg--deepOrange").removeClass("bg--olive").text("Save");
            $(this).text("Edit");
        }
    });
});


function convert($obj, $lang, $eng, word, english) {
    $obj.addClass("editing");
    $obj.addClass("fa-check");
    $obj.removeClass("fa-pencil");

    $lang.text("");
    $eng.text("");

    $lang.append($("<input>", {id: "hiddenLang", type: "hidden"}).val(word));
    $eng.append($("<input>", {id: "hiddenEng", type: "hidden"}).val(english));

    $lang.append($("<input>", {class: "langEdit", id: "langEdit", type: "text"}).val(word));
    $eng.append($("<input>", {class: "englishEdit", id: "englishEdit", type: "text"}).val(english));
}