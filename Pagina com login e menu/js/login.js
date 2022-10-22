function login(){

    var usuario = document.getElementById('usuario').value;
    var senha = document.getElementById('senha').value;

    if(usuario == '' || usuario == null || usuario == undefined){
        alert('Campo Usuario nao pode ficar vazio!');
    }
    else if(senha == '' || senha == null || senha == undefined){
        alert('Campo senha nao pode ficar vazio!');
    }
    else{
        alert('Login efetuado com sucesso!!');
        window.location.href = "menu.html"
    }
}