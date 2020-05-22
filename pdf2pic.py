# -*- coding: utf-8 -*-
"""
Created on Thu May 21 19:17:29 2020

@author: cq.zan
"""

import fitz
import os
import datetime
 
def pyMuPDF_fitz(pdfPath, imagePath):
    pdfDoc = fitz.open(pdfPath)
    print(pdfDoc.pageCount)
    if pdfDoc.pageCount==1: #如果pdf只有一页
        for pg in range(pdfDoc.pageCount):
            page = pdfDoc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
            # 此处若是不做设置，默认图片大小为：792X612, dpi=96
            zoom_x = 1.33333333 #(1.33333333-->1056x816)   (2-->1584x1224)
            zoom_y = 1.33333333
            mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pix = page.getPixmap(matrix=mat, alpha=False)    
        pix.writePNG(imagePath)#将图片写入指定的文件夹内
    else:
        for pg in range(pdfDoc.pageCount):
            page = pdfDoc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
            # 此处若是不做设置，默认图片大小为：792X612, dpi=96
            zoom_x = 1.33333333 #(1.33333333-->1056x816)   (2-->1584x1224)
            zoom_y = 1.33333333
            mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pix = page.getPixmap(matrix=mat, alpha=False)
            path="E:/数据/发票/"+'多张图片'+str(pg)+'.png'
            pix.writePNG(path)#将图片写入指定的文件夹内 
            print("已保存第"+str(pg)+'张')    
def file_name():
    list_name=[]
    for  root,dirs,files in os.walk("E:\数据\发票\"): 
       for file in files:
          filename=os.path.join(root,file)
          list_name.append(filename)
    return list_name   

if __name__ == "__main__":
    f=file_name()
    i=0
    for name in f:
        pdfPath=name
        i+=1
        imagePath = "E:/数据/发票/"+str(i)+'.png'
        pyMuPDF_fitz(pdfPath, imagePath)