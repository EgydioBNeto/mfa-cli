# Multi-Factor Authentication Command Line Interface

<div align="center"> <img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/714533aa-22a2-4127-8d40-363e59a573fa" width="300px"> </div>

## Descrição

Esta é uma ferramenta simples de interface de linha de comando (CLI) escrita em Python para gerenciar segredos e gerar códigos de autenticação multifator (MFA). O script permite aos usuários adicionar, excluir, atualizar, listar e exportar segredos, bem como gerar códigos MFA.

## Visão geral

<div align="center"> <img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/4fe8c766-8e76-4183-a80c-9ac143cbc18f" width="1000px"> </div>

## Características

### Comandos

- **mfa_add** &lt;nome&gt; &lt;segredo&gt;: Adicione um novo segredo.
- **mfa_delete** &lt;nome&gt; Exclui um segredo armazenado.
- **mfa_list** Lista todos os segredos armazenados.
- **mfa_update** &lt;nome&gt; &lt;segredo&gt;: atualiza um segredo existente.
- **mfa_generate** &lt;nome&gt;: gera um código MFA.
- **mfa_export** &lt;nome_do_arquivo&gt;: exporta segredos para um arquivo.
- **mfa_help** Mostre esta mensagem de ajuda.

### Comandos resumidos

- **mfa** &lt;nome&gt; &lt;segredo&gt;: Adicione um novo segredo.
- **mfd** &lt;nome&gt; Exclua um segredo armazenado.
- **mfl** Lista todos os segredos armazenados.
- **mfu** &lt;nome&gt; &lt;segredo&gt;: atualiza um segredo existente.
- **mfg** &lt;nome&gt;: gera um código MFA.
- **mfe** &lt;nome_do_arquivo&gt;: exporta segredos para um arquivo.
- **mfh** Mostre esta mensagem de ajuda.

## Requisitos

- **Python3**

## Instalação

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/install.py)"
```

## Desinstalação

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/uninstall.py)"
```

## Autor

[EgydioBNeto](https://github.com/EgydioBNeto)

## Licença

Este projeto está licenciado sob a [Licença MIT](https://github.com/EgydioBNeto/mfa-cli/blob/main/LICENSE) .
