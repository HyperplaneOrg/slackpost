"""
slackpost is a convenience package to help post slack messages to channels that have predefined 
webhooks. The webhooks are taken from a standard configuration file. This package is intended to 
be dead simple and for users that just want to send messages to a channel with minimal effort, there 
is no need for an api token but a user of this utility might request a team administrator to create 
a predefined webhook for them, if needed.

Example usage::
      >>> from slackpost import ChannelPost 
      >>> s = ChannelPost.Msgs('~/.slack/user.cfg')
      >>> s.post('testing 1, 2, 3, ...', 'mychannel')
 
The config file is of the format:

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
"""
import urlparse, re, json
import ConfigParser, os

try:
   import requests
except ImportError, e: 
   raise Exception(str(e)+', see https://pypi.python.org/pypi/requests')

class Msgs:
   def __init__(self, config=None, logger=None):
      self.config, self.logger = config, logger
      self.confp, self.caauth, self.chans = None, None, {}
      self.sent = 0
      self.loadConfig()
   #__init__
   
   def loadConfig(self, config=None):
      '''Loads the config file'''
      if config != None:
         self.config = config
      if self.config != None:
         if self.config.startswith('~'):
            self.config = os.path.expanduser(self.config)
         if not os.path.exists(self.config): 
            raise Exception('ERROR : '+self.config+' doesn\'t exist')
         self.confp = ConfigParser.ConfigParser()
         self.confp.read(self.config)
         for c in self.confp.sections(): 
            if self.confp.has_option(c, 'hook'):
               self.chans[c] = self.confp.get(c, 'hook')
         # You can have a channel named ssl if needed, but this name is intended to
         # be reserved to note a certificate auth pem file to verify ssl, when needed.
         if self.confp.has_section('ssl') and self.confp.has_option('ssl', 'caauth'):
            self.caauth = self.confp.get( 'ssl', 'caauth')
            if re.search('NA|False|none', self.caauth, re.I): 
               self.caauth = False
   # loadConfig
   
   def channels(self):
      '''Returns a list of the available channels as defined in the config file.'''
      return self.chans.keys()
   
   def msgsSent(self):
      '''Returns the number of messages sent for this session.'''
      return self.sent 
   
   def post(self, msgtext, channelName=None):
      '''Post a simple text message to a channel

         Args:
            msgtext (string): The message to post
            channelName (string): The name of the channel to post the message to. 
                        The default channel name is 'default'. The channel should 
                        have a predefined webhook, as noted in the config file; see 
                        your slack team administrator for this if necessary.
      '''
      if len(self.chans.keys()) == 0:
         raise Exception('ERROR : no channels available, check config file')
      if channelName != None and channelName in self.chans:
         webhook = self.chans[channelName]
      elif 'default' in self.chans:
         webhook = self.chans['default']
      else:
         raise Exception('ERROR : no default channel available or bad channel name, check config file')
      slackpost = {}
      slackpost['text'] = msgtext

      coninfo = urlparse.urlparse(webhook)
      if coninfo.scheme != 'https':
         raise Exception('ERROR : bad channel hook config (hook is not https)')

      conn = requests.post(webhook, data=json.dumps(slackpost), verify=self.caauth)
      if conn.status_code != requests.codes.ok and self.logger: 
         self.logger.warn('post to channel hook failed, code = '+str(conn.status_code)+', '+str(webhook))
      else:
         self.sent += 1
         if self.logger: 
            self.logger.info('post to channel hook '+str(webhook))
   # post

   def __str__(self):
      return "config file=%s\nchannels=%s\nsent=%d" % ( str(self.config), str(self.channels()), self.sent)
#Msgs

