"""
Module and command line application for summarizing JWST data products
"""
import os
import sys
from argparse import ArgumentParser

import asdf
# Hack to suppress AsdfDeprecationWarning
asdf.exceptions.AsdfDeprecationWarning = DeprecationWarning


__all__ = ['parse_metadata', 'read_metadata']


def parse_metadata(asdffile):
    """
    Extracts JWST metadata fields from an AsdfFile object

    Parameters
    ----------
    asdffile : `~asdf.AsdfFile`
        AsdfFile instance representing the JWST data file to be summarized

    Returns
    -------
    dict :
        `dict` containing JWST metadata fields of interest
    """
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
    """
    Reads JWST data product and extracts metadata fields of interest

    Parameters
    ----------
    filename : `str`
        Path of JWST data file to be summarized

    Returns
    -------
    dict :
        `dict` contaning JWST metadata fields of interest
    """
    with asdf.open(filename,
                   ignore_unrecognized_tag=True,
                   ignore_missing_extensions=True) as af:
        return parse_metadata(af)


def main():
    """
    Entry point for command line application
    """
    p = ArgumentParser(description='Summarizes JWST data files')
    p.add_argument('filename', help='Path of JWST data file')

    args = p.parse_args()

    filename = os.path.abspath(args.filename)

    try:
        metadata = read_metadata(sys.argv[1])
    except (IndexError, ValueError) as err:
        sys.stderr.write('Error: {}\n'.format(err))
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
