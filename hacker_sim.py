#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Hacker Terminal Simulation - Af Soomaali
# TikTok Content Tool - Simulation Kaliya

import time
import random
import sys
import os

# Midabada terminal
class C:
    GREEN  = '\033[92m'
    RED    = '\033[91m'
    YELLOW = '\033[93m'
    CYAN   = '\033[96m'
    WHITE  = '\033[97m'
    BOLD   = '\033[1m'
    DIM    = '\033[2m'
    RESET  = '\033[0m'
    BLINK  = '\033[5m'

def type_text(text, delay=0.03, color=C.GREEN):
    """Si tartiib ah u muuji qoraalka"""
    print(color, end='', flush=True)
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print(C.RESET)

def fast_text(text, color=C.GREEN):
    print(f"{color}{text}{C.RESET}")

def pause(s=1.0):
    time.sleep(s)

def clear():
    os.system('clear')

def header():
    clear()
    print(f"{C.CYAN}{C.BOLD}")
    print("=" * 60)
    print("   NIDAAMKA AMNIGA SOOMAALIYA  v2.4.1")
    print("   Xarunta Xogta Qaranka — Muqdisho, SO")
    print("=" * 60)
    print(f"{C.RESET}")
    pause(0.5)

# ─── Emailo fake ah ───
EMAILS = [
    "axmed.cali@gov.so",
    "fadumo.xasan@somtelecom.net",
    "cabdullahi.omar@ministry.so",
    "hodan.muuse@dalmar.com.so",
    "xasan.warsame@nisa.gov.so",
    "faadumo.ahmed@hormuud.so",
    "ciise.jaamac@puntland.gov.so",
    "nimco.duale@sombank.so",
]

# ─── IP Addresses fake ───
def fake_ip():
    return f"196.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"

def fake_coords():
    # Xadka Soomaaliya
    lat = round(random.uniform(2.0, 11.5), 4)
    lon = round(random.uniform(41.0, 51.4), 4)
    return lat, lon

# ─── Scene 1: Sawir radar ah ───
def scene_radar():
    header()
    type_text(">> Radar Xakamaynta Hawada La'aanta — MOGADISHU CTR", delay=0.04, color=C.CYAN)
    pause(0.5)

    cities = ["Muqdisho", "Kismaayo", "Boosaaso", "Hargeysa", "Garoowe", "Berbera"]
    flights = ["SL-401", "QC-117", "ET-882", "SO-204", "KQ-551", "FJ-303"]

    print(f"\n{C.DIM}{'─'*60}{C.RESET}")
    fast_text(f"{'DUULIMAAD':<12} {'MAGAALO':<14} {'JOOGITAAN':<18} {'XAALAD'}", C.YELLOW)
    print(f"{C.DIM}{'─'*60}{C.RESET}")

    for i, (fl, city) in enumerate(zip(flights, cities)):
        lat, lon = fake_coords()
        speed = random.randint(420, 890)
        alt   = random.randint(8000, 39000)
        status = random.choice(["✓ CAADI", "✓ CAADI", "✓ CAADI", "⚠ HUBI"])
        color  = C.GREEN if "CAADI" in status else C.YELLOW
        print(f"{color}{fl:<12} {city:<14} {lat}°N {lon}°E  {status}{C.RESET}")
        time.sleep(0.3)

    pause(1)
    print(f"\n{C.DIM}{'─'*60}{C.RESET}")
    type_text(f">> Diyaaradaha la socda: {len(flights)}", color=C.GREEN)
    type_text(">> Xaalad: CAADI — Khatar ma jirto", color=C.GREEN)
    pause(2)

# ─── Scene 2: Emailo scan ───
def scene_email_scan():
    header()
    type_text(">> Xarunta Xogta Email — Baaritaan Socda...", delay=0.04, color=C.CYAN)
    pause(0.8)

    print(f"\n{C.DIM}{'─'*55}{C.RESET}")
    fast_text(f"  {'EMAIL':<32} {'XAALAD'}", C.YELLOW)
    print(f"{C.DIM}{'─'*55}{C.RESET}\n")

    for email in EMAILS:
        time.sleep(random.uniform(0.15, 0.45))
        action = random.choice([
            f"{C.GREEN}✓ AMMAAN",
            f"{C.GREEN}✓ AMMAAN",
            f"{C.GREEN}✓ AMMAAN",
            f"{C.YELLOW}⚠ HUBI   ",
            f"{C.RED}✗ XAD-GUDUB",
        ])
        print(f"  {C.WHITE}{email:<32}{C.RESET} {action}{C.RESET}")

    pause(1)
    print(f"\n{C.DIM}{'─'*55}{C.RESET}")
    fast_text(f"\n  Wadarta: {len(EMAILS)} email la baaray", C.CYAN)
    fast_text(f"  Khatar: 1 la helay — La xareeyay", C.YELLOW)
    pause(2)

