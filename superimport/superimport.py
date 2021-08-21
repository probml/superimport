# If you add `import superimport` to the top of your script
# then running it should automatically trigger installation of all required packages
# Author: Mahmoud Soliman (mjs@aucegypt.edu)

# Code is based on
# https://stackoverflow.com/questions/44210656/how-to-check-if-a-module-is-installed-in-python-and-if-not-install-it-within-t
# https://stackoverflow.com/questions/52311738/get-name-from-python-file-which-called-the-import
# https://gist.github.com/gene1wood/9472a9d0dffce1a56d6e796afc6539b8
# https://stackoverflow.com/questions/8718885/import-module-from-string-variable

import sys
import subprocess
from typing import Optional
import pkg_resources
import requests
import inspect
import re
import logging
import os
import argparse
from glob import glob
pipreqs_mapping_url="https://raw.githubusercontent.com/bndr/pipreqs/master/pipreqs/mapping"
superimport_mappin_url="https://raw.githubusercontent.com/probml/superimport/main/superimport/mapping2"

def download_url(url, file_name):
    # NOTE the stream=True parameter
    with requests.get(url, stream=True) as r:
        with open(file_name, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
def load_file_from_url(url):
     with requests.get(url) as r:
         return r.content

def get_packages_from_string(the_string, dim="="):
    
    if dim:
        packages = {
            c.split(dim)[0]: c.split(dim)[1] for c in packages_string.split("\n") if c
        }
    else:
        packages = {c: True for c in packages_string.split("\n") if c}
    return packages

def get_packages_from_txt(file, dim="="):

    packages_string = open(file).read()
    return get_packages_from_string(packages_string, dim)


def install_if_missing(packages_names, verbose=False):

    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = packages_names - installed
    if missing:
        python3 = sys.executable
        if verbose:
            subprocess.check_call([python3, "-m", "pip", "install", *missing])
        else:
            subprocess.check_call(
                [python3, "-m", "pip3", "install", *missing], stdout=subprocess.DEVNULL
            )


def get_match_list(the_string, the_regex_pattern, guard="#"):
    if not the_string or the_string == "":
        return None
    re_string = re.compile(the_regex_pattern)
    matches_itr = re.finditer(re_string, the_string)
    matches_list = list(matches_itr)
    matches_list = [m for m in matches_list if the_string[m.span()[0] - 1] != guard]
    return matches_list

def preprocess_imports(name):
    if name.find(".")!=-1:
        name = name.split(".")[0]
    if name.endswith(" "):
        name = name[:-1]
    if name.find(" as ")!=-1:
        name = name.split(" as ")[0]
    return name

def get_imports(
    file_string=None,
    patterns=[r"^import (.+)$", r"^from ((?!\.+).*?) import (?:.*)$"]
                ):
    matches = []
    for p in patterns:
        strings = file_string.split("\n")
        for s in strings:
            re_matches = get_match_list(s, p)
            if re_matches:
                for m in re_matches:
                    the_string = m.group()
                    if the_string.startswith("from"):
                        i = the_string.find("import")
                        name = the_string[5:i]
                        name = preprocess_imports(name)
                    else:
                        name = the_string.replace("import ", "")
                        name = preprocess_imports(name)
                    matches.append(name)
    return set(matches)


def check_if_package_on_pypi(packages_name):
    response = requests.get(f"https://pypi.python.org/pypi/{packages_name}/json")
    if response.status_code == 200:
        meta = response.json()
        name = meta["info"]["name"]
        return True, name, meta
    else:
        return False, None, None


def import_module(module_name, verbose=False):
    try:
        # because we want to import using a variable, do it this way
        module_obj = __import__(module_name)
        # create a global object containging our module
        globals()[module_name] = module_obj
    except ImportError as e:
        if verbose:
            sys.stderr.write(
                f"ERROR: superimport : missing python module: {module_name} \nTrying try to install automatcially\n"
            )
        raise e


def get_imports_from_dir(the_dir):
    if not os.path.isdir(the_dir):
                sys.stderr.write("ERROR: superimport : input directory does not exist\n")
    else:
        python_files = glob(os.path.join(the_dir, "*.py"))

    for f in python_files:
        with open(f) as fp:
            file_string = fp.read()
            imports = get_imports(file_string)
            for i in imports:
                yield i    

### Globals


pipreqs_mapping_string = load_file_from_url(pipreqs_mapping_url)
superimport_mapping_string = load_file_from_url(superimport_mappin_url)
mapping = get_packages_from_string(pipreqs_mapping_string, ":")
mapping2= get_packages_from_string(superimport_mapping_string, ":")


dir_name = os.path.dirname(__file__)
maping = {**mapping, **mapping2}  # adding two dictionaries

gnippam = {v: k for k, v in mapping.items()}  # reversing the mapping

if __name__ != "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('-superimport_input_dir', help='input directory')
    parser.add_argument('-superimport_input_file', help='optional input file')
    args=parser.parse_args()

    if not args.superimport_input_dir or not args.superimport_input_file:
            sys.stderr.write("ERROR: superimport : missing input directory or file\n")
    else:
        if args.superimport_input_dir:
            imports = get_imports_from_dir(args.superimport_input_dir)
            # from https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
            imports = {item for sublist in imports for item in sublist}
        elif args.superimport_input_file:
            imports = get_imports(args.superimport_input_file)




    for frame in inspect.stack()[1:]:
        if frame.filename[0] != "<":
            fc = open(frame.filename).read()
            fc = fc.replace("import superimport\n", "")
            matches = get_imports(fc)
            for package in matches:
                try:
                    import_module(package, True)
                except Exception as e:
                    if package in mapping:

                        try:
                            install_if_missing({mapping[package]}, True)
                        except:
                            print("Could not install automatically from map, trying reverse map")
                            install_if_missing({gnippam[package]}, True)
                    else:
                        logging.warning("Package was not found in the reverse index, trying pypi.")
                        status, name, meta = check_if_package_on_pypi(package)
                        if status:
                            logging.info(
                                f"Package{name} was found on PyPi\nNow installing {name}"
                            )
                            install_if_missing({package}, True)
                        else:
                            logging.warning(
                                f"Failed to install {package} automatically"
                            )
            break
