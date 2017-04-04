$(document).ready(function() {
    comma();
});

function comma() {
    $(".english").each(function () {
        $(this).html($(this).html().replace(/,/g, ", "));
    });
}
