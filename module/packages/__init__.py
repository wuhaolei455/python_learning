print('this is __init__.py')
# part1 package config

# part2 package export
from .no_main import vip_lv_name
from . import no_main

# part3 package version、author
__version__ = '1.0'
__author__ = 'wuhaolei'