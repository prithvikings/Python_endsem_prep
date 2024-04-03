from pytube import YouTube

def download_video(url, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution video stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video to the specified output path
        video_stream.download(output_path)
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
video_url = 'https://youtu.be/PvFshrgv9sc?list=TLPQMDgwMTIwMjQc9ORBIjdNCA'  # Replace 'VIDEO_ID' with the actual video ID or URL
output_directory = 'C:\\Users\\prith\\OneDrive\\Desktop\\Learn For Now'  # Replace with the desired output directory

download_video(video_url, output_directory)
