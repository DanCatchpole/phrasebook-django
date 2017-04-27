$("body").on('keyup', 'input[type=text]', function(e) {
    let $input = $(this);
    let inVal = $input.val();
    if (inVal.endsWith("aa")) {
        $input.val(inVal.substr(0, inVal.length - 2) + "å");
    }

    if (inVal.endsWith("AA")) {
        $input.val(inVal.substr(0, inVal.length - 2) + "Å");
    }
})