import string



class NewsStory(object):
    
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
        
    def getGuid(self):
        return self.guid
    
    def getTitle(self):
        return self.title
    
    def getSubject(self):
        return self.subject
    
    def getSummary(self):
        return self.summary
    
    def getLink(self):
        return self.link
        
class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        self.NewsStory = story
# TODO: WordTrigger

class WordTrigger(Trigger):
    
    def __init__(self, word):
        self.word = word.lower()
    
    def isWordIn(self,text):
        newText = ""
        for letter in text.lower():
            if letter in string.punctuation:
                newText += " "
            else:
                newText += letter
        newText = newText.split(' ');
        return self.word in newText
        
# TODO: TitleTrigger
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())
        
# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())
        
# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())
   
koala     = NewsStory('', 'Winter in Boston!', '', '', '')
s2  = TitleTrigger('Boston')
print s2.evaluate(koala)
