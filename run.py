from honeypot import ssh_honey, http_honey

print("""
[1] Run SSH Honeypot
[2] Run HTTP Honeypot
""")

choice = input("Select honeypot to start: ")

if choice == "1":
    ssh_honey.start_ssh_honeypot()
elif choice == "2":
    http_honey.start_http_honeypot()
else:
    print("Invalid option.")
