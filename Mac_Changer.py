import subprocess

interface = raw_input("Choose Your Interface >")
New_Mac = raw_input("Enter Your New_Mac >")

print("[+] Changing Mac_Address for" + interface + "to" + New_Mac)

subprocess.call( ["ifconfig", interface, "down"] )
subprocess.call( ["ifconfig", interface, "hw", "ether", New_Mac] )
subprocess.call( ["ifconfig", interface, "up"] )