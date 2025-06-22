import pytest
from ipatel.asn import (
    get_asn_info_for_ip,
    get_record,
    get_ip_ranges_for_asn
)

# Example public IP (Google DNS)
PUBLIC_IP = "8.8.8.8"
PRIVATE_IP = "192.168.1.1"
INVALID_IP = "999.999.999.999"

def test_get_asn_info_for_public_ip():
    result = get_asn_info_for_ip(PUBLIC_IP)
    assert result["ip"] == PUBLIC_IP
    assert result["type"] == "public"
    assert result["asn"] is not None
    assert result["country_code"] is not None
    assert result["owner"] is not None

def test_get_asn_info_for_private_ip():
    result = get_asn_info_for_ip(PRIVATE_IP)
    assert result["ip"] == PRIVATE_IP
    assert result["type"] == "private"
    assert result["asn"] is None
    assert result["owner"] == "Private Network"

def test_get_asn_info_for_invalid_ip():
    result = get_asn_info_for_ip(INVALID_IP)
    assert result["ip"] == INVALID_IP
    assert result["type"] == "invalid"
    assert result["asn"] is None
    assert result["owner"] == "Invalid IP"

def test_get_record_for_public_ip():
    record = get_record(PUBLIC_IP)
    assert record["asn"] is not None
    assert record["country_code"] is not None
    assert record["owner"] is not None

def test_get_record_for_invalid_ip():
    record = get_record(INVALID_IP)
    assert record["asn"] is None
    assert record["owner"] == "Invalid IP"

def test_get_ip_ranges_for_asn():
    # Google ASN for 8.8.8.8 is usually 15169
    asn_data = get_ip_ranges_for_asn(15169)
    assert asn_data["asn"] == 15169
    assert len(asn_data["ip_ranges"]) > 0
    assert asn_data["owner"] is not None
    assert asn_data["country_code"] is not None
