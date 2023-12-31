const textInput = document.getElementById("text-input");
const checkButton = document.getElementById("check-btn");
const output = document.getElementById("result");

const isLengthOne = () =>{
    if(textInput.value.length === 1){
        output.textContent = `${textInput.value} is a Palindrome`;
    } 
};

const isPalindrome = () =>{
    const word = textInput.value.toLowerCase();
    const new_Word = word.replace(/[^0-9a-z]/gi, '');
    const back_Word = [];


    for(let i = 0; i <= new_Word.length; i++){
        back_Word.push(new_Word[new_Word.length - i]);
    }
    back_Word.shift();
    const stringBack_Word = back_Word.join("");
    console.log(stringBack_Word);
    console.log(new_Word);
    return new_Word == stringBack_Word;
};


checkButton.addEventListener("click", () =>{
    if(textInput.value.length === 0){
        alert("Please input a value");
    } else {
        isLengthOne();

        if(isPalindrome()){
            output.textContent = `${textInput.value} is a Palindrome`;
        } else {
            output.textContent = `${textInput.value} is not a Palindrome`;
        }
    }
});