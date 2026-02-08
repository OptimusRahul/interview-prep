import java.util.*;

class ResumeEditor {
    private String name;
    private String education;
    private String experience;
    private List<String> skills;

    public void setName(String name) {
        this.name = name;
    }

    public void setEducation(String education) {
        this.education = education;
    }

    public void setExperience(String experience) {
        this.experience = experience;
    }

    public void addSkill(String skill) {
        skills.add(skill);
    }

    public void printResume() {
        System.out.println("x:----- Resume -----x:");
        System.out.println("Name: " + name);
        System.out.println("Education: " + education);
        System.out.println("Experience: " + experience);
        System.out.println("Skills: " + skills);
    }

    public Memento save() {
        return new Memento(name, education, experience, skills);
    }

    public void restore(Memento memento) {
        this.name = memento.name;
        this.education = memento.education;
        this.experience = memento.experience;
        this.skills = memento.skills;
    }

    public static class Memento {
        private String name;
        private String education;
        private String experience;
        private List<String> skills;

        public Memento(String name, String education, String experience, List<String> skills) {
            this.name = name;
            this.education = education;
            this.experience = experience;
            this.skills = skills;
        }

        public String getName() {
            return name;
        }

        public String getEducation() {
            return education;
        }

        public String getExperience() {
            return experience;
        }

        public List<String> getSkills() {
            return skills;
        }
    }
}