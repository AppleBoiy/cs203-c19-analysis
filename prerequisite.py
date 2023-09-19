#!/usr/bin/env python3
import pkgutil
import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# Check if the 'example' package is installed
if pkgutil.find_loader('kaggle') is None:
    install('kaggle')

