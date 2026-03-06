import java.util.concurrent.Callable;
import java.util.concurrent.FutureTask;
import java.util.concurrent.ExecutionException;

class Main {
    public static void main(String[] args) {
        FutureTask<String> etaTask = new FutureTask<>(new ETACalculationTask());

        SMSDeliveryTask smsDeliveryTask = new SMSDeliveryTask();
        EmailDeliveryTask emailDeliveryTask = new EmailDeliveryTask();

        Thread etaThread = new Thread(etaTask);
        Thread smsDeliveryThread = new Thread(smsDeliveryTask);
        Thread emailDeliveryThread = new Thread(emailDeliveryTask);

        System.out.println("Task Started. \n");

        etaThread.start();
        System.out.println("Task 1 started. \n");
        smsDeliveryThread.start();
        System.out.println("Task 2 started. \n");
        emailDeliveryThread.start();
        System.out.println("Task 3 started. \n");
        
        try {
            String eta = etaTask.get();
            System.out.println("ETA: " + eta);
        } catch(InterruptedException e) {
            e.printStackTrace();
        } catch(ExecutionException e) {
            e.printStackTrace();
        }
    }
}

class ETACalculationTask implements Callable<String> {
    public String call() throws InterruptedException {
        Thread.sleep(5000);
        System.out.println("ETA calculated");
        return "25 minutes";
    }
}

class SMSDeliveryTask implements Runnable {
    public void run() {
        try {
            Thread.sleep(2000);
            System.out.println("SMS sent");
        } catch(InterruptedException e) {
            e.printStackTrace();
        }
    }
}

class EmailDeliveryTask implements Runnable {
    public void run() {
        try {
            Thread.sleep(3000);
            System.out.println("Email sent");
        } catch(InterruptedException e) {
            e.printStackTrace();
        }
    }
}