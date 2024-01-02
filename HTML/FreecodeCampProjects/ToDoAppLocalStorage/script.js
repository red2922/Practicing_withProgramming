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

const reset = () => {
    titleInput.value = "";
    dateInput.value = "";
    descriptionInput.value ="";
    taskForm.classList.toggle("hidden");
    currentTask = {};
};

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

    const taskObj = {
        id: `${titleInput.value.toLowerCase().split(' ').join('-')}-${Date.now()}`,
        title: titleInput.value, //These will automatically be in strings so you don't have to string literal them
        date: dateInput.value,
        description: descriptionInput.value,
    };

    if(dataArrIndex === -1){
        taskData.unshift(taskObj);
    }

    taskData.forEach(({id,title,date,description}) => 
        tasksContainer.innerHTML += 
        `<div class="task" id="${id}"></div>
         <p><strong>Title:</strong>${title}</p>
         <p><strong>Date:</strong>${date}</p>
         <p><strong>Description:</strong>${description}</p>
         <button type="button" class="btn">Edit</button>
         <button type="button" class="btn">Delete</button>
        `
    );

    reset();
});




