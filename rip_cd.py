#!/usr/bin/env python3

import tempfile
import subprocess
import glob
import os
from cd_info import get_cd_info
from pprint import pprint as pp

info = get_cd_info()

pp(info)

with tempfile.TemporaryDirectory() as tmp_dir:
    '''
    subprocess.run([
        'cdda2wav',
        '--alltracks',
        '--no-infofile',
        os.path.join(tmp_dir, 'audio')
    ])
    '''
    subprocess.run(['cdda2wav', os.path.join(tmp_dir, 'audio')])

    for i, file in enumerate(glob.iglob(os.path.join(tmp_dir, '*.wav'))):
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
            f'--picture=art.png',
            '--output-name', f'{i+1:02}_{info.tracks[i]}.flac',
            os.path.join(tmp_dir, file)
        ])
