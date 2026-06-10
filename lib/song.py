class Song:
    """Represents a song in the music library system.
    
    Tracks individual song details (name, artist, genre) and maintains
    global insights such as total song count, unique artists/genres,
    and per-genre/per-artist song counts.
    """

    # Class attributes to track all songs globally
    count = 0               # Total number of songs created
    genres = []             # List of unique genres
    artists = []            # List of unique artists
    genre_count = {}        # e.g. {"Rap": 5, "Rock": 1}
    artist_count = {}       # e.g. {"Beyonce": 17, "Jay-Z": 40}

    def __init__(self, name, artist, genre):
        """Initialize a Song instance and update all class-level trackers."""
        self.name = name
        self.artist = artist
        self.genre = genre

        # Trigger all class methods to update global song data
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increment the total song count by 1."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add a genre to the genres list if it doesn't already exist."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add an artist to the artists list if they don't already exist."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increment the count for the given genre, or initialize it to 1."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Increment the count for the given artist, or initialize it to 1."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1