import os
import sys
from pathlib import Path

try:
    import instaloader
except ImportError:
    print("instaloader is not installed. Run: py -m pip install --user instaloader")
    sys.exit(1)

if len(sys.argv) < 2:
    print("Usage: py download_instagram.py <instagram_username>")
    sys.exit(1)

username = sys.argv[1]
out_dir = Path("downloads") / username
out_dir.mkdir(parents=True, exist_ok=True)

L = instaloader.Instaloader(download_video_thumbnails=False, download_pictures=True, compress_json=False)

try:
    profile = instaloader.Profile.from_username(L.context, username)
except Exception as e:
    print(f"Could not load profile '{username}': {e}")
    sys.exit(1)

print(f"Downloading posts from {username} into {out_dir}...")

count = 0
for post in profile.get_posts():
    if count >= 12:
        break
    L.download_post(post, target=out_dir)
    count += 1

print(f"Done. Downloaded {count} posts to {out_dir}")
