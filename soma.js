function clicar() {
    var peso = document.querySelector(".peso").value;
    var altura = document.querySelector(".altura").value;

    var resultado = parseInt(peso) / parseInt(altura * altura);
    document.querySelector(".resultado").innerHTML = resultado;


}