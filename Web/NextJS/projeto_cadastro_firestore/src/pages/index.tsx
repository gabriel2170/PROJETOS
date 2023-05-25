import Botao from "../components/Botao";
import Formulario from "../components/Formulario";
import Layout from "../components/Layout";
import Tabela from "../components/Tabela";
import useClientes from "../hooks/useClientes";

export default function Home() {


  const { selecionarCliente, excluirCliente, cliente, clientes , novoCliente, salvarCliente, tabelaVisivel, formularioVisivel, exibirFormulario, exibirTabela} = useClientes()

  return (
    <div className={`
    flex h-screen justify-center items-center
    bg-gradient-ro-r from-blue-500 text-white to-purble-600 text-2xl
    `}>
      <Layout titulo="Cadastro Simples">
        { tabelaVisivel ? (
          <>
            <div className='flex justify-end'>
              <Botao
                cor='green'
                className='mb-4'
                onClick={() => novoCliente}>
                Novo Cliente
              </Botao>
            </div>
            <Tabela
              clientes={clientes}
              clienteSelecionado={selecionarCliente}
              clienteExcluido={excluirCliente} />
          </>
        ) : (
          <Formulario
            cliente={cliente}
            cancelado={() => exibirTabela}
            clienteMudou={salvarCliente}
          />
        )}

      </Layout>
    </div >
  )
}
