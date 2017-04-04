var constantsURL = $("#constantsURL").text();
function escapeHtml(text) {
  return text
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
}

$(function(){
    $('#search').on('keyup', function(e){
        if ($(".editing").length == 0) {
            if ($("#category")) {
                var parameters = { search: $(this).val(), username: $("#username").val(), category: $("#category").val(), short: $("#shortenedLanguage").val()};
            } else {
                var parameters = { search: $(this).val(), username: $("#username").val(), short: $("#shortenedLanguage").val()};
            }
            $.post( constantsURL + '/words/search', parameters, function(data) {
                $(".allWords").html("");
                if (data.length == 0) {
                    $(".allWords").html(`<div style='padding: 1rem; color:#d12929; font-weight: 600;' class='wordBlock'> No words match this query: ${escapeHtml(parameters.search)} </div>`);
                }
                for (elem of data) {
                    var $wordBlock = $("<div>", {class: "wordBlock"});
                    var $lang = $("<span>", {class: "lang"});
                    $lang.html(elem.word);

                    var $padding1 = $("<span>", {class: "padding"});

                    var $translations = $("<span>", {class: "english"});
                    $translations.text(elem.translations);


                    $wordBlock.append($lang);
                    $wordBlock.append($padding1);
                    $wordBlock.append($translations);
                    if ($("#categoryRequired").text() == "Category") {
                        var $padding2 = $("<span>", {class: "padding"});
                        var $category = $("<span>", {class: "category"});
                        $category.text(elem.catName);


                        $wordBlock.append($padding2);
                        $wordBlock.append($category);
                    } else {
                        var $padding3 = $("<span>", {class: "padding"});
                        $wordBlock.append($padding3);

                        var $star = $("<span>", {class: "starred"});
                        if (elem.starred) {
                            $star.append($("<i>", {class: "fa fa-fw fa-star star-on"}))
                        } else {
                            $star.append($("<i>", {class: "fa fa-fw fa-star star-off"}))
                        }
                        $wordBlock.append($star);

                        var $edit = $("<span>", {class: "edit"});
                        $edit.append($("<i>", {class: "fa fa-fw fa-pencil"}))
                        $wordBlock.append($edit);

                    }

                    $(".allWords").append($wordBlock);
                }
                comma();
            });
        }
    });
});
