// input(type="submit", value="Save").button.button-save

$(document).ready(function() {
    $(".language-block").click(function(event) {
        $(".language-selected").removeClass("language-selected");
        $(this).addClass("language-selected");
        var $submit = $("<input>", {type: "submit", value:"Save", class: "button button-save"});
        $(".button-save").remove();
        $(".submit-section").append($submit);
        console.log($(".hidden", this).html());
        $(".langVal").val($(".hidden", this).html());
    });
});