# ─── Scene 3: Access Denied ───
def scene_access():
    header()
    type_text(">> Isku xirka Nidaamka Qaranka...", delay=0.05, color=C.CYAN)
    pause(0.5)

    steps = [
        ("Xiriirka shabakadda", True),
        ("Xaqiijinta SSL", True),
        ("Aqoonsiga isticmaalaha", True),
        ("Oggolaanshaha heerka A1", False),
        ("Gelitaanka xogta qaranka", False),
    ]

    print()
    for step, success in steps:
        time.sleep(0.6)
        if success:
            fast_text(f"  [  OK  ]  {step}", C.GREEN)
        else:
            time.sleep(0.4)
            fast_text(f"  [DIIDO ]  {step}", C.RED)

    pause(0.8)
    print(f"\n{C.RED}{C.BOLD}")
    print("  ╔══════════════════════════════════════╗")
    print("  ║                                      ║")
    print("  ║      GELITAANKA WAXAA DIIDEY         ║")
    print("  ║      ACCESS DENIED — FASAX MA LIHID  ║")
    print("  ║                                      ║")
    print("  ╚══════════════════════════════════════╝")
    print(C.RESET)
    fast_text(f"  Dhacdada waxaa la diiwaan geliyay: {fake_ip()}", C.DIM)
    fast_text(f"  Waqtiga: {time.strftime('%Y-%m-%d %H:%M:%S')}", C.DIM)
    pause(2)

# ─── Scene 4: Network map ───
def scene_network():
    header()
    type_text(">> Khariidada Shabakadda — Soomaaliya NOC", delay=0.04, color=C.CYAN)
    pause(0.6)

    nodes = [
        ("Muqdisho-CORE", "196.201.0.1",  "ONLINE",  "94%"),
        ("Kismaayo-HUB",  "196.201.1.5",  "ONLINE",  "71%"),
        ("Garoowe-HUB",   "196.201.2.3",  "ONLINE",  "88%"),
        ("Hargeysa-HUB",  "196.201.3.7",  "ONLINE",  "65%"),
        ("Boosaaso-NODE", "196.201.4.2",  "ONLINE",  "52%"),
        ("Baydhabo-NODE", "196.201.5.9",  "OFFLINE", "0%"),
    ]

    print(f"\n{C.DIM}{'─'*62}{C.RESET}")
    fast_text(f"  {'NODE':<18} {'IP':<18} {'XAALAD':<10} {'LOAD'}", C.YELLOW)
    print(f"{C.DIM}{'─'*62}{C.RESET}\n")

    for name, ip, status, load in nodes:
        time.sleep(0.35)
        color = C.GREEN if status == "ONLINE" else C.RED
        sym   = "●" if status == "ONLINE" else "○"
        print(f"  {color}{sym} {name:<17} {ip:<18} {status:<10} {load}{C.RESET}")

    pause(1)
    print(f"\n{C.DIM}{'─'*62}{C.RESET}")
    fast_text("  Wadarta nodes: 6  |  Online: 5  |  Offline: 1", C.CYAN)
    type_text(">> Wargelin: Baydhabo-NODE xiriirka kuma jirto", color=C.YELLOW)
    pause(2)

# ─── Xulashada muuqaalka ───
def menu():
    clear()
    print(f"{C.CYAN}{C.BOLD}")
    print("╔══════════════════════════════════════╗")
    print("║   TERMINAL SIM — TIKTOK CONTENT      ║")
    print("║   Af Soomaali | Simulation Kaliya    ║")
    print("╚══════════════════════════════════════╝")
    print(C.RESET)
    print(f"{C.GREEN}  [1]{C.RESET} Radar Diyaaradaha")
    print(f"{C.GREEN}  [2]{C.RESET} Baaritaanka Emailada")
    print(f"{C.GREEN}  [3]{C.RESET} Access Denied Scene")
    print(f"{C.GREEN}  [4]{C.RESET} Khariidada Shabakadda")
    print(f"{C.GREEN}  [5]{C.RESET} Dhammaan si toos ah (TikTok mode)")
    print(f"{C.RED}  [0]{C.RESET} Ka bax\n")

def tiktok_mode():
    """Dhammaan scenes si joogto ah"""
    scene_radar()
    scene_email_scan()
    scene_access()
    scene_network()
    clear()
    fast_text("\n  ✓ Muuqaalka wuu dhamaaday — Ku kaydi TikTok!", C.CYAN)
    fast_text("  Simulation kaliya — Xog dhab ah ma jirto\n", C.DIM)

def main():
    while True:
        menu()
        choice = input(f"{C.GREEN}>> Xulo: {C.RESET}").strip()
        if   choice == "1": scene_radar()
        elif choice == "2": scene_email_scan()
        elif choice == "3": scene_access()
        elif choice == "4": scene_network()
        elif choice == "5": tiktok_mode()
        elif choice == "0":
            fast_text("\nNabad gelyo!\n", C.CYAN)
            break
        else:
            fast_text("Xulo 0-5 dhexdooda\n", C.YELLOW)
        input(f"\n{C.DIM}Riix Enter si aad u sii waddo...{C.RESET}")

if __name__ == "__main__":
    main()
