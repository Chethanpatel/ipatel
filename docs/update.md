# Updating the Database

`ipatel` relies on a local copy of the IP-to-ASN database to provide fast and offline enrichment. This section describes how the database is managed and how you can update it manually or programmatically.

---

## 1. Why Update the Database?

The IP-to-ASN mapping data changes frequently as networks evolve. Keeping the local database updated ensures that:

* Enrichment results are accurate
* New ASN allocations and IP ranges are recognized
* Country and ownership info remains current

---

## 2. One-Time Auto Download

When you run any `ipatel` command for the **first time**, it will automatically:

* Download the latest `ip2asn-v4.tsv.gz` file from [iptoasn.com](https://iptoasn.com)
* Extract and cache it locally for fast lookups

No action is needed on your part during first use.

---

## 3. Manual Update (Recommended Weekly)

You can manually refresh the database anytime using the CLI:

### 3.1 Command

```bash
ipatel --update-db
```

### 3.2 What It Does

* Downloads the latest compressed TSV file
* Extracts and stores it in the local cache directory
* Overwrites the previous database copy

---

## 4. Auto-Refresh Logic

On every usage, `ipatel` checks:

* If the local database exists
* If the file is older than **7 days**

If the data is outdated, a warning will be printed suggesting you to run:

```bash
ipatel --update-db
```

This helps you stay current without automatic background downloads.

---

## 5. Programmatic Update (Advanced)

You can also trigger a database update from Python code.

### 5.1 Code Snippet

```python
from ipatel.asn import download_ip2asn_db

download_ip2asn_db()
```

This is useful when integrating into scripts or scheduled jobs (e.g., cron).

---

## 6. Where is the DB Stored?

The database is stored locally in a cache directory like:

```bash
~/.cache/ipatel/ip2asn-v4.tsv
```

You do **not** need to manage this path manually unless doing advanced customizations.

---

## 7. Troubleshooting

* If download fails, check your internet connection.
* You can delete the cache file to force a fresh download.
* If `ipatel` doesn't recognize an IP, it's possible the DB is outdated — try updating it.

---

## 8. Source of Data

The IP-to-ASN data is freely provided by:

> 🌐 [iptoasn.com](https://iptoasn.com)

It is redistributed and used locally for enrichment, with no external calls after download.

---