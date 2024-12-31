 ## Network Traffic Analysis with Wireshark

## Objective
The goal of this project is to develop a vulnerable Flask web application with common security flaws, including Cross-Site Scripting (XSS), SQL Injection, Broken Authentication, Security Misconfigurations, and Cross-Site Request Forgery (CSRF). After building the vulnerable application, we use Bandit, a static code analysis tool for Python, to identify and fix these vulnerabilities. The project demonstrates secure coding practices, vulnerability identification, and remediation techniques.

### Skills Learned/ Tools Used

- Flask web application development
- Identification and exploitation of common web vulnerabilities (XSS, SQL Injection, CSRF, etc.)
- Static code analysis using Bandit
- Fixing security vulnerabilities, including input sanitization and session management
- Secure coding practices to protect against attacks
- Using Flask for building web applications with security considerations
- Configuring Python and Bandit for vulnerability analysis
- Generating secure authentication and password management systems




## Steps
1. Create a Vulnerable Flask Application
Built a Flask app with several common vulnerabilities:

XSS: User input directly rendered without sanitization.
SQL Injection: Unsanitized user input used in SQL queries.
Broken Authentication: Session management without proper checks.
Security Misconfiguration: Exposed sensitive data like API keys.
CSRF: Vulnerable to CSRF attacks due to lack of protection.


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

In this project, I successfully installed and used Wireshark to capture and analyze network traffic. I learned how to apply filters, inspect individual packets, and follow TCP/UDP streams, developing a strong foundatio
