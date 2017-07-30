import falcon
import json
import sys
import codecs
import urllib
import html
#from BeautifulSoup import BeautifulSoup

sys.path.insert(0, 'solver')
import SI

class ThingsResource(object):
    def on_get(self, req, resp,filename):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open(filename, 'r') as f:
            resp.body = f.read()

class Starting(object):
	#def on_get(self, req, resp):
	#	p = ('\nTwo things awe me most, the starry sky '
    #                 'above me and the moral law within me.\n'
    #                 '\n'
    #                 '    ~ Immanuel Kant\n\n')
	#	print("p")

    def on_post(self,req,resp):
        print("called\n\n")
        data=req.stream.read()
        print(data)
        print("\n\n\nnow printing resolved \n\n")
        data=data.decode()
        
        data=json.loads(data)

        print(data["result"]["resolvedQuery"])
        answer=SI.mainp(data["result"]["resolvedQuery"])
        answer=str(answer)
        print(answer)
        d={}
        d["type"]=0
        d["siaplayText"]="The answer is "+str(answer)
        d["speech"]="The answer is "+str(answer)
        d["answer"]=answer

        resp.body = json.dumps(d, ensure_ascii=False)
        resp.status = falcon.HTTP_200

        #html_decoded_string = BeautifulSoup(data, convertEntities=BeautifulSoup.HTML_ENTITIES)
        #print(html_decoded_string)
        #da.read()
        #print(da)



	#def on_post(self,req,resp):
    #    print(req.stream)
		#reader = codecs.getreader("utf-8")
		#obj = json.loads(reader(req.stream))
		#resp.status = falcon.HTTP_201
        #resp.location = '/things/' + name
app = falcon.API()
things = ThingsResource()
thi = Starting()

app.add_route('/things/{filename}', things)
app.add_route('/things',thi)
