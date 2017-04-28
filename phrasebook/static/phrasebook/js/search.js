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
    const nosearch = $(".allWords").html();

    $('#search').on('keyup', function(e){
        if ($("#search").val() === "") {
            $(".allWords").html(nosearch);
        } else {
            if ($(".editing").length === 0) {
                let parameters;
                if ($("#category")) {
                    parameters = { search: $(this).val(), category: $("#category").val(), short: $("#shortenedLanguage").val()};
                } else {
                    parameters = { search: $(this).val(), short: $("#shortenedLanguage").val()};
                }
                $.post( constantsURL + '../../word/search/', parameters, function(data) {
                    $(".allWords").html("");
                    if (data.length === 0) {
                        $(".allWords").html();
                    } else {
                        $(".allWords").html(data);
                    }
                });
            }
        }
    });
});
