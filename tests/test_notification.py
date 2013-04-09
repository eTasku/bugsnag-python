from nose.tools import with_setup

import bugsnag
from bugsnag.configuration import Configuration

def setup_func():
    bugsnag.configure(api_key="dcc345d219ef5107c6ce8aca68a40af2")

def teardown_func():
    bugsnag.configuration = Configuration()

@with_setup(setup_func, teardown_func)
def test_notification():
    pass # TODO