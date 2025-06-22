import subprocess

def test_ip_lookup():
    result = subprocess.run(
        ["ipatel", "-i", "8.8.8.8"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    assert "8.8.8.8" in result.stdout
    assert "asn" in result.stdout.lower()

def test_asn_lookup():
    result = subprocess.run(
        ["ipatel", "-a", "15169"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    assert "ASN 15169" in result.stdout
    assert "IP Range" in result.stdout or "IP Ranges" in result.stdout

def test_help_message():
    result = subprocess.run(
        ["ipatel"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    assert "usage" in result.stdout.lower()
