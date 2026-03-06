import java.util.concurrent.*;

class FutureExample {
    public static void main(String[] args) throws Exception  {
        ExecutorService executor = Executors.newFixedThreadPool(2);

        Future<Integer> future = executor.submit(() -> {
            Thread.sleep(1000);
            return 42;
        });

        System.out.println("Task submitted");

        Integer result = future.get();
        System.out.println("Result: " + result);

        executor.shutdown();
    }
}