# Multi-Factor Authentication Command Line Interface

<div align="center"> <img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/714533aa-22a2-4127-8d40-363e59a573fa" width="300px"> </div>

## विवरण

यह रहस्यों को प्रबंधित करने और मल्टी-फैक्टर ऑथेंटिकेशन (एमएफए) कोड उत्पन्न करने के लिए पायथन में लिखा गया एक सरल कमांड लाइन इंटरफ़ेस (सीएलआई) टूल है। स्क्रिप्ट उपयोगकर्ताओं को रहस्य जोड़ने, हटाने, अपडेट करने, सूचीबद्ध करने और निर्यात करने के साथ-साथ एमएफए कोड उत्पन्न करने की अनुमति देती है।

## अवलोकन

<div align="center"> <img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/4fe8c766-8e76-4183-a80c-9ac143cbc18f" width="1000px"> </div>

## विशेषताएँ

### आदेश

- **mfa_add** &lt;नाम&gt; &lt;गुप्त&gt;: एक नया रहस्य जोड़ें।
- **mfa_delete** &lt;नाम&gt; संग्रहीत रहस्य हटाएं।
- **mfa_list** सभी संग्रहीत रहस्यों की सूची बनाएं।
- **mfa_update** &lt;नाम&gt; &lt;गुप्त&gt;: किसी मौजूदा रहस्य को अपडेट करें।
- **mfa_generate** &lt;नाम&gt;: एक MFA कोड जनरेट करें।
- **mfa_export** &lt;file_path&gt;: किसी फ़ाइल में रहस्य निर्यात करें।
- **mfa_help** यह सहायता संदेश दिखाएँ।

### सारांशित आदेश

- **mfa** &lt;नाम&gt; &lt;गुप्त&gt;: एक नया रहस्य जोड़ें।
- **mfd** &lt;नाम&gt; संग्रहीत रहस्य हटाएं।
- **mfl** सभी संग्रहीत रहस्यों की सूची बनाएं।
- **mfu** &lt;नाम&gt; &lt;गुप्त&gt;: मौजूदा रहस्य को अपडेट करें।
- **mfg** &lt;नाम&gt;: एक एमएफए कोड जेनरेट करें।
- **mfe** &lt;file_path&gt;: किसी फ़ाइल में रहस्य निर्यात करें।
- **mfh** यह सहायता संदेश दिखाएँ।

## आवश्यकताएं

- **Python3**

## इंस्टालेशन

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/install.py)"
```

## विस्थापना

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/uninstall.py)"
```

## लेखक

[EgydioBNeto](https://github.com/EgydioBNeto)

## लाइसेंस

यह प्रोजेक्ट [एमआईटी लाइसेंस](https://github.com/EgydioBNeto/mfa-cli/blob/main/LICENSE) के तहत लाइसेंस प्राप्त है।
