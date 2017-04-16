$(document).ready(function() {
    $(".shrink").click(function() {
        if($('.sidebar').hasClass("small")) {
            $('.sidebar').animate({"width": 20*16 + ""}, 300, "swing");
            $.get( '/phrasebook/app/sidebar', { sidebar: "big" }, function(data) {

            });
            $(".sidebar span:not(.counter)").animate({"opacity": "1"}, 200);
            $('.sidebar').removeClass("small", "swing");
        } else {
            $(".sidebar span:not(.counter)").animate({"opacity": "0"}, 10, function () {

            });
            $('.sidebar').animate({"width": "130px"}, 200, "swing", function() {
                $(".sidebar").addClass("small", "swing");
            });
            $(".dropdown-elements > li").each(function () {
                if (!$(this).hasClass("hidden")) {
                    $(this).slideUp();
                }
            });
            $.get( '/phrasebook/app/sidebar', { sidebar: "small" }, function(data) {

            });
        }
        // $(".hideBar").toggleClass('rot-180');
    });

    $(".userSection .flag").click(function(event) {
        $("div.language-picker").css({'display': "flex"});
        $("div.language-picker").animate({"opacity": 1});
        event.stopPropagation();
    });

    $("#language-change-link").click(function(event) {
        $("div.language-picker").css({'display': "flex"});
        $("div.language-picker").animate({"opacity": 1});
    });
    $(".language-picker div.container").click(function(event) {
        event.stopPropagation();
    });


    $(".language-picker").click(function(event) {
        $("div.language-picker").animate({"opacity": 0}, function() {
            $("div.language-picker").css({'display': "none"});

        });
    })

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
