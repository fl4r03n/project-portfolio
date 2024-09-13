function toggleResume() {
    // Seleccionamos todos los elementos con la clase 'extra-resume'
    var extraResume = document.querySelectorAll('.extra-resume');
    var buttonEdu = document.getElementById('show-more-btn-edu');
    var buttonExp = document.getElementById('show-more-btn-exp');

    // Alternamos la clase 'd-none' para mostrar/ocultar
    extraResume.forEach(function(item) {
        item.classList.toggle('d-none');
    });

    // Cambiamos el texto del botón según el estado
    if (buttonExp.innerText === "Más...") {
        buttonExp.innerText = "Mostrar menos";
    } else {
        buttonExp.innerText = "Más...";
    }

    // Cambiamos el texto del botón según el estado
    if (buttonEdu.innerText === "Más...") {
        buttonEdu.innerText = "Mostrar menos";
    } else {
        buttonEdu.innerText = "Más...";
    }
}