# Bad Example
interface Logistics {
    void send();
}

class Road implements Logistics {
    @Override
    public void send() {
        System.out.println("Sending by road logic");
    }
}

class Air implements Logistics {
    @Override
    public void send() {
        System.out.println("Sending by air logic");
    }
}

class LogisticsService {
    public void send(String mode) {
        if(mode.equals("road")) {
            return new Road();
        } else if(mode.equals("air")) {
            return new Air();
        }
    }
}

# Good Example
interface Logistics {
    void send();
}

class Road implements Logistics {
    @Override
    public void send() {
        System.out.println("Sending by road logic");
    }
}

class Air implements Logistics {
    @Override
    public void send() {
        System.out.println("Sending by air logic");
    }
}

class LogisticsFactory {
    public static Logistics getLogistics(String mode) {
        if(mode.equals("road")) {
            return new Road();
        } else if(mode.equals("air")) {
            return new Air();
        } else {
            throw new IllegalArgumentException("Invalid mode: " + mode);
        }
    }
}

class LogisticsService {
    public void send(String mode) {
        Logistics logistics = LogisticsFactory.getLogistics(mode);
        logistics.send();
    }
}

