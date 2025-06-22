# API

`ipenrich` is a lightweight Python library and CLI tool to enrich IP addresses and ASNs with:

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
ipenrich.enrich.enrich_ip(ip: str) -> dict
```

#### 1.3 Example

```python
from ipenrich.enrich import enrich_ip

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
ipenrich.asn.get_record(ip: str) -> dict
```

#### 2.3 Example

```python
from ipenrich.asn import get_record

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
ipenrich.asn.get_asn(ip: str) -> int | None
```

#### 3.3 Example

```python
from ipenrich.asn import get_asn

get_asn("8.8.8.8")  # ➜ 15169
```

---

## 4. Get Country Code

#### 4.1 Description

Returns the 2-letter ISO country code for a given IP address.

#### 4.2 API

```python
ipenrich.asn.get_country_code(ip: str) -> str | None
```

#### 4.3 Example

```python
from ipenrich.asn import get_country_code

get_country_code("8.8.8.8")  # ➜ 'US'
```

---

## 5. Get Owner / AS Description

#### 5.1 Description

Return the organization or description (owner) of the ASN associated with an IP.

#### 5.2 API

```python
ipenrich.asn.get_owner(ip: str) -> str
```

#### 5.3 Example

```python
from ipenrich.asn import get_owner

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
ipenrich.asn.get_ip_ranges_for_asn(asn: int) -> dict
```

#### 6.3 Example

```python
from ipenrich.asn import get_ip_ranges_for_asn

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
ipenrich.asn.download_ip2asn_db() -> None
```

#### 7.3 Example

```python
from ipenrich.asn import download_ip2asn_db

download_ip2asn_db()
```

---

## 8. Ensure Local Database is Fresh

#### 8.1 Description

Check if the local database is fresh (within 7 days); otherwise, trigger a warning or update.

#### 8.2 API

```python
ipenrich.asn.ensure_ip2asn_db() -> None
```

---

## 9. Command Line Interface (CLI)

#### 9.1 Description

After installation, use `ipenrich` from your terminal to enrich IPs or fetch ASN data.

#### 9.2 Commands

```bash
ipenrich -i 1.1.1.1         # Enrich an IP
ipenrich -a 15169           # Lookup ASN details
ipenrich --update-db        # Manually update the database
ipenrich --version          # Show current version
ipenrich -h                 # Show help and usage
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

