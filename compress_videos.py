import argparse
import os
import subprocess


def compress_video(input_file, output_file):
    cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vcodec", "libx264",
        "-crf", "24",
        "-preset", "slow",
        "-acodec", "aac",
        "-b:a", "128k",
        output_file,
    ]
    subprocess.run(cmd, check=True)


def process_directory(directory):
    for root, _, files in os.walk(directory):
        for name in files:
            if name.lower().endswith((".mp4", ".mov")):
                input_path = os.path.join(root, name)
                base, ext = os.path.splitext(name)
                output_name = f"{base}_compressed{ext}"
                output_path = os.path.join(root, output_name)
                compress_video(input_path, output_path)


def main():
    parser = argparse.ArgumentParser(description="Compress videos in a directory")
    parser.add_argument("directory", help="Path to directory containing videos")
    args = parser.parse_args()
    process_directory(args.directory)


if __name__ == "__main__":
    main()
