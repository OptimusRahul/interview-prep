import java.util.*;

class Video {
    private String title;

    public Video(String title) {
        this.title = title;
    }

    public String getTitle() {
        return title;
    }
}

class YouTubePlaylist {
    private List<Video> videos = new ArrayList<>();

    public void addVideo(Video video) {
        videos.add(video);
    }

    public List<Video> getVideos() {
        return videos;
    }
}

interface PlaylistIterator {
    boolean hasNext();
    Video next();
}

class YouTubePlaylistIterator implements PlaylistIterator {
    private List<Video> videos;
    private int position = 0;

    public YouTubePlaylistIterator(List<Video> videos) {
        this.videos = videos;
        this.position = 0;
    }

    @Override
    public boolean hasNext() {
        return position < videos.size();
    }

    @Override
    public Video next() {
        return hasNext() ? videos.get(position++) : null;
    }
}

class Main {
    public static void main(String[] args) {
        YouTubePlaylist playlist = new YouTubePlaylist();
        playlist.addVideo(new Video("Mahindra 7XO"));
        playlist.addVideo(new Video("Tata Safari"));

        PlaylistIterator iterator = new YouTubePlaylistIterator(playlist.getVideos());

        while(iterator.hasNext()) {
            System.out.println(iterator.next().getTitle());
        }
    }
}