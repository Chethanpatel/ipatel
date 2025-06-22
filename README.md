# ENRICH IP (`ipatel`)

## Overview

`ipatel` is a lightweight and efficient Python library and CLI tool for enriching IP addresses and ASNs with metadata such as:

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
pip install ipatel 
```

### 🧠 Author

* **Chethan Patel**
* 🌐 [GitHub](https://github.com/Chethanpatel/ipatel)
* 💼 [LinkedIn](https://www.linkedin.com/in/Chethanpatelpn)

# API

`ipatel` is a lightweight Python library and CLI tool to enrich IP addresses and ASNs with:

* ASN (Autonomous System Number)
* Owner / AS Description
* Country Code
* IP Type (Public / Private / Invalid)
* IP Ranges associated with ASNs

It works offline after downloading a one-time IP-to-ASN mapping database and offers both programmatic and command-line interfaces.

---

## 1. Enrich an IP Address

#### 1.1 Description

Enrich a public IP address with detailed metadata including ASN, country, owner, and whether it is public or private.

#### 1.2 API

```python
ipatel.enrich.enrich_ip(ip: str) -> dict
```

#### 1.3 Example

```python
from ipatel.enrich import enrich_ip

result = enrich_ip("8.8.8.8")
print(result)
```

**Output:**

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

## 2. Get Raw ASN Record

#### 2.1 Description

Fetch the raw record for an IP from the IP-to-ASN database.

#### 2.2 API

```python
ipatel.asn.get_record(ip: str) -> dict
```

#### 2.3 Example

```python
from ipatel.asn import get_record

record = get_record("8.8.8.8")
print(record)
```

**Output:**

```python
{
    "asn": 15169,
    "country_code": "US",
    "owner": "GOOGLE"
}
```

---

## 3. Get ASN Number

#### 3.1 Description

Return the ASN number for a given IP address.

#### 3.2 API

```python
ipatel.asn.get_asn(ip: str) -> int | None
```

#### 3.3 Example

```python
from ipatel.asn import get_asn

get_asn("8.8.8.8")  # ➜ 15169
```

---

## 4. Get Country Code

#### 4.1 Description

Returns the 2-letter ISO country code for a given IP address.

#### 4.2 API

```python
ipatel.asn.get_country_code(ip: str) -> str | None
```

#### 4.3 Example

```python
from ipatel.asn import get_country_code

get_country_code("8.8.8.8")  # ➜ 'US'
```

---

## 5. Get Owner / AS Description

#### 5.1 Description

Return the organization or description (owner) of the ASN associated with an IP.

#### 5.2 API

```python
ipatel.asn.get_owner(ip: str) -> str
```

#### 5.3 Example

```python
from ipatel.asn import get_owner

get_owner("8.8.8.8")  # ➜ 'GOOGLE'
```

---

## 6. Get IP Ranges for ASN

#### 6.1 Description

Given an ASN, return:

* ASN number
* Owner
* Country code
* All IP ranges associated with that ASN

#### 6.2 API

```python
ipatel.asn.get_ip_ranges_for_asn(asn: int) -> dict
```

#### 6.3 Example

```python
from ipatel.asn import get_ip_ranges_for_asn

info = get_ip_ranges_for_asn(15169)
print(info)
```

**Output:**

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

## 7. Force Download Database

#### 7.1 Description

Manually download the latest IP-to-ASN database from [iptoasn.com](https://iptoasn.com).
This is usually handled automatically.

#### 7.2 API

```python
ipatel.asn.download_ip2asn_db() -> None
```

#### 7.3 Example

```python
from ipatel.asn import download_ip2asn_db

