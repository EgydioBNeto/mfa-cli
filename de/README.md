# Multi-Factor Authentication Command Line Interface

<div align="center"> <img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/714533aa-22a2-4127-8d40-363e59a573fa" width="300px"> </div>

## Beschreibung

Dabei handelt es sich um ein einfaches, in Python geschriebenes Command Line Interface (CLI)-Tool zum Verwalten von Geheimnissen und zum Generieren von Multi-Factor Authentication (MFA)-Codes. Mit dem Skript können Benutzer Geheimnisse hinzufügen, löschen, aktualisieren, auflisten und exportieren sowie MFA-Codes generieren.

## Überblick

<div align="center"> <img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/4fe8c766-8e76-4183-a80c-9ac143cbc18f" width="1000px"> </div>

## Merkmale

### Befehle

- **mfa_add** &lt;Name&gt; &lt;Geheimnis&gt;: Neues Geheimnis hinzufügen.
- **mfa_delete** &lt;Name&gt; Ein gespeichertes Geheimnis löschen.
- **mfa_list** Alle gespeicherten Geheimnisse auflisten.
- **mfa_update** &lt;Name&gt; &lt;Geheimnis&gt;: Ein vorhandenes Geheimnis aktualisieren.
- **mfa_generate** &lt;Name&gt;: Generieren Sie einen MFA-Code.
- **mfa_export** &lt;Dateipfad&gt;: Geheimnisse in eine Datei exportieren.
- **mfa_help** Diese Hilfemeldung anzeigen.

### Zusammengefasste Befehle

- **mfa** &lt;Name&gt; &lt;Geheimnis&gt;: Neues Geheimnis hinzufügen.
- **mfd** &lt;Name&gt; Ein gespeichertes Geheimnis löschen.
- **mfl** Alle gespeicherten Geheimnisse auflisten.
- **mfu** &lt;Name&gt; &lt;Geheimnis&gt;: Ein vorhandenes Geheimnis aktualisieren.
- **mfg** &lt;Name&gt;: Generieren Sie einen MFA-Code.
- **mfe** &lt;file_path&gt;: Geheimnisse in eine Datei exportieren.
- **mfh** Diese Hilfemeldung anzeigen.

## Anforderungen

- **Python3**

## Installation

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/install.py)"
```

## Deinstallation

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/uninstall.py)"
```

## Autor

[EgydioBNeto](https://github.com/EgydioBNeto)

## Lizenz

Dieses Projekt ist unter der [MIT-Lizenz](https://github.com/EgydioBNeto/mfa-cli/blob/main/LICENSE) lizenziert.
