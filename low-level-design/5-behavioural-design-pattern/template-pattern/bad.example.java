import java.util.*;

class EmailNotification {
    public void send(String to, String message) {
        System.out.println("Checking rate limit for: "+ to);
        System.out.println("Validating email recipiient: "+ to);
        String formatted = message.trim();
        System.out.println("Logging before send: "+ formatted + " to "+ to);

        String composeMessage = "<html><body><p>" + formatted + "</p></body></html>";
        System.out.println("Sending EMAIL to " + to + " with content:\n" + composeMessage);

        System.out.println("Analytics updated for: "+ to);
    }
}

// SMSNotification handles sending SMS messages
class SMSNotification {

    public void send(String to, String message) {
        System.out.println("Checking rate limits for: " + to);
        System.out.println("Validating phone number: " + to);
        String formatted = message.trim();
        System.out.println("Logging before send: " + formatted + " to " + to);

        // Compose SMS
        String composedMessage = "[SMS] " + formatted;

        // Send SMS
        System.out.println("Sending SMS to " + to + " with message: " + composedMessage);

        // Analytics (custom)
        System.out.println("Custom SMS analytics for: " + to);
    }
}

class Main {
    public static void main(String[] args) {
        // Create objects for both notification services
        EmailNotification emailNotification = new EmailNotification();
        SMSNotification smsNotification = new SMSNotification();

        // Sending email notification
        emailNotification.send("example@example.com", "Your order has been placed!");
        
        System.out.println(" ");
        
        // Sending SMS notification
        smsNotification.send("1234567890", "Your OTP is 1234.");
    }
}