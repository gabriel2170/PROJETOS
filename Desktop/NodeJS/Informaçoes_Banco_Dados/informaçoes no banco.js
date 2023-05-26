const mysql = require('mysql')
const readline = require('readline-sync')

class Data {

    iniciarBanco() {
        const db = mysql.createConnection({
            host: '127.0.0.1',
            user: 'root',
            password: 'klmolk127'
        })

        db.connect((err) => {
            if (err) {
                console.log('Falha ao Conectar!!')
                db.end()
            } else {
                db.query('CREATE DATABASE Data', (err) => {
                    if (err) {
                        console.log('Banco ja Existe!!')
                        db.end()
                    } else {
                        console.log('Banco foi Criado!!')
                        db.end()
                    }
                })
            }

        })
    }

    criarTabela() {
        const db = mysql.createConnection({
            host: '127.0.0.1',
            user: 'root',
            password: 'klmolk127',
            database: 'Data'
        })

        db.connect((err) => {
            if (err) {
                console.log('Falha ao Conectar no Banco!!')
                db.end()
            } else {
                db.query("CREATE TABLE usuario (id INT AUTO_INCREMENT PRIMARY KEY , nome VARCHAR(255) , idade INT)", (err, res) => {
                    if (err) {
                        console.log('Tabela ja existe!!')
                        db.end()
                    } else {
                        console.log('Tabela foi Criada!!')
                        db.end()
                    }
                })
            }
        })
    }


    inserirDados(nome, idade) {
        const db = mysql.createConnection({
            host: '127.0.0.1',
            user: 'root',
            password: 'klmolk127',
            database: 'Data'
        })

        db.connect((err) => {
            if (err) {
                console.log('Falha ao Conectar no Banco!!')
                db.end()
            } else {
                db.query(`INSERT INTO usuario (nome, idade) VALUES ('${nome}', '${idade}')`, (err, res) => {
                    if (err) {
                        console.log('Tabela nao existe!!')
                        db.end()
                    } else {
                        console.log(`Usuario ${nome} foi criado!!`)
                        db.end()
                    }
                })
            }
        })
    }

    deletarDadosNome(nome) {
        const db = mysql.createConnection({
            host: '127.0.0.1',
            user: 'root',
            password: 'klmolk127',
            database: 'Data'
        })

        db.connect((err) => {
            if (err) {
                console.log('Falha ao Conectar no Banco!!')
                db.end()
            } else {
                db.query(`DELETE FROM usuario WHERE nome = ${nome}`, (err, res) => {
                    if (err) {
                        console.log('Tabela nao existe!!')
                        db.end()
                    } else {
                        if(res.affectedRows == 0){
                            console.log(`Nao ha dados do usuario ${nome}!!`)
                            db.end()
                        }else{
                            console.log(`Dados do Usuario ${nome} foram deletados!!`)
                            db.end()
                        }
                       
                    }
                })
            }
        })
    }

    deletarDadosIdade(idade) {
        const db = mysql.createConnection({
            host: '127.0.0.1',
            user: 'root',
            password: 'klmolk127',
            database: 'Data'
        })

        db.connect((err) => {
            if (err) {
                console.log('Falha ao Conectar no Banco!!')
                db.end()
            } else {
                db.query(`DELETE FROM usuario WHERE idade = ${idade}`, (err, res) => {
                    if (err) {
                        console.log('Tabela nao existe!!')
                        db.end()
                    } else {
                        if(res.affectedRows == 0){
                            console.log(`Nao ha dados com a idade igual a ${idade} !!`)
                            db.end()
                        }else{
                            console.log(`Dados cuja a idade e igual a ${idade} foram deletados!!`)
                            db.end()
                        }
                        
                    }
                })
            }
        })
    }

    consultarTabelas() {
        const db = mysql.createConnection({
            host: '127.0.0.1',
            user: 'root',
            password: 'klmolk127',
            database: 'Data'
        })


        db.connect((err) => {
            if (err) {
                console.log('Falha ao Conectar no Banco!!')
                db.end()
            } else {
                db.query("SHOW TABLES", (err, res) => {
                    if (err) {
                        console.log('Nao Ha tabelas para consulta!!')
                        db.end()
                    } else {
                        res.map((x) => {
                            console.log(x)
                            db.end()
                        })
                    }
                })
            }
        })
    }

