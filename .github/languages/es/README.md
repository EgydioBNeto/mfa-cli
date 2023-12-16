# Multi-Factor Authentication Command Line Interface

<div align="center"> <img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/714533aa-22a2-4127-8d40-363e59a573fa" width="300px"> </div>

## Descripción

Esta es una herramienta simple de interfaz de línea de comandos (CLI) escrita en Python para administrar secretos y generar códigos de autenticación multifactor (MFA). El script permite a los usuarios agregar, eliminar, actualizar, enumerar y exportar secretos, así como generar códigos MFA.

## Visión general

<div align="center"> <img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/4fe8c766-8e76-4183-a80c-9ac143cbc18f" width="1000px"> </div>

## Características

### Comandos

- **mfa_add** &lt;nombre&gt; &lt;secreto&gt;: agrega un nuevo secreto.
- **mfa_delete** &lt;nombre&gt; Eliminar un secreto almacenado.
- **mfa_list** Lista todos los secretos almacenados.
- **mfa_update** &lt;nombre&gt; &lt;secreto&gt;: actualiza un secreto existente.
- **mfa_generate** &lt;nombre&gt;: genera un código MFA.
- **mfa_export** &lt;file_path&gt;: exporta secretos a un archivo.
- **mfa_help** Muestra este mensaje de ayuda.

### Comandos resumidos

- **mfa** &lt;nombre&gt; &lt;secreto&gt;: agrega un nuevo secreto.
- **mfd** &lt;nombre&gt; Elimina un secreto almacenado.
- **mfl** Lista todos los secretos almacenados.
- **mfu** &lt;nombre&gt; &lt;secreto&gt;: actualiza un secreto existente.
- **mfg** &lt;nombre&gt;: genera un código MFA.
- **mfe** &lt;file_path&gt;: exporta secretos a un archivo.
- **mfh** Mostrar este mensaje de ayuda.

## Requisitos

- **Python3**

## Instalación

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/install.py)"
```

## Desinstalación

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/uninstall.py)"
```

## Autor

[EgydioBNeto](https://github.com/EgydioBNeto)

## Licencia

Este proyecto está bajo la [licencia MIT](https://github.com/EgydioBNeto/mfa-cli/blob/main/LICENSE) .
