Bpex
====

Managing Yamaha RTX1200/810 routers 

Yamaha RTXシリーズをコマンドラインで操作するためのpythonスクリプトです。
pexpectが必須です。
サンプルスクリプトではログインユーザ情報等を保管するためにPitを使っています。


## pexpectのインストール方法
pipをつかってインストールするのが最も簡単
    $ sudo pip install pexpect


## pitのインストールと下準備
同じくpipを使ってインストールするのが簡単
    $ sudo pip install pit
    $ export EDITOR=vim
    $ python
    -- in python shell --
    from pit import Pit
    Pit.get('label名', {'require':{'username':'your USERNAME','password':'your PASSORD','adminpassword':'adminpass'}})
    -- from here --


## bpexの使い方
yamahaルータにssh可能な踏み台サーバを経由する前提でサンプルスクリプトを書いています。

    #ログインするルータのリストを定義
    routers = ['192.168.0.1',
               '192.168.9.1',
               '192.168.10.1',
               '192.168.24.1']
               
    # 個々のルータに順番にログインしてコマンドを投入する           
    for ipaddr in routers:
        print ipaddr
        pex.login_rtx(ipaddr,user,passwd,adminpasswd)
        
        pex.sendln('# something')

        pex.logout_rtx()
        
        
