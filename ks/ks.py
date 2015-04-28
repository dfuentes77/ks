#!/usr/bin/env python
# Kickstarter Interview script
# Created by:  Damian Fuentes

import os
import sys
import re
import click
import sqlite3 as lite
from baluhn import verify

databasefile='ks.db'


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """Mini Kickstarter command line tool."""
    pass

####  Create a new project with a project name and a target dollar amount 
@cli.command('project', short_help='Creates a project')
@click.argument('projectname')
@click.argument('targetamount')
def project(projectname,targetamount):
    """Create a new project with a project name and a target dollar amount"""
    if (validatename(projectname) and validatenum(targetamount)):
        targetamount=float(targetamount)
        con = lite.connect(databasefile)
        with con:
            cur = con.cursor()    
            cur.execute("SELECT Id FROM projects where name=?", (projectname,))
            exists = cur.fetchone()
            if exists:
                click.echo("Project name already exists!")
                sys.exit()
            cur.execute("INSERT INTO projects (Name, Tamount) VALUES (?, ?)", (projectname, targetamount))
            click.echo("Added %s project with target of $%-.2f" % (projectname, targetamount))


####  Back a project with a given name of the backer, the project to be backed, a credit card number and a backing dollar amount 
@cli.command('back', short_help='Backs a project')
@click.argument('backername')
@click.argument('projectname')
@click.argument('creditcard')
@click.argument('backeramount')
def back(backername,projectname,creditcard,backeramount):
    """Back a project with a given backer name, the project to be backed, a credit card number and a backing dollar amount"""
    if (validatename(backername) and validatename(projectname) and validateCC(creditcard) and validatenum(backeramount)):
        backeramount=float(backeramount)
        con = lite.connect(databasefile)
        with con:
            cur = con.cursor()    
            cur.execute("SELECT Id FROM backers where CC=?", (creditcard,))
            exists = cur.fetchone()
            if exists:
                click.echo('ERROR: That card has already been added by another user!')
                sys.exit()
            cur.execute("INSERT INTO backers (Name, Projectname, CC, Bamount) VALUES (?, ?, ?, ?)", (backername, projectname, creditcard, backeramount))
            click.echo("%s backed project %s for $%-.2f" % (backername, projectname, backeramount))


####  Display a project including backers and backed amounts
@cli.command('list', short_help='List backers of a project')
@click.argument('projectname')
def list(projectname):
    """Display a project including backers and backed amounts"""
    backedamount=0
    con = lite.connect(databasefile)
    with con:
        cur = con.cursor()    
        cur.execute("SELECT Id FROM projects where name=?", (projectname,))
        exists = cur.fetchone()
        if exists:
            cur.execute("SELECT * FROM backers where Projectname=?", (projectname,))
            rows = cur.fetchall()
            numbackers=len(rows)
            for row in rows:
                backedamount+=row[4]
                click.echo("-- %s backed for $%-.2f" % (row[1],row[4]))
        else:
            click.echo("That project doesn't exist!")
            sys.exit()

        cur.execute("SELECT Tamount FROM projects where name=?", (projectname,))
        tamount = cur.fetchone()
        if tamount[0] > backedamount:
            amountneeds = tamount[0] - backedamount
            click.echo("%s needs $%-.2f more dollars to be successful.  It has %d backers" % (projectname,amountneeds,numbackers))
        else:
            click.echo("%s is successful!  It has %d backers" % (projectname,numbackers))
        

####  Display a list of projects that a backer has backed and the amounts backed
@cli.command('backer', short_help='List projects a backer has backed')
@click.argument('backername')
def backer(backername):
    """Display a list of projects that a backer has backed and the amounts backed"""
    con = lite.connect(databasefile)
    with con:
        cur = con.cursor()    
        cur.execute("SELECT * FROM backers where Name=?", (backername,))
        rows = cur.fetchall()
        if len(rows) > 0:
            for row in rows:
                click.echo("-- Backed %s for $%-.2f" % (row[2],row[4]) )
        else:
            click.echo("That backer doesn't exist!")
            sys.exit()



def validatename(name):
    valid = re.match('^[\w_-]+$', name) is not None
    if not (valid and len(name) > 3 and len(name) <= 20):
        click.echo("All names must be between 4 and 20 characters in length and be alphanumeric but can include dashes and underscores")
        sys.exit()
    return True 

def validatenum(num):
    if not float(num):
        click.echo("Dollar amount must be a real number with no dollar sign or other symbols")
        sys.exit()
    return True

def validateCC(cc):
    if not verify(cc):
        click.echo("ERROR: This card is invalid")
        sys.exit()
    return True


def createtables():
    con = lite.connect(databasefile)
    with con:
    
        cur = con.cursor()    
        cur.execute("CREATE TABLE projects (Id      INTEGER PRIMARY KEY   AUTOINCREMENT, \
                                            Name    TEXT NOT NULL CHECK(length(Name) <=20 and \
                                                                        length(Name) > 3) , \
                                            Tamount REAL)")
        cur.execute("CREATE TABLE backers  (Id      INTEGER PRIMARY KEY   AUTOINCREMENT, \
                                            Name    TEXT NOT NULL CHECK(length(Name) <=20 and \
                                                                        length(Name) > 3) , \
                                            Projectname    TEXT NOT NULL CHECK(length(Projectname) <=20 and \
                                                                        length(Projectname) > 3) , \
                                            CC      BIGINT CHECK(length(CC) <=19) , \
                                            Bamount REAL, \
                                            FOREIGN KEY(Projectname) REFERENCES projects(Name))")



def main():
    if not os.path.isfile(databasefile):
        createtables()
    cli()

