#!/usr/bin/env python3

import argparse
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.box import SIMPLE_HEAVY
from ipenrich.enrich import enrich_ip
from ipenrich.asn import get_ip_ranges_for_asn

console = Console()

def handle_ip_lookup(ip: str):
    result = enrich_ip(ip)

    panel = Panel.fit(
        "[bold cyan]IP Enrichment[/bold cyan]\n[green]by Chethan Patel · https://github.com/Chethanpatel/ipenrich[/green]",
        border_style="cyan"
    )
    console.print(panel)

    table = Table(
        show_header=True,
        header_style="bold green",
        box=SIMPLE_HEAVY,
        expand=False
    )
    table.add_column("Field", style="bold yellow")
    table.add_column("Value", style="magenta")

    for key, value in result.items():
        table.add_row(key, str(value))

    console.print(table)
    console.print("⭐ [yellow]Star this tool:[/yellow] [bold blue]https://github.com/Chethanpatel/ipenrich[/bold blue]\n")

def handle_asn_lookup(asn: int):
    result = get_ip_ranges_for_asn(asn)

    if not result["ip_ranges"]:
        console.print(f"[red]No entries found for ASN {asn}[/red]")
        return

    panel = Panel.fit(
        f"[bold cyan]ASN {asn} Enrichment[/bold cyan]\n[green]by Chethan Patel · https://github.com/Chethanpatel/ipenrich[/green]",
        border_style="cyan"
    )
    console.print(panel)

    info_table = Table(
        show_header=True,
        header_style="bold green",
        box=SIMPLE_HEAVY
    )
    info_table.add_column("Field", style="bold yellow")
    info_table.add_column("Value", style="magenta")

    info_table.add_row("asn", str(result["asn"]))
    info_table.add_row("owner", result["owner"] or "-")
    info_table.add_row("country_code", result["country_code"] or "-")

    console.print(info_table)

    ip_table = Table(title="IP Ranges", show_header=True, header_style="bold green", box=SIMPLE_HEAVY)
    ip_table.add_column("Start IP", style="cyan")
    ip_table.add_column("End IP", style="cyan")

    for start, end in result["ip_ranges"]:
        ip_table.add_row(start, end)

    console.print(ip_table)
    console.print("⭐ [yellow]Star this tool:[/yellow] [bold blue]https://github.com/Chethanpatel/ipenrich[/bold blue]\n")

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
