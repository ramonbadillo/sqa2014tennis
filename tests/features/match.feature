Feature: As a player 
	 I want to score a match of tennis
         
Scenario: Straight Sets (corridas)
	  Given: "Alice" and "Bob" start a match to "5" sets
	  Then: I see score: "Alice plays with Bob | 0-0"

Scenario: First player wins straight
	  Given: "Mary" and "Sally" start a match to "3" sets
      When: "Mary" won the "1st" set "6"-"4"
      And: "Mary" won the "2nd" set "6"-"3"
	  Then: The match score is: "Mary defeated Sally | 6-4, 6-3"

Scenario: Second player wins straight
	  Given: "Jeff" and "Jim" start a match to "3" sets
          When: "Jim" won the "1st" set "6"-"1"
          And: "Jim" won the "2nd" set "7"-"5"
	  Then: The match score is: "Jim defeated Jeff | 6-1, 7-5"

Scenario: Second player wins straight at 5 sets
	  Given: "John McEnroe" and "Jimmy Connors" start a match to "5" sets
          When: "John McEnroe" won the "1st" set "6"-"2"
          And: "John McEnroe" won the "2nd" set "6"-"3"
          And: "John McEnroe" won the "3rd" set "6"-"4"
	  Then: The match score is: "John McEnroe defeated Jimmy Connors | 6-2, 6-3, 6-4"

Scenario: First player wins split at 3 sets
	  Given: "Jane" and "Lisa" start a match to "3" sets
          When: "Jane" won the "1st" set "6"-"3"
          And: "Lisa" won the "2nd" set "6"-"2"
          And: "Jane" won the "3rd" set "6"-"4"
          Then: The match score is: "Jane defeated Lisa | 6-3, 2-6, 6-4"
         
Scenario: 2nd player wins split at 5 sets
	  Given: "Ivan Lendl" and "Boris Becker" start a match to "5" sets
          When: "Boris Becker" won the "1st" set "6"-"2"
          And: "Boris Becker" won the "3rd" set "6"-"4"
          And: "Boris Becker" won the "5th" set "7"-"5"
          And: "Ivan Lendl" won the "2nd" set "6"-"3"
          And: "Ivan Lendl" won the "4th" set "6"-"1"
          Then: The match score is: "Boris Becker defeated Ivan Lendl | 6-2, 3-6, 6-4, 1-6, 7-5"