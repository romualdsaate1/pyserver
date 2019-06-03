# The MIT License (MIT)
#
# Copyright (c) 2019 Romuald Saatepounou Kingni
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
"""
This example displays the orientation, pose and RSSI as well as EMG data
if it is enabled and whether the device is locked or unlocked in the
terminal.

Enable EMG streaming with double tap and disable it with finger spread.
"""

from __future__ import print_function
from myo.utils import TimeInterval
import myo
import sys
import csv



class Listener(myo.DeviceListener):

  def __init__(self):
    self.interval = TimeInterval(None, 0.05)
    self.orientation = None
    self.accelerometor = None
    self.gyroscope = None
    self.pose = myo.Pose.rest
    self.emg_enabled = False
    self.locked = False
    self.rssi = None
    self.emg = None
    self.data1=""
    self.data2=""
    self.data3=""
    self.data4=""
    self.datawo=""
    self.datawi=""
    self.datadt=""
    self.datafs=""
    self.dataf=""
    self.datar=""
    self.dataacc=""
    self.text= []
    self.spamwriter1 = ""
     

  def output(self):
    if not self.interval.check_and_reset():
      return

    #spamwriter1 = csv.writer(self.data1,'excel', delimiter=';')
    #spamwriter1.writerow(["acc1","acc2","acc3","acc4"])
    spamwriter1  = self.spamwriter1


    parts = []
    parts2 = []
    parts3 = []
    parts4 = []
    if self.orientation:
      for comp in self.orientation:
        parts.append('{}{:.4f}'.format(' ' if comp >= 0 else '', comp))
    if self.accelerometor:
      for comp in self.accelerometor:
        parts.append('{}{:.4f}'.format(' ' if comp >= 0 else '', comp))
    if self.gyroscope:
      for comp in self.gyroscope:
        parts.append('{}{:.4f}'.format(' ' if comp >= 0 else '', comp))        
      #spamwriter1 = csv.writer(self.data1,'excel', delimiter=';')
    spamwriter1.writerow(parts)     
    parts.append(str(self.pose).ljust(10))
    parts3.append(str(self.pose).ljust(10))
    parts.append('E' if self.emg_enabled else ' ')
    parts3.append('E' if self.emg_enabled else ' ')
    parts.append('L' if self.locked else ' ')
    parts3.append('L' if self.locked else ' ')
    parts.append(self.rssi or 'NORSSI')
    parts3.append(self.rssi or 'NORSSI')
    
    spamwriter4 = csv.writer(self.data4,'excel', delimiter=';')
       
    spamwriter4.writerow(parts3)


    #if self.accelerometor:
      #print("accelerometer")
      #for comp in self.accelerometor:
        #parts4.append('{}{:.3f}'.format(' ' if comp >= 0 else '', comp))
      #spamwriter5 = csv.writer(self.dataacc,'excel', delimiter=';')
      #spamwriter5.writerow(parts4)
    #print(self.orientation)
    #print(self.gyroscope)
    #print(self.accelerometor)
    
    i = 0
    if self.emg:
      
      for comp in self.emg:
        parts.append(str(comp).ljust(5))
        if str(comp).ljust(5) != '':
          i = 1
          parts2.append(str(comp).ljust(5))
      if i == 1:
        spamwriter3 = csv.writer(self.data2,'excel', delimiter=';')
        spamwriter3.writerow(parts2)
    if i == 1:
      if parts[10] == 'Pose.wave_out':
        spamwriterwo = csv.writer(self.datawo,'excel', delimiter=';')
        spamwriterwo.writerow(parts)
      if parts[10] == 'Pose.wave_in':
        spamwriterwi = csv.writer(self.datawi,'excel', delimiter=';')
        spamwriterwi.writerow(parts)
      if parts[10] == 'Pose.double_tap':
        spamwriterdt = csv.writer(self.datadt,'excel', delimiter=';')
        spamwriterdt.writerow(parts)
      if parts[10] == 'Pose.fist ':
        spamwriterf = csv.writer(self.dataf,'excel', delimiter=';')
        spamwriterf.writerow(parts)
      if parts[10] == 'Pose.rest ':
        spamwriterr = csv.writer(self.datar,'excel', delimiter=';')
        spamwriterr.writerow(parts) 
      if parts[10] == 'Pose.fingers_spread':
        spamwriterfs = csv.writer(self.datafs,'excel', delimiter=';')
        spamwriterfs.writerow(parts)      

      
    spamwriter2 = csv.writer(self.data3,'excel', delimiter=';')
    spamwriter2.writerow(parts)
    

    
   
    #self.text = ''.join('[{}]'.format(p) for p in parts)
    print('\r' + ''.join('[{}]'.format(p) for p in parts), end='')  
    #print(parts)
    #self.data.write(self.text+'\n')  
    sys.stdout.flush()

  def on_connected(self, event):
    self.spamwriter1=csv.writer(self.data1,'excel', delimiter=';')
    self.spamwriter1.writerow(["acc1","acc2","acc3","acc4"])
    event.device.request_rssi()

  def on_rssi(self, event):
    self.rssi = event.rssi
    self.output()

  def on_pose(self, event):
    self.pose = event.pose
    if self.pose == myo.Pose.double_tap:
      event.device.stream_emg(True)
      self.emg_enabled = True
    elif self.pose == myo.Pose.fingers_spread:
      event.device.stream_emg(True)
      self.emg_enabled = True
      #self.emg = None
    self.output()

  def on_orientation(self, event):
    self.orientation = event.orientation
    self.gyroscope = event.gyroscope
    self.accelerometor = event.acceleration
    self.output()

  def on_emg(self, event):
    self.emg = event.emg
    self.output()

  def on_accelerometor(self, event):
    self.accelerometor = event.accelerometor
    self.output()
 
  def on_gyroscope(self, event):
    self.gyroscope = event.gyroscope
    self.output()


  def on_unlocked(self, event):
    self.locked = False
    self.output()

  def on_locked(self, event):
    self.locked = True
    self.output()


if __name__ == '__main__':
  myo.init()
  feed = myo.ApiDeviceListener
  hub = myo.Hub()
  listener = Listener()
  listener.data1 = open("acc1.csv","w", newline='')
  listener.data2 = open("orient.csv","w", newline='')
  da = listener.data3 = open("all.csv","w", newline='')
  listener.data4 = open("autre.csv","w", newline='')
  listener.datawo = open("wave_out.csv","w", newline='')
  listener.datawi = open("wave_in.csv","w", newline='')
  listener.datadt = open("double_tab.csv","w", newline='')
  listener.datafs = open("fingers_spread.csv","w", newline='')
  listener.dataf = open("first.csv","w", newline='')
  listener.datar = open("rest.csv","w", newline='')
  while hub.run(listener.on_event, 500):
    pass
