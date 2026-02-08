from abc import ABC, abstractmethod
import copy

# Bad Example
# Target Interface
# Abstract class to represent an Email Template
class EmailTemplate(ABC):
    @abstractmethod
    def set_content(self, content):
        pass

    @abstractmethod
    def send(self, to):
        pass

# A concrete email class, hardcoded
class WelcomeEmail(EmailTemplate):
    def __init__(self):
        self.subject = "Welcome to TUF+"
        self.content = "Hi there! Thanks for joining us."

    def set_content(self, content):
        self.content = content

    def send(self, to):
        print(f"Sending to {to}: [{self.subject}] {self.content}")

if __name__ == "__main__":
    # Create a welcome email
    email1 = WelcomeEmail()
    email1.send("user1@example.com")

    # Suppose we want a similar email with slightly different content
    email2 = WelcomeEmail()
    email2.set_content("Hi there! Welcome to TUF Premium.")
    email2.send("user2@example.com")

    # Yet another variation
    email3 = WelcomeEmail()
    email3.set_content("Thanks for signing up. Let's get started!")
    email3.send("user3@example.com")


# Good Example
# ========== Defining the Prototype Interface ==========
class EmailTemplate:
    def clone(self):
        return copy.deepcopy(self)  # Recommended to perform deep copy

    def set_content(self, content):
        pass

    def send(self, to):
        pass

# Concrete Class implementing clone logic
class WelcomeEmail(EmailTemplate):
    def __init__(self):
        self.subject = "Welcome to TUF+"
        self.content = "Hi there! Thanks for joining us."

    def set_content(self, content):
        self.content = content

    def send(self, to):
        print(f"Sending to {to}: [{self.subject}] {self.content}")

# Template Registry to store and provide clones
class EmailTemplateRegistry:
    templates = {
        "welcome": WelcomeEmail(),
        # "discount": DiscountEmail(),
        # "feature-update": FeatureUpdateEmail(),
    }

    @staticmethod
    def get_template(type_):
        return EmailTemplateRegistry.templates[type_].clone()  # clone to avoid modifying original

# Driver code
if __name__ == "__main__":
    welcome_email1 = EmailTemplateRegistry.get_template("welcome")
    welcome_email1.set_content("Hi Alice, welcome to TUF Premium!")
    welcome_email1.send("alice@example.com")

    welcome_email2 = EmailTemplateRegistry.get_template("welcome")
    welcome_email2.set_content("Hi Bob, thanks for joining!")
    welcome_email2.send("bob@example.com")

    # Reuse the base WelcomeEmail structure, just changing dynamic content
