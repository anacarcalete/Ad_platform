# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 22:09:42 2016

@author: Any
"""
import json
import unirest;
response = unirest.get("https://enclout-dmoz.p.mashape.com/show.json?auth_token=Vs5_-zExrpLc_SymWMiT&url=http://www.ncaa.com/sports/football",
  headers={
    "X-Mashape-Key": "xrLJ2Gzg1bmshbTvNBkEysKpEM5op1XjyzPjsnHGAnY9zDthFj",
    "Accept": "application/json"
  }
  
  
)


print response.body