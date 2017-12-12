$(document).ready(function() {
    $(".allWords").on('click', ".wordBlock .move i.fa-long-arrow-right", function() {
        console.log("CLICKED");
        $modal = $("<div>", {"class": "language-picker", "style": "display: flex;"});
        $.post("/phrasebook/category/all/", {
            "word_id": $(this).parent().parent().children(".word_id").val()
        }, function(data) {
            $modal.html(data);
            $("body").prepend($modal);
            $modal.animate({"opacity": 1})
        });
    });
});