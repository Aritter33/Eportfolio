 ## Network Traffic Analysis with Wireshark

## Objective

The aim of this project is to install, configure, and use Wireshark to capture and analyze network traffic in real-time, applying filters to focus on specific data and protocols, including testing for potential security risks like exposed credentials in HTTP traffic.

### Skills Learned/ Tools Used

- Wireshark installation, configuration, and usage
- Network traffic analysis through packet capture and inspection
- Protocol filtering using Wireshark’s filtering language
- TCP/UDP stream analysis to follow and inspect specific network conversations
- Packet inspection at multiple layers (Ethernet, IP, TCP, HTTP)
- Advanced tools like Protocol Hierarchy, Conversations, and Endpoints
- Network troubleshooting and identifying potential security issues
- Identifying security risks, including plaintext transmission of credentials over HTTP




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

In this project, I successfully installed and used Wireshark to capture and analyze network traffic. I learned how to apply filters, inspect individual packets, and follow TCP/UDP streams, developing a strong foundation in network traffic analysis. I also tested HTTP traffic for exposed usernames and passwords in plaintext, highlighting the security risks associated with unencrypted HTTP connections. By exploring advanced Wireshark tools, I gained deeper insights into network protocols and communication patterns, essential for diagnosing network issues and enhancing cybersecurity efforts.
