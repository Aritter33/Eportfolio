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
## Install Snort
Followed Tutorial found on Snorts website and verified the correct version was installed. ![Screenshot 2024-10-01 200240](https://github.com/user-attachments/assets/649ba0b2-b102-4138-bea1-2cdd9ec43003)


##  Configure Snort Rules 
Downloaded Snorts community rules also found on their website.![Screenshot 2024-10-01 200217](https://github.com/user-attachments/assets/e5cdcc05-20e6-4ef3-87b9-b52082fd963c)



## Launch Snort
Ensured there were no errors with the rules i configured and launched snort![Screenshot 2024-10-01 205017](https://github.com/user-attachments/assets/349134d9-d8bb-4f79-a465-c14deef140ca)




## Simulate SYN Flood Attack Using Kali Linux
Launched a SYN flood attack from Kali Linux, sending large numbers of connection requests to overwhelm the target system.![Screenshot 2024-10-01 205231](https://github.com/user-attachments/assets/9452b661-fdcb-4a78-a3b2-f0088909643e)


## Analyze Network Traffic with Snort
Used Snort’s alert system to verify that the SYN flood attack was identified and logged appropriately. This verified that the intrusion detection system (IDS) was working as expected.![Screenshot 2024-10-01 200523](https://github.com/user-attachments/assets/96e30419-3989-47b3-a866-cb2c89e3d906)


## Conclusion
In this project, I successfully installed and used Snort as a network intrusion detection system. By applying and modifying Snort rules, I was able to detect and log suspicious activity, specifically a SYN flood attack simulated using Kali Linux. This demonstrated Snort’s ability to monitor, identify, and respond to network-based threats, which is essential for protecting network infrastructure from malicious attacks.
