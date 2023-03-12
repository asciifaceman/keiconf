# SPDX-FileCopyrightText: 2023-present Charles C. <nafredy@gmail.com>
#
# SPDX-License-Identifier: MIT
import logging
from typing import Any, Union
from pathlib import Path
import json

class KeiConf:
    '''
    A minimalist application json configuration tool with file watches
    for the developer who just wants to get going
    '''
    
    _filepath: Path
    _json_indent: int
    _fail_on_missing_key: bool
    _create_if_not_exist: bool
    _conf = {}
    
    def __init__(self, filepath: Union[str, Path], indent: int = 2, \
                fail_on_missing_key: bool = True, create_if_not_exist: bool = False):
        '''
        Initialize the configuration interface
        
        :param [str|Path] filepath: The /path/to/file.json where the config file is or should be
        :param int indent: The json indent to use in the written file
        :param bool fail_on_missing_key: Raises KeyError if requested config key does not exist, False just returns None
        :param bool create_if_not_exist: Creates the given filepath if it does not exist (including directory tree)
        :raises TypeError: if the filepath is not str or Path
        :raises TypeError: if the indent is not int
        :raises TypeError: if the fail_on_missing_key is not bool
        :rasised TypeError: if the create_if_not_exist is not bool
        '''
        
        if isinstance(filepath, str):
            self._filepath = Path(filepath)
        elif isinstance(filepath, Path):
            self._filepath = filepath
        else:
            raise TypeError(f'expected filepath to be (str | Path), got {type(filepath)}')
        
        self.__class__.__check_filepath_is_dir(self._filepath)
        
        if isinstance(indent, int):
            self._json_indent = indent
        else:
            raise TypeError(f'expected indent to be (int), got {type(indent)}')
    
        if isinstance(fail_on_missing_key, bool):
            self._fail_on_missing_key = fail_on_missing_key
        else:
            raise TypeError(f'expected fail_on_missing_key to be (bool), got {type(fail_on_missing_key)}')
        
        if isinstance(create_if_not_exist, bool):
            self._create_if_not_exist = create_if_not_exist
        else:
            raise TypeError(f'expected create_if_not_exist to be (bool), got {type(create_if_not_exist)}')
    
        self.__create_config_if_not_exist()
        self.__load_config()
    
    def __load_config(self):
        '''
        Read the configfile into memory
        '''
        with open(self._filepath, 'r') as file:
            self.__conf = json.load(file)
        
    def __create_config_if_not_exist(self):
        '''
        If __create_if_not_exist, creates the config file and its directory tree 
        if it doesn't exist
        '''
        
        if self._create_if_not_exist and not self._filepath.is_file():
            self._filepath.mkdir(parents=True, exist_ok=True)
            self.__write()
    
    def __write(self):
        '''
        Write KeiConf config file to disk
        '''
        self._filepath.write_text(json.dumps(self._conf, indent=self._json_indent))
    
    def __repr__(self) -> str:
        return json.dumps(self._conf, indent=self._json_indent)
    
    @staticmethod
    def __check_filepath_is_dir(path: Path):
        if path.is_dir():
            raise IsADirectoryError(f'given filepath {path} is a directory, expected path/to/file.json')
