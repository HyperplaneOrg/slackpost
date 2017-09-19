SlackPost
=========
_slackpost_ is a convenience package to help post slack messages to channels that have predefined webhooks. The webhooks are taken from a standard configuration file. This package is intended to be dead simple and for users that just want to send messages to a channel with minimal effort, there is **no need for an api token** but a user of this utility needs to create a predefined webhook, request a team administrator to add a hook if needed.

_slckp_ is a simple command line utility to post  messages to channels that have predefined webhooks. This tool may be useful to sysadmins that want to periodically post event messages; possibly send a message post at tail end of a script, etc...

Examples:

```shell
$ slckp "chan message"
```
The text "chan message" is sent to the default channel via the webhook defined in the config file, usually something like ~/.slack/user.conf"

```shell
$ slckp -c foobar "chan message"
```
The text "chan message" is sent to the foobar channel via the webhook defined in the config file.

```shell
$ echo "chan message" | slckp
```
The text "chan message", taken from stdin, is sent to the default channel.

Scripting with the python module directly:
```python
      >>> from slackpost import ChannelPost
      >>> s = ChannelPost.Msgs('~/.slack/user.cfg')
      >>> s.post('testing 1, 2, 3, ...', 'mychannel')
      >>> s.post('testing 4, 5, 6, ...', 'mychannel')

```

The config file is of the format:
---------------------------------

```
# This is the default channel to post the messages to.
[default]
hook = https://hooks.slack.com/services/S146F5N10/B1B3A062B/FFFFFJbQxQLgJbiiiiizRZfz

# A named channel to post the messages to.
[mychannel]
hook = https://hooks.slack.com/services/.....

# Another named channel to post the messages to.
[mychannel2]
hook = https://hooks.slack.com/services/.....

# If you need to pass a cert authority to the requests package then include the ssl
# section, the caauth points to a trusted certificate authority chain (see a potential
# chain from curl's website https://curl.haxx.se/ca/cacert.pem)
[ssl]
caauth = /home/foobar/cacert.pem

```
