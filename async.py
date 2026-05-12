import asyncio
import sys
import os
import traceback
import re
import unicodedata
from functools import reduce

import pandas as pd
import yt_dlp
import youtube_search

YDL_OPTS = {
  'overwrites': False,
  'format': 'mp3/bestaudio/best',
  'postprocessors': [{  # Extract audio using ffmpeg
      'key': 'FFmpegExtractAudio',
      'preferredcodec': AUDIO_EXTENSION,
  }]
}

def get_valid_filename(value):
  return re.sub(r'[\/:*?"<>|\\]', '_', value).strip("-_\n ")


def parse_duration_to_seconds(duration: str):
  return reduce(
    lambda sum, value: sum + 60 ** value[0] * int(value[1]),
    enumerate(duration.split(':')[::-1]),
    0
  )


def pick_best_yt_search_result(results):
  return next((r for r in results if parse_duration_to_seconds(r['duration']) > 4 * 60), results[0])


def yt_search(name):
  with youtube_search.YoutubeSearch() as ytsearch:
    print(f"YouTube: Searching for '{name}'")
    ytsearch.search(name)
    result = pick_best_yt_search_result(ytsearch.list())

  return (result['title'], result['id'])


async def process_track(title, error_counter=0):
  try:
    (yt_title, id) = yt_search(title)
    full_title = get_valid_filename(title)

    url = f"https://www.youtube.com/watch?v={id}"
    print(f"YouTube: Downloading '{title}'")
    opts = YDL_OPTS.copy()
    opts['outtmpl'] = f"shazamlibrary/{full_title}.%(ext)s"
    with yt_dlp.YoutubeDL(opts) as ydl:
      ydl.download([url])
  except yt_dlp.networking.exceptions.HTTPError as e:
    if error_counter < 3:
      print(f"YouTube: Retrying because {str(e)}")
      process_track_id(id, error_counter + 1)
    else:
      raise e


async def main():
  for title in tracks:
    try:
      await process_track(title)
    except Exception as e:
      print(e)

loop = asyncio.new_event_loop()
loop.run_until_complete(main())
