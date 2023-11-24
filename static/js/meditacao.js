document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('iniciarMeditacao').addEventListener('click', function () {
        var duracaoSelecionada = parseInt(document.getElementById('duracao').value);
        var somChuva = document.getElementById('somChuva');
        var contador = document.getElementById('contador');
        var tempoRestante = duracaoSelecionada;

        document.getElementById('iniciarMeditacao').disabled = true;

        somChuva.play();

        var intervalo = setInterval(function () {
            var minutos = Math.floor(tempoRestante / 60);
            var segundos = tempoRestante % 60;

            contador.textContent = minutos + 'm ' + segundos + 's';

            if (tempoRestante <= 0) {
                clearInterval(intervalo);
                contador.textContent = 'Meditação Concluída';
                somChuva.pause();
                document.getElementById('iniciarMeditacao').disabled = false;
            } else {
                tempoRestante--;
            }
        }, 1000);
    });
});