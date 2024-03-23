// let sidebar = document.querySelector(".sidebar");
// let toggler = document.querySelector(".toggler");

// toggler.addEventListener("click", function () {
//   this.classList.toggle("open");
//   sidebar.classList.toggle("open");
// });

let instruct1 = document.querySelector(".instruction-1");
let instruct2 = document.querySelector(".instruction-2");

function display1() {
  instruct1.classList.remove("none");
  instruct1.classList.add("instruction-1");
  setTimeout(() => {
    instruct1.classList.remove("instruction-1");

    instruct1.classList.add("none");
  }, 3000);
}
function display2() {
  instruct2.classList.remove("none");
  instruct2.classList.add("instruction-2");
  setTimeout(() => {
    instruct2.classList.remove("instruction-2");

    instruct2.classList.add("none");
  }, 3000);
}

// let navtoggle=document.querySelector('.nav-toggle');
// let sidebar=document.querySelector('.sidebar');

// navtoggle.addEventListener("click",function(){
//     if(navtoggle.firstElementChild.classList.contains('fa-bars')){
//         navtoggle.firstElementChild.classList.replace("fa-bars","fa-times");
//     }
//     else{
//         navtoggle.firstElementChild.classList.replace("fa-times","fa-bars");

//     }
//     sidebar.classList.toggle('sidebar_open');

// })

let sidebar = document.querySelector(".sidebar");
let btn = document.querySelector("#btn");

let searchBtn = document.querySelector("fa-plus ");

function openSideBar() {
  sidebar.classList.toggle("active");
}

// function show(){
//     let msg=document.querySelector('.tooltip');
//     msg.classList.remove('none');
//     msg.classList.add('tooltip-pro');
// }
// function removeShow(){
//     let msg=document.querySelector('.tooltip');
//     msg.classList.remove('tooltip-pro');
//     msg.classList.add('none');

// }
