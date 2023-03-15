const body = document.getElementById("body");
const popUp = document.getElementById("popUp");
const popUpBtn = document.getElementById("popUpBtn");

var firstTime = localStorage.getItem("first_time");

popUpBtn.addEventListener("click", closed);

if (!firstTime) {
  console.log("h")
  localStorage.setItem("first_time", "1");
  body.classList.add("closed");
  popUp.classList.remove("closed");
} else{
  popUp.classList.add("closed");
  body.classList.remove("closed");
}

function closed() {
  popUp.classList.add("closed");
  body.classList.remove("closed");
}
