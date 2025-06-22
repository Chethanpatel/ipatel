#!/usr/bin/env python3

import argparse
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from ipenrich.enrich import enrich_ip
from ipenrich.asn import get_ip_ranges_for_asn

console = Console()

def handle_ip_lookup(ip: str):
    result = enrich_ip(ip)

    table = Table(title="IP Enrichment", show_header=True, header_style="bold green")
    table.add_column("Field", style="dim")
    table.add_column("Value")

    for key, value in result.items():
        table.add_row(key, str(value))

    console.print(table)

def handle_asn_lookup(asn: int):
    result = get_ip_ranges_for_asn(asn)

    if not result["ip_ranges"]:
        console.print(f"[red]No entries found for ASN {asn}[/red]")
        return

    console.print(Panel(f"[bold blue]ASN {asn}[/bold blue]\n[bold]Owner:[/bold] {result['owner']}\n[bold]Country:[/bold] {result['country_code']}"))

    table = Table(title="IP Ranges", show_header=True, header_style="bold green")
    table.add_column("Start IP")
    table.add_column("End IP")

    for start, end in result["ip_ranges"]:
        table.add_row(start, end)

    console.print(table)

def main():
    parser = argparse.ArgumentParser(description="IP and ASN Enrichment CLI")
    parser.add_argument("-i", "--ip", help="IP address to enrich")
    parser.add_argument("-a", "--asn", type=int, help="ASN to lookup")

    args = parser.parse_args()

    if args.ip:
        handle_ip_lookup(args.ip)
    elif args.asn:
        handle_asn_lookup(args.asn)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
