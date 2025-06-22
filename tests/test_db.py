import os
from ipatel.asn import (
    download_ip2asn_db,
    get_asn_info_for_ip,
    get_ip_ranges_for_asn,
)
from ipatel.utils import CACHE_DIR

def test_download_ip2asn_db():
    download_ip2asn_db()
    db_path = CACHE_DIR / "ip2asn-v4.tsv"
    assert db_path.exists()
    assert os.path.getsize(db_path) > 10_000  # sanity check

def test_enrich_public_ip():
    result = get_asn_info_for_ip("8.8.8.8")
    assert result["asn"] is not None
    assert result["type"] == "public"
    assert result["owner"] is not None
    assert result["country_code"] == "US"

def test_enrich_private_ip():
    result = get_asn_info_for_ip("192.168.1.1")
    assert result["type"] == "private"
    assert result["asn"] is None
    assert result["country_code"] is None
    assert result["owner"] == "Private Network"

def test_get_ip_ranges_for_asn():
    records = get_ip_ranges_for_asn("15169")
    assert isinstance(records, list)
    assert any("GOOGLE" in r["owner"].upper() for r in records)
    assert all("ip_range" in r for r in records)
