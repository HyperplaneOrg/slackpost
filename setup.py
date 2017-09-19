try:
   from setuptools import setup
except:
   from distutils.core import setup

from slackpost import __version__

long_description = """A convenience utility that helps one post slack messages to channels that have defined webhooks."""

setup (
   name = "slackpost",
   version = __version__,
   description = "Posts messages to slack channels",
   long_description=long_description,
   author = "Andrew Michaelis",
   author_email = "amac@hyperplane.org",
   license = "MIT",
   url = "https://github.com/HyperplaneOrg/slackpost",
   packages = ["slackpost"],
   scripts=['slckp']
)

try:
   inst_prefix = None
   iopts = distutils.core._setup_distribution.command_options['install']
   inst_prefix = iopts['prefix'][1]
except:
   pass