    consultarBancos() {
        const db = mysql.createConnection({
            host: '127.0.0.1',
            user: 'root',
            password: 'klmolk127',
            database: 'Data'
        })


        db.connect((err) => {
            if (err) {
                console.log('Falha ao Conectar no Banco!!')
                db.end()
            } else {
                db.query("SHOW DATABASES", (err, res) => {
                    if (err) {
                        console.log('Nao Ha Bancos para consulta!!')
                        db.end()
                    } else {
                        res.map((x) => {
                            console.log(x)
                            db.end()
                        })
                    }
                })
            }
        })
    }


    consultarDados() {
        const db = mysql.createConnection({
            host: '127.0.0.1',
            user: 'root',
            password: 'klmolk127',
            database: 'Data'
        })


        db.connect((err) => {
            if (err) {
                console.log('Falha ao Conectar no Banco!!')
                db.end()
            } else {
                db.query("SELECT * FROM usuario", (err, res, fields) => {
                    if (err) {
                        console.log('Nao Ha Bancos para consulta!!')
                        db.end()
                    } else {
                        console.log(res)
                        db.end()
                    }
                })
            }
        })
    }

    deletarTabela() {
        const db = mysql.createConnection({
            host: '127.0.0.1',
            user: 'root',
            password: 'klmolk127',
            database: 'Data'
        })


        db.connect((err) => {
            if (err) {
                console.log('Falha ao Conectar no Banco!!')
                db.end()
            } else {
                db.query("DROP TABLE usuario", (err, res) => {
                    if (err) {
                        console.log('Nao existe Tabela usuario!!')
                        db.end()
                    } else {
                        console.log('Tabela Deletada!!')
                        db.end()
                    }
                })
            }
        })
    }

    deletarBanco() {

        const db = mysql.createConnection({
            host: '127.0.0.1',
            user: 'root',
            password: 'klmolk127',
            database: 'Data'
        })

        db.connect((err) => {
            if (err) {
                console.log('Falha ao Conectar no Banco!!')
                db.end()
            } else {
                db.query('DROP DATABASE Data', (err, res) => {
                    if (err) {
                        console.log('Nao existe Banco Data!!')
                        db.end()
                    } else {
                        console.log('Banco Deletado!!')
                        db.end()
                    }
                })
            }
        })

    }
}


const query = new Data()

var n = parseInt(readline.question('Selecione uma das Opcoes (1-Criar Banco/ 2-Criar Tabela/ 3-Inserir dados/ 4-Deletar Dados/ 5-Consultar Tabelas/ 6-Consultar Dados/ 7-Consultar Bancos/ 8-Deletar Tabela/ 9-Deletar Banco): '))

if (n < 0 || n > 9) {
    console.log('Opcao Invalida!!')
}

if (n == 1) {
    query.iniciarBanco()

}

if (n == 2) {
    query.criarTabela()
}

if (n == 3) {
    let nome = readline.question("Digite seu nome: ")
    let idade = readline.question("Digite sua idade: ")
    query.inserirDados(nome, idade)
}

if (n == 4) {

    x = parseInt(readline.question('Selecione um Criterio para Deletar os Dados (1-Nome/ 2-Idade/ 0-Sair): '))

    if (x < 0 || x > 2) {
        console.log('Opcao Invalida')
    }

    if (x == 1) {
        let nome = readline.question("Digite seu nome: ")
        query.deletarDadosNome(nome)
    }

    if (x == 2) {
        let idade = readline.question("Digite sua idade: ")
        query.deletarDadosIdade(idade)
    }

}

if (n == 5) {
    query.consultarTabelas()
}

if (n == 6) {
    query.consultarDados()
}

if (n == 7) {
    query.consultarBancos()
}

if (n == 8) {
    query.deletarTabela()
}

if (n == 9) {
    query.deletarBanco()
}
