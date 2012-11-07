#!/usr/bin/env python

import os,subprocess as sub

sub.call(['make'])
sub.call(['sudo','make','install'])
