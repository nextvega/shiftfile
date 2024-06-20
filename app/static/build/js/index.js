console.log('Ejecutando..');


document.addEventListener("DOMContentLoaded", function() {
    // var featuredTools = document.querySelector(".featured__tools__grid");
    // featuredTools.addEventListener("scroll", function() {
    //     // Centrar el elemento en la pantalla
    //     featuredTools.scrollIntoView({ block: 'center', behavior: 'smooth' });
    // });

    // window.addEventListener("scroll", function() {
    //     isScrolling = true;
    //     setTimeout(function() {
    //         isScrolling = false;
    //     }, 100);
    // });

    let galeryTools = document.querySelectorAll(".galery__tools__grid__body__list__item") 

    galeryTools.forEach((i, index) => {
        if (index === 1) {
            i.style.setProperty('--pseudo-background-color', `linear-gradient(to top, rgba(0, 0, 0, 0.555), rgba(0, 0, 0, 0)), url("https://images.hipdf.com/images2024/homepage/pic-person-${index+1}.png"`);
        }
        i.addEventListener('click', function(e){

            if (index === 1) {
                galeryTools[1].classList.remove('galery__tools__grid__body__list__item-active');
            }

            galeryTools.forEach(item => {
                item.classList.remove('galery__tools__grid__body__list__item-active');
            });

            
            i.classList.add('galery__tools__grid__body__list__item-active');
            i.style.setProperty('--pseudo-background-color', `linear-gradient(to top, rgba(0, 0, 0, 0.555), rgba(0, 0, 0, 0)), url("https://images.hipdf.com/images2024/homepage/pic-person-${index+1}.png"`);
        })
    })
});
