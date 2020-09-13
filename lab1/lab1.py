#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
cv2.__version__


# In[4]:


#прочитать видео с вебки, сохранить его в "output.avi"
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("lab1.avi",fourcc,60.0,(640,480))
while(cap.isOpened()):
    ret, frame=cap.read()
    if ret==True:
        cv2.imshow("frame",frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
#закрыть захват видео
cap.release()
out.release()
cv2.destroyAllWindows()


# In[18]:


#прочитать видео из файла. наложить на него чб и цветные геометрические фигуры.
cap=cv2.VideoCapture('output.avi')
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter('output_gray.avi',fourcc,60.0,(640,480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        grayBGR= cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        begin = (200,200) 
        end = (400,400) 
        thickness = 5
        cv2.rectangle(grayBGR, begin, end,(0,255,0) , thickness)
        x1, y1 = (640,480)
        x2, y2 = (0,0)
        cv2.line(grayBGR, (x1,y1), (x2,y2), (255,0,0), thickness+2)
        out.write(grayBGR)
    else:
        break
#закрыть захват видео
cap.release()
out.release()
cv2.destroyAllWindows()

