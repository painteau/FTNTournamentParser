import json
import csv
import array as arr
import operator

# Variables
_elimpoints = 1
_player_db = {}


with open('parsedReplay.json', encoding="utf8") as f:
    data = json.load(f)


for _eliminations in data["eliminations"]:
    _player_db[_eliminations["eliminator"]["id"]] = _player_db.get(_eliminations["eliminator"]["id"], 0)

#print(str(_player_db))
print("-------------------------------------")



# Initialize dictionary
_player_elimination_score = {}

for _eliminations in data["eliminations"]: 
    if _eliminations["knocked"] is False :
            _player_elimination_score[_eliminations["eliminator"]["id"]] = _player_elimination_score.get(_eliminations["eliminator"]["id"], 0) + _elimpoints
            print(_eliminations["eliminator"]["id"] + " killed " + _eliminations["eliminated"]["id"])
     
# printing result 
_sorted_player_elimination_score = dict( sorted(_player_elimination_score.items(), key=operator.itemgetter(1),reverse=True))
#print(str(_sorted_player_elimination_score))

print("-------------------------------------")

# Initialize dictionary
_player_final_rank = {}
rank = 1

for _eliminations in data["eliminations"]: 
    if _eliminations["knocked"] is False :
        _player_final_rank[_eliminations["eliminated"]["id"]] = _player_final_rank.get(_eliminations["eliminated"]["id"], 0) + rank
        rank = rank + 1
_player_final_rank[_eliminations["eliminator"]["id"]] = _player_final_rank.get(_eliminations["eliminator"]["id"], 0) + rank

# sorting 
_sorted_player_final_rank = dict( sorted(_player_final_rank.items(), key=operator.itemgetter(1),reverse=True))

# printing result 

#print(str(_sorted_player_final_rank))

print("-------------------------------------")

# Attributing Score
_player_final_rank_score = {}
score = 26
for i in _sorted_player_final_rank: 
     _player_final_rank_score[i] = _player_final_rank_score.get(i, 0) + score
     score = score - 3
     if score <= 0 :
        score = 0 


# sorting 
_sorted_player_final_rank_score = dict( sorted(_player_final_rank_score.items(), key=operator.itemgetter(1),reverse=True))

# printing result 
#print(str(_sorted_player_final_rank_score))

print("-------------------------------------")
print("-------------------------------------")

# Final Score


for i in _player_db: 
     _player_db[i] = _sorted_player_final_rank_score.get(i, 0) + _sorted_player_elimination_score.get(i, 0)


# sorting 
_sorted_player_db = dict( sorted(_player_db.items(), key=operator.itemgetter(1),reverse=True))

# printing result 
#print(str(_sorted_player_db))

print("-------------------------------------")

for key,value in _sorted_player_db.items():
    print(key, ':', value, ' points')
