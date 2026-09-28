import socket 

class Target :
    def __init__(self,ip_address,hostname) :
        self.ip_address = ip_address
        self.hostname = hostname
        self.open_ports = []


    def scan_port(self,port) : 
        print(f"[*] Scanning {self.ip_address} on port {port}")

        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((self.ip_address,port))

        print(f" [DEBUG] Result of scanning port {port} : {result}")

        if result == 0 :
            self.open_ports.append(port)
            print(f"[+] Port {port} is open")
        else :
            print(f"[-] Port {port} is closed")     

        s.close()


    def report (self) :
            print(f"\n---- Report for {self.ip_address} ({self.hostname})-----")
            print(f"[*] Open ports : {self.open_ports}")


class WebTarget (Target) :
    def __init__(self,ip_address,hostname,domain) :
        super().__init__(ip_address,hostname)
        self.domain = domain 
        self.vulnerabilities = []

    def check_sql_injection(self) :
        print(f"[*] Checking {self.domain} for SQL injection ......")
        self.vulnerabilities.append("SQL Injection")
        print(f"[+] SQL Injection vulnerability found on {self.domain}")


    def check_default_passwords(self) :
        print(f"[*] Checking {self.database_type} on {self.ip_address} for default passwords ......")
        self.default_credentials.append("Default Passwords")
        self.default_credentials = True 
        print(f"[!]WARNING: Default Passwords vulnerability found on {self.database_type}")




class DatabaseTarget(Target):
    def __init__(self,ip_address,hostname,database_type) :
        super().__init__(ip_address,hostname)
        self.database_type = database_type
        self.default_credentials = []

    def check_default_passwords(self) :
        print(f"[*] Checking {self.database_type} on {self.ip_address} for default passwords ......")
        self.default_credentials = True 
        print(f"[!]WARNING: Default Passwords vulnerability found on {self.database_type}")

    def report (self) :
        super().report()
        print(f"[*] Default credentials found : {self.default_credentials}")
        print(f"[*] Database type : {self.database_type}")





print("=" * 40)
print("   WELCOME TO SHARDUL'S SECURITY TOOL")
print("=" * 40)

while True:
    print("\nSelect an option:")
    print("1. Scan a Web Target")
    print("2. Scan a Database Target")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        ip = input("Enter IP address: ")
        host = input("Enter hostname: ")
        domain = input("Enter domain name: ")
        
        user_web = WebTarget(ip, host, domain)
        user_web.scan_port(80)
        user_web.scan_port(8000)
        user_web.scan_port(22)
        user_web.check_sql_injection()
        user_web.report()
        
    elif choice == "2":

        ip = input("Enter IP address: ")
        host = input("Enter hostname: ")
        db_type = input("Enter database type (e.g., MySQL, PostgreSQL): ")
        
        
        user_db = DatabaseTarget(ip, host, db_type)
        user_db.scan_port(3306) 
        user_db.check_default_passwords()
        user_db.report()
        
    elif choice == "3":
        print("Exiting the tool. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please select 1, 2, or 3.")