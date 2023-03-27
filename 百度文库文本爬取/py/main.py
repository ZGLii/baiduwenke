import wx
import time
import os,sys
import py_bdwenku
# import hello

class windwClass(wx.Frame):
    def __init__(self ,parent ,title):
        super(windwClass ,self).__init__(parent , title= title ,size=(1000,600))
        self.panel = wx.Panel()
        self.Move(250,150)
        self.basicGUI()
        self.my_button()
        self.Status_Bar()
        self.InitUI()
        self.mySetIcon()
        self.Show()
    #文本
    def InitUI(self):
        ''
        self.panel = wx.Panel(self, -1,size = (1000,600))
        self.panel.Layout()
        wx.StaticText(self.panel, label = "百度文库网址:" ,pos = (20,20))
        self._URL = wx.TextCtrl(self.panel,pos = (100,19),size = (850,20), style = wx.TE_LEFT|wx.TE_AUTO_URL)
        self._TXT = wx.TextCtrl(self.panel, pos = (15,80),size = (935,430), style= wx.TE_MULTILINE|wx.TE_RICH2|wx.HSCROLL)
    #图标
    def mySetIcon(self):
        ''' 用我的马里奥'''
        img_path = os.path.abspath(os.path.dirname(__file__))+'\img\mlo.png'
        icon = wx.Icon(img_path)
        self.SetIcon(icon)
    #状态栏
    def Status_Bar(self):
        sb = self.CreateStatusBar(2)
        self.SetStatusWidths([-3, -1])
        self.SetStatusText('Ready', 0)
        #timer
        self.timer = wx.PyTimer(self.Notify)
        self.timer.Start(1000, wx.TIMER_CONTINUOUS)
        self.Notify()
    def Notify(self):
        t = time.localtime(time.time())
        st = time.strftime('%Y-%m-%d   %H:%M:%S', t)
        self.SetStatusText(st,1)
    #菜单栏
    def basicGUI(self):
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        editButton = wx.Menu()
        save_asBUtton = wx.Menu()#保存
        saveBItem = fileButton.Append(wx.ID_SAVE, '保存(&S)', '保存文件')
        exitBItem = fileButton.Append(wx.ID_EXIT, '退出(&X)','单机即可退出')
        aboutBItem = editButton.Append(wx.ID_ABOUT,'关于(&A)', '关于此软件')
        menuBar.Append(fileButton, '菜单(&F)')
        menuBar.Append(editButton, '帮助(&H)')
        self.SetMenuBar(menuBar)#将按钮加入界面
        #菜单按钮行为绑定
        wx.EVT_MENU(self, wx.ID_EXIT, self.OnMenuExit)
        wx.EVT_MENU(self, wx.ID_ABOUT, self.OnMenuAbout)
        wx.EVT_MENU(self, wx.ID_SAVE, self.OnMenuSave)

    def OnMenuExit(self ,event):
        self.Close()
    def OnMenuAbout(self, event):
        wx.MessageBox("百度问库文本下载\n版本号:0.0.1\n作者:余涛")
    def OnMenuSave(self, event):
        text = wx.SaveFileSelector('','txt','yutao')
        self._TXT.SaveFile(filename = text)
    #按钮
    def my_button(self):
        self.OKbutton = wx.Button(self, -1, "确定", pos=(150,45),size=(50,30))
        self.Bind(wx.EVT_BUTTON , self.OnClick, self.OKbutton)

        self.Canclebutton = wx.Button(self, -1, "重置", pos=(250,45),size=(50,30))
        self.Bind(wx.EVT_BUTTON , self.OnClick, self.Canclebutton)
    def OnClick(self,event):
        '''
        按钮实现
        '''
        if event.GetEventObject() == self.OKbutton:
            url = self._URL.GetLineText(0)
            txt = py_bdwenku.my_Get(url)
            self._TXT.SetValue(txt)
        elif event.GetEventObject() == self.Canclebutton:
            self._URL.SetValue('')
        else:
            print('None')

def main():
    app = wx.App()
    windwClass(None, title = '百度文库文本爬取')
    app.MainLoop()

main()