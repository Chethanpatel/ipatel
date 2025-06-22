import ipatel as ip

def run_tests():
    test_ip = "8.8.8.8"
    test_asn = 15169

    print("Version:", ip.__version__)
    print()

    print("Testing enrich_ip...")
    print(ip.enrich_ip(test_ip))
    print()

    print("Testing get_record...")
    print(ip.get_record(test_ip))
    print()

    print("Testing get_asn...")
    print("ASN:", ip.get_asn(test_ip))
    print()

    print("Testing get_country_code...")
    print("Country:", ip.get_country_code(test_ip))
    print()

    print("Testing get_owner...")
    print("Owner:", ip.get_owner(test_ip))
    print()

    print("Testing get_ip_ranges_for_asn...")
    print(ip.get_ip_ranges_for_asn(test_asn))
    print()

    print("Testing download_ip2asn_db...")
    ip.download_ip2asn_db()
    print("Download complete.")
    print()

    print("Testing ensure_ip2asn_db...")
    ip.ensure_ip2asn_db()
    print("DB freshness ensured.")
    print()

    print("Testing get_asn_info_for_ip...")
    print(ip.get_asn_info_for_ip(test_ip))
    print()

    print("Testing ip_to_int...")
    ip_int = ip.ip_to_int(test_ip)
    print("IP to int:", ip_int)
    print()

    print("Testing int_to_ip...")
    print("Int to IP:", ip.int_to_ip(ip_int))
    print()

    print("Testing get_ip_type...")
    print("IP Type:", ip.get_ip_type(test_ip))
    print()

if __name__ == "__main__":
    run_tests()
