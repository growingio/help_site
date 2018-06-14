#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from fabric.api import *

env.hosts = "apps@cnprd3"

@task
def deploy():
    local("gitbook install")
    local("gitbook build")
    run('[ -d "/tmp/_book" ] && rm -rf /tmp/_book/* || mkdir -p /tmp/_book')
    put("_book/", "/tmp")
    run('[ -d "/tmp/_back" ] && rm -rf /tmp/_back/* || mkdir -p /tmp/_back')
    run("mv /var/www/cms/new_help_html /tmp/_back")
    run("cp -r /tmp/_book  /var/www/cms/new_help_html")
    run("sudo /usr/sbin/nginx -s reload")


#如何发布pdf
#https://calibre-ebook.com/download 下载安装calibre
#ln -s /Applications/calibre.app/Contents/MacOS/ebook-convert /usr/local/bin
#gitbook pdf . GrowingIO帮助文档.pdf
