# CD Ripping

Ripping a CD with a blunt instrument.

## Features

- Rips CD to current directory
- Encodes files as flac
- Adds tags to the files based on the first match it finds from CDDB
- If there is file called `art.png` in the local directory, it'll add it as the cover art

## Requirements

1. python-audio-tools

    Currently cannot be installed using `pip`.  Instead, check out the [GitHub Repo](https://github.com/tuffy/python-audio-tools) and read the `INSTALL` file.

2. python-cddb

    Again, cannot be installed using `pip`, so get from the [Github Repo](https://github.com/cbxbiker61/python-cddb).

3. flac

    Install from your package provider

## How to Install

At the minute I haven't created a setup file, so you'll have to move the file rip_cd.py to somewhere in your path and give it execute permissions.

## How to Use

1. Put CD into the disk drive.  If you have more than one, guess which one it might pick.
2. Create a folder for the music to be ripped into and `cd` yourself into it.
3. Copy the album art into the current directory with a name of `art.png`.
4. Run `cd_rip.py`
5. Sit back and wait.

## To Do

1. Allow the album art file to be specified from the command line.
2. Allow the file for the album art to be a URL.
3. Download the album art based on the name of the album and artist.  Not sure where from, though.
4. If there are multiple sets of CD info downloaded from the CDDB, let the user pick which one to use.
5. Create folders for the Artist and the Album, instead of just dumping the the files in the current directory.
6. Allow the user to specify a 'Music' directory on the command line, environment variable or in a config file in their home directory.
7. Create a setup file to install the application properly.
8. Allow other forms of encoding: mp3, ogg, etc.