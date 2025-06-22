# CLI

`ipenrich` includes a built-in CLI tool that allows you to enrich IPs and fetch ASN data directly from the terminal.

## 11. Command Line Interface (CLI) 

---

### 11.1 Basic Syntax

```bash
ipenrich [-i IP_ADDRESS] [-a ASN] [--update-db] [--version] [-h]
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
ipenrich -i 8.8.8.8
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
ipenrich -a 15169
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
ipenrich --update-db
```

Downloads the latest IP-to-ASN dataset and replaces the local cache.

---

###### 11.3.4 Show Current Version

```bash
ipenrich --version
```

Prints the installed version of `ipenrich`.

---

### 11.4 Database Management

###### 11.4.1 Offline Usage

The tool uses a local database (`ip2asn-v4.tsv`) fetched from [iptoasn.com](https://iptoasn.com), enabling fully offline lookups after the initial download.

---

###### 11.4.2 Auto-Download Behavior

* When `ipenrich` is used for the first time, it automatically downloads the latest IP-to-ASN dataset.
* If the local copy is older than **7 days**, a prompt is shown to refresh.

---

###### 11.4.3 Manual Refresh

You can also force an update manually:

```bash
ipenrich --update-db
```

This will:

* Download the latest `ip2asn-v4.tsv.gz`
* Extract it
* Replace the outdated local copy

---

### 11.5 Programmatic Update (Advanced)

For advanced use cases or library integration, update the database manually via code:

```python
from ipenrich.asn import download_ip2asn_db

download_ip2asn_db()
```

---

### 11.6 Contribution & Support

For issues, feature requests, or contributions:

🌐 [GitHub Repository](https://github.com/chethanpatel/ipenrich)

---
