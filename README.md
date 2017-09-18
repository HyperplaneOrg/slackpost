SlackPost
=========
slackpost is a convenience module to help post slack messages to channels that have defined webhooks. The webhooks are taken from a standard configuration file. This is intended to be dead simple and for users that just want to send messages to a channel with minimal effort and there is no need for an api token.

Example usage:
```python
      >>> from slackpost import ChannelPost 
      >>> s = ChannelPost.Msgs('u.cfg')
      >>> s.post('testing 1, 2, 3, ...', 'mychannel')

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

# If you need to pass a cert authority to the requests package then include the ssl section, the caauth points to a trusted certificate authority chain (see a potential chain from curl's website https://curl.haxx.se/ca/cacert.pem)
[ssl]
caauth = /home/foobar/cacert.pem

```
