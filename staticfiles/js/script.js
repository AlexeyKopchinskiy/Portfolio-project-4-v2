console.log("Eat as 4, pay as 3!");

document.addEventListener("DOMContentLoaded", function() {
    // Initialize Summernote (if applicable)
    if (document.querySelector("#summernote")) {
        $("#summernote").summernote();
    }

    // Example: Auto-adjust number of guests based on table size
    const guestsInput = document.querySelector("input[name='num_of_guests']");
    if (guestsInput) {
        guestsInput.addEventListener("input", function() {
            if (this.value < 1) {
                this.value = 1;
            }
        });
    }

    console.log("Booking scripts loaded!");
});