# Vulnerability Report for Flask App

## 1. Cross-Site Scripting (XSS)

- **Vulnerability**: Improper sanitization of user input allows attackers to inject malicious scripts.
- **Risk**: Attackers could execute arbitrary JavaScript on the user's browser, stealing cookies or session tokens.
- **Fix**: Used `escape()` function from the `markupsafe` module to sanitize user input in templates.
- **Impact**: Mitigates potential attacks like stealing user data or performing actions on behalf of the user.

## 2. Broken Authentication and Session Management

- **Vulnerability**: Session cookies were not secure, and authentication lacked proper management.
- **Risk**: Attackers could hijack user sessions or impersonate authenticated users.
- **Fix**: Implemented `Flask-Login` for secure session management and set `SESSION_COOKIE_SECURE=True` to enforce secure cookies.
- **Impact**: Stronger session handling and reduced risk of session hijacking.

## 3. Security Misconfigurations

- **Vulnerability**: The app had debugging enabled, exposing sensitive information in production.
- **Risk**: Exposing debugging information could allow attackers to find other vulnerabilities.
- **Fix**: Disabled debugging in production and removed sensitive configuration data.
- **Impact**: Prevents information leakage in a live environment.

## 4. Cross-Site Request Forgery (CSRF)

- **Vulnerability**: Application was vulnerable to CSRF attacks.
- **Risk**: Attackers could trick users into performing actions without their consent.
- **Fix**: Enabled CSRF protection using `Flask-WTF` and added CSRF tokens to forms.
- **Impact**: Mitigates CSRF attacks by ensuring all state-changing requests are properly validated.
