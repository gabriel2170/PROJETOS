//Lista com uso do Enum

enum mySpace {
    numberOne = 1,
    Galaxia = 'Padrao',
    Estrela = 'Cadente',
    Planeta = 'Venus'
};


console.log(mySpace.Galaxia);

//Lista de valores

const nome:string[] = [];

nome.push('Gabriel');
nome.push('messi');

console.log(nome);

nome.pop();

console.log(nome);

const readNome: readonly string[] = nome;

//readNome.pop() - Erro pois variavel é apenas para leitura 

console.log(readNome);


//Tupla de Valores

let tuplaDeValores: [number, string, string];

tuplaDeValores = [25, 'Gabriel', 'Casado'];

console.log(tuplaDeValores)

//console.clear()