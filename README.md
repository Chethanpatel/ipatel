# ENRICH IP (`ipenrich`)

## Overview

`ipenrich` is a lightweight and efficient Python library and CLI tool for enriching IP addresses and ASNs with metadata such as:

* **ASN** (Autonomous System Number)
* **Owner / AS Description**
* **Country Code**
* **IP Type** (Public / Private / Invalid)
* **IP Ranges for ASN**

### 🔑 Features

* Works offline after downloading the IP-to-ASN database.
* Built-in support to auto-update the enrichment database.
* Friendly CLI with rich output formatting.
* Fully tested and modular codebase.

### 📦 Install

```bash
pip install ipenrich 
```

### 🧠 Author

* **Chethan Patel**
* 🌐 [GitHub](https://github.com/Chethanpatel/ipenrich)
* 💼 [LinkedIn](https://www.linkedin.com/in/Chethanpatelpn)

### ✅ Example:

```python
from ipenrich.enrich import enrich_ip

result = enrich_ip("8.8.8.8")
print(result)
```

### 🧾 Output:

```python
{
    "ip": "8.8.8.8",
    "asn": 15169,
    "owner": "GOOGLE",
    "country_code": "US",
    "type": "public"
}
```

---

## 🔹 `ipenrich.asn.get_record(ip: str) -> dict`

### 🔍 Description:

Internal utility that fetches raw ASN record from the database.

### ✅ Example:

```python
from ipenrich.asn import get_record

record = get_record("8.8.8.8")
print(record)
```

### 🧾 Output:

```python
{
    "asn": 15169,
    "country_code": "US",
    "owner": "GOOGLE"
}
```

---

## 🔹 `ipenrich.asn.get_asn(ip: str) -> int | None`

### 🔍 Description:

Returns ASN number of a given IP address.

```python
from ipenrich.asn import get_asn
get_asn("8.8.8.8")  # ➜ 15169
```

---

## 🔹 `ipenrich.asn.get_country_code(ip: str) -> str | None`

### 🔍 Description:

Returns the 2-letter ISO country code.

```python
from ipenrich.asn import get_country_code
get_country_code("8.8.8.8")  # ➜ 'US'
```

---

## 🔹 `ipenrich.asn.get_owner(ip: str) -> str`

### 🔍 Description:

Returns the owner (AS description) of the IP address.

```python
from ipenrich.asn import get_owner
get_owner("8.8.8.8")  # ➜ 'GOOGLE'
```

---

## 🔹 `ipenrich.asn.get_ip_ranges_for_asn(asn: int) -> dict`

### 🔍 Description:

Given an ASN, returns:

* Owner
* Country
* IP ranges associated with that ASN

### ✅ Example:

```python
from ipenrich.asn import get_ip_ranges_for_asn

info = get_ip_ranges_for_asn(15169)
print(info)
```

### 🧾 Output:

```python
{
    "asn": 15169,
    "owner": "GOOGLE",
    "country_code": "US",
    "ip_ranges": [
        ("8.8.4.0", "8.8.4.255"),
        ("8.8.8.0", "8.8.8.255"),
        ...
    ]
}
```

---

## 🔹 `ipenrich.asn.download_ip2asn_db()`

### 🔍 Description:

Force-downloads the latest IP-to-ASN TSV database from `iptoasn.com`. This is typically managed automatically.

```python
from ipenrich.asn import download_ip2asn_db
download_ip2asn_db()
```

---

## 🔹 `ipenrich.asn.ensure_ip2asn_db()`

### 🔍 Description:

Checks if the local database exists and is fresh (within 7 days); otherwise suggests update.

---

## 🔹 CLI Commands

Once installed, use `ipenrich` via command line:

```bash
ipenrich -i 1.1.1.1         # Enrich an IP
ipenrich -a 15169           # Lookup ASN details
ipenrich --update-db        # Manually update database
ipenrich --version          # Show current version
ipenrich -h                 # Show help and usage examples
```

---

## 📦 Dependencies

* `rich` — for beautiful CLI formatting
* `ipaddress` - for the ipaddress formatting
* `argparse` — for command-line handling
* `pathlib`, `urllib`, `gzip`, `shutil` — built-in

---

