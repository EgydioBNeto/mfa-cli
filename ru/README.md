# Multi-Factor Authentication Command Line Interface

<div align="center"> <img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/714533aa-22a2-4127-8d40-363e59a573fa" width="300px"> </div>

## Описание

Это простой инструмент интерфейса командной строки (CLI), написанный на Python для управления секретами и генерации кодов многофакторной аутентификации (MFA). Скрипт позволяет пользователям добавлять, удалять, обновлять, составлять список и экспортировать секреты, а также генерировать коды MFA.

## Обзор

<div align="center"> <img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/4fe8c766-8e76-4183-a80c-9ac143cbc18f" width="1000px"> </div>

## Функции

### Команды

- **mfa_add** &lt;имя&gt; &lt;секрет&gt;: добавить новый секрет.
- **mfa_delete** &lt;имя&gt; Удалить сохраненный секрет.
- **mfa_list** Список всех сохраненных секретов.
- **mfa_update** &lt;имя&gt; &lt;секрет&gt;: обновить существующий секрет.
- **mfa_generate** &lt;имя&gt;: создать код MFA.
- **mfa_export** &lt;путь_файла&gt;: экспортировать секреты в файл.
- **mfa_help** Показать это справочное сообщение.

### Сводные команды

- **mfa** &lt;имя&gt; &lt;секрет&gt;: добавьте новый секрет.
- **mfd** &lt;имя&gt; Удалить сохраненный секрет.
- **mfl** Список всех сохраненных секретов.
- **mfu** &lt;имя&gt; &lt;секрет&gt;: обновить существующий секрет.
- **mfg** &lt;имя&gt;: создать код MFA.
- **mfe** &lt;путь_файла&gt;: экспортировать секреты в файл.
- **mfh** Показать это справочное сообщение.

## Требования

- **Python3**

## Монтаж

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/install.py)"
```

## Удаление

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/uninstall.py)"
```

## Автор

[EgydioBNeto](https://github.com/EgydioBNeto)

## Лицензия

Этот проект лицензируется по [лицензии MIT](https://github.com/EgydioBNeto/mfa-cli/blob/main/LICENSE) .
