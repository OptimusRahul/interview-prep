import java.util.*;

class ResumeEditor {
    String name;
    String education;
    String experience;
    List<String> skills;
}

class ResumeSnapshot {
    public String name;
    public String education;
    public String experience;
    public List<String> skills;

    public ResumeSnapshot(ResumeEditor editor) {
        this.name = editor.name;
        this.education = editor.education;
        this.experience = editor.experience;
        this.skills = new ArrayList<>(editor.skills);
    }

    public void restore(ResumeEditor editor) {
        editor.name = this.name;
        editor.education = this.education;
        editor.experience = this.experience;
        editor.skills = new ArrayList<>(this.skills);
    }
}

class Main {
    public static void main(String[] args) {
        ResumeEditor editor = new ResumeEditor();
        editor.name = "John Doe";
        editor.education = "Bachelor of Science in Computer Science";
        editor.experience = "2 years of experience in software development";
        editor.skills = Arrays.asList("Java", "Python", "SQL");

        ResumeSnapshot snapshot = new ResumeSnapshot(editor);
        
        editor.name = "Jane Doe";
        editor.education = "Master of Science in Computer Science";
        editor.experience = "3 years of experience in software development";
        editor.skills = Arrays.asList("Java", "Python", "SQL", "JavaScript");

        snapshot.restore(editor);

        System.out.println("\nAfter undo:");
        System.out.println("Name: " + editor.name);
        System.out.println("Skills: " + editor.skills);
    }
} 