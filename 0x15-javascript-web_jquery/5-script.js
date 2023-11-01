$(document).ready(function() {
    // Waits for doc to be ready
    $("#add_item").click(function() {
        const newItem = $("<li>Item</>");
        $("ul.my_list").append(newItem);
    });
});
