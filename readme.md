 ## Network Intrusion Detection with Snort
## Objective
The aim of this project is to download, install, and configure Snort to monitor and analyze network traffic in real-time, using pre-defined and custom rules to detect intrusions. This also includes launching a SYN flood attack simulation using Kali Linux to demonstrate Snort’s effectiveness in identifying and logging potential threats.
### Skills Learned/ Tools Used
- Snort installation, configuration, and rule management
- Network traffic analysis through real-time monitoring and logging
- Creation and customization of Snort rules for specific threats
- Detection of TCP-based SYN flood attacks
- Use of Kali Linux for launching network attacks
- Intrusion detection and packet inspection at multiple layers (Ethernet, IP, TCP)
- Advanced tools like unified logging and alert management
- Network security troubleshooting and identification of malicious activities
- Understanding of Snort's rule syntax and optimization for better performance
## Steps
## Install Wireshark
Used the package manager to install Wireshark![Screenshot 2024-09-20 190604](https://github.com/user-attachments/assets/055ccc9e-00b7-4a03-8579-4de12141e3c6)
##  Launch Wireshark 
 Launched Wireshark by typing the command in the terminal. ![Screenshot 2024-09-20 190629](https://github.com/user-attachments/assets/b284eb3d-3fc4-481a-93d4-c350ba06d75b)
 
## Capture Network Traffic
Started scanning the network. ![Screenshot 2024-09-20 190705](https://github.com/user-attachments/assets/648c06a4-d373-43a0-b0ab-2548eada4491)
##  Analyze Network Traffic
Used display filters to focus on specific types of traffic. ![Screenshot 2024-09-20 190805](https://github.com/user-attachments/assets/d663ba24-3cf1-47a1-958f-648b060fa760)
## Test for HTTP Credentials in Plain Text
While capturing HTTP traffic, I visited a website that uses HTTP (not HTTPS) for login credentials.![Screenshot 2024-09-20 185031](https://github.com/user-attachments/assets/f11d97eb-d817-4100-8cb6-421693772691)
In the stream, I inspect the HTTP request to see if the username and password were transmitted in plaintext. If HTTP is used, credentials may be visible directly in the payload wich was proven correctly through wireshark.![Screenshot 2024-09-20 185012](https://github.com/user-attachments/assets/7bf40b1d-b48b-4efc-8136-cc6d03d556bc)
## Conclusion
In this project, I successfully installed and used Snort as a network intrusion detection system. By applying and modifying Snort rules, I was able to detect and log suspicious activity, specifically a SYN flood attack simulated using Kali Linux. This demonstrated Snort’s ability to monitor, identify, and respond to network-based threats, which is essential for protecting network infrastructure from malicious attacks.