download_ip2asn_db()
```

---

## 8. Ensure Local Database is Fresh

#### 8.1 Description

Check if the local database is fresh (within 7 days); otherwise, trigger a warning or update.

#### 8.2 API

```python
ipatel.asn.ensure_ip2asn_db() -> None
```

---

## 9. Command Line Interface (CLI)

#### 9.1 Description

After installation, use `ipatel` from your terminal to enrich IPs or fetch ASN data.

#### 9.2 Commands

```bash
ipatel -i 1.1.1.1         # Enrich an IP
ipatel -a 15169           # Lookup ASN details
ipatel --update-db        # Manually update the database
ipatel --version          # Show current version
ipatel -h                 # Show help and usage
```

---

## 10. Dependencies

#### 10.1 Required

* `rich` — Beautiful CLI formatting
* `argparse` — Command-line parser
* Standard library:

  * `pathlib`
  * `ipaddress`
  * `urllib`
  * `gzip`
  * `shutil`

---

# CLI

`ipatel` includes a built-in CLI tool that allows you to enrich IPs and fetch ASN data directly from the terminal.

## 11. Command Line Interface (CLI) 

---

### 11.1 Basic Syntax

```bash
ipatel [-i IP_ADDRESS] [-a ASN] [--update-db] [--version] [-h]
```

---

### 11.2 Available Flags

| Flag           | Description                         |
| -------------- | ----------------------------------- |
| `-i`, `--ip`   | Enrich the given IP address.        |
| `-a`, `--asn`  | Lookup IP ranges for the given ASN. |
| `--update-db`  | Force re-download of the DB.        |
| `--version`    | Show the installed version.         |
| `-h`, `--help` | Show usage and help message.        |

---

### 11.3 Example Commands

###### 11.3.1 Enrich an IP Address

```bash
ipatel -i 8.8.8.8
```

Returns:

```text
IP      : 8.8.8.8
ASN     : 15169
Owner   : GOOGLE
Country : US
Type    : public
```

---

###### 11.3.2 Lookup ASN Information

```bash
ipatel -a 15169
```

Returns:

```text
ASN     : 15169
Owner   : GOOGLE
Country : US
IP Ranges:
  - 8.8.4.0 - 8.8.4.255
  - 8.8.8.0 - 8.8.8.255
  ...
```

---

###### 11.3.3 Manually Update the Database

```bash
ipatel --update-db
```

Downloads the latest IP-to-ASN dataset and replaces the local cache.

---

###### 11.3.4 Show Current Version

```bash
ipatel --version
```

Prints the installed version of `ipatel`.

---

### 11.4 Database Management

###### 11.4.1 Offline Usage

The tool uses a local database (`ip2asn-v4.tsv`) fetched from [iptoasn.com](https://iptoasn.com), enabling fully offline lookups after the initial download.

---

###### 11.4.2 Auto-Download Behavior

* When `ipatel` is used for the first time, it automatically downloads the latest IP-to-ASN dataset.
* If the local copy is older than **7 days**, a prompt is shown to refresh.

---

###### 11.4.3 Manual Refresh

You can also force an update manually:

```bash
ipatel --update-db
```

This will:

* Download the latest `ip2asn-v4.tsv.gz`
* Extract it
* Replace the outdated local copy

---

### 11.5 Programmatic Update (Advanced)

For advanced use cases or library integration, update the database manually via code:

```python
from ipatel.asn import download_ip2asn_db

download_ip2asn_db()
```

---

### 11.6 Contribution & Support

For issues, feature requests, or contributions:

🌐 [GitHub Repository](https://github.com/chethanpatel/ipatel)

---

# 12. Updating the Database

`ipatel` relies on a local copy of the IP-to-ASN database to provide fast and offline enrichment. This section describes how the database is managed and how you can update it manually or programmatically.

---

## 12.1 Why Update the Database?

The IP-to-ASN mapping data changes frequently as networks evolve. Keeping the local database updated ensures that:

* Enrichment results are accurate
* New ASN allocations and IP ranges are recognized
* Country and ownership info remains current

---

## 12.2. One-Time Auto Download

When you run any `ipatel` command for the **first time**, it will automatically:

* Download the latest `ip2asn-v4.tsv.gz` file from [iptoasn.com](https://iptoasn.com)
* Extract and cache it locally for fast lookups

No action is needed on your part during first use.

---

## 12.3. Manual Update (Recommended Weekly)

You can manually refresh the database anytime using the CLI:

### 12.3.1 Command

```bash
ipatel --update-db
```

### 12.3.2 What It Does

* Downloads the latest compressed TSV file
* Extracts and stores it in the local cache directory
* Overwrites the previous database copy

---

## 12.4 Auto-Refresh Logic

On every usage, `ipatel` checks:

* If the local database exists
* If the file is older than **7 days**

If the data is outdated, a warning will be printed suggesting you to run:

```bash
ipatel --update-db
```

This helps you stay current without automatic background downloads.

---

## 12.5 Programmatic Update (Advanced)

You can also trigger a database update from Python code.

### 5.1 Code Snippet

```python
from ipatel.asn import download_ip2asn_db

download_ip2asn_db()
```

This is useful when integrating into scripts or scheduled jobs (e.g., cron).

---

## 12.6 Where is the DB Stored?

The database is stored locally in a cache directory like:

```bash
~/.cache/ipatel/ip2asn-v4.tsv
```

You do **not** need to manage this path manually unless doing advanced customizations.

---

## 12.7 Troubleshooting

* If download fails, check your internet connection.
* You can delete the cache file to force a fresh download.
* If `ipatel` doesn't recognize an IP, it's possible the DB is outdated — try updating it.

---

## 12.8 Source of Data

The IP-to-ASN data is freely provided by:

> 🌐 [iptoasn.com](https://iptoasn.com)

It is redistributed and used locally for enrichment, with no external calls after download.

---