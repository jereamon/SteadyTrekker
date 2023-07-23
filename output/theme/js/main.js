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


    //#region grid gallery
    let galleryImages = document.querySelectorAll(".grid-gallery .grid-gallery-image");
    if (galleryImages.length > 0) {
        let modalDiv = document.querySelector(".modal-div");
        let modalImage = document.querySelector(".modal-image");

        for (let i = 0; i < galleryImages.length; i++) {
            galleryImages[i].addEventListener('click', function () {
                modalDiv.style.display = "flex";
                modalImage.src = galleryImages[i].src;
            })
        }

        modalDiv.addEventListener('click', function() {
            modalDiv.style.display = "none";
        })


    }

    function createModal() {
        let modalDiv = document.createElement("div");
        modalDiv.style.background
    }
    //#endregion grid gallery
}, false);