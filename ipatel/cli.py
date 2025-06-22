#!/usr/bin/env python3

import argparse
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from ipatel.enrich import enrich_ip
from ipatel.asn import get_ip_ranges_for_asn, download_ip2asn_db

from ipatel import __version__ as VERSION
console = Console()

def handle_ip_lookup(ip: str):
    result = enrich_ip(ip)

    banner = Panel.fit(
        "[bold cyan]IP Enrichment     [/bold cyan]",
        subtitle="by [green]Chethan Patel[/green] · [blue]https://github.com/Chethanpatel/ipatel[/blue]",
        border_style="cyan"
    )
    console.print(banner)

    table = Table(show_header=True, header_style="bold green")
    table.add_column("Field", style="dim", no_wrap=True)
    table.add_column("Value", style="bold")

    for key, value in result.items():
        table.add_row(key, str(value))

    console.print(table)
    console.print("\n:star: [bold yellow]Star this tool:[/bold yellow] [blue]https://github.com/Chethanpatel/ipatel[/blue]")

def handle_asn_lookup(asn: int):
    result = get_ip_ranges_for_asn(asn)

    banner = Panel.fit(
        f"[bold cyan]ASN Lookup: {asn}[/bold cyan]",
        subtitle="by [green]Chethan Patel[/green] · [blue]https://github.com/Chethanpatel/ipatel[/blue]",
        border_style="cyan"
    )
    console.print(banner)

    if not result["ip_ranges"]:
        console.print(f"[red]No entries found for ASN {asn}[/red]")
        return

    console.print(Panel(f"[bold]Owner:[/bold] {result['owner']}\n[bold]Country:[/bold] {result['country_code']}", title="ASN Details"))

    table = Table(title="IP Ranges", header_style="bold green")
    table.add_column("Start IP")
    table.add_column("End IP")

    # for start, end in result["ip_ranges"][:10]:  # Limit for readability
    for start, end in result["ip_ranges"]:  # Not Limit for readability    
        table.add_row(start, end)

    console.print(table)
    console.print("\n:star: [bold yellow]Star this tool:[/bold yellow] [blue]https://github.com/Chethanpatel/ipatel[/blue]")

def main():
    parser = argparse.ArgumentParser(description="IP and ASN Enrichment CLI", add_help=False)
    parser.add_argument("-i", "--ip", help="IP address to enrich")
    parser.add_argument("-a", "--asn", type=int, help="ASN to lookup")
    parser.add_argument("--update-db", action="store_true", help="Force update of the IP2ASN database")
    parser.add_argument("-v", "--version", action="store_true", help="Show version information")
    parser.add_argument("-h", "--help", action="store_true", help="Show help message and exit")
    parser.add_argument("--about", action="store_true", help="Show information about the tool and author")

    args = parser.parse_args()

    if args.version:
        console.print(f"[bold cyan]ipatel[/bold cyan] version [yellow]{VERSION}[/yellow]")
        return

    if args.help:
        banner = Panel.fit(
            f"[bold cyan]ipatel CLI[/bold cyan] [magenta]v{VERSION}[/magenta]\n[green]by Chethan Patel[/green] · [blue]https://github.com/Chethanpatel/ipatel[/blue]",
            border_style="cyan"
        )
        console.print(banner)

        help_table = Table(title="Options", header_style="bold green", show_lines=False)
        help_table.add_column("Flag", style="cyan", no_wrap=True)
        help_table.add_column("Description", style="white")

        help_table.add_row("-i, --ip IP", "IP address to enrich")
        help_table.add_row("-a, --asn ASN", "ASN to lookup")
        help_table.add_row("--update-db", "Force update of the IP2ASN database")
        help_table.add_row("-v, --version", "Show version information")
        help_table.add_row("-h, --help", "Show help message and exit")

        console.print(help_table)

        console.print("\n[bold cyan]Examples:[/bold cyan]")
        console.print(" • Enrich an IP address: [green]ipatel -i 8.8.8.8[/green]")
        console.print(" • Lookup IP ranges for ASN: [green]ipatel -a 15169[/green]")
        console.print(" • Force update database: [green]ipatel --update-db[/green]")
        console.print(" • Show version: [green]ipatel -v[/green]")

        return


    if args.update_db:
        console.print("[cyan]⬇️ Updating the IP2ASN database...[/cyan]")
        download_ip2asn_db()
        console.print("[green]✅ Database update completed.[/green]")
        return
    
    if args.about:
        banner = Panel.fit(
            f"[bold cyan]    ipatel CLI            [/bold cyan] [magenta]v{VERSION}[/magenta]\n\n"
            f"[bold green]IP and ASN Enrichment Tool[/bold green]\n"
            f"[dim]• Enrich any public IP with ASN, country, owner, and its type(public/private)[/dim]\n"
            f"[dim]• Get all IP ranges for a given ASN[/dim]\n"
            f"[dim]• Works offline after database is downloaded[/dim]\n"
            f"[dim]• Weekly freshness check for data[/dim]\n"
            f"[dim]• Checks for stale data weekly (older than 7 days)[/dim]\n"
            f"[dim]• Supports manual refresh to fetch the latest IP2ASN dataset[/dim]\n\n"
            f"[bold green]Author:[/bold green] Chethan Patel\n"
            f"[bold green]GitHub:[/bold green] https://github.com/Chethanpatel/ipatel\n"
            f"[bold green]LinkedIn:[/bold green] https://www.linkedin.com/in/chethanpatelpn\n"
            f"[bold green]Email:[/bold green] helpfromchethan@gmail.com",
            border_style="cyan"
        )
        console.print(banner)
        return

    if args.ip:
        handle_ip_lookup(args.ip)
    elif args.asn:
        handle_asn_lookup(args.asn)
    else:
        banner = Panel.fit(
            "[bold cyan]  ipatel CLI     [/bold cyan]",
            subtitle="by [green]Chethan Patel[/green] · [blue]https://github.com/Chethanpatel/ipatel[/blue]",
            border_style="cyan"
        )
        console.print(banner)

        console.print("\n[bold cyan]Examples:[/bold cyan]")
        console.print("  • Enrich an IP address: [green]ipatel -i 8.8.8.8[/green]")
        console.print("  • Lookup IP ranges for ASN: [green]ipatel -a 15169[/green]")
        console.print("  • Force update database: [green]ipatel --update-db[/green]")
        console.print("  • Show version: [green]ipatel -v[/green]")
        console.print("\nRun [yellow]ipatel -h[/yellow] for full help.")

if __name__ == "__main__":
    main()
