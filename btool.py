# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:15:34 2015

@author: aneasystone
"""

import transformor

def main():
    
    link = transformor.torrent2magnet('torrents\\ubuntu.torrent')
    print link
    
    r = transformor.magnet2torrent(
        #'magnet:?xt=urn:btih:1619ecc9373c3639f4ee3e261638f29b33a6cbd6&dn=ubuntu-14.10-desktop-i386.iso', 
        'magnet:?xt=urn:btih:2bc66f04d4d7ab3815158f89779d50965adb0ae4',
        't.torrent')
    if r == True:
        print 'Torrent created successfully!'
    else:
        print 'Torrent created Failed!'

 
if __name__ == '__main__':
    main()