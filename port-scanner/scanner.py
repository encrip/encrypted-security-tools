"""Interactive TCP scanner. Python standard library only."""

import errno
import ipaddress
import os
import shutil
import socket
import sys
import time

PORTS = {21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS",
         3306: "MySQL", 8080: "HTTP alternate"}
COLOR = sys.stdout.isatty() and "NO_COLOR" not in os.environ and os.name != "nt"


def paint(text, color):
    codes = {"purple": 35, "cyan": 36, "green": 32, "yellow": 33, "dim": 90}
    return f"\033[{codes[color]}m{text}\033[0m" if COLOR else text


def rule():
    print(paint("─" * min(64, shutil.get_terminal_size().columns), "dim"))


def get_target():
    while True:
        value = input("  Target IPv4 [127.0.0.1] > ").strip() or "127.0.0.1"
        try:
            return str(ipaddress.IPv4Address(value))
        except ipaddress.AddressValueError:
            print(paint("  Enter a valid IPv4 address, such as 192.168.1.10.", "yellow"))


def scan_port(target, port, timeout=1.0):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
            connection.settimeout(timeout)
            result = connection.connect_ex((target, port))
        if result == 0:
            return "OPEN"
        if result in (errno.ECONNREFUSED, 10061):
            return "CLOSED"
        if result in (errno.ETIMEDOUT, errno.EAGAIN, 10060):
            return "NO RESPONSE"
        return "NETWORK ERROR"
    except socket.timeout:
        return "NO RESPONSE"
    except OSError:
        return "NETWORK ERROR"


def run_scan(target):
    print()
    rule()
    print(f"  TARGET  {target}    |    TCP    |    {len(PORTS)} ports")
    print("  Connection timeout: 1 second per port")
    rule()
    print(f"  {'PORT':<8}{'COMMON SERVICE':<20}STATUS")
    print()
    results = []
    started = time.monotonic()
    for number, (port, service) in enumerate(PORTS.items(), 1):
        if sys.stdout.isatty():
            print(f"  Checking {number}/{len(PORTS)}: TCP {port}...", end="", flush=True)
        status = scan_port(target, port)
        if sys.stdout.isatty():
            print("\r" + " " * 45 + "\r", end="")
        color = "green" if status == "OPEN" else "dim" if status == "CLOSED" else "yellow"
        print(f"  {port:<8}{service:<20}{paint(status, color)}", flush=True)
        results.append((port, status))
    rule()
    opened = [str(port) for port, status in results if status == "OPEN"]
    closed = sum(status == "CLOSED" for _, status in results)
    unknown = len(results) - len(opened) - closed
    print(paint(f"  Scan complete · {time.monotonic() - started:.1f}s", "cyan"))
    print(f"  Open: {len(opened)}    Closed: {closed}    Inconclusive: {unknown}")
    if opened:
        print("  Open TCP ports: " + ", ".join(opened))
    print("\n  Service labels are common port names, not detected services.")
    print("  No response can indicate filtering or a timeout.")
    rule()


def main():
    print()
    rule()
    print(paint("  ENCRYPTED / SECURITY TOOLS", "purple"))
    print("  TCP Port Scanner")
    rule()
    print("  Scan devices you own or have permission to test.")
    print("  Enter = this computer · Ctrl+C = exit\n")
    while True:
        run_scan(get_target())
        while True:
            choice = input("\n  Scan another target? [y/N] > ").strip().lower()
            if choice in ("", "n", "no"):
                print("\n  Session ended.\n")
                return
            if choice in ("y", "yes"):
                print()
                break
            print("  Please enter y or n.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n  Session cancelled.\n")
