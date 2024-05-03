#!/usr/bin/env python3

import collections
import os
import os.path
import re

ROOT = '/var/lib/awstats'


def main():
  downloads = collections.defaultdict(int)

  for stat_file in os.listdir(ROOT):
    if not stat_file.endswith('p6drad-teel.txt'):
      # Only look at full stats files for p6drad-teel.net
      continue

    with open(os.path.join(ROOT, stat_file), 'r') as f:
      for l in f.readlines():
        if not 'audio/eisaaaru' in l:
          # Only look at audio/eisaaru
          continue

        parts = l.split(' ')
        url = os.path.basename(parts[0])
        download_count = int(parts[1])
        m = re.match(r'.*?([0-9]+).mp3', url)
        if not m:
          # print(f'unexpected attempt: {l}')
          continue
        episode = int(m.group(1))
        downloads[episode] += download_count

  for episode in sorted(downloads.keys(), reverse=True):
    print('/audio/eisaaaru%d.mp3 %d' % (episode, downloads[episode]))


if __name__ == '__main__':
  main()
