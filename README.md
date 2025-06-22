# 🌐 `ipatel` — IP Enrichment Library & CLI

## 🔍 What is `ipatel`?

**`ipatel`** is a lightweight Python library and CLI tool that enriches IP addresses and ASNs with useful metadata:

* 🛰️ **ASN (Autonomous System Number)**
* 🏢 **AS Owner / Organization**
* 🌎 **Country Code**
* 🧭 **IP Type** — Public / Private / Reserved
* 📶 **IP Ranges for ASN**

## ✨ Key Features

* ⚡ Fast and works **offline** after initial DB download
* 🔄 Auto-updates the enrichment database
* 💻 Simple and intuitive **Python API & CLI**
* 🧪 Fully tested, clean, and modular codebase
* 📦 Easy to install via `pip`

### 🔧 Installation

```bash
pip install ipatel
```

## Command Line Interface (CLI) 

`ipatel` also includes a built-in CLI tool that allows you to enrich IPs and fetch ASN data directly from the terminal.

### Basic Syntax

```bash
ipatel [-i IP_ADDRESS] [-a ASN] [--update-db] [--version] [-h]
```

### Available Flags

| Flag           | Description                         |
| -------------- | ----------------------------------- |
| `-i`, `--ip`   | Enrich the given IP address.        |
| `-a`, `--asn`  | Lookup IP ranges for the given ASN. |
| `--update-db`  | Force re-download of the DB.        |
| `--version`    | Show the installed version.         |
| `-h`, `--help` | Show usage and help message.        |


## 🚀 Quickstart Guide

## 🧩 Basic Setup

```python
import ipatel as ip
```

```python
# Let's declare ip and asn here, to check the quick functionality
test_ip = "8.8.8.8"
test_asn = 15169
```

## 🌐 IP Enrichment

### 🔹 Enrich IP with full metadata

```python
ip.enrich_ip("8.8.8.8")
```

**Returns:**

```python
{
    'ip': '8.8.8.8',
    'asn': 15169,
    'country_code': 'US',
    'owner': 'GOOGLE',
    'ip_type': 'Public'
}
```

## 🧠 ASN Lookup Functions

| Function                        | Description               | Example                           |
| ------------------------------- | ------------------------- | --------------------------------- |
| `ip.get_record(ip)`             | Full ASN record           | `ip.get_record("8.8.8.8")`        |
| `ip.get_asn(ip)`                | Get ASN only              | `15169`                           |
| `ip.get_country_code(ip)`       | Get country code          | `"US"`                            |
| `ip.get_owner(ip)`              | Get AS owner              | `"GOOGLE"`                        |
| `ip.get_ip_ranges_for_asn(asn)` | List of IP ranges for ASN | `ip.get_ip_ranges_for_asn(15169)` |



## 🛠️ Utilities

| Function                      | Description    | Output       |
| ----------------------------- | -------------- | ------------ |
| `ip.ip_to_int("8.8.8.8")`     | IP → Integer   | `134744072`  |
| `ip.int_to_ip(134744072)`     | Integer → IP   | `"8.8.8.8"`  |
| `ip.get_ip_type("127.0.0.1")` | Detect IP type | `"Loopback"` |


## 🔄 Database Management

| Task               | Function                  | Description                         |
| ------------------ | ------------------------- | ----------------------------------- |
| 📥 Download DB     | `ip.download_ip2asn_db()` | Manually fetch latest DB            |
| 🔁 Ensure Fresh DB | `ip.ensure_ip2asn_db()`   | Checks & auto-downloads if outdated |


---

## 📚 Learn More

* 📌 [CLI Usage](docs/cli.md)
* 🧾 [Detailed API Reference](docs/api.md)
* 🔁 [Database Update Guide](docs/update.md)
* 📂 [GitHub Repository](https://github.com/Chethanpatel/ipatel)
