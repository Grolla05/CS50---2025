// Aciona a funcao quando clicado no botao submit
form.addEventListener("submit", function (event) {
  document.querySelector("form").addEventListener("submit", function (event) {
    // Exibe o "alerta" quando executado
    alert("Hello, " + document.querySelector("#name".value));
    event.preventDefault();
  });
});
