//Já que o input-submit fica acima da image, não tem como adicionar o hover nela pelo css. Precisa de js.

var search_icon__box = document.querySelector(".search-icon__box");
var search_icon = document.querySelector(".search-icon")

search_icon__box.addEventListener("mouseover", function () {
    search_icon.style.width = "31px";
    search_icon.style.height = "31px";
})

search_icon__box.addEventListener("mouseout", function () {
    search_icon.style.width = "32px";
    search_icon.style.height = "32px";
})

//add preventDefault ao formulário
/* var form = document.querySelector(".search-box__form");
form.addEventListener("submit", () => { event.preventDefault() }) */