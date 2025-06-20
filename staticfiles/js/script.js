/* jshint esversion: 6 */
/* global $ */

document.addEventListener("DOMContentLoaded", function () {
  // Initialize Summernote (if applicable)
  if (document.querySelector("#summernote")) {
    $("#summernote").summernote({
      placeholder: "Enter any special requests or notes here...",
      tabsize: 2,
      height: 200,
      toolbar: [
        ["style", ["bold", "italic", "underline", "clear"]],
        ["font", ["strikethrough", "superscript", "subscript"]],
        ["fontsize", ["fontsize"]],
        ["color", ["color"]],
        ["para", ["ul", "ol", "paragraph"]],
        ["height", ["height"]]
      ]
    });
  }

  // toggle navbar on small screens
  document.addEventListener("click", function (event) {
    let navbar = document.querySelector(".navbar-collapse");  // ✅ Selects the Bootstrap collapse menu
    let toggleButton = document.querySelector(".navbar-toggler");  // ✅ Menu button

    // Check if the click is outside the navbar and toggle button
    if (!navbar.contains(event.target) && !toggleButton.contains(event.target)) {
      navbar.classList.remove("show");  // ✅ Closes the menu
    }
  });

  // Auto-adjust number of guests based on table size
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

/*** 
  * Script to handle location and table selection on the booking page
  * This script dynamically updates the table options based on the selected location
*/
document.addEventListener("DOMContentLoaded", function () {
  console.log("Booking page script loaded.");

  // const locationSelect = document.getElementById("location");
  const tableSelect = document.getElementById("table");

  if (tableSelect) {
    const originalTableOptions = Array.from(tableSelect.options).map(opt => ({
      html: opt.innerHTML,
      value: opt.value,
      dataLocation: opt.getAttribute("data-location")
    }));

    // You can store this globally if needed
    window.originalTableOptions = originalTableOptions;
  } else {
    console.warn("⚠️ Could not find element with ID 'table'. Skipping table logic.");
  }
});

// Script to dynamically update table options based on date and time selection
document.addEventListener("DOMContentLoaded", function () {
  const dateInput = document.getElementById("booking_date");
  const timeInput = document.getElementById("booking_time");
  const guestCountInput = document.getElementById("num_of_guests");
  const smokingCheckbox = document.getElementById("smoking");
  const accessibleCheckbox = document.getElementById("accessible");
  const tableSelect = document.getElementById("table");

  if (!guestCountInput) {
    console.warn("guestCountInput not found on this page. Skipping script.");
    return;
  }

  // ✅ Disable guest count, smoking, and accessible checkboxes initially
  guestCountInput.disabled = true;
  smokingCheckbox.disabled = true;
  accessibleCheckbox.disabled = true;

  /**
  * Updates available table options based on selected date, time, guest count,
  * smoking preference, and accessibility preference.
  */
  function updateTableOptions() {
    const selectedDate = dateInput.value;
    const selectedTime = timeInput.value;
    const selectedGuests = parseInt(guestCountInput.value, 10) || 0;
    const smokingOnly = smokingCheckbox.checked;
    const accessibleOnly = accessibleCheckbox.checked;

    // ✅ Enable filters only if date & time are selected
    const enableFilters = selectedDate && selectedTime;
    guestCountInput.disabled = !enableFilters;
    smokingCheckbox.disabled = !enableFilters;
    accessibleCheckbox.disabled = !enableFilters;

    // ✅ Prevent request if date or time is missing
    if (!enableFilters) {
      console.warn("Date and time must be selected before filtering tables.");
      return;
    }

    /**
     * Fetches available tables from the server based on selected date and time.
     * Filters tables further based on guest count, smoking preference, and accessibility.
     */
    fetch(`/booking/get-available-tables/?date=${selectedDate}&time=${selectedTime}`)
      .then(response => response.json())
      .then(data => {
        console.log("Available tables:", data.available_tables);

        // ✅ Clear existing options
        tableSelect.innerHTML = `<option value="">-- Select a Table --</option>`;

        // ✅ Filter tables based on guest count, smoking, and accessibility
        const filteredTables = data.available_tables.filter(table => {
          const fitsGuests = selectedGuests <= table.size;
          const fitsSmoking = !smokingOnly || table.smoking === true;
          const fitsAccessible = !accessibleOnly || table.accessible === true;
          return fitsGuests && fitsSmoking && fitsAccessible;
        });

        if (filteredTables.length === 0) {
          console.warn("No tables available for the selected criteria");
          tableSelect.innerHTML = `<option value="">No available tables</option>`;
        } else {
          filteredTables.forEach(table => {
            const option = document.createElement("option");
            option.value = table.id;
            option.textContent = `Table ${table.id} | Seats: ${table.size} | Location: ${table.location}` +
              (table.smoking ? " | Smoking" : "") +
              (table.accessible ? " | Accessible" : "");
            tableSelect.appendChild(option);
          });
        }
      })
      .catch(error => console.error("Error fetching tables:", error));
  }

  // ✅ Update tables when date, time, guest count, smoking, or accessibility changes
  dateInput.addEventListener("change", updateTableOptions);
  timeInput.addEventListener("change", updateTableOptions);
  guestCountInput.addEventListener("change", updateTableOptions);
  smokingCheckbox.addEventListener("change", updateTableOptions);
  accessibleCheckbox.addEventListener("change", updateTableOptions);
});