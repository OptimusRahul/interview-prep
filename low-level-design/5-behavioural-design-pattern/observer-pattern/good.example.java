import java.util.*;

interface Subscriber {
    void update(String title);
}

class EmailSubscriber implements Subscriber {
    private String email;

    public EmailSubscriber(String email) {
        this.email = email;
    }

    @Override
    public void update(String title) {
        System.out.println("Sending email to " + email + ": New video uploaded - "+ title);
    }
}

class MobileAppSubscriber implements Subscriber {
    private String userId;

    public MobileAppSubscriber(String userId) {
        this.userId = userId;
    }

    @Override
    public void update(String title) {
        System.out.println("Pushing in-app notification to " + userId + ": New video uploaded - "+ title);
    }
}

interface Channel {
    void subscribe(Subscriber subscriber);
    void unsubscribe(Subscriber subscriber);
    void notifySubscribers(String title);
}

class YouTubeChannel implements Channel {
    private List<Subscriber> subscribers = new ArrayList<>();
    private String channelName;

    public YouTubeChannel(String channelName) {
        this.channelName = channelName;
    }

    @Override
    public void subscribe(Subscriber subscriber) {
        subscribers.add(subscriber);
    }

    @Override
    public void unsubscribe(Subscriber subscriber) {
        subscribers.remove(subscriber);
    }

    @Override
    public void notifySubscribers(String title) {
        for (Subscriber subscriber : subscribers) {
            subscriber.update(title);
        }
    }

    public void uploadNewVideo(String title) {
        System.out.println("Uploading: " + title + "\n");
        notifySubscribers(title);
    }
}

class Main {
    public static void main(String[] args) {
        YouTubeChannel channel = new YouTubeChannel("YouTube Channel");

        channel.subscribe(new EmailSubscriber("user1@example.com"));
        channel.subscribe(new MobileAppSubscriber("user3@example.com"));

        channel.uploadNewVideo("Mahindra 7XO"); 
    }
}