# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 23:42:17 2021

@author: raang
"""

#pip install python-gantt

from datetime import date
import gantt


# Change font default
gantt.define_font_attributes(fill='black', stroke='black', stroke_width=0, font_family="Verdana")

# Create 2 employees
JD = gantt.Resource("JD")
Alguien = gantt.Resource("Alguien")
