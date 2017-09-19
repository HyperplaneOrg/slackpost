SlackPost
=========
slackpost is a convenience package to help post slack messages to channels that have predefined webhooks. The webhooks are taken from a standard configuration file. This package is intended to be dead simple and for users that just want to send messages to a channel with minimal effort, there is **no need for an api token** but a user of this utility needs to create a predefined webhook, request a team administrator to add a hook if needed. 

Example usage:
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
hook = https://hooks.slack.com/services/.....

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
