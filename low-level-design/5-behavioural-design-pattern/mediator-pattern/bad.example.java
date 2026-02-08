import java.util.*;

class User {
    private String name;
    private List<User> others;

    public User(String name) {
        this.name = name;
        this.others = new ArrayList<>();
    }

    public void addCollaborator(User user) {
        others.add(user);
    }

    public void makeChange(String change) {
        for(User u: others) {
            u.receiveChange(change, this);
        }
    }

    public void receiveChange(String change, User sender) {
        System.out.println(name + " received change from " + sender.name + ": " + change);
    }
}

class Main {
    public static void main(String[] args) {
        User john = new User("John");
        User jane = new User("Jane");
        User jim = new User("Jim");

        john.addCollaborator(jane);
        john.addCollaborator(jim);

        john.makeChange("John made a change");
        jane.makeChange("Jane made a change");
        jim.makeChange("Jim made a change");
    }
}