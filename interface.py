#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
ZetCode wxPython tutorial

This example shows a simple menu.

author: Jan Bodnar
website: www.zetcode.com
last modified: September 2011
'''

import wx

class Example(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs) 
            
        self.InitUI()
        
    def InitUI(self):    
        #CRIA A BARRA DE MENU
        menubar = wx.MenuBar()

        #CRIA OS INDEXES DO MENU
        fileMenu = wx.Menu()
        #GERA O CONTEÚDO DO INDEX DO MENU
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')


        #CRIA OS INDEXES DO MENU
        fileMenu2 = wx.Menu()
        #GERA O CONTEÚDO DO INDEX DO MENU
        fitem2 = fileMenu2.Append(wx.ID_EXIT, 'Copiar', 'Quit application')

        #INSERE OS INDEXES DO MENU
        menubar.Append(fileMenu, '&File')
        menubar.Append(fileMenu2, '&Editar')
        self.SetMenuBar(menubar)

        #DEFINE A FUNÇÃO DO MENU DANDO BIND EM fitem
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)
        
        #DEFINE A FUNÇÃO DO MENU DANDO BIND EM fitem2
        self.Bind(wx.EVT_MENU, self.Copiar, fitem2)
        self.SetSize((300, 200))
        self.SetTitle('Simple menu')
        self.Centre()
        self.Show(True)
        
    def OnQuit(self, e):
        self.Close()

    #PARA DEFINIR UMA FUNÇÃO, FAÇA ELA RECEBER COMO PARAMETRO SELF E e
    def Copiar(self, e):
        print('Não é possível copiar.')
def main():
    #INVOCA O MÉTODO PARA A CONTRUÇÃO DO APP
    ex = wx.App()
    Example(None)
    #LOOPING DA INTERFACE GRAFICA
    ex.MainLoop()    


if __name__ == '__main__':
    main()
