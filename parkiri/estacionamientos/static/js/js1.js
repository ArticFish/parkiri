function send_email() {
    fetch('recuperarContrasena')
        .then(response => {
            if (response.ok) {
                console.log('Función llamada exitosamente');
            } else {
                console.log('Error al llamar a la función');
            }
        })
        .catch(error => console.log('Error en la solicitud:', error));
}