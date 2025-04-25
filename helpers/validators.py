import requests

# Load a blacklist from a public source
BLACKLIST_URL = "https://raw.githubusercontent.com/disposable-email-domains/disposable-email-domains/master/disposable_email_blocklist.conf"
DISPOSABLE_DOMAINS = set()

def load_blacklist():
    try:
        response = requests.get(BLACKLIST_URL)
        DISPOSABLE_DOMAINS.update(line.strip() for line in response.text.splitlines() if line.strip())
        print("Blacklist loaded")
    except Exception as e:
        print(f"Error loading blacklist: {e}")

def is_temp_email(email):
    domain = email.split('@')[1].lower()
    if domain in DISPOSABLE_DOMAINS:
        print(f"Rejected: {domain} is a known temporary email domain")
        return True
    print(f"Accepted: {domain} not flagged as temporary")
    return False

# Load the list once (could be scheduled or run at app startup)
# load_blacklist()

# # Test it
# email = "genaji2168@lxheir.com"
# if is_temp_email(email):
#     print("Signup blocked")
# else:
#     print("Signup allowed")