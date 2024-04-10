from pytube import YouTube

link = "https://www.youtube.com/shorts/BxopymsAHLM"
youtube_1 = YouTube(link)

# Fetching all available streams without using .all()
videos = youtube_1.streams

vid = list(enumerate(videos))
for i in vid:
    print(i)
    print()
    strm = int(input("Enter: "))
    videos[strm].download()
    print('Successfully downloaded!')
