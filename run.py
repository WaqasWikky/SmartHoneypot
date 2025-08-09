from honeypot import ssh_honey, http_honey

while True:
    print("""
[1] Run SSH Honeypot
[2] Run HTTP Honeypot
[0] Exit
""")

    choice = input("Select honeypot to start: ")

    if choice == "1":
        try:
            ssh_honey.start_ssh_honeypot()
        except KeyboardInterrupt:
            print("\n[!] SSH Honeypot stopped. Returning to menu...\n")

    elif choice == "2":
        try:
            http_honey.start_http_honeypot()
        except KeyboardInterrupt:
            print("\n[!] HTTP Honeypot stopped. Returning to menu...\n")

    elif choice == "0":
        print("Exiting...")
        break

    else:
        print("Invalid option. Please try again.")
