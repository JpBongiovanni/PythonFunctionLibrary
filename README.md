
# Python Function Library
<h2>The Python Basics Library is an agrigation of numerous Python functions that are ready to be integrated into any Python project. The functions range from basic to advanced and can be run in both a terminal and in accompanying HTML</h2>


<h3>contents:</h3>
  <h4>
    <ul>
      <li><a href="#zigzag">Zig Zag</a></li>
      <li><a href="#callstack">Call Stack Funciton</a></li>
      <li><a href="#collatz">Collatz</a></li>
      <li><a href="#guessnum">Guess the Number</a></li>
      <li><a href="#m8">The Magic 8 Ball</a></li>
      <li><a href="#rps">Rock Paper Scissors</a></li>
      <li><a href="#coinFlip">The Coin Flip</a></li>
      <li><a href="#conway">Conway</a></li>
      <li><a href="#ticTacToe">Tic Tac Toe</a></li>
    <ul>
      
      
  

<hr>
Zig Zag - <p id="zigzag">The Zig Zag function makes use of a while True infinite loop and the time.sleep() function to slow down the rendering of our program in the terminal. Every tenth of a second the program prints again on a different line but with a ' ' before or after the text to give the illusion the text is "zigzagging" down the page like a snake.<p>  

<img src="{{site.baseurl | prepend: site.url}}movies/zigzag.gif" alt="zigzag" />

<div id="callstack">Call Stack Function - The Call Stack Function is how Python remembers where a function first started and then returns there after the function is complete. It is usually running behind the scenes but it is demonstrated here. </div>

<img src="{{site.baseurl | prepend: site.url}}movies/abcdCallStack.gif" alt="callstack" />


<div id="collatz">Collatz Sequence - The Collatz function takes one integer. If the integer is even then it is divided by 2, if it is odd, it is multiplied by 3 and adds 1. No one is sure why, but whatever integer is given the final result is always one.</div>

<img src="{{site.baseurl | prepend: site.url}}movies/collatz.gif" alt="collatz" />


<div id="guessnum">Guess the Number - The program uses the random.randint() function by way of the random module to find the target number between the set number parameters. The user is then asked for an imput and the input is checked against the target number. The program then responds with either "too low," "too high," or "correct." Each input is traced and the player will lose if the input number exceeds 6. </div>
      
<img src="{{site.baseurl | prepend: site.url}}movies/guessTheNumber.gif" alt="guessTheNumber" />

<div id="m8">The Magic 8 Ball - The program uses the random.randint() function by way of the random module to find the target number depending on the number of possible responses.</div>

<img src="{{site.baseurl | prepend: site.url}}movies/magic8ball.gif" alt="magic8ball" />


<div id="rps">Rock Paper Scissors - the program first calls the random and sys modules to use random.ranint() and sys.exit(). Three variables are then established to keep track of our wins, loses, and draws. There are two while loops at play, the first loop runs the whole game, while the second takes inputs from the player. The inner loop then breaks and the random.randint() function chooses an integer assigned to rock, paper, or scissors. The user input and the random integer are then compared and the winner is declared.</div>

<img src="{{site.baseurl | prepend: site.url}}movies/rock_paper_scissors.gif" alt="rps" />

<div id="coinFlip">The Coin Flip - </div>

<img src="{{site.baseurl | prepend: site.url}}movies/coinFlip.gif" alt="Coin Flip gif" />
      
<div id="conway">Conway - </div>

<img src="{{site.baseurl | prepend: site.url}}movies/conway.gif" alt="Conway gif" />

<div id="ticTacToe">Tic Tac Toe - </div>

<img src="{{site.baseurl | prepend: site.url}}movies/ttt1.gif" alt="Tic Tac Toe gif" />
<img src="{{site.baseurl | prepend: site.url}}movies/ttt2.gif" alt="Tic Tac Toe gif" />


