from ipatel.enrich import enrich_ip
from ipatel.asn import get_ip_ranges_for_asn
import json

# Enriching a public IP address
ip_result = enrich_ip("8.8.8.8")
print(json.dumps(ip_result))
# Output: {'ip': '8.8.8.8', 'asn': 15169, 'owner': 'GOOGLE', 'country_code': 'US', 'type': 'public'}

# ASN lookup
asn_result = get_ip_ranges_for_asn(15169)
print(json.dumps(asn_result))
# Output:
# {
#   'asn': 15169,
#   'owner': 'GOOGLE',
#   'country_code': 'US',
#   'ip_ranges': [('8.8.4.0', '8.8.4.255'), ...]
# }
