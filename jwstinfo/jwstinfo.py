#!/usr/bin/env python3
import os
import sys
from argparse import ArgumentParser

import asdf
# Hack to suppress AsdfDeprecationWarning
asdf.exceptions.AsdfDeprecationWarning = DeprecationWarning


__all__ = ['parse_metadata', 'read_metadata']


def parse_metadata(asdffile):

    metadata = asdffile['meta']
    extracted = {
        'original filename':    metadata['filename'],
        'file creation date':   metadata['date'],
        'pipeline version':     metadata['calibration_software_version'],
        'instrument':           metadata['instrument']['name'],
        'detector':             metadata['instrument']['detector'],
        'model type':           metadata['model_type'],
        'target name':          metadata['target']['catalog_name'],
        'observation id':       metadata['observation']['obs_id'],
    }
    return extracted


def read_metadata(filename):
    with asdf.open(filename,
                   ignore_unrecognized_tag=True,
                   ignore_missing_extensions=True) as af:
        return parse_metadata(af)


def main():

    p = ArgumentParser(description='Summarizes JWST data files')
    p.add_argument('filename', help='Path of JWST data file')

    args = p.parse_args()

    filename = os.path.abspath(args.filename)

    try:
        metadata = read_metadata(sys.argv[1])
    except (IndexError, ValueError):
        sys.stderr.write('File does not appear to be JWST data product\n')
        return 1
    except FileNotFoundError:
        sys.stderr.write("Given file '{}' can't be found \n".format(sys.argv[1]))
        return 1

    longest = max([len(x) for x in metadata.keys()])
    fmt_string = '{:' + str(longest) + '}: {}'
    for key, value in metadata.items():
        print(fmt_string.format(key, value))


if __name__ == '__main__':
    sys.exit(main())
