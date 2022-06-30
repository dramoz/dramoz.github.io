# Copyright 2022 - Danilo Ramos
# Python script to automatically generate a sitemap TOC from collections information
import site
import sys, os
import frontmatter
import oyaml as yaml
from pathlib import Path
from addict import Dict
from pprint import pprint

if __name__ == "__main__":
  cfg_path = "_config.yml"
  config = Dict(yaml.safe_load(Path(cfg_path).read_text()))
  sitemap = {}
  for collection in config.collections:
    tree = {}
    c_path = f"_{collection}/"
    for fl in Path(c_path).rglob('**/*'):
      if fl.is_file():
        fm = frontmatter.load(str(fl))
        print(fm.metadata)
        fl = Path(str(fl).replace(c_path, ""))
        clvl = tree
        if str(fl.parent) != '.':
          tags_lst = str(fl.parent).split('/')
          for tag in tags_lst:
            if tag not in clvl:
              clvl[tag] = {}
            clvl = clvl[tag]
        
        else:
          tags_lst = []
        
        if 'tags' in fm.metadata:
          tags_lst.extend(fm.metadata['tags'])
          
        fm.metadata['tags'] = list(set(tags_lst))
        clvl[fl.stem] = fm.metadata
        
    sitemap[collection.title()] = tree
  pprint(sitemap)
