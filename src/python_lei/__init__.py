# -*- coding: utf-8 -*-
import logging

from pkg_resources import DistributionNotFound, get_distribution
from python_lei import pylei

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "python-lei"
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = "unknown"
finally:
    del get_distribution, DistributionNotFound


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
