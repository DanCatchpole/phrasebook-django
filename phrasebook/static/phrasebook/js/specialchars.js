$("body").on('keyup', 'input[type=text]', function(e) {
    let $input = $(this);
    let inVal = $input.val();
    if (inVal.endsWith("aaa")) {
        $input.val(inVal.substr(0, inVal.length - 3) + "å");
    }

    if (inVal.endsWith("AAA")) {
        $input.val(inVal.substr(0, inVal.length - 3) + "Å");
    }
})