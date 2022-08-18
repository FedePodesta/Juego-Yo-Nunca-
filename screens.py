
import tkinter as tk
from constantes import style, config


class Home(tk.Frame):

    def __init__(self,parent,controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.gameMode= tk.StringVar(self,value="Normal")

        self.init_widgets()
    def move_to_game(self):
        self.controller.mode =self.gameMode.get()
        self.controller.show_frame(Game)

    def init_widgets(self):
        tk.Label(
            self,
            text="Yo nunca : THE GAME",
            justify= tk.CENTER,
            **style.STYLE
            ).pack(
            side =tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
            )
        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background = style.COMPONENT)
        optionsFrame.pack(
            side =tk.TOP,
            fill = tk.BOTH,
            expand= True,
            padx = 22,
            pady = 11
        )
        tk.Label(
            optionsFrame,
            text = "Elige tu modo de juego",
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            side=tk.TOP,
            fill = tk.X,
            padx=22,
            pady =11
        )
        
        for (key,value) in config.MODES.items():
            tk.Radiobutton(
                optionsFrame,
                text = key + ("🔥" if key == "PICANTE" else ""),
                variable = self.gameMode,
                value = value,
                activebackground= style.BACKGROUND,
                activeforeground= style.TEXT,
                **style.STYLE
            ).pack(
                side = tk.LEFT,
                fill = tk.BOTH,
                expand = True,
                padx = 5,
                pady = 5
            )

        tk.Button(
            self,
            text="EMPEZAR!!!!",
            command = self.move_to_game,
            **style.STYLE,
            relief = tk.FLAT,
            activebackground= style.BACKGROUND,
            activeforeground= style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 22,
            pady = 11
        )






class Game(tk.Frame):

    def __init__(self,parent,controller):
        super().__init__(parent)
        self.configure(background= style.BACKGROUND)
        self.controller = controller
        self.currentQuestion = tk.StringVar (self, value ="Preparate !")
        self.fichero = None
        self.init_widgets()
        
    def update_question(self):
        self.mode = self.controller.mode
        if (self.fichero == None) or (self.controller.mode.lower() not in self.fichero.name.lower()):
            self.fichero = open(f'./ficheros/{self.mode}.txt','r' , encoding="utf-8")
        tmp = self.fichero.readline()
        if tmp != "":
            self.currentQuestion.set(tmp)
        else:
            self.currentQuestion.set("se acabaron las preguntas")
            self.fichero.close()
            self.fichero = open(f'./ficheros/{self.mode}.txt','r' , encoding="utf-8")
           
            

    

    def init_widgets(self):
        tk.Label(
            self,
            text="Yo nunca ...",
            justify= tk.CENTER,
            **style.STYLE
            ).pack(
            side =tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
            )
        
        tk.Label(
            self,
            text = "Preparate !",
            textvar= self.currentQuestion,
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            side=tk.TOP,
            fill = tk.X,
            padx=22,
            pady =11
        )
        
       

        tk.Button(
            self,
            text="SIGUIENTE ->",
            command = self.update_question,
            **style.STYLE,
            relief = tk.FLAT,
            activebackground= style.BACKGROUND,
            activeforeground= style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )

        tk.Button(
            self,
            text="HOME",
            command = lambda: self.controller.show_frame(Home),
            **style.STYLE,
            relief = tk.FLAT,
            activebackground= style.BACKGROUND,
            activeforeground= style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )