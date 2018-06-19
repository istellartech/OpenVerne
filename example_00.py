# -*- coding: utf-8 -*-
""" Simplest example """

from OpenVerne import IIP
import numpy as np

posLLH_ = np.array([35.0, 140.0, 100])
velNED_ = np.array([10, 0, 0])

_IIP = IIP(posLLH_, velNED_)
print(_IIP)
