-- Creating facts_chart
CREATE TABLE youtube_charts.fact_chart (
  fact_id STRING NOT NULL,
  dim_track_id STRING NOT NULL,
  dim_artist_id STRING NOT NULL,
  rank INT64 NOT NULL,
  previous_rank INT64,
  week_end DATE NOT NULL,
  week_start DATE NOT NULL,
  weeks_on_chart INT64,
  views INT64,
  weekly_growth FLOAT64
);

-- Creating dim_track
CREATE TABLE youtube_charts.dim_track (
  dim_track_id STRING NOT NULL,
  track_video_id_youtube STRING(11) NOT NULL,
  track_name STRING NOT NULL,
  spotify_track_id STRING(22),
  yt_published_dates DATE
);

-- Creating dim_artist
CREATE TABLE youtube_charts.dim_artist (
  dim_artist_id STRING NOT NULL,
  main_artist STRING NOT NULL,
  artist_id_spotify STRING(22)
);

-- Creating dim_track_tag
CREATE TABLE youtube_charts.dim_track_tag (
  dim_track_tag_id STRING NOT NULL,
  dim_track_id STRING NOT NULL,
  tag STRING NOT NULL
);

-- Creating dim_genre
CREATE TABLE youtube_charts.dim_genre (
  dim_genre_id STRING NOT NULL,
  dim_artist_id STRING NOT NULL,
  genre_name STRING NOT NULL
);
