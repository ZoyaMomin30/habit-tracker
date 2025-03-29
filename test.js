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