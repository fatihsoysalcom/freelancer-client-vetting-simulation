import random

class Freelancer:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
        self.rating = 5.0

    def __str__(self):
        return f"{self.name} (Skills: {', '.join(self.skills)}, Rating: {self.rating:.1f})"

class Client:
    def __init__(self, name, project_requirements):
        self.name = name
        self.project_requirements = project_requirements
        self.verified = False

    def __str__(self):
        status = "Verified" if self.verified else "Unverified"
        return f"{self.name} (Requirements: {', '.join(self.project_requirements)}, Status: {status})"

def simulate_project_match(freelancer, client):
    """Simulates a project match based on skills and client verification."""
    print(f"\nAttempting to match {freelancer.name} with {client.name}...")

    # Core concept: Freelancers prefer verified clients to mitigate risk.
    # Unverified clients pose a higher risk of payment issues, scope creep, etc.
    if not client.verified:
        print(f"  -> {client.name} is UNVERIFIED. This increases risk for {freelancer.name}.")
        # Simulate a lower chance of acceptance or a higher risk perception
        risk_factor = random.uniform(0.5, 1.0) # Higher risk factor for unverified clients
        if random.random() < 0.3 * risk_factor: # Lower chance of accepting
            print(f"  -> {freelancer.name} is hesitant due to unverified client. Project declined.")
            return False
        else:
            print(f"  -> {freelancer.name} accepts despite risk, but with caution.")
            # Simulate potential negative outcome due to risk
            if random.random() < 0.2 * risk_factor:
                print(f"  -> Project with {client.name} encountered issues due to lack of verification.")
                freelancer.rating = max(0.0, freelancer.rating - 0.5)
            return True
    else:
        print(f"  -> {client.name} is VERIFIED. Lower risk for {freelancer.name}.")
        # Simulate a higher chance of acceptance for verified clients
        if random.random() < 0.8:
            print(f"  -> {freelancer.name} happily accepts the project with {client.name}.")
            # Simulate positive outcome for good matches
            if all(skill in freelancer.skills for skill in client.project_requirements):
                freelancer.rating = min(5.0, freelancer.rating + 0.2)
            return True
        else:
            print(f"  -> Project with {client.name} did not proceed for other reasons.")
            return False

# --- Setup --- 

# Freelancers with different skill sets
freelancer1 = Freelancer("Alice", ["Python", "Web Development", "API Design"])
freelancer2 = Freelancer("Bob", ["JavaScript", "React", "UI/UX Design"])
freelancer3 = Freelancer("Charlie", ["Python", "Data Science", "Machine Learning"])

# Clients with varying verification status and project needs
client_a = Client("Alpha Corp", ["Python", "API Design"])
client_a.verified = True  # This client has been vetted

client_b = Client("Beta Solutions", ["JavaScript", "React"])
client_b.verified = False # This client has NOT been vetted

client_c = Client("Gamma Innovations", ["Python", "Data Science"])
client_c.verified = True

client_d = Client("Delta Enterprises", ["Java", "Backend Development"])
client_d.verified = False

# --- Simulation --- 

print("--- Freelancer Client Vetting Simulation ---")

# Scenario 1: Verified client with matching skills
freelancer_list = [freelancer1, freelancer3]
client_list = [client_a, client_c]

for client in client_list:
    for freelancer in freelancer_list:
        simulate_project_match(freelancer, client)

# Scenario 2: Unverified client with matching skills
freelancer_list = [freelancer1, freelancer2]
client_list = [client_b, client_d]

for client in client_list:
    for freelancer in freelancer_list:
        simulate_project_match(freelancer, client)

print("\n--- Final Freelancer Status ---")
print(freelancer1)
print(freelancer2)
print(freelancer3)
