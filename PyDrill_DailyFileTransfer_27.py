import shutil
import os
from os import path
import datetime
from datetime import date, time, timedelta


def f_change(fname):

  file_m_time = datetime.datetime.fromtimestamp(path.getmtime(fname))
  
  td = datetime.datetime.now() - file_m_time

  if td.days == 0:
    global ready_to_archive
    ready_to_archive = ready_to_archive + 1
    return True
  else: return False
  



def main():
  global ready_to_archive
  global archived
  ready_to_archive, archived = 0, 0
  
  # src_folder = "c:\users\V\desktop\FA"
  # dst_folder = "c:\users\V\desktop\FB"

  for fname in os.listdir('c:\users\V\Desktop\FA'):

    src_fname = 'c:\users\V\Desktop\FA\%s' % fname

    if f_change(src_fname):    
      dst_fname = 'c:\users\V\Desktop\FB\%s' % fname
      dst_folder = 'c:\users\V\Desktop\FB'


      try:
        shutil.copy2(src_fname, dst_folder)
        global archived;
        archived = archived + 1

      except IOError as e:
        print 'could not open the file: %s ' % e
         
        
      
if __name__ == "__main__":

  main()

  print '******   Archive Report for %s   ******' % datetime.datetime.now()
  print '%d files ready for archiving ' % ready_to_archive
  print '%d files archived' % archived
  print '******   End of Archive Report   ******'


##LOOK UP:
##-get
##-set
##-askdirectory
##
##Have 3 functions:
##
##*2 to browse:
##-source*
##-destination*
##-button

