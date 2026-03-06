class Main {
    public static void main(String[] args) {
        SMSThread smsThread = new SMSThread();
        EmailThread emailThread = new EmailThread();
        ETAThread etaThread = new ETAThread();

        System.out.println("Task Started. \n");

        smsThread.start();
        System.out.println("Task 1 started. \n");
        emailThread.start();
        System.out.println("Task 2 started. \n");
        etaThread.start();
        System.out.println("Task 3 started. \n");

        try {
            smsThread.join();
            emailThread.join();
            etaThread.join();
            System.out.println("Task Completed. \n");
        } catch(InterruptedException e) {
            e.printStackTrace();
        }
    }
}

class SMSThread extends Thread {
    public void run() {
        try {
            Thread.sleep(2000);
            System.out.println("SMS sent using Thread.");
        } catch(InterruptedException e) {
            e.printStackTrace();
        }
    }
}

class EmailThread extends Thread {
    public void run() {
        try {
            Thread.sleep(3000);
            System.out.println("Email sent using Thread.");
        } catch(InterruptedException e) {
            e.printStackTrace();
        }
    }
}

class ETAThread extends Thread {
    public void run() {
        try {
            Thread.sleep(5000);
            System.out.println("ETA calculated using Thread.");
        } catch(InterruptedException e) {
            e.printStackTrace();
        }
    }
}