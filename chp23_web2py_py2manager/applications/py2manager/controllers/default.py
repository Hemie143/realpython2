# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

@auth.requires_login()
def index():
    project_form = SQLFORM(db.project).process()
    projects = db(db.project).select()
    users = db(db.auth_user).select()
    companies = db(db.company).select()
    return locals()

def tester():
    return locals()
