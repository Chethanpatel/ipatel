# 🚀 Quickstart Guide

Welcome to **IPATEL** — a fast and lightweight IP enrichment library.

This guide shows how to quickly get started with importing the library and using all core functions.

---

## 📦 Installation

```bash
pip install ipatel
````

---

## ✨ Basic Usage

```python
import ipatel as ip

# Sample test inputs
test_ip = "8.8.8.8"
test_asn = 15169
```

---

## 🔍 IP Enrichment

### Enrich an IP address with all available fields:

```python
ip.enrich_ip(test_ip)
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

---

## 🧠 ASN Lookups

### Get ASN record (raw dict):

```python
ip.get_record(test_ip)
```

### Get ASN number:

```python
ip.get_asn(test_ip)  # ➝ 15169
```

### Get country code:

```python
ip.get_country_code(test_ip)  # ➝ "US"
```

### Get AS owner/organization:

```python
ip.get_owner(test_ip)  # ➝ "GOOGLE"
```

### Get all IP ranges owned by an ASN:

```python
ip.get_ip_ranges_for_asn(test_asn)
```

---

## 🛠️ Utilities

### Convert IP to integer:

```python
ip.ip_to_int("8.8.8.8")  # ➝ 134744072
```

### Convert integer to IP:

```python
ip.int_to_ip(134744072)  # ➝ "8.8.8.8"
```

### Detect IP type (public/private/reserved):

```python
ip.get_ip_type("127.0.0.1")  # ➝ "Loopback"
```

---

## 🔄 Database Handling

### Download the latest IP-to-ASN database:

```python
ip.download_ip2asn_db()
```

### Ensure local DB is fresh:

```python
ip.ensure_ip2asn_db()
```

---

## 🧪 Full Test Script

You can try this all together:

```python
def run_tests():
    ip.ensure_ip2asn_db()
    print(ip.enrich_ip("8.8.8.8"))

if __name__ == "__main__":
    run_tests()
```

---

## 📝 Notes

* All functions are safe for both IPv4 inputs.
* Private, reserved, and loopback IPs are handled gracefully.

---

## 📚 See Also

* [CLI Usage](cli.md)
* [Detailed API](api.md)
* [DB Upadte](update.md)
* [Project Repo](https://github.com/Chethanpatel/ipatel)


