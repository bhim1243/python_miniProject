from moviepy.editor import ImageSequenceClip, AudioFileClip
import os
# Paths to your audio and image files
audio_path = "C:/Users/bhimb/Downloads/audior/audio.mp3"
image_folder_path = "C:/Users/bhimb/Downloads/image"

# Load audio and images
audio_clip = AudioFileClip(audio_path)
image_files = sorted(os.listdir(image_folder_path))  # Assuming the images are sorted properly

# Create ImageSequenceClip from images
image_clip = ImageSequenceClip([os.path.join(image_folder_path, img) for img in image_files], fps=24)

# Make sure the durations match
audio_clip = audio_clip.set_duration(image_clip.duration)

# Combine audio and video
final_clip = image_clip.set_audio(audio_clip)

# Export the final video
final_clip.write_videofile("output_video.mp4", codec="libx264", fps=24)
