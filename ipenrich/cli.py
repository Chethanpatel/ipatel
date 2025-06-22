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
    parser = argparse.ArgumentParser(description="IP and ASN Enrichment CLI", add_help=False)
    parser.add_argument("-i", "--ip", help="IP address to enrich")
    parser.add_argument("-a", "--asn", type=int, help="ASN to lookup")
    parser.add_argument("-h", "--help", action="store_true", help="Show help message and exit")

    args = parser.parse_args()

    if args.help:
        parser.print_help()
        console.print("\n[bold cyan]Examples:[/bold cyan]")
        console.print("  • Enrich an IP address: [green]ipenrich -i 8.8.8.8[/green]")
        console.print("  • Lookup IP ranges for ASN: [green]ipenrich -a 15169[/green]")
        console.print("\n[bold yellow]By Chethan Patel[/bold yellow] · [blue]https://github.com/chethanpatel/ipenrich[/blue]")
        return

    if args.ip:
        handle_ip_lookup(args.ip)
    elif args.asn:
        handle_asn_lookup(args.asn)
    else:
        banner = Panel.fit(
            "[bold cyan]ipenrich CLI[/bold cyan]\n[green]by Chethan Patel[/green] · [blue]https://github.com/chethanpatel/ipenrich[/blue]",
            border_style="cyan"
        )
        console.print(banner)

        console.print("\n[bold cyan]Examples:[/bold cyan]")
        console.print("  • Enrich an IP address: [green]ipenrich -i 8.8.8.8[/green]")
        console.print("  • Lookup IP ranges for ASN: [green]ipenrich -a 15169[/green]")

        console.print("\nRun [yellow]ipenrich -h[/yellow] for full help.")

        # Example 1: IP lookup preview
        example_ip = "8.8.8.8"
        result = enrich_ip(example_ip)
        ip_table = Table(title=f"Example: Enrichment for IP {example_ip}", show_header=True, header_style="bold magenta")
        ip_table.add_column("Field", style="dim", no_wrap=True)
        ip_table.add_column("Value", style="bold")

        for key, value in result.items():
            ip_table.add_row(key, str(value))

        console.print(ip_table)

        # Example 2: ASN lookup preview
        example_asn = 15169
        result_asn = get_ip_ranges_for_asn(example_asn)
        asn_panel = Panel(
            f"[bold blue]ASN {example_asn}[/bold blue]\n[bold]Owner:[/bold] {result_asn['owner']}\n[bold]Country:[/bold] {result_asn['country_code']}",
            title="Example: ASN Lookup"
        )
        console.print(asn_panel)

        range_table = Table(title="Sample IP Ranges for ASN 15169", header_style="bold green")
        range_table.add_column("Start IP")
        range_table.add_column("End IP")

        for i, (start, end) in enumerate(result_asn["ip_ranges"][:3]):
            range_table.add_row(start, end)

        console.print(range_table)


if __name__ == "__main__":
    main()
