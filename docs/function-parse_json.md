



# parse_json()
  
+++section;title=Path;hash=7090eb0d3c931a090b48

`yblackjack/yoco_exam_1.py`
  
+++

\
  
+++section;title=Source Code;hash=d04e5db570ab42588abd
```
def parse_json ():
	with open('yoco_tests.json') as f:
	    return json.load(f)
```  
+++

\
  
+++section;title=References;hash=a89bee40371221317e6b

**Line 205** `/yoco_exam_1.py`

```

#runs the rounds through parsing the json and starting the game
def run_rounds ():

	tests  = parse_json()

	if not tests:
		print('There was an error parsing the json file')
		exit(1)


```
\  
+++