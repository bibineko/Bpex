#! /usr/bin/env python
# -*- coding:utf-8 -*-

""" [NAME] に続くScriptの簡易説明文

[DESCRIPTION] Scriptの詳細説明文

ユーザ名とパスワードの保存にpitを使っている。
username: sshのユーザ
password: パスワード
adminpassword: 特権パスワード

pitのインストールは次のようにする。
$ sudo pip install pit
$ export EDITOR=vim
$ python
-- in python shell --
from pit import Pit
Pit.get('label名', {'require':{'username':'your USERNAME','password':'your PASSORD','adminpassword':'adminpass'}})
-- from here --

"""
__author__ = 'Tomofumi Oga <bibineko@gmail.com>'
__version__ = '0.1'

import pexpect
import sys
from pit import Pit


class Bpex(pexpect.spawn):
    """
    [CLASSES] Class説明文
    """
    def output(self):
        self.logfile = sys.stdout
        
    
    def login_rtx(self, ipaddr, username, password, adminpassword):
        """ [CLASSES] 関数説明文
        Keyword arguments:
        hoge -- 引数説明
        """
        
        self.username = username
        self.password = password
        self.adminpassword = adminpassword
        
        res_login = 0
        while res_login == 0:
            print "login"
            self.flush()
            self.sendline('ssh ' + username + '@' + ipaddr)
            res = 0
            while res == 0:
                
                res = self.expect(['connecting','ssword:'])
                if res == 0:
                    print 'add ssh key'
                    self.sendline('yes')
                else:
                    print "send password"
                    self.sendline(password)
            
            res_login = pex.expect(['gw0','RTX1200','RTX810'])
        
        self.flush()
        self.sendline('administrator')
        self.expect('Password')
        self.sendline(adminpassword)
        self.expect('#')

    def logout_rtx(self, save_config = 'Y'):
        """ [CLASSES] 関数説明文
        Keyword arguments:
        hoge -- 引数説明
        """
        res = 1
        while res != 0:
            self.flush()
            self.sendline('')
            res = self.expect(['>','#'])
            if res == 1:
                self.sendline('exit')
                res2 = self.expect(['>','(Y/N)'])
                if res2 == 1:
                    self.sendline(save_config)
            
        self.sendline('exit')
        self.expect('closed')
        

if __name__ == "__main__":
    """
    """

    conf = Pit.get('ssh-logins')    # Pitでログイン情報を取得
    user = conf['username']         # user名
    passwd = conf['password']       # password
    adminpasswd = conf['adminpassword']
    server = conf['gateway']        # 踏み台
    
    
    pex = Bpex('ssh %s@%s' % (user, server)) # 踏み台へログイン
    pex.output()

    pex.expect('.*ssword:')
    pex.sendline(passwd)
    pex.expect(user)
    pex.flush()
    
    routers = ['192.168.0.1',
               '192.168.9.1',
               '192.168.10.1',
               '192.168.11.1',
               '192.168.12.1',
               '192.168.13.1',
               '192.168.14.1',
               '192.168.15.1',
               '192.168.16.1',
               '192.168.17.1',
               '192.168.24.1']
    
    for ipaddr in routers:
        print ipaddr
        pex.login_rtx(ipaddr,user,passwd,adminpasswd)
        
        pex.sendln('# something')

        pex.logout_rtx()
    
 
    
    



