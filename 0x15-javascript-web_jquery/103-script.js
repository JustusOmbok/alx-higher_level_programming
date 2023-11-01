$(document).ready(function() {
    // Waits for doc to load
    function fetchTranslation() {
        const languageCode = $("#language_code").val();

        $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(code) {
            const translation = data.hello;
            $("#hello").text(translation);
        });
    }

    // Adds a click event
    $("#btn_translate").click(function() {
        fetchTranslation();
    });

    // Adds an event listener
    $("#language_code").keypress(function(event) {
      if (event.which == 13) {
        fetchTranslation();
      }  
    });
});
