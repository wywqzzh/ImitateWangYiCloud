# from tools.Mysnow import MySnow
#
# mysnow=MySnow()
# print(mysnow.get_id())
# import pandas as pd
# import numpy as np
# MasterData=pd.read_csv('C:/Users/76774/Desktop/P2P/Training_Master.csv')
# UserupdateData=pd.read_csv('C:/Users/76774/Desktop/P2P/Training_Userupdate.csv')
# LogInfoData=pd.read_csv('C:/Users/76774/Desktop/P2P/Training_LogInfo.csv')


# def dropNullStd(data):
#     beforelen = data.shape[1]
#     colisNull = data.describe().loc['count'] == 0
#     for i in range(len(colisNull)):
#         if colisNull[i] :
#             data.drop(colisNull.index[i], axis=1, inplace=True)
#
#     stdisZero = data.describe().loc['std'] == 0
#     for i in range(len(stdisZero)):
#         if stdisZero[i]:
#             data.drop(stdisZero.index[i], axis=1, inplace=True)
#     afterlen = data.shape[1]
#     print("剔除的列的数目为:\n",beforelen - afterlen)
#     print("剔除空值或值相同数据后的数据表的形状为:\n",data.shape)
# #查看维度、大小、内存信息
# print('P2P网络贷款主表数据维度:',MasterData.ndim)
# print('P2P网络贷款主表数据大小:',MasterData.shape)
# print('P2P网络贷款主表数据占用内存:\n',MasterData.memory_usage())
# print('P2P网络贷款主表数据所有参数的描述性统计:\n',MasterData.describe())
# dropNullStd(MasterData)

# UserupdateData['ListingInfo1']=pd.to_datetime(UserupdateData['ListingInfo1'])
# UserupdateData['UserupdateInfo2']=pd.to_datetime(UserupdateData['UserupdateInfo2'])
# LogInfoData['Listinginfo1']=pd.to_datetime(LogInfoData['Listinginfo1'])
# LogInfoData['LogInfo3']=pd.to_datetime(LogInfoData['LogInfo3'])
#
# UserupdateData=UserupdateData.groupby(by='Idx')
# LogInfoData=LogInfoData.groupby(by='Idx')
#
# UserupdateCross = pd.crosstab(index=UserupdateData['UserupdateInfo2'],
#                               columns=UserupdateData['ListingInfo1'],
#                               values=UserupdateData['Idx'],
#                               aggfunc= np.size,
#                               margins=True)
# print("使用crosstab方法进行长宽表转换后的用户信息更新表为:\n",UserupdateCross)
# LoginCross = pd.crosstab(index=LogInfoData['LogInfo3'],
#                               columns=LogInfoData['Listinginfo1'],
#                               values=LogInfoData['Idx'],
#                               aggfunc= np.size,
#                               margins=True)
# print("使用crosstab方法进行长宽表转换后的用户信息更新表为:\n",LoginCross)
import tkinter as tk
import os
class Application(tk.Frame):
    def __init__(self,master):
        self.files=os.listdir(r'c:\pythonpa\images\gif')
        self.index=0
        print(r'c:\pythonpa\images\gif'+'\\'+self.files[self.index])
        self.img=tk.PhotoImage(file=r'c:\pythonpa\images\gif'+'\\'+self.files[self.index])
        tk.Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.lblImage=tk.Label(self,width=300,height=300)
        self.lblImage['image']=self.img
        self.lblImage.pack()
        self.f=tk.Frame()
        self.f.pack()
        self.btnPrev=tk.Button(self.f,text='上一张',command=self.prev)
        self.btnPrev.pack(side=tk.LEFT)
        self.btnNext = tk.Button(self.f, text='下一张', command=self.next)
        self.btnNext.pack(side=tk.LEFT)
    def prev(self):
        self.showfile(-1)
    def next(self):
        self.showfile(1)
    def showfile(self,n):
        self.index=(self.index+n)%(len(self.files))
        self.img=tk.PhotoImage(file=r'c:\pythonpa\images\gif'+'\\'+self.files[self.index])
        self.lblImage['image']=self.img
root=tk.Tk()
root.title('简易图片浏览器')
app=Application(master=root)
app.mainloop()