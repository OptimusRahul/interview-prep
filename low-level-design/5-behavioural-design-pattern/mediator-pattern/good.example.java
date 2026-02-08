import java.util.*;

interface DocumentSessionMediator {
    void broadcastChange(String change, User sender);
    void join(User user);
}

class CollaborativeDocument implements DocumentSessionMediator {
    private List<User> users = new ArrayList<>();

    public void join(User user) {
        users.add(user);
    }

    public void broadcastChange(String change, User sender) {
        for(User user: users) {
            if(user != sender) {
                user.receiveChange(change);
            }
        }
    }
}

class User {
    protected String name;
    protected DocumentSessionMediator mediator;

    public User(String name, DocumentSessionMediator mediator) {
        this.name = name;
        this.mediator = mediator;
    }

    public void makeChange(String change) {
        System.out.println(name + " made a change: " + change);
        mediator.broadcastChange(change, this);
    }

    public void receiveChange(String change) {
        System.out.println(name + " received change: " + change);
    }
}

class Main {
    public static void main(String[] args) {
        CollaborativeDocument document = new CollaborativeDocument();
        User john = new User("John", document);
        User jane = new User("Jane", document);
        User jim = new User("Jim", document);

        document.join(john);
        document.join(jane);
        document.join(jim);

        john.makeChange("John made a change");
        jane.makeChange("Jane made a change");
        jim.makeChange("Jim made a change");
    }
}