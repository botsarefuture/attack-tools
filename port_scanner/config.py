def define_ports() -> list:
    # Defining ports

    ports = []

    ports.append(20)  # Add FTP port
    ports.append(21)  # Add second FTP port
    ports.append(22)  # Add SSH and SFTP port
    ports.append(23)  # Add TELNET port
    ports.append(25)  # Add SMPT port
    ports.append(53)  # Add DNS port
    ports.append(69)  # Add TFTP port
    ports.append(80)  # Add HTTP port
    ports.append(110)  # Add POP3 port
    ports.append(119)  # Add NNTP port
    ports.append(123)  # Add NTP port
    ports.append(137)  # Add NetBIOS Name Service
    ports.append(139)  # Add NetBios Datagram service
    ports.append(143)  # Add IMAP port
    ports.append(161)  # Add SNMP port
    ports.append(194)  # Add IRC port
    ports.append(443)  # Add HTTPS port
    ports.append(445)  # Add ActiveDirectory port and SMB port
    ports.append(8080)  # Add second HTTP port
    ports.append(8443)  # Add second HTTPS port

    return ports

ports = define_ports()
