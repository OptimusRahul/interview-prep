import java.util.*;

class Light {
    public void on() {
        System.out.println("Light is turned ON");
    }

    public void off() {
        System.out.println("Light is turned OFF");
    }
}

class AC {
    public void on() {
        System.out.println("AC is turned ON");
    }

    public void off() {
        System.out.println("AC is turned OFF");
    }
}

class NativeRemoteControl {
    private Light light;
    private AC ac;
    private String lastAction = "";

    public NativeRemoteControl(Light light, AC ac) {
        this.light = light;
        this.ac = ac;
    }

    public void pressLightOn() {
        light.on();
        lastAction = "LIGHT_ON";
    }

    public void pressLightOff() {
        light.off();
        lastAction = "LIGHT_OFF";
    }

    public void pressACOn() {
        ac.on();
        lastAction = "AC_ON";
    }

    public void pressACOff() {
        ac.off();
        lastAction = "AC_OFF";
    }

    public void pressUndo() {
        switch(lastAction) {
            case "LIGHT_ON": light.off(); lastAction = "LIGHT_OFF"; break;
            case "LIGHT_OFF": light.on(); lastAction = "LIGHT_ON"; break;
            case "AC_ON": ac.off(); lastAction = "AC_OFF"; break;
            case "AC_OFF": ac.on(); lastAction = "AC_ON"; break;
            default: System.out.println("No action to undo"); break;
        }
    }
}

class Main {
    public static void main(String[] args) {
        Light light = new Light();
        AC ac = new AC();
        NativeRemoteControl remote = new NativeRemoteControl(light, ac);

        remote.pressLightOn();
        remote.pressACOn();
        remote.pressLightOff();
        remote.pressUndo();
        remote.pressUndo();
    }
}