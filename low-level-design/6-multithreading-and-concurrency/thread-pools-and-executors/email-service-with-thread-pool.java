import java.util.concurrent.*;

class EmailService {
    private static final ExecutorService exectuor = Executors.newFixedThreadPool(10);

    public static void sendEmail(String recipient) {
        exectuor.execute(() -> {
            System.out.println("Sending email to " + recipient + " on " + Thread.currentThread().getName());
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                System.out.println("Email sent to " + recipient + " on " + Thread.currentThread().getName());
            }
        });
    }

    public static void main(String[] args) {
        for (int i = 0; i < 25; i++) {
            EmailService.sendEmail("user" + i + "@example.com");
        }

        exectuor.shutdown();
    }
}