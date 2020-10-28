import wx

class EjemploMenu(wx.Frame):
    def __init__(self, parent, title):
        super(EjemploMenu, self).__init__(parent, title = title)
        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        ###############
        #fileMenu = wx.Menu()

        #fileItem = fileMenu.Append(wx.ID_EXIT, 'Salir', 'Salir de la App')
        #menubar.Append(fileMenu, '&Archivo')
        #self.SetMenuBar(menubar)
        ###############

        archivo = wx.Menu()
        archivo.Append(wx.ID_FILE, '&Archivo')
        archivo.Append(wx.ID_EDIT, '&Editar')
        archivo.Append(wx.ID_SAVE, '&Guardar')
        archivo.Append(wx.ID_HELP, '&Ayuda')
        archivo.AppendSeparator()

        edit = wx.Menu()
        edit.Append(wx.ID_ANY, '&Zitem')
        edit.Append(wx.ID_ANY, '&Xitem')
        edit.Append(wx.ID_ANY, '&Witem')

        archivo.Append(wx.ID_ANY, '&Edit', edit)

        opcion = wx.MenuItem(archivo, wx.ID_ANY, '&Salir')
        archivo.Append(opcion)

        self.Bind(wx.EVT_MENU, self.OnQuit, opcion)
        menubar.Append(archivo, '&Archivo')

        #Pruebo yo
        test = wx.Menu()
        test.Append(wx.ID_CLEAR, '&Probando')
        menubar.Append(test, '&Test')
        tedit = wx.Menu()
        tedit.Append(wx.ID_EXIT, '&Item2')
        test.Append(wx.ID_ANY, '&Item', tedit)

        test2 = wx.Menu()
        test2.Append(wx.ID_CLEAR, 'Probando&2')
        menubar.Append(test2, 'Test&2')
        #Fin test
        self.SetMenuBar(menubar)
        self.Show(True)
        ############

        #self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)
        #self.Show(True)

    def OnQuit(self, e):
        self.Close()


frame = wx.App()
EjemploMenu(None, 'Word')
frame.MainLoop()