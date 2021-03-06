from __future__ import print_function
from bs4 import BeautifulSoup
from copy import deepcopy
import os, errno

class HtmlParse:
  SoureFile = ""
  Output = ""
  WorkingDir = ""
  Soup = BeautifulSoup
  Lst_Dangerous = list()
  hMap_Files = dict()

  def __init__(self, SoureFile, Output, ListDangerous):
    if os.path.exists(SoureFile) == 0:
      print ("Oops: Missing HTML index file")
      return
    self.SoureFile = SoureFile
    self.Output = Output
    self.Lst_Dangerous = deepcopy(ListDangerous)
    with open(self.SoureFile) as fp:
      self.Soup = BeautifulSoup(fp)
    self.getWorkingDir()

  def analyzingSoureFile(self):
    if len(self.Lst_Dangerous) > 0:
      if os.path.isfile(self.Output):
        try:
          os.remove(self.Output)
        except OSError as e:
          if e.errno != errno.ENOENT:  # erro.ENOENT = no such file or directory
            raise
      with open(self.Output, "a+") as fp:
        for item in self.Soup.findAll("tr",{"class": self.Lst_Dangerous}):
          td_Tag = item.findAll('td')
          s_name = td_Tag[2].text.split("/")
          self.hMap_Files[int(td_Tag[4].text)] = s_name[-1]
        for key, value in sorted(self.hMap_Files.iteritems(), key=lambda (k, v): (v, k)):
          fp.writelines(self.hMap_Files[key] + ":" + str(key) + "\n");
        print ("\033[95mAnalyzing success fully \033[0m")
        print ("\033[92mOuput file: \033[0m" +'\033[94m' +self.Output  + '\033[0m')
    else:
      print ("Oops: doesn't have any warnings that you are expected")

  def getWorkingDir(self):
    infoTable = self.Soup.find("table")
    th_Tag = infoTable.findAll('td')
    self.WorkingDir = th_Tag[1].text + "/"
