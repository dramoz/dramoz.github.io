# Copyright 2022 - Danilo Ramos
# Python script to automatically generate a sitemap TOC from collections information
import sys, os
from pathlib import Path
from addict import Dict
import oyaml as yaml

if __name__ == "__main__":
  cfg_path = "_config.yml"
  config = Dict(yaml.safe_load(Path(cfg_path).read_text()))
  sitemap = {}
  for collection in config.collections:
    tree = {}
    c_path = f"_{collection}/"
    for fd in Path(c_path).rglob('**/*'):
      if fd.is_dir():
        tags_lst = str(fd).replace(c_path, "").split('/')
        print(tags_lst)
        
        
    
    sitemap[collection] = tree
