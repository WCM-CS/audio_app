import ffmpeg
import os

def convert_mp4_to_aac(input_file):
    
    output_file = input_file.replace('.mp4', '.aac')
    
    try:
        ffmpeg.input(input_file).output(
            output_file, 
            acodec='aac', 
            audio_bitrate='128k',
            ar='44100',
            ac=2,
            map_metadata='-1',
            preset='fast',
            vn=None
            ).run()
        print(f"MP4 file '{input_file}' converted to AAC file '{output_file}' successfully.")
    except ffmpeg.Error as e:
        print(f"Error converting MP4 file: {e}")
        
        

if __name__ == '__main__':
    audio_files = [
    "Pure_Noise.mp4",
    "Gym_Phonk.mp4",
    "Lofi_Long.mp4",
    "Lofi_Short.mp4",
    "Best_Classical.mp4",
    "Dark_Classical.mp4"
    ]
    
    for file in audio_files:
        temp = os.path.join("audio", file)
        convert_mp4_to_aac(temp)