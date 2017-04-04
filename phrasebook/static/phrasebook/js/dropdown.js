$(document).ready(function() {
    $(".drop").click(function() {
        if (!$(".sidebar").hasClass("small")) {
            $(".rot").toggleClass("rotate90", "0.2s");
            //$(".dropdown-icon").toggleClass("fa-angle-right");
            $(this).parent().parent().find(".dropdown-elements > li").each(function() {
                if ($(this).hasClass("hidden")) {
                    $(this).slideDown();
                } else {
                    $(this).slideUp();
                }
                $(this).toggleClass("hidden");
                $(this).toggleClass("shown");
            });
        }
    });
});
