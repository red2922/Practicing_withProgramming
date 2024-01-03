const numberInput = document.getElementById("number-input");
const convertBtn = document.getElementById("convert-btn");
const result = document.getElementById("result");

const a = () => "freeCodeCamp " + b();



const decimalToBinary = (input) => {
    //Not recursive but still infinitly better than the one under it 
    let binary = "";

    if(input === 0){
        binary = "0";
      }
    

    while(input > 0){
    
        binary = (input % 2) + binary;
        input = Math.floor(input / 2);
    }

    result.innerText = binary;


    /* Non-recursive approach
    const inputs = [];
    const quotients = [];
    const remainders = [];

    if(input === 0){
        result.innerText = "0";
        return;
    }

    while(input > 0){
        const quotient = Math.floor(input / 2);
        const remainder = input % 2;
        inputs.push(input);
        quotients.push(quotient);
        remainders.push(remainder);
        

        input = quotient;
    }

    console.log("Inputs: ",inputs); to have multiple things you need commas instead of + in Javascript
    console.log("Quotients: ", quotients);
    console.log("Remainders: ", remainders);
    
    result.innerText = remainders.reverse().join("");
    */
};






const checkUserInput = () => {
    if(!numberInput.value || isNaN(parseInt(numberInput.value))){
        alert("Please provide a decimal number");
        return;
    }

    decimalToBinary(parseInt(numberInput.value));
    numberInput.value = "";
};

convertBtn.addEventListener("click", checkUserInput);

numberInput.addEventListener("keydown", (e) => {
    if(e.key === "Enter"){
        checkUserInput();
    }
});