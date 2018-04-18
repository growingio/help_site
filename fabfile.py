#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
from fabric.api import *

env.hosts = "apps@cnprd3"

@task
def deploy():
    local("git pull")
    local('[ -d "_book" ] && rm -rf _book')
    local("gitbook build")
    local("cp ./_book/.gitbook/assets/* ./_book/assets/")
    local("rm -rf ./_book/.gitbook")
    #local('sed -i 's/\.gitbook\///g' ./_book/**/*.html')  # 连续两个*在命令行可以，但是这里运行无效
    local('find . -name "*.html" |xargs sed -i "s#\.gitbook/##g"')
    run('[ -d "/tmp/_book" ] && rm -r /tmp/_book/*')
    put("_book/", "/tmp")
    run('[ -d "/tmp/_back" ] && rm -r /tmp/_back/*')
    run("mv /var/www/cms/new_help_html /tmp/_back")
    run("cp -r /tmp/_book  /var/www/cms/new_help_html")
    run("sudo /usr/sbin/nginx -s reload")