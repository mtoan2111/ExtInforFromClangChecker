from __future__ import print_function
from bs4 import BeautifulSoup
import os, errno


class HtmlParse:

  SoureFile = ""
  Output = ""
  Lst_Dangerous = []
  hMap_Files = {}
  WorkingDir = ""
  Soup = BeautifulSoup

  def __init__(self, SoureFile, Output, ListDangerous):
    self.SoureFile = SoureFile
    self.Output = Output
    self.Lst_Dangerous = ListDangerous[:]
    self.rmOutputFile()
    with open(self.SoureFile) as fp:
      self.Soup = BeautifulSoup(fp)
    self.getWorkingDir()

  def analyzingSoureFile(self):
    if len(self.Lst_Dangerous) > 0:
      for danger in self.Lst_Dangerous:
        for item in self.Soup.findAll("tr",{"class": danger}):
          td_Tag = item.findAll('td')
          self.hMap_Files[int(td_Tag[4].text)] = self.WorkingDir + td_Tag[2].text
              # self.writeToFile(allTag[2].text, allTag[4].text)
      for key, value in sorted(self.hMap_Files.iteritems(), key=lambda (k, v): (v, k)):
        self.writeToFile(self.hMap_Files[key], key);

  def getWorkingDir(self):
  #find first table for collecting information
    temp = self.Soup.find("table")
    allTag = temp.findAll('td')
    self.WorkingDir = allTag[1].text + "/"

  def rmOutputFile(self):
    try:
      os.remove(self.Output)
    except OSError as e:
      if e.errno != errno.ENOENT:  #erro.ENOENT = no such file or directory
        raise

  def writeToFile(self, sourcename, linenumber):
    with open(self.Output, "a+") as fp:
      fp.writelines(sourcename + ": " + str(linenumber) + "\n")
