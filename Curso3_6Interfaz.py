import wx

class VentanaEj(wx.Frame):
    def __init__(self, parent, title):
        super(VentanaEj, self).__init__(parent, title = "Segunda Ventana", size = (450, 300))
        #self.Centre()
        self.SetPosition((100,500))
        self.Show(True)

#app = wx.App()
#ventana = VentanaEj(None, 'Hola')
#app.MainLoop()

if __name__== '__main__':
    app = wx.App()
    VentanaEj(None, title='Nueva Ventana')
    app.MainLoop()