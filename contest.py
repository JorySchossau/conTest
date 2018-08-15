
import argparse
import os
import sys
import shutil # rmtree, copyFile
import stat # file permissions (because shutil.copyFile does not retain permissions)
import subprocess # invoking command line module installation
#import psutil # cpu hw core count (not hyperthreading!)
import shlex
#from utils import pyreq
#pyreq.require("gitpython:git,pytest")
#import git
#import pytest

#from utils.helpers import copyfileAndPermissions, this_repo_path, mabe, dotSlashMabe, dirname_baseline, dirname_testline, path_baseline_exe, path_testline_exe
#from utils.helpers import cd, runCmdAndHideOutput, runCmdAndShowOutput, runCmdAndReturnOutput, runCmdAndSaveOutput, rmAllDiffFiles
#from utils.helpers import rmfile, isGCCAvail

## TODO: add ability to pass arguments to mbuild

## temporary stopgaps to make the script run w/o dependencies
def cd(string):
    pass
this_repo_path = 'this_repo_path'
dirname_baseline = 'baseline'
dirname_testline = 'testline'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('repo', type=str)
    parser.add_argument('branch1', type=str)
    parser.add_argument('branch2', type=str)
    parser.add_argument('makeCommand', type=str)
    parser.add_argument('-ls','--list', action='store_true', required = False, default = False, help='list all available tests found')
    parser.add_argument('-s','--subset', type=str, default='', help='test filter expression: "defaults and not settings"')
    args = parser.parse_args()
    cd(this_repo_path)
    if args.list:
        print("running pytest.main only performing test list")
        #pytest.main(shlex.split("--color=yes -v --tb=line --collect-only"))
    else:
        print("running pytest.main")
        compile_default_projects(args)
        #subsetTests = '' if not len(args.subset) else '-k "'+args.subset+'"'
        #pytest.main(shlex.split("--color=yes --tb=line -v {subset}".format(subset=subsetTests)))

def callBuild(makeCommand):
    print("making target with '{}'".format(makeCommand))
    #runCmdAndHideOutput(args.makeCommand)

def compile_default_projects(args):
    #if not os.path.isfile(path_baseline_exe) or args.force:
    if True: ## clone baseline
        print("clone new",args.branch1,"as baseline", flush=True)
        #shutil.rmtree(dirname_baseline,ignore_errors=True)
        if ':' in args.branch1: ## checkout branch at revision (ex: args.branch1 = 'master:5af88d6d5f')
            branch,commit = args.branch1.split(':')
            print("cloning repo '{}' and switching to branch {}".format(args.repo,args.branch1))
            #repo = git.Repo.clone_from(args.repo, dirname_baseline, branch=branch)
            #revision = repo.create_head('revision',commit)
            print("checking out commit'{}'".format(commit))
            #repo.heads.revision.checkout()
        else: ## checkout branch (ex: args.branch1 = 'master')
            #repo = git.Repo.clone_from(args.repo, dirname_baseline, branch=args.branch1)
            print("cloning repo '{}' and switching to branch {}".format(args.repo,args.branch1))
        cd(dirname_baseline)
        print("building baseline", flush=True)
        callBuild(args.makeCommand)
        cd("..")
    if True: ## clone testline
        print("clone new",args.branch2,"as testline", flush=True)
        #shutil.rmtree(dirname_baseline,ignore_errors=True)
        if ':' in args.branch2: ## checkout branch at revision (ex: args.branch1 = 'master:5af88d6d5f')
            branch,commit = args.branch2.split(':')
            print("cloning repo '{}' and switching to branch {}".format(args.repo,args.branch2))
            #repo = git.Repo.clone_from(args.repo, dirname_baseline, branch=branch)
            #revision = repo.create_head('revision',commit)
            print("checking out commit'{}'".format(commit))
            #repo.heads.revision.checkout()
        else: ## checkout branch (ex: args.branch1 = 'master')
            print("cloning repo '{}' and switching to branch {}".format(args.repo,args.branch2))
            #repo = git.Repo.clone_from(args.repo, dirname_baseline, branch=args.branch2)
        cd(dirname_testline)
        print("building testline", flush=True)
        callBuild(args.makeCommand)
        cd("..")
    cd(this_repo_path)

if __name__ == '__main__':
    main()
