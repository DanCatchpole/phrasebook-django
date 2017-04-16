// input(type="submit", value="Save").button.button-save

$(document).ready(function() {
    $(".language-block").click(function(event) {
        if ($(this).hasClass("language-selected")) {
            // is the selected one
            $(this).removeClass("language-selected");
            $(".button-save").prop('disabled', true);
            $(".langVal").val("");
        } else {
            // not the selected one
            $(".language-selected").removeClass("language-selected");
            $(this).addClass("language-selected");
            $(".button-save").prop('disabled', false);
            $(".langVal").val($(".hidden", this).html());
        }
    });
});
