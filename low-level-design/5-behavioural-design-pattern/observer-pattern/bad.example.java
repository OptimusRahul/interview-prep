import java.util.*;

class YouTubeChannel {
    public void uploadNewVideo(String title) {
        System.out.println("Uploading: " + title + "\n");

        System.out.println("Sending email to user1@example.com");
        System.out.println("Pushing in-app notification to user3@example.com");
    }
}

class Main {
    public static void main(String[] args) {
        YouTubeChannel channel = new YouTubeChannel();
        channel.uploadNewVideo("Mahindra 7XO");
    }
}