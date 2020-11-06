import nmap
import sys
import json

def mainMenu():
    print("This is an automated tool of Nmap")
    #time.sleep(1)
    print()

    choice = input("""
                        1: Scan all ports (1-45003).
                        2: Scan specific port.
                        3: Test
                        4: --------
                        5: --------
                        Please enter your choice: """)
    print()

    if choice == '1':
        addr = input("Ip: ")
        nmapScanPorts(addr)
    else:
        print("Wrong option")

        mainMenu()

def nmapScanPorts(addr):

    scanner = nmap.PortScanner()
    try:
        scanner.scan(addr, '22-200')
        ports = scanner[addr]['tcp'].keys()
        nmap_list = []
        for port in ports:
            report = {}
            state = scanner[addr]['tcp'][port]['state']
            service = scanner[addr]['tcp'][port]['name']
            product = scanner[addr]['tcp'][port]['product']
            report['port'] = port
            report['state'] = state
            report['service'] = service
            report['product'] = product

            if state == 'open':
                nmap_list.append(report)
        report = json.dumps(nmap_list)
        print(report)
    except Exception as e:
            print(e)
    mainMenu()

mainMenu()
