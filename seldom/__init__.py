from .Base_seldom.testCase.TestCase import TestCase
from .Bean_seldom.SeldomConfig import SeldomConfig
from .Base_seldom.testCase.loader_extend import SeldomTestLoader
from .Base_seldom.runner import main, TestMainExtend
from .Base_seldom.utils.send_extend import SMTP, DingTalk
from .Base_seldom.testCase.testCaseStaps import Steps

from .Base_seldom.testCase.skip import *
from .Base_seldom.driver.driver import *
from .Base_seldom.logging.log import *
from .Base_seldom.testdata.parameterization import *

from .Base_seldom.method.request import HttpRequest

__author__ = "bugmaster"

__version__ = "2.7.0"

__description__ = "WebUI/HTTP automation testing framework based on unittest."
