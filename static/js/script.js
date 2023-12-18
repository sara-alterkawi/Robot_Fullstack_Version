document.addEventListener("DOMContentLoaded", function () {
  const selectedCharsContainer = document.getElementById("selectedChars");
  const removeCharBtn = document.getElementById("removeCharBtn");
  const placeOrderBtn = document.getElementById("placeOrderBtn");
  let selectedChars = [];

  document.querySelectorAll(".product-option").forEach(function (option) {
    option.addEventListener("click", function () {
      const char = option.getAttribute("data-char");
      if (selectedChars.length < 4) {
        selectedChars.push(char);
        updateSelectedCharsDisplay();
        updatePlaceOrderButton();
      }
    });
  });

  removeCharBtn.addEventListener("click", function () {
    if (selectedChars.length > 0) {
      selectedChars.pop();
      updateSelectedCharsDisplay();
      updatePlaceOrderButton();
    }
  });

  function updateSelectedCharsDisplay() {
    selectedCharsContainer.textContent = selectedChars.join(" ");
    toggleOptionAvailability(selectedChars.length < 4);
  }

  function toggleOptionAvailability(enable) {
    document.querySelectorAll(".product-option").forEach(function (option) {
      option.style.pointerEvents = enable ? "auto" : "none";
      option.style.opacity = enable ? "1" : "0.5";
    });
  }

  function updatePlaceOrderButton() {
    if (selectedChars.length > 0) {
      placeOrderBtn.disabled = false;
    } else {
      placeOrderBtn.disabled = true;
    }
  }
});
