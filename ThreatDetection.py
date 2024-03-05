class CyberGuardInnovations:
    def __init__(self):
        self.users = {}  
        self.threats = []  

    def register_user(self, username, password):
        self.users[username] = {'password': password}

    def authenticate_user(self, username, password):
        if username in self.users and self.users[username]['password'] == password:
            return True
        else:
            return False

    def detect_threat(self, threat_type):
        self.threats.append(threat_type)

    def display_detected_threats(self):
        print("Detected Threats:")
        for threat in self.threats:
            print("- ", threat)

if __name__ == "__main__":
    cyber_guard = CyberGuardInnovations()

    cyber_guard.register_user("user1", "password123")

    if cyber_guard.authenticate_user("user1", "password123"):
        print("User authentication successful.")
    else:
        print("User authentication failed.")

    cyber_guard.detect_threat("Malware")
    cyber_guard.detect_threat("Phishing")

    cyber_guard.display_detected_threats()
