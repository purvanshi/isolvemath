def SDP(str):
	from nltk.parse.stanford import StanfordDependencyParser
	dep_parser=StanfordDependencyParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
	xyz = [parse.tree() for parse in dep_parser.raw_parse(str)]
	print(xyz)
       #print xyz (for Python 2.7)

if __name__ == "__main__":
    import sys
    SDP(str(sys.argv[1]))
