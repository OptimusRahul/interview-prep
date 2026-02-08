import java.util.*;

// A simple video class with title
class Video {
    String title;

    public Video(String title) {
        this.title = title;
    }

    public String getTitle() {
        return title;
    }
}

// YouTubePlaylist class holds a list of Video Objects
class YouTubePlaylist {
    private List<Video> videos = new ArrayList<>();

    public void addVideo(Video video) {
        videos.add(video);
    }

    public List<Video> getVideos() {
        return videos;
    }
}

class Main {
    public static void main(String[] args) {
        YouTubePlaylist playlist = new YouTubePlaylist();
        playlist.addVideo(new Video("Mahindra 7XO"));
        playlist.addVideo(new Video("Tata Safari"));

        for (Video video : playlist.getVideos()) {
            System.out.println(video.getTitle());
        }
    }
}