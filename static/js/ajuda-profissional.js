function mandarMensagem(telefone) {
    const numeroLimpo = telefone.replace(/\D/g, '');
    const urlWhatsapp = `https://wa.me/${numeroLimpo}`;
    window.location.href = urlWhatsapp;
}
