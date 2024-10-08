function mostrarMensagemEstranha() {
    const mensagens = [
        "Você clicou e nada aconteceu, parabéns!",
        "Um pato aparece do nada e nada acontece... ainda.",
        "O pato agora voa!",
        "Agora não voa mais rs!",
        "ERROR 4004 ou algo parecido"
    ];
    alert(mensagens[Math.floor(Math.random() * mensagens.length)]);
}

document.querySelectorAll('.action-button').forEach(button => {
    button.addEventListener('click', () => {
        const novaMensagem = document.createElement('p');
        novaMensagem.textContent = `Mais um Bug ${new Date().toLocaleTimeString()}`;
        document.body.appendChild(novaMensagem);
    });
});
