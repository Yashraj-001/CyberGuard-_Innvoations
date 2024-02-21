class CyberGuardInnovations:
    def __init__(self):
        self.users = {}  # Database for storing user information
        self.threats = []  # List to store detected threats

    def register_user(self, username, password):
        # Simulated user registration
        self.users[username] = {'password': password}

    def authenticate_user(self, username, password):
        # Simulated user authentication using password
        if username in self.users and self.users[username]['password'] == password:
            return True
        else:
            return False

    def detect_threat(self, threat_type):
        # Simulated threat detection
        self.threats.append(threat_type)

    def display_detected_threats(self):
        # Display detected threats
        print("Detected Threats:")
        for threat in self.threats:
            print("- ", threat)


# Sample usage
if __name__ == "__main__":
    # Create an instance of CyberGuardInnovations
    cyber_guard = CyberGuardInnovations()

    # Register a user
    cyber_guard.register_user("user1", "password123")

    # Authenticate the user
    if cyber_guard.authenticate_user("user1", "password123"):
        print("User authentication successful.")
    else:
        print("User authentication failed.")

    # Simulate threat detection
    cyber_guard.detect_threat("Malware")
    cyber_guard.detect_threat("Phishing")

    # Display detected threats
    cyber_guard.display_detected_threats()
