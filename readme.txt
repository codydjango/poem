apt-get git
apt-get python-virtualenv
apt-get python-pip



https://github.com/codydjango/poem




git clone git@github.com:codydjango/poem.git
(source venv/bin/activate)
pip install -r requirements.txt




def do_something():
  print 'something'


class Animal:
  def set_name(self, name):
    self.name = name

  def get_name(self):
    return self.name



cat = Animal()
cat.set_name('captain')



name = cat.get_name()

name == 'captain' 
# true


file_obj = open('war_and_peace.txt')
text = file_obj.read()



nlp = Spacy.load('en')

nlp











