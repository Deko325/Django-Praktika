const swiper = new Swiper('.header-slider', {
    direction: 'horizontal',
    loop: true,
    simulateTouch: true,
    dragable: true,
  })


  document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("burger").addEventListener("click", function() {
        document.querySelector(".container").classList.toggle("open")
    })
})

window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
      document.querySelector(".container").classList.remove("open")
    }
});

document.getElementById(".container").addEventListener('click', event => {
    event._isClickWithInMenu = true;
});

document.getElementById("burger").addEventListener('click', event => {
    event._isClickWithInMenu = true;
});

document.body.addEventListener('click', event => {
    if (event._isClickWithInMenu) return;

    document.querySelector(".container").classList.remove("open")
});