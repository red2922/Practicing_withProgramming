const number = document.getElementById("number");
const convert_btn = document.getElementById("convert-btn");
const output = document.getElementById("output");


const checkInput = () =>
{
    if(number.value === ""){
        output.innerText ="Please enter a valid number";
    }

    else if(number.value === "-1"){
        output.innerText = "Please enter a number greater than or equal to 1"
    }

    else if(number.value >= 4000){
        output.innerText = "Please enter a number less than or equal to 3999"
    }
};



convert_btn.addEventListener("click", checkInput);