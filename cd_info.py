#!/usr/bin/env python3

import subprocess
import Cddb

def get_cd_info():
    disc_id = subprocess.run(['cd-discid'], stdout=subprocess.PIPE).stdout

    cddb = Cddb.CddbServer()
    discs = cddb.getDiscs(disc_id)

    if discs:
        return cddb.getDiscInfo(discs[0])
