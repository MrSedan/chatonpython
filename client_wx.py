import wx


class MainWindow(wx.Frame):
    button: wx.Button
    text_box: wx.TextCtrl

    def __init__(self, *args, **kw):
        super(MainWindow, self).__init__(*args, **kw)

        sizer = wx.BoxSizer(wx.VERTICAL)

        self.text_box = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.button = wx.Button(self, label="Test button")

        sizer.Add(self.text_box, flags=wx.SizerFlags(1).Border(wx.ALL, 10).Expand())
        sizer.Add(self.button)

        self.button.Bind(wx.EVT_BUTTON, self.update_text)

        self.SetSizer(sizer)

    def update_text(self, event):
        self.text_box.AppendText(f"Button clicked! {event}")


if __name__ == '__main__':
    app = wx.App()
    frm = MainWindow(None, title="Precol")
    frm.Show()
    app.MainLoop()
