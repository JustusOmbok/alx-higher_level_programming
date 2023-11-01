$(document).ready(function() {
    // Wait for doc to be raedy
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
        $("#hello").text(data.hello);
    });
});