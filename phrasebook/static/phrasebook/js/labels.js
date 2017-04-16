var inText = {top: "2.75rem", left: "0.75rem"};
var outText = {top: "0.5rem", left: 0};

function check() {
    $(".login").each(function() {
        if ($(this).val() != "") {
            $(this).parent().children("label").animate(outText, 250);
        } else {
            $(this).parent().children("label").animate(inText, 250);
        }
    })
}

$(document).ready(function() {
    // console.log("test2")

    check();
    $(".login-form").on("change", ".login", check);
    $(".login-form").on("focus", ".login", function() {
        $(this).parent().children("label").animate(outText, 250);
    });

    $(".login-form").on("focusout", ".login", function() {
        if ($(this).val() == "") {
            $(this).parent().children("label").animate(inText, 250);
        }
    });

});
