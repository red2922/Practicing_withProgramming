const taskForm = document.getElementById("task-form");
const confirmCloseDialog = document.getElementById("confirm-close-dialog");
const openTaskFormBtn = document.getElementById("open-task-form-btn");
const closeTaskFormBtn = document.getElementById("close-task-form-btn");
const addOrUpdateTaskBtn = document.getElementById("add-or-update-task-btn");
const cancelBtn = document.getElementById("cancel-btn");
const discardBtn = document.getElementById("discard-btn");
const tasksContainer = document.getElementById("tasks-container");
const titleInput = document.getElementById("title-input");
const dateInput = document.getElementById("date-input");
const descriptionInput = document.getElementById("description-input");

//Allow to save them to local storage
const taskData = [];

//track state when editing tasks
let currentTask = {};

openTaskFormBtn.addEventListener("click",() => taskForm.classList.toggle("hidden"));
closeTaskFormBtn.addEventListener("click",() => confirmCloseDialog.showModal());
cancelBtn.addEventListener("click", () => confirmCloseDialog.close());

discardBtn.addEventListener("click", () => {
    confirmCloseDialog.close();
    taskForm.classList.toggle("hidden");
});

taskForm.addEventListener("submit", (e) =>{
    e.preventDefault();
    const dataArrIndex = taskData.findIndex((item) => item.id === currentTask.id);
});

const taskObj ={
    id: `${titleInput.value.toLowerCase().split(' ').join('-')}-${Date.now()}`,
    title: titleInput.value, //These will automatically be in strings so you don't have to string literal them
    date: dateInput.value,
    description: descriptionInput.value,
}