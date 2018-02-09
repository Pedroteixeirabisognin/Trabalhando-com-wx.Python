#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
ZetCode wxPython tutorial

In this example, we manually create 
a menu item.

author: Jan Bodnar
website: www.zetcode.com
last modified: September 2011
'''

import wx

APP_EXIT = 1

class Example(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs) 
            
        self.InitUI()
        
    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        #INSERE UM ATALHO NO MENU
        qmi = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q')
        #INSERE A IMAGEM NO MENU
        qmi.SetBitmap(wx.Bitmap('exit.png'))
        fileMenu.AppendItem(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.SetSize((250, 200))
        self.SetTitle('Icons and shortcuts')
        self.Centre()
        self.Show(True)
        
    def OnQuit(self, e):
        self.Close()

def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()
