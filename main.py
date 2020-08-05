{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "ename": "FailSafeException",
     "evalue": "PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe, set pyautogui.FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFailSafeException\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-24-9d3f07847698>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     22\u001b[0m             \u001b[0mcv2\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrectangle\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mframe\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m+\u001b[0m\u001b[0mw\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m+\u001b[0m\u001b[0mh\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m255\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     23\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0my\u001b[0m \u001b[1;33m<\u001b[0m \u001b[0mprev_y\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 24\u001b[1;33m                 \u001b[0mpyautogui\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpress\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'space'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     25\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     26\u001b[0m             \u001b[0mprev_y\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\MSAEvan\\appdata\\local\\programs\\python\\python38\\lib\\site-packages\\pyautogui\\__init__.py\u001b[0m in \u001b[0;36mwrapper\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m    585\u001b[0m         \u001b[0mfuncArgs\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0minspect\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgetcallargs\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mwrappedFunction\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    586\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 587\u001b[1;33m         \u001b[0mfailSafeCheck\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    588\u001b[0m         \u001b[0mreturnVal\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mwrappedFunction\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    589\u001b[0m         \u001b[0m_handlePause\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfuncArgs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"_pause\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\MSAEvan\\appdata\\local\\programs\\python\\python38\\lib\\site-packages\\pyautogui\\__init__.py\u001b[0m in \u001b[0;36mfailSafeCheck\u001b[1;34m()\u001b[0m\n\u001b[0;32m   1669\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mfailSafeCheck\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1670\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mFAILSAFE\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mtuple\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mposition\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mFAILSAFE_POINTS\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1671\u001b[1;33m         raise FailSafeException(\n\u001b[0m\u001b[0;32m   1672\u001b[0m             \u001b[1;34m\"PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe, set pyautogui.FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED.\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1673\u001b[0m         )\n",
      "\u001b[1;31mFailSafeException\u001b[0m: PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe, set pyautogui.FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED."
     ]
    }
   ],
   "source": [
    "'''\n",
    "Full Project Link :- https://github.com/Shahriar-Azad-Evan/Facebook-Hands-free-controller\n",
    "Author: Shahriar Azad Evan\n",
    "Email: shahriarazadevan@gmail.com\n",
    "Website :- http://www.msaevan.xyz\n",
    "FaceBook: http://faecbook.com/shahriarazadevan\n",
    "'''\n",
    "import cv2\n",
    "import numpy as np   \n",
    "import pyautogui\n",
    "\n",
    "cap=cv2.VideoCapture(0)\n",
    "\n",
    "yellow_lower =np.array([22,93,0])\n",
    "yellow_upper =np.array([45, 255 ,255])\n",
    "prev_y=0\n",
    "\n",
    "while True:\n",
    "    ret,frame=cap.read()\n",
    "    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)\n",
    "    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)\n",
    "    mask = cv2.inRange(hsv,yellow_lower,yellow_upper)\n",
    "    contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)\n",
    "    \n",
    "    \n",
    "    \n",
    "    for c in contours:\n",
    "        area =cv2.contourArea(c)\n",
    "        if area > 1000:\n",
    "            #cv2.drawContours(frame,c,-1,(0,255,0),2)\n",
    "            #print(area)\n",
    "            x,y,w,h=cv2.boundingRect(c)\n",
    "            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)\n",
    "            if y < prev_y:\n",
    "                pyautogui.press('space')\n",
    "                \n",
    "            prev_y=y\n",
    "            \n",
    "        \n",
    "    #cv2.imshow('mask',mask)\n",
    "    cv2.imshow('frame',frame)\n",
    "    if cv2.waitKey(10)== ord ('q'):\n",
    "        break\n",
    "        \n",
    "        \n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
