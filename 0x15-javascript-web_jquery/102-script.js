$(document).ready(function() {
    // Wait for document to be ready

    $("#btn_translate").click(function() {
        const languageCode = $("#language_code").val();
        // Tetching data
        $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
            const translation = data.hello;
            $("#hello").text(translation);
        });
    });
});
