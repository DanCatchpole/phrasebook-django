var constantsURL = $("#constantsURL").text();
var categoryID = $("#category").val();

var removeList = [];
var words = [];

$(function() {

    $(".mini-bar").on('click', '#edit-add', function() {
        $(this).attr('id', "save");
        $(this).text("");
        $(this).siblings().addClass('disabled');
        $(".search").addClass('disabled');
        $(this).append($("<i>", {"class": "fa fa-fw fa-check"})).append("Save").attr('title', "Save");

        $(".allWords .wordBlock").each(function() {
            $(this).addClass("editing");
            let $langField = $(this).children(".lang");
            let lang = $langField.text();
            $langField.text("");
            let $textBox = $("<input>", {"type": "text", "class": "langEdit"}).val(lang);
            $langField.append($textBox);

            let $engField = $(this).children(".english");
            let eng = $engField.text();
            $engField.text("");
            let $textBox2 = $("<input>", {"type": "text", "class": "englishEdit"}).val(eng);
            $engField.append($textBox2);
        });

        let $newWordBlock = $("<div>", {"class": "wordBlock new-word"});
        $newWordBlock.append($("<span>", {"class": "lang"}).append($("<input>", {"type": "text", "class": "langEdit"})));
        $newWordBlock.append($("<span>", {"class": "padding"}));
        $newWordBlock.append($("<span>", {"class": "english"}).append($("<input>", {"type": "text", "class": "englishEdit"}).keyup(function(e) {
            if (!$(this).parent().parent().next().hasClass("new-word")) {
                createNewWordBlock($(this).parent().parent());
                $(this).keyup(null);
            }
        })));
        $newWordBlock.append($("<span>", {"class": "padding"}));

        $(".allWords").prepend($newWordBlock);
    }).on('click', '#save', function() {
        // reset remove list
        removeList = [];
        words = [];
        newWords = [];
        $(this).attr('id', "edit-add");
        $(this).text("");
        $(this).siblings().removeClass('disabled');
        $(".search").removeClass('disabled');
        $(this).append($("<i>", {"class": "fa fa-fw fa-pencil"})).append("Edit/Add Words").attr('title', "Edit/Add Words");

        $(".allWords .wordBlock").each(function() {
            $(this).removeClass("editing");
            let $langField = $(this).children(".lang");
            let lang = $langField.children(".langEdit").val();
            let $engField = $(this).children(".english");
            let eng = $engField.children(".englishEdit").val();
            let id = $(this).children(".word_id").val();
            if (lang === "" || eng === "") {
                if (!$(this).hasClass("new-word")) {
                    removeList.push(id);
                }
                $(this).remove();
            } else {
                if (!$(this).hasClass("new-word")) {
                    words.push({ "foreign": lang, "english": eng, "id": id });
                } else {
                    newWords.push({ "foreign": lang, "english": eng });
                }
            }

            $langField.text(lang);
            $engField.text(eng);
        });
        console.log(removeList);
        console.log(words);
        let catID = $("#category_id").val();
        $.post("./update/", JSON.stringify({"removed_words": removeList, "updated_words": words, "new_words": newWords}), function(d) {
            location.reload();
        }, "text");
    });


    // Edit notes
    $("#edit_notes").click(function() {
        // check if "edit" or "save"
        let $content = $(".content");
        if($(this).text() === "Edit") {
            // edit
            $(".description-editor").removeClass("hidden");
            $(".notes").addClass("hidden");
            $(this).text("Save");
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
            $(this).text("Save");
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

function createNewWordBlock($insertAfter) {
        let $newWordBlock = $("<div>", {"class": "wordBlock new-word"});
        $newWordBlock.append($("<span>", {"class": "lang"}).append($("<input>", {"type": "text", "class": "langEdit"})));
        $newWordBlock.append($("<span>", {"class": "padding"}));
        $newWordBlock.append($("<span>", {"class": "english"}).append($("<input>", {"type": "text", "class": "englishEdit"}).keyup(function(e) {
            if (!$(this).parent().parent().next().hasClass("new-word")) {
                createNewWordBlock($(this).parent().parent());
                $(this).keyup(null);
            }
        })));
        $newWordBlock.append($("<span>", {"class": "padding"}));
        $newWordBlock.insertAfter($insertAfter);
        console.log("inserted")
}