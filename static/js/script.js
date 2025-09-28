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
});

/*** 
  * Script to handle location and table selection on the booking page
  * This script dynamically updates the table options based on the selected location
*/
document.addEventListener("DOMContentLoaded", function () {
  if (!document.body.classList.contains("booking-context")) return;

  const locationSelect = document.getElementById("location");
  const tableSelect = document.getElementById("id_table");

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
  // Only run on pages with booking context
  if (!document.body.classList.contains("booking-context")) return;

  const dateInput = document.getElementById("id_booking_date");
  const timeInput = document.getElementById("id_booking_time");
  const guestCountInput = document.getElementById("id_num_of_guests");
  const smokingCheckbox = document.getElementById("smoking");
  const accessibleCheckbox = document.getElementById("accessible");
  const tableSelect = document.getElementById("id_table");

  // ✅ Early exit if critical elements are missing
  if (!dateInput || !timeInput || !guestCountInput || !tableSelect) {
    console.warn("⚠️ Booking form elements missing. Skipping table filtering logic.");
    return;
  }

  // ✅ Disable filters initially
  guestCountInput.disabled = true;
  if (smokingCheckbox) smokingCheckbox.disabled = true;
  if (accessibleCheckbox) accessibleCheckbox.disabled = true;

  /**
   * Updates available table options based on selected date, time, guest count,
   * smoking preference, and accessibility preference.
   */
  function updateTableOptions() {
    const selectedDate = dateInput?.value || "";
    const selectedTime = timeInput?.value?.slice(0, 5) || "";
    const selectedGuests = parseInt(guestCountInput?.value || "0", 10);
    const smokingOnly = smokingCheckbox?.checked || false;
    const accessibleOnly = accessibleCheckbox?.checked || false;

    const enableFilters = selectedDate !== "" && selectedTime !== "";

    guestCountInput.disabled = !enableFilters;
    if (smokingCheckbox) smokingCheckbox.disabled = !enableFilters;
    if (accessibleCheckbox) accessibleCheckbox.disabled = !enableFilters;

    if (!enableFilters) {
      console.warn("⏳ Date and time must be selected before filtering tables.");
      return;
    }

    fetch(`/booking/get-available-tables/?date=${selectedDate}&time=${selectedTime}`)
      .then(response => {
        if (!response.ok) {
          throw new Error(`Server responded with ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        if (!data.available_tables) {
          console.warn("⚠️ No available_tables in response:", data);
          tableSelect.innerHTML = `<option value="">No available tables</option>`;
          return;
        }

        console.log("✅ Available tables:", data.available_tables);

        // Clear and repopulate
        tableSelect.innerHTML = `<option value="">-- Select a Table --</option>`;
        const filteredTables = data.available_tables.filter(table => {
          const fitsGuests = selectedGuests <= table.size;
          const fitsSmoking = !smokingOnly || table.smoking === true;
          const fitsAccessible = !accessibleOnly || table.accessible === true;
          return fitsGuests && fitsSmoking && fitsAccessible;
        });

        if (filteredTables.length === 0) {
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
      .catch(error => {
        console.error("❌ Error fetching tables:", error);
        tableSelect.innerHTML = `<option value="">Error loading tables</option>`;
      });
  }

  // ✅ Attach listeners
  dateInput.addEventListener("change", updateTableOptions);
  timeInput.addEventListener("change", updateTableOptions);
  guestCountInput.addEventListener("change", updateTableOptions);
  if (smokingCheckbox) smokingCheckbox.addEventListener("change", updateTableOptions);
  if (accessibleCheckbox) accessibleCheckbox.addEventListener("change", updateTableOptions);

});