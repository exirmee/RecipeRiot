// mouse hover glow effect for dark-card
var cards = document.querySelectorAll('.card');
cards.forEach(function(card) {
    card.addEventListener('mouseover', function() {
        this.style.setProperty('box-shadow', 'rgba(255, 255, 255,0.3) 0px 30px 60px -10px', 'important');
        this.style.setProperty('background-color', 'rgb(251 215 125 / 5%)', 'important');

    });
    card.addEventListener('mouseout', function() {
        this.style.removeProperty('background-color');
        this.style.removeProperty('box-shadow');    });
});


