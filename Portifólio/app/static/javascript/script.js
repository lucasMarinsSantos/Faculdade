document.addEventListener("DOMContentLoaded", () => {
    const playpause = document.querySelector(".playpause");
    const audio = document.getElementById("musicafundo");
    const volume = document.getElementById("volume");
    const icon = playpause.querySelector("i");
    const audioNavegacao = document.getElementById("audioNavegacao");
    const ovopascoaButton = document.querySelector(".ovopascoa button"); // Corrigido para selecionar o botão corretamente
    const ovopascoaAudio = document.getElementById('ovopascoaud');
    const buttons = document.querySelectorAll(".button");
    let selectedButtonIndex = 0;
    let isNavigatingWithKeyboard = false;

    if (buttons.length > 0) {
        buttons[0].classList.add("selected");
    }

    playpause.addEventListener("click", () => {
        if (audio.paused) {
            audio.play();
            icon.classList.remove("fa-play");
            icon.classList.add("fa-pause");
        } else {
            audio.pause();
            icon.classList.remove("fa-pause");
            icon.classList.add("fa-play");
        }
    });

    volume.addEventListener("input", () => {
        audio.volume = volume.value;
    });

    function removeSelectedClass() {
        buttons.forEach(button => button.classList.remove("selected"));
    }

    function selectButton(index) {
        removeSelectedClass();
        buttons[index].classList.add("selected");
        buttons[index].focus();
        audioNavegacao.currentTime = 0;
        audioNavegacao.play();
    }

    document.addEventListener("keydown", event => {
        isNavigatingWithKeyboard = true;
        if (event.key === "ArrowDown" || event.key === "ArrowRight") {
            selectedButtonIndex = (selectedButtonIndex + 1) % buttons.length;
            selectButton(selectedButtonIndex);
        } else if (event.key === "ArrowUp" || event.key === "ArrowLeft") {
            selectedButtonIndex = (selectedButtonIndex - 1 + buttons.length) % buttons.length;
            selectButton(selectedButtonIndex);
        }
    });

    buttons.forEach((button, index) => {
        button.addEventListener("mouseover", () => {
            if (!isNavigatingWithKeyboard) {
                selectedButtonIndex = index;
                selectButton(selectedButtonIndex);
            }
        });

        button.addEventListener("mouseleave", () => {
            isNavigatingWithKeyboard = false;
        });

        button.addEventListener("click", () => {
            redirectTo(button.textContent.trim().toLowerCase() + '.html');
        });
    });

    ovopascoaButton.addEventListener("click", () => {
        ovopascoaAudio.currentTime = 0;
        ovopascoaAudio.play();
    });

    function redirectTo(page) {
        console.log("Redirecionando para: " + page);
        window.location.href = 'loading.html?page=' + encodeURIComponent(page);
    }
});
