var toogle = document.querySelector(".toogle");
var sideView_navbar = document.querySelector(".sideview-navbar__container");

//animation toogle menu: 
toogle.addEventListener("click", function() {
    let traces = document.querySelectorAll(".trace"); 

    if(sideView_navbar.style.display=="none") {
        traces[0].style.position = 'absolute';
        traces[2].style.position = 'absolute';
        traces[0].style.transform = 'rotate(45deg)';
        traces[2].style.transform= 'rotate(-45deg)';

        traces[1].style.transform = 'translate(-100px)';
        traces[1].style.opacity = '0';
    } else {
        traces[0].style.position = 'static';
        traces[2].style.position = 'static';
        traces[0].style.transform = 'rotate(0)';
        traces[2].style.transform= 'rotate(0)';

        traces[1].style.transform = 'translate(0px)'
        traces[1].style.opacity = '1';
    }
})

//open sidebar:
toogle.addEventListener('click', toogleSideViewNavbar)

function toogleSideViewNavbar() {
    if (sideView_navbar.style.display == 'none') {
        sideView_navbar.style.display='flex';
    } else {
        sideView_navbar.style.display='none';
    }
}