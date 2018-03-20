#!/usr/bin/env python3

import tempfile
import subprocess
import glob
import os
import Cddb
import argparse


def get_cd_info():
    disc_id = subprocess.run(['cd-discid'], stdout=subprocess.PIPE).stdout

    cddb = Cddb.CddbServer()
    discs = cddb.getDiscs(disc_id)

    if discs:
        return cddb.getDiscInfo(discs[0])


parser = argparse.ArgumentParser(description='Ripping a CD with a blunt instrument.')
parser.add_argument(
    '-p',
    '--picture',
    help='Picture file for cover art'
)

args = parser.parse_args()
picture_param = ''

if args.picture:
    picture_param = f'--picture={args.picture}'

info = get_cd_info()

with tempfile.TemporaryDirectory() as tmp_dir:
    subprocess.run([
        'cdda2wav',
        '--alltracks',
        '--no-infofile',
        os.path.join(tmp_dir, 'audio')
    ])

    for i, file in enumerate(sorted(glob.iglob(os.path.join(tmp_dir, '*.wav')))):
        subprocess.run([
            'flac',
            '--best',
            '--tag', f'TRACKNUMBER={i+1}',
            '--tag', f'TITLE={info.tracks[i]:>02}',
            '--tag', f'ARTIST={info.artist}',
            '--tag', f'BAND={info.artist}',
            '--tag', f'COMPOSER={info.artist}',
            '--tag', f'ALBUM={info.title}',
            '--tag', f'GENRE={info.genre}',
            picture_param,
            '--output-name', f'{i+1:02}_{info.tracks[i]}.flac',
            os.path.join(tmp_dir, file)
        ])
