# Multi-Factor Authentication Command Line Interface

<div align="center"> <img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/714533aa-22a2-4127-8d40-363e59a573fa" width="300px"> </div>

## Description

Il s'agit d'un simple outil d'interface de ligne de commande (CLI) écrit en Python pour gérer les secrets et générer des codes d'authentification multifacteur (MFA). Le script permet aux utilisateurs d'ajouter, de supprimer, de mettre à jour, de répertorier et d'exporter des secrets, ainsi que de générer des codes MFA.

## Aperçu

<div align="center"> <img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/4fe8c766-8e76-4183-a80c-9ac143cbc18f" width="1000px"> </div>

## Caractéristiques

### Commandes

- **mfa_add** &lt;name&gt; &lt;secret&gt; : ajoutez un nouveau secret.
- **mfa_delete** &lt;nom&gt; Supprime un secret stocké.
- **mfa_list** Répertorie tous les secrets stockés.
- **mfa_update** &lt;name&gt; &lt;secret&gt; : met à jour un secret existant.
- **mfa_generate** &lt;nom&gt; : génère un code MFA.
- **mfa_export** &lt;file_path&gt; : exporte les secrets vers un fichier.
- **mfa_help** Afficher ce message d'aide.

### Commandes résumées

- **mfa** &lt;nom&gt; &lt;secret&gt; : ajoutez un nouveau secret.
- **mfd** &lt;nom&gt; Supprime un secret stocké.
- **mfl** Répertorie tous les secrets stockés.
- **mfu** &lt;name&gt; &lt;secret&gt; : mettre à jour un secret existant.
- **mfg** &lt;nom&gt; : génère un code MFA.
- **mfe** &lt;file_path&gt; : exporte les secrets vers un fichier.
- **mfh** Afficher ce message d'aide.

## Exigences

- **Python3**

## Installation

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/install.py)"
```

## Désinstallation

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/uninstall.py)"
```

## Auteur

[ÉgydioBNeto](https://github.com/EgydioBNeto)

## Licence

Ce projet est sous [licence MIT](https://github.com/EgydioBNeto/mfa-cli/blob/main/LICENSE) .
