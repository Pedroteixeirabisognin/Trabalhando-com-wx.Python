import wx

'''app = wx.App()

frame = wx.Frame(None, -1,'Window Title')

frame.Show()

app.MainLoop()'''
#Extende a classe wx.Frame
class WindowClass(wx.Frame):
    #Cria o método construtor
    
    '''def __init__(self, parent, title):'''
    #args e kwargs são atributos especiais do python que permitem que o método receba vários parâmetros sem a necessidade de modificar o contrutor.
    def __init__(self, *args, **kwargs):
        #Define a classe, chamando o método construtor da classe wx.Frame e passando os parâmetros
        super(WindowClass, self).__init__(*args, **kwargs)
        #Define que a janela abrirá nas cordenadas x,y especificadas
        '''self.Move((800,550)) '''
        '''self.Center()
        self.Show()'''

        self.basic_gui()

    def basic_gui(self):

        panel = wx.Panel(self)

        #CRIA A BARRA DE STATUS DO ARQUIVO
        self.CreateStatusBar()
        self.SetStatusText('Hello There!')

        #CRIA A BARRA DE MENU DO ARQUIVO
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        editMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')

        menuBar.Append(fileMenu,'&File')

        menuBar.Append(editMenu, 'Edit')

        #Cria uma caixa de texto
        wx.TextCtrl(panel, pos=(10,10), size = (250, 150))

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.onQuit, exitItem)

        #SETA O TAMANHO DA JANELA E O TÍTULO
        self.SetSize((300,200))
        self.SetTitle('Epic Window')

        #CENTRALIZA A POSIÇÃO QUE A JANELA APARECERÁ
        self.Centre()
        #TORNA OS ATRIBUTOS VISÍVEIS
        self.Show(True)
        
    def onQuit(self, e):
        #FECHA A APLICAÇÃO
        self.Close()

def main():
    app = wx.App()
    WindowClass(None)
    app.MainLoop()

#EXECUTA O MÉTODO MAIN
main()
