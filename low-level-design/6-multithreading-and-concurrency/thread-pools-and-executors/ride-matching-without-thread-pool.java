import java.util.*;

class Main {
    public static void main(String[] args) {
        RideMatchingService riderService1 = new RideMatchingService();
        RideMatchingService riderService2 = new RideMatchingService();

        riderService1.matchRide("Rahul");
        System.out.println("Ride matching task for rider Rahul started");

        riderService2.matchRide("Raj");
        System.out.println("Ride matching task for rider Raj started");
    }
}

class RideMatchingService {
    public void matchRide(String riderId) {
        Thread matchThread = new Thread(() -> {
            System.out.println("Matching ride for rider " + riderId);
            try {
                Thread.sleep(1000);
                System.out.println("Ride matched for rider " + riderId);
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                System.out.println("Ride matching thread for rider " + riderId + " completed");
            }
        });
        matchThread.start();
    }
}