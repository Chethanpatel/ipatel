from ipatel.asn import get_record
from ipatel.utils import get_ip_type

def enrich_ip(ip: str) -> dict:
    record = get_record(ip)
    ip_type = get_ip_type(ip)

    return {
        "ip": ip,
        "asn": record["asn"],
        "owner": record["owner"],
        "country_code": record["country_code"],
        "type": ip_type
    }
