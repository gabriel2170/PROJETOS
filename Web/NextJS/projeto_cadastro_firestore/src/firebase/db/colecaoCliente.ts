import firebase from "../config";
import Cliente from "../../core/Cliente";
import ClienteRepositorio from "../../core/clienteRepositorio";

export default class ColecaoCliente implements ClienteRepositorio{

    #conversor = {
        toFirestore(cliente: Cliente){
            return {
                nome: cliente.nome,
                idade: cliente.idade,

            }
        },
        fromFirestore(snapshot:firebase.firestore.QueryDocumentSnapshot, options: firebase.firestore.QueryOptions): Cliente{
            const dados = snapshot?.data(options)
            return new Cliente(dados.nome, dados.idade, snapshot.id)
        }
    }

    async salvar(cliente: Cliente): Promise<Cliente>{
        if(cliente?.id){
            await this.colecao().doc(cliente.id).set(cliente)
            return cliente
        }else{
            const docRef = await this.colecao().add(cliente)
            const doc = await docRef.get()
            return doc.data()
        }
    }
    async excluir(cliente: Cliente): Promise<Cliente>{
        return this.colecao().doc(cliente.id).delete()
    }
    async obterTodos(): Promise<Cliente[]>{
        const query = await this.colecao().get()
        return query.docs.map((doc: any)=> doc.data()) ?? [[]]
        
    }

    private colecao(){
        return firebase
        .firebase()
        .collection('clientes')
        .withConverter(this.#conversor)
    }
}
