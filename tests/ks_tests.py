import os
from scripttest import TestFileEnvironment

env = TestFileEnvironment('tests/test-output')

databasefile='ks.db'

def test_project():
    try:
        os.remove(databasefile)
    except OSError:
        pass
    result = env.run('ks project TestProj1 150')
    assert result.stdout.startswith('Added TestProj1 project with target of $150.00')
    assert databasefile in result.files_created

    result = env.run('ks project Test_Proj-2 200')
    assert result.stdout.startswith('Added Test_Proj-2 project with target of $200.00')

    result = env.run('ks project Test,Proj-3 300')
    assert result.stdout.startswith('All names must be between 4 and 20 characters in length and be alphanumeric but can include dashes and underscores')


def test_back():
    result = env.run('ks back john TestProj1 4111111111111111 40.50')
    assert result.stdout.startswith('john backed project TestProj1 for $40.50')

    result = env.run('ks back tom Test_Proj-2 5474942730093167 250.50')
    assert result.stdout.startswith('All names must be between 4 and 20 characters in length and be alphanumeric but can include dashes and underscores')

    result = env.run('ks back jack Test_Proj-2 5474942730093167 250.50')
    assert result.stdout.startswith('jack backed project Test_Proj-2 for $250.50')

    result = env.run('ks back jill Test_Proj-2 5461576474477163 150.30')
    assert result.stdout.startswith('jill backed project Test_Proj-2 for $150.30')

    result = env.run('ks back mike Test_Proj-4 1234567890123456 50')
    assert result.stdout.startswith('ERROR: This card is invalid')

    result = env.run('ks back mike Test_Proj-4 4111111111111111 60')
    assert result.stdout.startswith('ERROR: That card has already been added by another user!')

def test_list():
    result = env.run('ks list TestProj1')
    assert result.stdout.startswith('-- john backed for $40.50')
    assert result.stdout.endswith('TestProj1 needs $109.50 more dollars to be successful.  It has 1 backers\n') 

    result = env.run('ks list Test_Proj-2')
    assert result.stdout.startswith('-- jack backed for $250.50')
    assert result.stdout.endswith('Test_Proj-2 is successful!  It has 2 backers\n') 

    result = env.run('ks list NoProj1')
    assert result.stdout.startswith('That project doesn\'t exist!')


def test_backer():
    result = env.run('ks backer jack')
    assert result.stdout.startswith('-- Backed Test_Proj-2 for $250.50')
    
    result = env.run('ks backer ellis')
    assert result.stdout.startswith('That backer doesn\'t exist!')
