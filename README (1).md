   ## Network Security

## Objective


The objective of this project was to gain hands-on experience with network security by simulating a network attack using Kali Linux and defending against it with firewall configurations on an Ubuntu VM. The project involved updating and configuring both virtual machines, setting up security tools, and documenting the network environment through a diagram and detailed configuration records. This exercise enhanced system administration skills, familiarized me with network defense strategies, and deepened my understanding of Linux-based tools.

### Skills Learned


- System administration with Linux (Kali Linux and Ubuntu)
- Installing and updating software packages using command-line tools
- Configuring firewalls (UFW) to secure a network
- Simulating network attacks using Kali Linux
- Defending against network attacks using firewall configurations
- Creating and documenting network diagrams


### Tools Used


- Kali Linux VM
- Ubuntu VM
- Build-essential, git, curl
- Nmap, Wireshark, Metasploit framework
- UFW (Uncomplicated Firewall)

## Steps
System Setup:
Updated and upgraded both the Kali Linux and Ubuntu VMs. ![Screenshot 2024-09-17 191947](https://github.com/user-attachments/assets/88bf7f81-ac2f-473b-8d29-f1f725ec2bd1)
Installed essential tools like build-essential, git, curl on both VMs. ![Screenshot 2024-09-17 192031](https://github.com/user-attachments/assets/214af1f4-f309-49ee-aaad-bf3c67104782)
Installed additional network security tools (Nmap, Wireshark, Metasploit) on Kali Linux. ![Screenshot 2024-09-17 192125](https://github.com/user-attachments/assets/89c72a20-197c-4ae3-81ba-824e1affb784)
## Network Attack Simulation:
Ran a simple Nmap scan from Kali Linux against the Ubuntu VM. ![Screenshot 2024-09-17 192647](https://github.com/user-attachments/assets/752a22e7-812f-4f67-9ec7-3bc454984f83)
## Defense Against Attacks 
Installed and configured UFW on the Ubuntu VM. ![Screenshot 2024-09-17 192951](https://github.com/user-attachments/assets/525f3c06-eba1-47e6-b4f4-80008b635b5c)
Allowed SSH and set firewall rules to allow traffic from the Kali Linux VM IP.![Screenshot 2024-09-17 193055](https://github.com/user-attachments/assets/753c0174-5cd4-43ab-b702-27a9021f5476)
## Documentation 
Verified attack was succesful by using Wireshark ![Screenshot 2024-09-17 193816](https://github.com/user-attachments/assets/91b9fdae-593d-40fd-a8ab-42008499cca6)
