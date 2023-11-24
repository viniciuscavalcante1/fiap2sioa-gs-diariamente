document.addEventListener('DOMContentLoaded', function() {
  const cards = document.querySelectorAll('.card');

  cards.forEach(card => {
    card.addEventListener('click', function() {
      this.querySelector('.card-content').classList.toggle('show');
    });
  });
});
