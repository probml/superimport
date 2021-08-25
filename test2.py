
import sys
import subprocess
import pkg_resources
import requests
import inspect
import re
import logging
import os
import argparse
from glob import glob
import importlib


pipreqs_mapping_url="https://raw.githubusercontent.com/bndr/pipreqs/master/pipreqs/mapping"
superimport_mappin_url="https://raw.githubusercontent.com/probml/superimport/main/superimport/mapping2"

def load_file_from_url(url):
     with requests.get(url) as r:
         return r.content.decode("utf-8") 
def get_packages_from_string(packages_string, dim="="):
    
    if dim:
        packages = {
            c.split(dim)[0]: c.split(dim)[1] for c in packages_string.split("\n") if c
        }
    else:
        packages = {c: True for c in packages_string.split("\n") if c}
    return packages

pipreqs_mapping_string = load_file_from_url(pipreqs_mapping_url)
superimport_mapping_string = load_file_from_url(superimport_mappin_url)
mapping = get_packages_from_string(pipreqs_mapping_string, ":")
mapping2= get_packages_from_string(superimport_mapping_string, ":")


dir_name = os.path.dirname(__file__)
maping = {**mapping, **mapping2}  # adding two dictionaries

maping2={(k,v) for k,v in maping.items() if v =="pyro" or k=="pyro"}

gnippam = {v: k for k, v in maping.items() if v =="pyro" or k=="pyro"} 

print(maping2)
print(gnippam)