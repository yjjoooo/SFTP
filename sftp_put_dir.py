#!/usr/bin/python
# -*- coding : utf-8 -*-
'''
 @author : yjjo
'''
''' install '''

''' import '''
import python_modules as pym
import logging
from logging.config import dictConfig
import datetime
import traceback
import os

import paramiko
import config as cfg

''' log '''
script_abs_path, script_name = os.path.split(__file__)

pym.create_dir(os.path.join(script_abs_path, 'logs'))

dictConfig({
    'version' : 1,
    'formatters' : {
        'default' : {
            'format' : '[%(asctime)s] %(levelname)7s --- %(lineno)6d : %(message)s',
        },
    },
    'handlers' : {
        'file' : {
            'class' : 'logging.FileHandler',
            'level' : 'DEBUG',
            'formatter' : 'default',
            'filename' : os.path.join(script_abs_path, 'logs', '{}_{}.log'.format(script_name.rsplit('.', maxsplit = 1)[0], datetime.datetime.now().strftime('%Y%m%d'))),
        },
    },
    'root' : {
        'level' : 'DEBUG',
        'handlers' : ['file']
    }
})

def log(msg):
    logging.info(msg)
    
def log_warn(msg):
    logging.warning(msg)

def log_err(msg):
    logging.error(msg)

''' main function'''
def main():
    try:
        pym.script_start()
        
        host = cfg.SERVER_INFO['host']
        port = cfg.SERVER_INFO['port']
        transport = set_sftp_info(host, port)
        
        login_id = cfg.LOGIN_INFO['id']
        login_pw = cfg.LOGIN_INFO['pw']
        login_sftp(transport, login_id, login_pw)
        
        sftp = create_sftp_connection(transport)
        
        before_path = cfg.PATH['before_path']
        after_path = cfg.PATH['after_path']
        sftp_put(sftp, before_path, after_path)
        
        sftp.close()
        transport.close()
    except:
        log_err('############ Main Funtion Error')
        log_err(traceback.format_exc())
    
''' functions '''
# sftp info setter
def set_sftp_info(host, port):
    try:
        log('#### Setting SFTP Info')
        transport = paramiko.Transport.Trasnport(host, port)
        log('######## \"{}:{}\"'.format(host, port))
        
        return transport
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Setting SFTP Info Error')
        log_err(traceback.format_exc())

# sftp login
def login_sftp(transport, login_id, login_pw):
    try:
        log('#### Login')
        transport.connect(username = login_id, password = login_pw)
        log('######## Complete')
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Login Error')
        log_err(traceback.format_exc())

# sftp connection creater
def create_sftp_connection(transport):
    try:
        log('#### Create SFTP Connection')
        sftp = paramiko.SFTPClient.from_transport(transport)
        log('######## Complete')
        
        return sftp
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Create SFTP Connection Error')
        log_err(traceback.format_exc())

# file putter input path
def sftp_put(sftp, before_path, after_path):
    try:
        log('#### SFTP Put \"{}\" to \"{}\"'.format(before_path, after_path))
        file_list = os.listdir(before_path)
        for file_name in file_list:
            before_file = os.path.join(before_path, file_name)
            after_file = os.path.join(after_path, file_name)
            try:
                log('######## Put \"{}\" to \"{}\"'.format(before_file, after_file))
                sftp.put(before_file, after_file)
            except:
                log_err('######## Put \"{}\" to \"{}\" Error'.format(before_file, after_file))
                log_err(traceback.format_exc())
    except RuntimeWarning as w:
        log_warn(w)
    except:
        log_err('############ Put \"{}\" to \"{}\" Error'.format(before_path, after_path))
        log_err(traceback.format_exc())
    

def smtp_put():
    return
    
def smtp_get():
    return

''' main '''
if __name__ == '__main__':
    # Calculate Run Time
    start_time = datetime.datetime.now()

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    main()

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    log('==========================================================================================')
    log('#### Run Time {}'.format(str(datetime.datetime.now() - start_time)))
    log('==========================================================================================')