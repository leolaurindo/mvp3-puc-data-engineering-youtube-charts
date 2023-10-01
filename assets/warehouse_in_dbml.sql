Table fact_chart {
  fact_id INT [pk, increment]
  dim_track_id INT [ref: > dim_track.dim_track_id]
  dim_artist_id INT [ref: > dim_artist.dim_artist_id]
  rank INT
  previous_rank INT
  week_end DATE
  week_start DATE
  weeks_on_chart INT
  views INT
  weekly_growth FLOAT
}

Table dim_track {
  dim_track_id INT [pk, increment]
  track_video_id_youtube STRING
  track_name STRING
  spotify_track_id STRING
  yt_published_dates DATE
}

Table dim_artist {
  dim_artist_id INT [pk, increment]
  main_artist STRING
  artist_id_spotify STRING
}

Table dim_track_tag {
  dim_track_tag_id INT [pk, increment]
  dim_track_id INT [ref: > dim_track.dim_track_id]
  tag STRING
}

Table dim_genre {
  dim_genre_id INT [pk, increment]
  dim_artist_id INT [ref: > dim_artist.dim_artist_id]
  genre_name STRING
}
