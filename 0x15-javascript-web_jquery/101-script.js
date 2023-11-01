$(document).ready(function() {
    // Waits for doc to load
    $("#add_item").click(function() {
        const newItem = $("<li>Item</li>");
        $("ul.my_list").append(newItem);
    });

    // Removing last item from list
    $("#remove_item").click(function() {
        const list = $("ul.my_list");
        const lastItem = list.find("li:last");
        if (lastItem.length > 0) {
            lastItem.remove();
        }
    });

    //Clearing all items
    $("#clear_list").click(function() {
        $("ul.my_list").empty();
    });
});