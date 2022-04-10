## Game-Project-TrueOrFalse

I have created a game using the GUI library in Python, namely tkinter. Apart from using tkinter, I also use pygame to create sound effects.

This game is a game about right or wrong for 30 seconds in Indonesian. The existing questions consist of various kinds of questions that can be entered according to the wishes of the program maker. Here, there are some questions about mathematics as well as other general knowledge. I made this program as a final project for a computer programming course that I took.

There are two different program code files. The first, we just have to choose true or false by clicking the 'check' or 'cross'. The second one is a game with blank boxes to type in true or false answers. You can choose which one to use to play. I prefer the first one.

You can use your own music (.wav) to replace 'main.wav' in the program code in def main(). I can't upload the music I'm using because the file is too big.
   
	def bermain():
   
       pygame.mixer.music.load('main.wav')
       
       pygame.mixer.music.play(10)

#### This is the initial view of this game (the first one):
![image](https://user-images.githubusercontent.com/99526319/162600384-1ff39cd8-49d6-4db6-8bbd-b6f068d5184a.png)

#### This is the initial view of this game (the second one):
![image](https://user-images.githubusercontent.com/99526319/162600397-3314b8c7-de29-499b-9f1f-a284e4e223d0.png)

#### This is how it looks when playing (the first one):
![image](https://user-images.githubusercontent.com/99526319/162600474-ddef8c1f-fab7-4dc7-ba4f-7fef95620bfb.png)

#### This is how it looks when playing (the second one):
![image](https://user-images.githubusercontent.com/99526319/162600408-f98c3c73-a69c-44e6-bd91-e581af8f40a5.png)

You can see this project in the folder 'True or False'

#### Don't forget to provide the source if you use this project!
