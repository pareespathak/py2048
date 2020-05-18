# py2048
NAME : PAREESPATHAK

ABOUT GAME 

GAME IS TESTED AND PREPARED ON WINDOWS.

2048game is a single player game of sliding a number from one place to another place in a board to form a new number by adding two numbers.
The user is supposed to enter size of board and winning value else default value is selected .
only Same numbers can be added to form new number.numbers are added only when adjacent numbers are imposed over each other 
either horizontally or vertically .game begin with one place numbered '2'.
on every slide if new orientation of board is formed then a random place with '0' number is replaced by number '2'.
when the person achieved the winning value the game is over and player has won the game /
or when there is no non-zero place and no adjacent places with same numbers are remaining the game is over.

MODULES NEEDED :

1.numpy: to create matrix and perform operations on matrix.
2.random: to select an random element from the game board.
3.os: to clear screen after every step.
4.argparse: to take input from command line.

START OF GAME:

1. argparse module is used to take input from the user directly on command line.
   the inputs are BOARD SIZE AS "--p".and WINVALUE AS "--w" on the command line.
   if input is not given then default value is set . that is BOARD SIZE= 5, WINVALUE =2048.
   input must be integers . else input again if Winvalue is not the power of 2 then default value is set as win value.
   winvalue will be displayed above .
   
PLAYING MOVE :

     to slide upwards enter 'w' or 'W' key .
     to slide downwards enter 's' or 'S' key .
     to slide rightside enter 'd' or 'D' key .
     to slide leftside enter 'a' or 'A' key .
     if any other input is given . game will ask to play move again till valid input.

 after every move a new tile will be inserted to random place numbered as '0'.
 ENDING OF GAME:
 
  If the player reaches the win value  or when no adjacent place with same number is remaining and all the places are non zeros.
  the game will be compleated .board will be printed with status.
 
2. FUNCTIONS discription :

  1. zeros function of numpy module is used to form game board as matrix .
  2. inserting_tile:
  
     randit function from random module is used to choose a random element of the matrix.
     number '2' is placed in matrix of zeros.
  3. leftmove:
     1. all the non zeros elements are slided to left side of game board.
     2.elements with same adjacent number are added in order from left to right of every row.
     3. again all the elements are slided to left.
   4. rightmove:
      the above process is repeated along right direction
   5.moveup:
     1.all the elements are slided upside of game board.
     2.elements with same adajcent numbers are added in order from top to bottom of every column.
     3 again all the elemenst are slided upwards.
   6. movedown:
      the process of moveup is repeated in downward direction.
   7. playmove :
      taking input from the user after every move and sliding tile accordingly.
   8. clear:
      function operate to clear the screen after every move.
      os module is used to interact with the system.
      if operating system is windows the the functio will be operate 'cls'.
      else it will operate 'clear'
      
   MAIN CODE:
   
      tile is inserted using function inserting_tile.
      while loop is used to 
      check the ending conditions of game. i.e checking availability of adjacent common places.and non zeros places.
      then playmove is used to slide the numbers.
      boards before moving and after moving are checked .
      if both the boards are same then no new number '2' is inserted.
      after valid move and the orientation of boards is different then  screen is cleared and new tile is inserted.
      game is excecuted till the the loop is break .
      result of game is displayed.
   
