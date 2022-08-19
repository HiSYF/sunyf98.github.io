#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.chdir(r'D:\笔记\blog')
os.system('hexo d \-g')
os.system('git add .')
os.system("git commit -m 'Updated'")
os.system('git push origin source')
print('done')
