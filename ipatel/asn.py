import os
import gzip
import shutil
import urllib.request
import ipaddress
from datetime import datetime, timedelta
from pathlib import Path

from ipatel.utils import ip_to_int, int_to_ip, CACHE_DIR

DB_GZ_URL = "https://iptoasn.com/data/ip2asn-v4.tsv.gz"
DB_PATH = CACHE_DIR / "ip2asn-v4.tsv"


def download_file_with_headers(url: str, dest: Path):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; ipatel/0.1.0)"}
    )
    with urllib.request.urlopen(req) as response, open(dest, "wb") as out_file:
        out_file.write(response.read())


def download_ip2asn_db():
    print("⬇️  Downloading latest ip2asn data...")

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    gz_path = CACHE_DIR / "ip2asn-v4.tsv.gz"

    download_file_with_headers(DB_GZ_URL, gz_path)

    with gzip.open(gz_path, "rb") as f_in, open(DB_PATH, "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

    print(f"✅ Database downloaded and saved to: {DB_PATH}")


def ensure_ip2asn_db():
    """
    Ensures the IP to ASN TSV file exists and is not older than 7 days.
    If missing, downloads it. If stale, prints a warning.
    """
    if not DB_PATH.exists():
        download_ip2asn_db()
        return

    modified_time = datetime.fromtimestamp(DB_PATH.stat().st_mtime)
    if datetime.now() - modified_time > timedelta(days=7):
        print("⚠️  ip2asn data is older than 7 days.")
        print("   Run `ipatel-update` to refresh the database.")


def get_record(ip: str) -> dict:
    """
    Given an IP address, return ASN info dict if found in DB.
    """
    ensure_ip2asn_db()
    try:
        ip_obj = ipaddress.IPv4Address(ip)
        ip_int = ip_to_int(str(ip_obj))
    except ValueError:
        return {
            "asn": None,
            "country_code": None,
            "owner": "Invalid IP"
        }

    with open(DB_PATH, "r") as f:
        for line in f:
            start, end, asn, cc, desc = line.strip().split("\t")
            if ip_int >= ip_to_int(start) and ip_int <= ip_to_int(end):
                return {
                    "asn": int(asn),
                    "country_code": cc,
                    "owner": desc
                }

    return {
        "asn": None,
        "country_code": None,
        "owner": "Private Network"
    }


def get_asn(ip: str) -> int | None:
    return get_record(ip)["asn"]


def get_country_code(ip: str) -> str | None:
    return get_record(ip)["country_code"]


def get_owner(ip: str) -> str:
    return get_record(ip)["owner"]


def get_ip_ranges_for_asn(asn: int) -> dict:
    """
    Given an ASN, returns all IP ranges and owner/country info.
    """
    ensure_ip2asn_db()

    ranges = []
    owners = set()
    countries = set()

    with open(DB_PATH, "r") as f:
        for line in f:
            start, end, line_asn, cc, desc = line.strip().split("\t")
            if int(line_asn) == asn:
                ranges.append((start, end))
                owners.add(desc)
                countries.add(cc)

    return {
        "asn": asn,
        "owner": "; ".join(sorted(owners)) if owners else None,
        "country_code": "; ".join(sorted(countries)) if countries else None,
        "ip_ranges": ranges
    }


def get_asn_info_for_ip(ip: str) -> dict:
    """
    Public API: Given IP, return enriched info: type, owner, country, ASN.
    """
    try:
        ip_obj = ipaddress.IPv4Address(ip)
        if ip_obj.is_private:
            return {
                "ip": ip,
                "asn": None,
                "country_code": None,
                "owner": "Private Network",
                "type": "private"
            }

        record = get_record(ip)
        return {
            "ip": ip,
            "asn": record["asn"],
            "country_code": record["country_code"],
            "owner": record["owner"],
            "type": "public"
        }

    except Exception:
        return {
            "ip": ip,
            "asn": None,
            "country_code": None,
            "owner": "Invalid IP",
            "type": "invalid"
        }
