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

  if (!locationSelect || !tableSelect) {
    console.error("Required dropdown(s) are missing!");
    return;
  }

  // Save original table options.
  const originalTableOptions = Array.from(tableSelect.options).map(opt => ({
    html: opt.innerHTML,
    value: opt.value,
    dataLocation: opt.getAttribute("data-location")
  }));

  locationSelect.addEventListener("change", function () {
    const selectedLocationId = this.value;
    console.log("Location changed to:", selectedLocationId);
    tableSelect.innerHTML = "";

    // Add default option.
    const defaultOption = document.createElement("option");
    defaultOption.value = "";
    defaultOption.innerText = "-- Select a Table --";
    tableSelect.appendChild(defaultOption);

    // Filter and re-add table options.
    originalTableOptions.forEach(opt => {
      if (opt.value === "") return; // Skip default
      if (selectedLocationId === "" || opt.dataLocation === selectedLocationId) {
        const newOption = document.createElement("option");
        newOption.value = opt.value;
        newOption.innerHTML = opt.html;
        newOption.setAttribute("data-location", opt.dataLocation);
        tableSelect.appendChild(newOption);
        console.log("Added table option:", opt.value);
      }
    });

    tableSelect.value = "";
  });
});

// Script to dynamically update table options based on date and time selection
document.addEventListener("DOMContentLoaded", function () {
  const dateInput = document.getElementById("booking_date");
  const timeInput = document.getElementById("booking_time");
  const tableSelect = document.getElementById("table");

  function updateTableOptions() {
    const selectedDate = dateInput.value;
    const selectedTime = timeInput.value;

    if (selectedDate && selectedTime) {
      fetch(`/get-available-tables/?date=${selectedDate}&time=${selectedTime}`)
        .then(response => response.json())
        .then(data => {
          tableSelect.innerHTML = `<option value="">-- Select a Table --</option>`;
          data.available_tables.forEach(table => {
            const option = document.createElement("option");
            option.value = table.id;
            option.textContent = `Table ${table.id} | Seats: ${table.size} | Location: ${table.location}`;
            tableSelect.appendChild(option);
          });
        });
    }
  }

  dateInput.addEventListener("change", updateTableOptions);
  timeInput.addEventListener("change", updateTableOptions);
});