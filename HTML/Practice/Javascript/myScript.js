const hamBurger = document.getElementsByClassName("back");
const nav = document.getElementsByClassName("nav-bar");
const menu = document.getElementsByClassName("ham");

hamBurger[0].addEventListener("click", () => {
  nav[0].classList.toggle("active");
  menu[0].classList.toggle("active");
});

menu[0].addEventListener("click", () => {
  nav[0].classList.toggle("active");
  menu[0].classList.toggle("active");
});
