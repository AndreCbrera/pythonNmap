import nmap
import sys

print("Esto es una herramienta automatizada de Nmap")
print("############################################")

def mainMenu():
    """mainMenu
        1- Port scan
    """
    addr = input("Introduzca una ip: ")
    print("Has introducido es: ", addr)
    type(addr)

    resp = input("""\n Opciones a elegir
                    1.- Escaneo de puertos \n""")

    print("########################################")

    if resp == '1':
        nmapScanPorts(addr)
    else:
        print("Acción erronea")
        mainMenu()
"""
    Scan for a single host
"""
def nmapScanPorts(addr):

    scanner = nmap.PortScanner()
    scanner.scan(addr, '1-45003', '-P')
    print("Version nmap:  ", scanner.nmap_version())
    print("Host: %s (%s)"% (addr, scanner[addr].hostname()))
    print("Disponibilidad: %s" % scanner[addr].state())

    for protocol in scanner[addr].all_protocols():
        print('----------------------------------')
        print('Protocolo : %s' % protocol)
        lport = scanner[addr][protocol].keys()
        lports = sorted(lport)
        for ports in lports:
            print('Puerto : %s\tEstado : %s' % (ports, scanner[addr][protocol][ports]['state']))
        print('----------------------------------')
    mainMenu()


mainMenu()
