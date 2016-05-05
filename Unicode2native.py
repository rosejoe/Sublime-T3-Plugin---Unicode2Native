import sublime, sublime_plugin, math

class Unicode2nativeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    allcontent = sublime.Region(0, self.view.size())
    allcontentstring = self.view.substr(allcontent)
    character = allcontentstring.split("\\u")
    #print (character[0:10])
    native = character[0]
    for i in range (1,len(character)):
      code = character[i]
      native += chr(int("0x" + code[0:4],16))
      if len(code) > 4 :
        native += code[4:len(code)]
    self.view.replace(edit, allcontent, native)

class Native2unicodeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    allcontent = sublime.Region(0, self.view.size())
    allcontentstring = self.view.substr(allcontent)
    #character = allcontentstring.split("")
    #print (character[0:10])
    native = ""
    l = list(allcontentstring)
    for i in range (len(l)):
      code = int(ord(l[i][0]))
      #if str(args)!="T" or code>127 :
      if code>127 :
        charAscii = format(code,'x')
        charAscii = charAscii.zfill(4)
        native += "\\u" + charAscii
      else :
        native += l[i]
    self.view.replace(edit, allcontent, native)