console.log("Eat as 4, pay as 3!");

document.addEventListener("DOMContentLoaded", function () {
  // Initialize Summernote (if applicable)
  if (document.querySelector("#summernote")) {
    $("#summernote").summernote();
  }

  // Example: Auto-adjust number of guests based on table size
  const guestsInput = document.querySelector("input[name='num_of_guests']");
  if (guestsInput) {
    guestsInput.addEventListener("input", function () {
      if (this.value < 1) {
        this.value = 1;
      }
    });
  }

  console.log("Booking scripts loaded!");
});

document.addEventListener("DOMContentLoaded", function () {
  console.log("Booking page script loaded.");

  const locationSelect = document.getElementById("location");
  const tableSelect = document.getElementById("table");

  // Save original table options.
  const originalTableOptions = Array.from(tableSelect.options).map(opt => ({
    html: opt.innerHTML,
    value: opt.value,
    dataLocation: opt.getAttribute("data-location")
  }));

});

// Script to dynamically update table options based on date and time selection
document.addEventListener("DOMContentLoaded", function () {
  const dateInput = document.getElementById("booking_date");
  const timeInput = document.getElementById("booking_time");
  const guestCountInput = document.getElementById("num_of_guests");
  const tableSelect = document.getElementById("table");

  // ✅ Disable guest count field initially
  guestCountInput.disabled = true;

  function updateTableOptions() {
    const selectedDate = dateInput.value;
    const selectedTime = timeInput.value;
    const selectedGuests = parseInt(guestCountInput.value, 10) || 0;

    // ✅ Enable guest count field only if date & time are selected
    guestCountInput.disabled = !selectedDate || !selectedTime;

    // ✅ Prevent request if date or time is missing
    if (!selectedDate || !selectedTime) {
      console.warn("Date and time must be selected before filtering tables.");
      return;
    }

    fetch(`/booking/get-available-tables/?date=${selectedDate}&time=${selectedTime}`)
      .then(response => response.json())
      .then(data => {
        console.log("Available tables:", data.available_tables);

        // ✅ Clear existing options
        tableSelect.innerHTML = `<option value="">-- Select a Table --</option>`;

        // ✅ Filter tables based on guest count
        const filteredTables = data.available_tables.filter(table => selectedGuests <= table.size);

        if (filteredTables.length === 0) {
          console.warn("No tables available for this guest count");
          tableSelect.innerHTML = `<option value="">No available tables</option>`;
        } else {
          filteredTables.forEach(table => {
            const option = document.createElement("option");
            option.value = table.id;
            option.textContent = `Table ${table.id} | Seats: ${table.size} | Location: ${table.location}`;
            tableSelect.appendChild(option);
          });
        }
      })
      .catch(error => console.error("Error fetching tables:", error));
  }

  // ✅ Update tables when date, time, or guest count changes
  dateInput.addEventListener("change", updateTableOptions);
  timeInput.addEventListener("change", updateTableOptions);
  guestCountInput.addEventListener("change", updateTableOptions);
});