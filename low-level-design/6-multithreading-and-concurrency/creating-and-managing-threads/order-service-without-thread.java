class OrderService {
    public static void main(String[] args) {
        System.out.println("Placing order...\n");

        sendSMS();
        System.out.println("Task 1 done. \n");

        sendEmail();
        System.out.println("Task 2 done. \n");

        String eta = calculateETA();
        System.out.println("Order placed. Estimated Time of Arrival: " + eta);
        System.out.println("Task 3 done. \n");
    }

    private static void sendSMS() {
        try {
            Thread.sleep(2000);
            System.out.println("Sending SMS...");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private static void sendEmail() {
        try {
            Thread.sleep(3000);
            System.out.println("Sending Email...");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    
    private static String calculateETA() {
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return "25 minutes";
    }
}

class Main {
    public static void main(String[] args) {
        OrderService.main(args);
    }
}