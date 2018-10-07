# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2017, 2018 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""ZeroMQ tracker class."""

import json


class ZeroMQTracker(object):
    """ZeroMQ Tracker class."""

    def __init__(self, socket=None, connect_string=None, identifier='cwl'):
        """Constructor."""
        self.identifier = identifier
        self.socket = socket
