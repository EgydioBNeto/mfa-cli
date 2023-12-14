# Multi-Factor Authentication Command Line Interface

<div align="center"> <img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/714533aa-22a2-4127-8d40-363e59a573fa" width="300px"> </div>

## 描述

这是一个用 Python 编写的简单命令行界面 (CLI) 工具，用于管理机密和生成多重身份验证 (MFA) 代码。该脚本允许用户添加、删除、更新、列出和导出机密，以及生成 MFA 代码。

## 概述

<div align="center"> <img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/4fe8c766-8e76-4183-a80c-9ac143cbc18f" width="1000px"> </div>

## 特征

### 命令

- **mfa_add** &lt;名称&gt; &lt;秘密&gt;：添加新秘密。
- **mfa_delete** &lt;名称&gt; 删除存储的机密。
- **mfa_list**列出所有存储的机密。
- **mfa_update** &lt;名称&gt; &lt;秘密&gt;：更新现有秘密。
- **mfa_generate** &lt;名称&gt;：生成 MFA 代码。
- **mfa_export** &lt;file_path&gt;：将机密导出到文件。
- **mfa_help**显示此帮助消息。

### 命令汇总

- **mfa** &lt;名称&gt; &lt;秘密&gt;：添加新秘密。
- **mfd** &lt;name&gt; 删除存储的机密。
- **mfl**列出所有存储的机密。
- **mfu** &lt;名称&gt; &lt;秘密&gt;：更新现有秘密。
- **mfg** &lt;名称&gt;：生成 MFA 代码。
- **mfe** &lt;file_path&gt;：将机密导出到文件。
- **mfh**显示此帮助消息。

## 要求

- **Python3**

## 安装

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/install.py)"
```

## 卸载

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/uninstall.py)"
```

## 作者

[EgydioBNeto](https://github.com/EgydioBNeto)

## 执照

该项目根据[MIT 许可证](https://github.com/EgydioBNeto/mfa-cli/blob/main/LICENSE)获得许可。
