import wx

class EjemploLogin(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)

        self.Centre()


        self.panel = wx.Panel(self)
        self.sizer = wx.GridBagSizer(4,2)

        self.textoU = wx.StaticText(self.panel, label = 'Usuario:')
        self.sizer.Add(self.textoU, pos = (0, 0), flag = wx.TOP, border = 3)

        self.textoP = wx.StaticText(self.panel, label='Password:')
        self.sizer.Add(self.textoP, pos=(1, 0), flag=wx.LEFT, border=3)

        self.textoR = wx.StaticText(self.panel, label='Respuesta:')
        self.sizer.Add(self.textoR, pos=(2, 0), flag=wx.BOTTOM, border=3)


        self.textoEditU = wx.TextCtrl(self.panel)
        self.sizer.Add(self.textoEditU, pos = (0, 1), span = (1, 3), flag = wx.EXPAND | wx.LEFT | wx.RIGHT)

        self.textoEditP = wx.TextCtrl(self.panel)
        self.sizer.Add(self.textoEditP, pos = (1, 1), span = (3, 1), flag = wx.EXPAND)

        self.boton = wx.Button(self.panel, label = 'log', size = (40, 20))
        self.sizer.Add(self.boton, pos = (3, 3), flag = wx.RIGHT)


        self.panel.Bind(wx.EVT_BUTTON, self.Validar, self.boton)

        self.panel.SetSizerAndFit(self.sizer)

    def Validar(self, event):
        usuario = self.textoEditU.GetValue()
        password = self.textoEditP.GetValue()

        if (usuario == 'Ale' and password == 'asd'):
            self.textoR.SetLabel('OK')
            nv = NuevaVentana(None)
            nv.Show()
        else:
            self.textoR.SetLabel('NO')

class NuevaVentana(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        panel = wx.Panel(self, -1)
        txt = wx.StaticText(panel, label = 'Entramos!')


app = wx.App(False)
frame = EjemploLogin(None)
frame.Show()
app.MainLoop()
