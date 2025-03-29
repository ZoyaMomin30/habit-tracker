
const drawer = document.getElementById("drawer");
const openButton = document.getElementById("openDrawer");
const closeButton = document.getElementById("closeDrawer");
const goalValue = document.getElementById("goalValue");
const increaseButton = document.getElementById("increase");
const decreaseButton = document.getElementById("decrease");
let goal = 12;

openButton.addEventListener("click", () => {
    drawer.classList.add("open");
});

closeButton.addEventListener("click", () => {
    drawer.classList.remove("open");
});

function updateButtons() {
    decreaseButton.disabled = goal <= 0;
    increaseButton.disabled = goal >= 24;
}

increaseButton.addEventListener("click", () => {
    if (goal < 24) {
        goal++;
        goalValue.textContent = goal;
        updateButtons();
    }
});

decreaseButton.addEventListener("click", () => {
    if (goal > 0) {
        goal--;
        goalValue.textContent = goal;
        updateButtons();
    }
});

updateButtons();

// MODAL
document.getElementById("habitForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevents page reload
    let habitName = document.getElementById("habitName").value;
    let graphName = document.getElementById("graphName").value;
    let quantity = document.getElementById("quantity").value;
    
    console.log("Habit Created:", { habitName, graphName, quantity });
    
    // Close modal
    var habitModal = new bootstrap.Modal(document.getElementById('habitModal'));
    habitModal.hide();
});