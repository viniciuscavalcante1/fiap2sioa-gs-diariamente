function selecionarHumor(valor) {
    document.getElementById("humor").value = valor;
    document.querySelectorAll('.humor-buttons button').forEach(btn => {
        btn.style.backgroundColor = btn.innerText.includes(valor) ? '#3fbc9b' : '#c3e6d9'; // Muda a cor para verde se o botão corresponder ao valor selecionado
        btn.style.color = btn.innerText.includes(valor) ? '#fff' : '#40be9c'; // Muda a cor do texto para branco se o botão estiver selecionado
    });
}

function redirecionarParaEntradasAnteriores(email) {
    window.location.href = "/diario/entradas?email=" + email;
}