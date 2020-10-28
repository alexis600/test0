import wx

#import sys
#print(sys.path)
##sino sale la ruta q me hace falta, la agrego asi:
#sys.path.append('C:/etc')
from wx import Frame

app = wx.App()

#frame = wx.Frame(None, -1, '2 Ventana')  # type: Frame

frame = wx.Frame(None, -1, '2 Ventana', size = (300, 400))


#frame = wx.Frame(None, -1, 'Primer Ventana', style = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)


frame.Show()
app.MainLoop()


