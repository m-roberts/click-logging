# -*- coding: utf-8 -*-
# flake8: noqa

import click

__version__ = '1.0.0'


if not hasattr(click, 'get_current_context'):
    raise RuntimeError('You need Click 5.0.')

from .core import (
    ClickHandler,
    ColorFormatter,
    basic_config,
)

from .options import simple_verbosity_option
