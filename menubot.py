import json
from logger import log

menuStore = "data/menu.json"

class MenuBot():
    status = "Empty"
    menu = dict()

    def getStatus(self):
        return self.status

    def saveMenu(self):
        with open( menuStore, 'w' ) as outfile:
            jstr = json.dumps( self.menu )
            outfile.write(jstr)

    def loadMenu(self):
        try:
            with open(menuStore) as json_file:
                self.menu = json.load( json_file )
            log( self.menu )

            self.status = "Ready"
        except Exception as e:
            print( e )
            self.status = "Read Error"

    def determineReply(self, req):
        all = ""
        delim = ""

        try:
            t = req.lower().strip()
            for row in self.menu:
                if not row['active']:
                    continue
                choice = row['query']
                if t == choice.lower():
                    return row['reply']
                all += delim + choice
                delim = ', '
        except Exception as e:
            print(e)
            return "Sorry, error formulating response to " + req

        return 'I can reply to ' + all

    # def __init__(self):
    #     self.loadMenu()


