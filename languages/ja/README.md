# Multi-Factor Authentication Command Line Interface

<div align="center"> <img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/714533aa-22a2-4127-8d40-363e59a573fa" width="300px"> </div>

## 説明

これは、シークレットを管理し、多要素認証 (MFA) コードを生成するために Python で書かれたシンプルなコマンド ライン インターフェイス (CLI) ツールです。このスクリプトを使用すると、ユーザーはシークレットを追加、削除、更新、リスト、エクスポートしたり、MFA コードを生成したりできます。

## 概要

<div align="center"> <img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/4fe8c766-8e76-4183-a80c-9ac143cbc18f" width="1000px"> </div>

## 特徴

### コマンド

- **mfa_add** &lt;名前&gt; &lt;シークレット&gt;: 新しいシークレットを追加します。
- **mfa_delete** &lt;name&gt; 保存されたシークレットを削除します。
- **mfa_list**保存されているすべてのシークレットをリストします。
- **mfa_update** &lt;name&gt; &lt;secret&gt;: 既存のシークレットを更新します。
- **mfa_generate** &lt;名前&gt;: MFA コードを生成します。
- **mfa_export** &lt;file_path&gt;: シークレットをファイルにエクスポートします。
- **mfa_help**このヘルプ メッセージを表示します。

### 要約されたコマンド

- **mfa** &lt;名前&gt; &lt;シークレット&gt;: 新しいシークレットを追加します。
- **mfd** &lt;name&gt; 保存されているシークレットを削除します。
- **mfl**保存されているすべてのシークレットをリストします。
- **mfu** &lt;name&gt; &lt;secret&gt;: 既存のシークレットを更新します。
- **mfg** &lt;名前&gt;: MFA コードを生成します。
- **mfe** &lt;file_path&gt;: シークレットをファイルにエクスポートします。
- **mfh**このヘルプ メッセージを表示します。

## 要件

- **Python3**

## インストール

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/install.py)"
```

## アンインストール

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/uninstall.py)"
```

## 著者

[EgydioBNeto](https://github.com/EgydioBNeto)

## ライセンス

このプロジェクトは[MIT ライセンス](https://github.com/EgydioBNeto/mfa-cli/blob/main/LICENSE)に基づいてライセンスされています。
