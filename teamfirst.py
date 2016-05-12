#!/usr/bin/python

import requests
import argparse
import sys
import webbrowser

API_BASE="https://api.github.com"

def main():
    parser = argparse.ArgumentParser(description='Force yourself to put the team first.')
    parser.add_argument('-t', '--token', help='Github oauth token (ie XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX)')
    parser.add_argument('-r', '--repo', help='Github repo (ie cbarraford/teamfirst)')
    parser.add_argument('-p', '--participating', help="Only participating github notifications", action='store_true')
    parser.add_argument('-o', '--open', help="Launch browser if there are unread notifications", action="store_true")
    args = parser.parse_args()

    # ensure we have a github api token
    if args.token is None:
        print("Must specify token (--token)")
        sys.exit(1)

    # use repo notifications api endpoint if repo given
    if args.repo:
        api_endpoint="%s/repos/%s/notifications" % (API_BASE, args.repo)
    else:
        api_endpoint="%s/notifications" % API_BASE

    # ensure we only get participating notifications
    if args.participating:
        api_endpoint+="?participating=true"

    headers=dict(Authorization="token %s" % args.token)
    resp = requests.get(api_endpoint, headers=headers)
    json = resp.json()

    if resp.status_code >= 300:
        print("Failed to get notifications")
        print(json['message'])
        sys.exit(1)

    notification_count = len(json)
    if notification_count > 0:
        print("You have unread notifications that need your attention (%d)" % notification_count)
        if args.open:
            launch_browser(args)
        sys.exit(1)

def launch_browser(args):
    if args.participating:
        webbrowser.open("https://github.com/notifications/participating")
    else:
        if args.repo:
            webbrowser.open("https://github.com/%s/notifications" % args.repo)
        else:
            webbrowser.open("https://github.com/notifications")

if __name__ == "__main__":
    main()
