# SPDX-FileCopyrightText: 2023-present Charles C. <nafredy@gmail.com>
#
# SPDX-License-Identifier: MIT


from pathlib import Path

class KeiConf:
    '''
    A simple and minimalist flat file configuration for small projects and prototyping
    '''

    def __init__(self, filepath: Path = None):
        '''
        Initialize the configuration manager
        '''

        if not isinstance(filepath, Path):
            raise TypeError(f"Expected filepath to be PATH but got {type(filepath)}: {filepath}")

        self._filepath = filepath
