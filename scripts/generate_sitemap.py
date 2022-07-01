# Copyright 2022 - Danilo Ramos
# Python script to automatically generate a sitemap TOC from collections information
import site
import sys, os
import frontmatter
import oyaml as yaml
import re
from pathlib import Path
from addict import Dict
from pprint import pprint

if __name__ == "__main__":
  cfg_path = "_config.yml"
  config = Dict(yaml.safe_load(Path(cfg_path).read_text()))
  sitemap = {}
  posts = {}
  
  tags = set()
  tags_chk = set()
  tag_rerule = re.compile('[^a-zA-Z]')
  dir_tags = set()
  
  for collection in config.collections:
    tree = {}
    c_path = f"_{collection}/"
    for fl in Path(c_path).rglob('**/*'):
      if fl.is_file():
        fm = frontmatter.load(str(fl))
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
          # validate tags
          for tag in fm.metadata['tags']:
            tchk = tag_rerule.sub('', tag.lower())
            if tchk in tags_chk and tag not in tags:
              print("<WARNING> Similar tag: {tag} already present in {tags}")
            tags_chk.add(tchk)
            tags.add(tag)
        
        fm.metadata['dir_tags'] = list(set(tags_lst))
        dir_tags.update(set(tags_lst))
        
        clvl[fl.name] = fm.metadata['title']
        posts[fl.name] = fm.metadata
      
    sitemap[collection.title()] = tree
    
  """
  # Generate YAML files
  sitemap_path = "_data/sitemap.yml"
  def get_children(tree):
    toc = []
    for c in tree:
      if isinstance(tree[c], str):
        toc.append(tree[c])
      else:
        toc.append( {c:get_children(tree[c])} )
        
    return toc
  
  sitemap_tree = {}
  for p in sitemap:
    sitemap_tree[p] = get_children(sitemap[p])
    
  Path(sitemap_path).write_text(yaml.dump(sitemap_tree))
  """
  
  # Generate sitemap html
  sitemap_path = "_includes/sitemap.html"
  #close_folder = "fa-solid fa-caret-right"
  #open_folder  = "fa-solid fa-caret-down"
  close_folder = "fa-solid fa-folder"
  open_folder  = "fa-solid fa-folder-open"
  
  def html_accordion_button(id, div):
    return f"""
<button onclick="sitemapAccordion('{id}')" class="w3-button w3-block w3-left-align">
  <{div}><i class="{close_folder}" id="{id}_i"></i> {id}</{div}>
</button>
"""
  
  def html_doc_link(url, title):
    return f"""<a href="{url}" class="w3-button" style="text-overflow: wrap;">{title}</a>\n"""
  
  def get_children_html(tree):
    html = ""
    for c in tree:
      if isinstance(tree[c], str):
        html += html_doc_link(c, tree[c])
      else:
        html += html_accordion_button(c, 'h4')
        html += f'<div id="{c}" class="w3-container w3-hide">\n'
        html += get_children_html(tree[c])
        html += '</div>\n\n'
      
    return html
  
  sitemap_html = "<!-- Sitemap TOC -->\n"
  for p in sitemap:
    sitemap_html += html_accordion_button(p, "h5")
    sitemap_html += f'<div id="{p}" class="w3-container w3-hide">\n'
    sitemap_html += get_children_html(sitemap[p])
    sitemap_html += '</div>\n\n'
  
  Path(sitemap_path).write_text(sitemap_html)
  