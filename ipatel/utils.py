import ipaddress
from pathlib import Path

CACHE_DIR = Path.home() / ".cache" / "ipatel"

def get_ip_type(ip: str) -> str:
    """
    Classifies an IP address as public, private, reserved, etc.
    """
    try:
        ip_obj = ipaddress.ip_address(ip)

        if ip_obj.is_private:
            return "private"
        elif ip_obj.is_loopback:
            return "loopback"
        elif ip_obj.is_multicast:
            return "multicast"
        elif ip_obj.is_reserved:
            return "reserved"
        elif ip_obj.is_link_local:
            return "link-local"
        elif ip_obj.is_unspecified:
            return "unspecified"
        else:
            return "public"
    except ValueError:
        return "invalid"


def ip_to_int(ip: str) -> int:
    """Convert IPv4 address to integer."""
    return int(ipaddress.IPv4Address(ip))


def int_to_ip(ip_int: int) -> str:
    """Convert integer to IPv4 address."""
    return str(ipaddress.IPv4Address(ip_int))
