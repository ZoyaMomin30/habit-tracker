document.addEventListener("DOMContentLoaded", function () {
    const drawer = document.getElementById("drawer");
    const overlay = document.getElementById("drawerOverlay");
    const openButton = document.getElementById("openDrawer");
    const closeButtons = document.querySelectorAll(".drawer-close");
    const goalValue = document.getElementById("goal-value"); // Displayed value
    const goalInput = document.getElementById("goal-input"); // Hidden input
    const increaseButton = document.getElementById("increase");
    const decreaseButton = document.getElementById("decrease");

    let goal = 12; // Initial value

    // Function to update button states
    function updateButtons() {
        decreaseButton.disabled = goal <= 0;
        increaseButton.disabled = goal >= 24;
    }

    // Open Drawer
    openButton.addEventListener("click", () => {
        drawer.classList.add("open");
        overlay.classList.add("show");
    });

    // Close Drawer (for all close buttons)
    closeButtons.forEach(button => {
        button.addEventListener("click", () => {
            drawer.classList.remove("open");
            overlay.classList.remove("show");
        });
    });

    // Increase Goal
    increaseButton.addEventListener("click", () => {
        if (goal < 24) {
            goal++;
            goalValue.textContent = goal; // Update display
            goalInput.value = goal; // Update hidden input
            updateButtons();
        }
    });

    // Decrease Goal
    decreaseButton.addEventListener("click", () => {
        if (goal > 0) {
            goal--;
            goalValue.textContent = goal; // Update display
            goalInput.value = goal; // Update hidden input
            updateButtons();
        }
    });

    updateButtons(); // Initialize button states
});
