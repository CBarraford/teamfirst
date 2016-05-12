Team First
==========

Team First helps you as a developer to be more responsive to github
notifications. When working apart of a development team, it is important to be attentive and quick to respond to requests from the team, because in many cases they are blocked until you do.

This is accomplished by using a simple python script in a git hook to check if
you having any unread github notifications and fail the hook if you do. This
forces you to not be able to ignore your teammates.

## Features

 * specify a single github repo to check for notifications
 * only check for participating notifications
 * automatically open a browser to github notifications if there are unread
   notifications


## Setup
1. Goto [github tokens page](https://github.com/settings/tokens), and create a
   new token that only has notifications permissions.
1. Create a [git
   hook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) (`pre-push` or `pre-commit` are recommended) that runs `teamfirst.py`

## Command line options

```
usage: teamfirst.py [-h] [-t TOKEN] [-r REPO] [-p] [-o]

Force yourself to put the team first.

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        Github oauth token (ie XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX)
  -r REPO, --repo REPO  Github repo (ie cbarraford/teamfirst)
  -p, --participating   Only participating github notifications
  -o, --open            Launch browser if there are unread notifications
```
