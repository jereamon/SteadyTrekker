document.addEventListener('DOMContentLoaded', function() {
    //#region NAV Section 
    const burger  = document.querySelector(".burger").parentElement,
          nav     = document.querySelector("nav"),
          nav_height = parseInt(nav.offsetHeight),
          nav_els = document.querySelector("nav ul");
    let burger_switch = false;


    burger.addEventListener("click", function() {
        if (!burger_switch) {
            console.log("close menu")
            burger.classList.add('open');
            nav.style.height = (nav_els.children.length * nav_height) + "px";
            burger_switch = true;
        } else {
            console.log("open menu");
            burger.classList.remove('open');
            nav.style.height = nav_height + "px";
            burger_switch = false;
        }
    })
    //#endregion NAV Section


    //#region HOME Section
    const body = document.querySelector("body"),
          body_length = body.children.length;
          body.style.gridTemplateRows = `repeat(${body_length}, ${window.innerHeight - nav_height}px)`;
    // body.style.gridTemplateRows = `repeat(${body_length}, ${window.offsetHeight - nav_height})`;
    //#endregion HOME Section
}, false);