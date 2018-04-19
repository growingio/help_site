#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
from fabric.api import *

env.hosts = "apps@cnprd3"


@task
def deploy():
    local("git pull")
    local("gitbook build")
    run('[ -d "/tmp/_book" ] && rm -r /tmp/_book/*')
    put("_book/", "/tmp")
    run('[ -d "/tmp/_back" ] && rm -r /tmp/_back/*')
    run("mv /var/www/cms/new_help_html /tmp/_back")
    run("cp -r /tmp/_book  /var/www/cms/new_help_html")
    run("sudo /usr/sbin/nginx -s reload")
