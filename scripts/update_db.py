#!/usr/bin/env python3

from ipatel.asn import download_ip2asn_db

def main():
    print("🔄 Updating ip2asn database...")
    download_ip2asn_db()
    print("✅ Update complete!")

if __name__ == "__main__":
    main()
