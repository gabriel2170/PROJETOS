import React, { useState } from 'react';
import { cnpj, cpf } from 'cpf-cnpj-validator'
import CnpjPromise from 'cnpj-promise'
import './App.css';

export default () => {
  const [dados, setDados] = useState('');
  const [info, setInfo] = useState('');


  function validarCNPJ() {
    if (cnpj.isValid(dados)) {
      setInfo(`CNPJ ${cnpj.format(dados)} é Valido`)
    } else {
      setInfo(`CNPJ ${dados} é Invalido`)
    }
  }

  function validarCPF() {
    if (cpf.isValid(dados)) {
      setInfo(`CPF ${cpf.format(dados)} é Valido`)
    } else {
      setInfo(`CPF ${dados} é Invalido`)
    }
  }

  async function buscarCNPJ() {
    CnpjPromise(dados)
    .then(data => setInfo(`CNPJ: ${data.cnpj} Fantasia: ${data.fantasia} Data de Abertura: ${data.abertura} Situação: ${data.situacao} Porte: ${data.porte} Tipo: ${data.tipo} Cidade: ${data.municipio} Estado: ${data.uf} CEP: ${data.cep} Endereco: ${data.logradouro}, ${data.numero}, ${data.bairro}`))
    .catch(err =>{
      setInfo(`CNPJ ${dados} é Invalido`)
    })
  }

  function limpar() {
    setDados('')
    setInfo('')
  }

  return (

    <div className="interface">
      <label>N° Documento</label>
      <input type="text" id="cnpj" value={dados} onChange={(e) => setDados(e.target.value)} placehoder="000000-000" />
      <div className='botoes'>
        <button className="validar" onClick={() => validarCNPJ()}>Validar CNPJ</button>
        <button className="validar" onClick={() => buscarCNPJ()}>Buscar CNPJ</button>
        <button className="validar" onClick={() => validarCPF()}>Validar CPF</button>
        <button className="limpar" onClick={() => limpar()}>Limpar</button>
      </div>
      <span className='info'>{info}</span>

    </div>
  )
}
