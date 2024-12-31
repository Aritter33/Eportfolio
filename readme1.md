 ## Flask Vulnerability Analysis and Security Fixes

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

![Screenshot 2024-12-31 155752](https://github.com/user-attachments/assets/116c0722-a1f4-4894-80a0-6b78ab997e0c)


##  2. Install Bandit and Run Security Analysis
Installed Bandit to scan Python files for security issues.

Ran Bandit to identify vulnerabilities like hardcoded credentials and unsafe coding practices.

Used Bandit’s output to address critical vulnerabilities in the codebase.
![Screenshot 2024-12-31 152317](https://github.com/user-attachments/assets/68ba095a-0029-4f54-83d3-1ace0ac5efdd)

## 3. Fix Vulnerabilities
Implemented security measures to fix the vulnerabilities:

XSS: Used Flask’s escape() function to sanitize user inputs.

SQL Injection: Switched to parameterized queries to prevent injection attacks.

Broken Authentication: Implemented secure session management.

Security Misconfiguration: Removed sensitive data from responses and environment variables.

CSRF: Added CSRF protection using Flask’s Flask-WTF extension.

Updated code to fix vulnerabilities

![Screenshot 2024-12-31 160726](https://github.com/user-attachments/assets/35bb9cb8-4292-4461-987b-26ec67038213)


##  4. Verify Fixes with Bandit
After making the necessary changes, I ran Bandit again to verify that the vulnerabilities were fixed and no new vulnerabilities were introduced.

![Screenshot 2024-12-31 152333](https://github.com/user-attachments/assets/3fa3e823-e9b1-4332-b7c8-caba5095071c)

## Created report identifying all vulnerabilities found

 ![Screenshot 2024-12-31 161133](https://github.com/user-attachments/assets/0bc4a0d3-b0d3-4309-b427-2cde8b8a7c0e)




## Conclusion

In this project, I developed a vulnerable Flask application to simulate common web security issues and then applied Bandit to identify and fix those vulnerabilities. By learning to secure applications against XSS, SQL injection, CSRF, and other attacks, I gained hands-on experience with Python web application security.

The project demonstrates the importance of implementing security best practices and using automated tools like Bandit for vulnerability analysis and continuous security improvement.
