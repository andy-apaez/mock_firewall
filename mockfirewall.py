import random


def generate_random_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"


def mock_firewall_rules(ip, rule):
    for rule_ip, action in rule.items():
        if rule_ip == ip:
            return action
    return "ALLOW"


def main():
    firewall_rules = {
        "192.168.1.1": "DENY",
        "10.0.0.1": "DENY",
        "172.16.0.1": "DENY",
        "192.168.0.1": "DENY"
    }

    for _ in range(10):
        random_ip = generate_random_ip()
        action = mock_firewall_rules(random_ip, firewall_rules)
        random_number = random.randint(1, 9999)
        print(f"IP: {random_ip}, Action: {action}, Random Number: {random_number}")

if __name__ == "__main__":
    main()
