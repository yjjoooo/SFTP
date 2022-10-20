import logging
import os
import traceback
import platform
import sys
import shutil
import pandas as pd

# logger
def log(msg):
    logging.info(msg)

def log_warn(msg):
    logging.warning(msg)

def log_err(msg):
    logging.error(msg)

# script start logger
def script_start():
    log('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    log('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    log('@@@@                                                                                  @@@@')
    log('@@@@    ___            _     _                                      _     _           @@@@')
    log('@@@@   / _ \          | |   | |                      _             (_)   (_)          @@@@')
    log('@@@@  / /_\ \  _   _  | |_  | |__     ___    _ __   (_)   _   _     _     _    ___    @@@@')
    log('@@@@  |  _  | | | | | | __| |  _ \   / _ \  |  __|       | | | |   | |   | |  / _ \   @@@@')
    log('@@@@  | | | | | |_| | | |_  | | | | | (_) | | |      _   | |_| |   | |   | | | (_) |  @@@@')
    log('@@@@  \_| |_/  \__ _|  \__| |_| |_|  \___/  |_|     (_)   \__  |   | |   | |  \___/   @@@@')
    log('@@@@                                                       __/ |  _/ |  _/ |          @@@@')
    log('@@@@                                                      |___/  |__/  |__/           @@@@')
    log('@@@@                                                                                  @@@@')
    log('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    log('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    log('==========================================================================================')
    log('#### OS              : {}'.format(platform.platform()))
    log('#### Python Version  : {}'.format(sys.version))
    log('#### Process ID(PID) : {}'.format(os.getpid()))
    log('==========================================================================================')

''' file & directory controller '''

# file list reader input path return list
def read_file_list(path):
    try:
        log('#### Read Path \"{}\"'.format(path))
        file_list = list([])
        
        for dir_path, _, file_name in os.walk(path):
            for f in file_name:
                try:
                    file_list.append(os.path.abspath(os.path.join(dir_path, f)))
                except:
                    log('######## Read File \"{}\" Error'.format(file_name))
                    log(traceback.format_exc())

        log('############ Path \"{}\" File Count : {}'.format(path, len(file_list)))
        return file_list
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Read Path \"{}\" Error'.format(path))
        log_err(traceback.format_exc())
        
# directory creater
def create_dir(path):
    try:
        if not os.path.exists(path):
            log('#### Create Directory \"{}\"'.format(path))
            os.makedirs(path)
        else:
            log('#### Directory \"{}\" Already Exist'.format(path))
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Create Directory \"{}\" Error'.format(path))
        log_err(traceback.format_exc())
        
# file copier
def copy_file(file_from, file_to):
    try:
        log('#### Copy File \"{}\" to \"{}\"'.format(file_from, file_to))
        if not os.path.exists(file_to):
            shutil.copy2(file_from, file_to)
        else:
            log('######## File \"{}\" Already Exist'.format(file_to))
            file_to = '{}_copy.{}'.format(file_to.rsplit('.', maxsplit = 1)[0], file_to.rsplit('.', maxsplit = 1)[1])
            log('######## Copy File \"{}\" to \"{}\"'.format(file_from, file_to))
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Copy File \"{}\" to \"{}\" Error'.format(file_from, file_to))
        log_err(traceback.format_exc())

# directory copier
def copy_dir(dir_from, dir_to):
    try:
        log('#### Copy Direcotry \"{}\" to \"{}\"'.format(dir_from, dir_to))
        if not os.path.exists(dir_to):
            shutil.copytree(dir_from, dir_to, dirs_exist_ok = True)
        else:
            log('######## Direcotry \"{}\" Already Exist'.format(dir_to))
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Copy Direcotry \"{}\" to \"{}\" Error'.format(dir_from, dir_to))
        log_err(traceback.format_exc())

# file or directory mover
def move(fd_from, fd_to):
    try:
        log('#### Move \"{}\" to \"{}\"'.format(fd_from, fd_to))
        if not os.path.exists(fd_to):
            shutil.move(fd_from, fd_to)
        else:
            log('######## \"{}\" Already Exist'.format(fd_to))
            fd_to = '{}_copy.{}'.format(fd_to.rsplit('.', maxsplit = 1)[0], fd_to.rsplit('.', maxsplit = 1)[1])
            log('######## Move \"{}\" to \"{}\"'.format(fd_from, fd_to))
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Move \"{}\" to \"{}\" Error'.format(fd_from, fd_to))
        log_err(traceback.format_exc())
        
# file remover
def remove_file(path):
    try:
        log('#### Remove File \"{}\"'.format(path))
        if os.path.exists(path):
            os.remove(path)
        else:
            log('######## No File \"{}\"'.format(path))
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Remove File \"{}\" Error'.format(path))
        log_err(traceback.format_exc())

# directory remover
def remove_dir(path):
    try:
        log('#### Remove Directory \"{}\"'.format(path))
        if os.path.exists(path):
            shutil.rmtree(path)
        else:
            log('######## No Directory \"{}\"'.format(path))
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Remove Directory \"{}\" Error'.format(path))
        log_err(traceback.format_exc())

# file or directory renamer
def rename(fd_from, fd_to):
    try:
        log('#### Rename \"{}\" to \"{}\"'.format(fd_from, fd_to))
        if os.path.exists(fd_from):
            os.rename(fd_from, fd_to)
        else:
            log('######## No \"{}\"'.format(fd_from))
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Rename \"{}\" to \"{}\" Error'.format(fd_from, fd_to))
        log_err(traceback.format_exc())

# file size collector input list return dataframe
def get_size_of_file(path_list):
    try:
        log('#### Get File Size')
        
        # define dataframe
        df = pd.DataFrame([], columns = ['file_path', 'byte'])
        df['file_path'] = path_list
        
        for idx, path in enumerate(path_list):
            try:
                if os.path.exists(path):
                    file_size = os.path.getsize(path)
                    log('######## #{} File \"{}\" Size : {} bytes'.format(idx, path, file_size))
                    df.loc[idx, 'byte'] = file_size
                else:
                    log('######## #{} No File \"{}\"'.format(idx, path))
            except:
                log('######## #{} Get File Size of \"{}\" Error'.format(idx, path))
                log(traceback.format_exc())
        
        return df
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Get File Size Error')
        log_err(traceback.format_exc())