import matplotlib.pyplot as plt
player_names=["Shahid Afridi","Babar Azam","Virat Kohli","Chris Gale","Malinga"]
player_scores=[122,123,124,234,342]

score_perc = []
for i in player_scores:
    res = (i/350)*100
    score_perc.append(res)

print(score_perc)


games_name=["Football","Cricket(T20)","Badminton","Table Tennis","Hockey","Golf"]
Highest_recorded_scores=["6 goals in a single match","The biggest win by runs in T20 cricket is 273 runs scored by Nepal against Mongolia.","Brian Lara of the West Indies holds the record for the highest individual score in a Test match with 400 runs not out against England in 2004.", "The longest badminton rally in a competitive match is believed to be the 211-shot rally that took place during the 2023 Malaysia Masters women's doubles quarterfinals. The rally was played between Malaysia's Pearly Tan and Thinaah Muralitharan, who went on to win the match 21-17, 18-21, 21-19.","(The longest table tennis rally in the world is 15-24155.) China has been the most successful country in Olympic table tennis, winning 66 medals. Since 1992, Chinese players have won at least one medal in every event.","The highest score in an international ice hockey game is 82–0, which Slovakia achieved against Bulgaria in 2008. The game was played in Liepāja, Latvia, as part of the first round of qualification for the 2010 Winter Olympics. Janka Culicova was the top scorer with 10 goals. The highest-scoring professional ice hockey game was between the Edmonton Oilers and the Chicago Blackhawks, with the Oilers winning 12–9. The total of 21 goals broke previous scoring records." ]
