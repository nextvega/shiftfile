document.addEventListener("DOMContentLoaded", function() {
    let galeryTools = document.querySelectorAll(".galery__tools__grid__body__list__item") 

    galeryTools.forEach((i, index) => {
        if (index === 0) {
            i.style.setProperty('--pseudo-background-color', `linear-gradient(to top, rgba(0, 0, 0, 0.555), rgba(0, 0, 0, 0)), url("https://images.hipdf.com/images2024/homepage/pic-person-${index+1}.png"`);
        }
        i.addEventListener('click', function(e){
            if (index === 0) {
                galeryTools[0].classList.remove('galery__tools__grid__body__list__item-active');
            }
            galeryTools.forEach(item => {
                item.classList.remove('galery__tools__grid__body__list__item-active');
            });
            i.classList.add('galery__tools__grid__body__list__item-active');
            i.style.setProperty('--pseudo-background-color', `linear-gradient(to top, rgba(0, 0, 0, 0.555), rgba(0, 0, 0, 0)), url("https://images.hipdf.com/images2024/homepage/pic-person-${index+1}.png"`);
        })
    })

});
