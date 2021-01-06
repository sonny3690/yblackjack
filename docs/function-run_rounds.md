



# run_rounds()
  
+++section;title=Path;hash=7090eb0d3c931a090b48

`yblackjack/yoco_exam_1.py`
  
+++

\
  
+++section;title=Source Code;hash=9b96460733aeaaf3ed93
```
def run_rounds ():

	tests  = parse_json()

	if not tests:
		print('There was an error parsing the json file')
		exit(1)

	game = Game (tests)
	game.run_rounds()
```  
+++

\
  
+++section;title=References;hash=6ffacea0b1b607d2ce30

**Line 223** `/yoco_exam_1.py`

```
	    return json.load(f)


#starts everything
run_rounds()






```
\  
+++