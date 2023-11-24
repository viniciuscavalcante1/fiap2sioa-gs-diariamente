document.addEventListener('DOMContentLoaded', function () {
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('click', function () {
            this.querySelector('.card-content').classList.toggle('show');
        });
    });
});

function copiar(titulo, humor, conteudo, momentoFeliz, timestamp) {
    var copyText = `
Título: ${titulo}
Humor: ${humor}
Conteúdo: ${conteudo}
Momento Feliz: ${momentoFeliz}
Timestamp: ${timestamp}`;

    var textarea = document.createElement('textarea');
    textarea.value = copyText;
    document.body.appendChild(textarea);

    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);

    var dados = document.getElementById('dadosCopiados');
    dados.style.display = 'block';

    setTimeout(function () {
        dados.style.display = 'none';
    }, 2000);
}

function redirecionarParaDiario(email) {
    window.location.href = "/diario?email=" + email;
}