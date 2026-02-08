import java.util.*;

abstract class NotificationSender {
    public final void send(String to, String message) {
        rateLimitCheck(to);
        validateRecipient(to);
        String formatted = formatMessage(message);
        preSendAuditLog(to, formatted);

        String composedMessage = composeMessage(formatted);
        sendMessage(to, composedMessage);
        
        postSendAnalytics(to);
    }

    private void rateLimitCheck(String to) {
        System.out.println("Checking rate limit for: "+ to);
    }

    private void validateRecipient(String to) {
        System.out.println("Validating email recipiient: "+ to);
    }

    private String formatMessage(String message) {
        return message.trim();
    }

    private void preSendAuditLog(String to, String formatted) {
        System.out.println("Logging before send: "+ formatted + " to "+ to);
    }

    protected abstract String composeMessage(String formattedMessage);

    protected abstract void sendMessage(String to, String message);

    protected void postSendAnalytics(String to) {
        System.out.println("Analytics updated for: "+ to);
    }
}

class EmailNotification extends NotificationSender {
    @Override
    protected String composeMessage(String formattedMessage) {
        return "<html><body><p>" + formattedMessage + "</p></body></html>";
    }

    @Override
    protected void sendMessage(String to, String message) {
        System.out.println("Sending EMAIL to " + to + " with content:\n" + message);
    }
}

class SMSNotification extends NotificationSender {
    // Implement message composition for SMS
    @Override
    protected String composeMessage(String formattedMessage) {
        return "[SMS] " + formattedMessage;
    }

    // Implement SMS sending logic
    @Override
    protected void sendMessage(String to, String message) {
        System.out.println("Sending SMS to " + to + " with message: " + message);
    }

    // Override optional hook for custom SMS analytics
    @Override
    protected void postSendAnalytics(String to) {
        System.out.println("Custom SMS analytics for: " + to);
    }
}

class Main {
    public static void main(String[] args) {
        NotificationSender emailNotification = new EmailNotification();
        emailNotification.send("example@example.com", "Your order has been placed!");

        NotificationSender smsNotification = new SMSNotification();
        smsNotification.send("1234567890", "Your OTP is 1234.");
    }
}