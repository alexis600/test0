import wx

class EjemploTexto(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        self.InitUI()
        self.Centre()

    def InitUI(self):

        self.panel = wx.Panel(self)
        self.sizer = wx.GridBagSizer(4, 3)

        self.texto = wx.StaticText(self.panel, label = "Nombre: ")
        self.sizer.Add(self.texto, pos = (0,0), flag = wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        self.textoNuevo = wx.StaticText(self.panel, label="Me llamo: ")
        self.sizer.Add(self.textoNuevo, pos=(2, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=4)

        self.textoEdit = wx.TextCtrl(self.panel)
        self.sizer.Add(self.textoEdit, pos=(0, 1), span = (1, 2), flag=wx.EXPAND | wx.LEFT | wx.BOTTOM, border=2)

        self.boton = wx.Button(self.panel, label="enviar", size = (50, 20))
        self.sizer.Add(self.boton, pos=(2, 4), flag=wx.RIGHT | wx.BOTTOM)

        self.panel.Bind(wx.EVT_BUTTON, self.TomarTexto, self.boton)

        self.panel.SetSizerAndFit(self.sizer)

        self.meLlamo = wx.StaticText(self.panel, label = "")
        self.sizer.Add(self.meLlamo, pos = (2, 2), span = (2,2))

    def TomarTexto(self, event):
            textoTomado = 'Hola mundo'
            textoTomado = self.textoEdit.GetValue()
            self.meLlamo.SetLabel(textoTomado)


app = wx.App(False)
frame = EjemploTexto(None)
frame.Show()
app.MainLoop()




