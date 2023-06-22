    # Python code to convert video to audio
import moviepy.editor as mp
  
# Insert Local Video File Path 
clip = mp.VideoFileClip(r"song.mp4")
  
# Insert Local Audio File Path
clip.audio.write_audiofile(r"converted.mp3")