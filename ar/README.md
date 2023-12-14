# Multi-Factor Authentication Command Line Interface

<div align="center"> <img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/714533aa-22a2-4127-8d40-363e59a573fa" width="300px"> </div>

## وصف

هذه أداة بسيطة لواجهة سطر الأوامر (CLI) مكتوبة بلغة Python لإدارة الأسرار وإنشاء رموز المصادقة متعددة العوامل (MFA). يسمح البرنامج النصي للمستخدمين بإضافة الأسرار وحذفها وتحديثها وإدراجها وتصديرها، بالإضافة إلى إنشاء رموز MFA.

## ملخص

<div align="center"> <img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/4fe8c766-8e76-4183-a80c-9ac143cbc18f" width="1000px"> </div>

## سمات

### الأوامر

- **mfa_add** &lt;name&gt; &lt;secret&gt;: أضف سرًا جديدًا.
- **mfa_delete** &lt;name&gt; حذف السر المخزن.
- **mfa_list** قم بإدراج كافة الأسرار المخزنة.
- **mfa_update** &lt;name&gt; &lt;secret&gt;: تحديث سر موجود.
- **mfa_generate** &lt;name&gt;: قم بإنشاء رمز MFA.
- **mfa_export** &lt;file_path&gt;: تصدير الأسرار إلى ملف.
- **mfa_help** عرض رسالة المساعدة هذه.

### الأوامر الموجزة

- **mfa** &lt;name&gt; &lt;secret&gt;: أضف سرًا جديدًا.
- **mfd** &lt;name&gt; حذف السر المخزن.
- **MFL** قائمة بجميع الأسرار المخزنة.
- **mfu** &lt;name&gt; &lt;secret&gt;: تحديث سر موجود.
- **mfg** &lt;name&gt;: إنشاء رمز MFA.
- **mfe** &lt;file_path&gt;: تصدير الأسرار إلى ملف.
- **mfh** عرض رسالة المساعدة هذه.

## متطلبات

- **Python3**

## تثبيت

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/install.py)"
```

## إلغاء التثبيت

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/uninstall.py)"
```

## مؤلف

[EgydioBNeto](https://github.com/EgydioBNeto)

## رخصة

هذا المشروع مرخص بموجب [ترخيص MIT](https://github.com/EgydioBNeto/mfa-cli/blob/main/LICENSE) .
