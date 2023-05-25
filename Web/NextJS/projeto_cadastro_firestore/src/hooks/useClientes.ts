import { useEffect, useState } from "react"
import ColecaoCliente from "../firebase/db/colecaoCliente"
import Cliente from "../core/Cliente"
import ClienteRepositorio from "../core/clienteRepositorio"
import useTabelaOuForm from "./useTabelaOuForm"


export default function useClientes() {
    const repo: ClienteRepositorio = new ColecaoCliente()
    const {tabelaVisivel, formularioVisivel, exibirFormulario, exibirTabela} = useTabelaOuForm()
    const [cliente, setCliente] = useState<Cliente>(Cliente.vazio())
    const [clientes, setClientes] = useState<Cliente[]>([])

    useEffect(() => {
        obterTodos
    }, [])

    function obterTodos() {
        repo.obterTodos().then(clientes => {
            setClientes(clientes)
            exibirTabela()
        })
    }

    function selecionarCliente(cliente: Cliente) {
        setCliente(cliente)
        exibirFormulario()
    }

    function novoCliente() {
        setCliente(Cliente.vazio())
        exibirFormulario()
    }

    async function excluirCliente(cliente: Cliente) {
        await repo.excluir(cliente)
        obterTodos()
    }

    async function salvarCliente(cliente: Cliente) {
        await repo.salvar(cliente)
        obterTodos()
    }

    return{
        salvarCliente,
        novoCliente,
        excluirCliente,
        selecionarCliente,
        obterTodos,
        cliente,
        clientes,
        tabelaVisivel,
        formularioVisivel,
        exibirTabela,
        exibirFormulario
        
    }
}
