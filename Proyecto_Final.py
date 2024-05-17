import random
import math
import os
from graphviz import Digraph####
from os import startfile

#X is max = 1
#O in min = -1

tree = Digraph(comment='Movimientos totito')###############################
tree.graph_attr['ranksep'] = '1.5'########################################
tree.graph_attr['nodesep'] = '1.5'########################################
tree.graph_attr['splines'] = 'true'########################################
#tree.graph_attr['dpi'] = '300'

class TreeNodeC:
    def __init__(self, state, move=None):
        self.state = state
        self.move = move
        self.children = []

    def add_child(self, nodo_child):
        self.children.append(nodo_child)

class GTree:
    def __init__(self, initial_state):
        self.root = TreeNodeC(initial_state)
        self.current_node = self.root

    def add_move(self, new_state, move):
        new_node = TreeNodeC(new_state, move)
        self.current_node.add_child(new_node)
        self.current_node = new_node

    def reset_to_root(self):
        self.current_node = self.root
    
    def print_tree(self, node=None, depth=0):
        if node is None:
            node = self.root

        #imprimo el estado actual del nodo y el movimiento
        indent = " " * depth * 2
        move_info = f"Movimiento: {node.move}" if node.move is not None else "Estado inicial"
        state_info = f"Estado: {''.join(node.state)}"
        print(f"{indent}{move_info}, {state_info}")

        for child in node.children:
            self.print_tree(child, depth +1)

class TicTacToe:
    def __init__(self):
        self.board = ['-' for _ in range(9)]
        if random.randint(0, 1) == 1:
            self.humanPLayer = 'X'
            self.botPlayer = "O"
        else:
            self.humanPLayer = "O"
            self.botPlayer = "X"
        self.current_nodo = str(self.board)########################################
        tree.node(self.current_nodo, self.current_nodo)########################################
        self.game_tree = GTree(self.board.copy())##########################

    def show_board(self):
        print("")
        for i in range(3):
            print("  ",self.board[0+(i*3)]," | ",self.board[1+(i*3)]," | ",self.board[2+(i*3)])
            print("")
            
    def is_board_filled(self,state):
        return not "-" in state

    def is_player_win(self,state,player):
        if state[0]==state[1]==state[2] == player: return True
        if state[3]==state[4]==state[5] == player: return True
        if state[6]==state[7]==state[8] == player: return True
        if state[0]==state[3]==state[6] == player: return True
        if state[1]==state[4]==state[7] == player: return True
        if state[2]==state[5]==state[8] == player: return True
        if state[0]==state[4]==state[8] == player: return True
        if state[2]==state[4]==state[6] == player: return True

        return False

    def checkWinner(self):
        if self.is_player_win(self.board,self.humanPLayer):
            os.system("cls")
            print(f"   Jugador {self.humanPLayer} ganan la partida!!!")
            return True
            
        if self.is_player_win(self.board,self.botPlayer):
            os.system("cls")
            print(f"   Jugador {self.botPlayer} gana la partida!!!")
            return True

        # checking whether the game is draw or not
        if self.is_board_filled(self.board):
            os.system("cls")
            print("   Partida empatada!!!")
            return True
        return False

    def start(self):
        bot = ComputerPlayer(self.botPlayer)
        human = humanPLayer(self.humanPLayer)
        while True:
            os.system("cls")
            print(f"   Player {self.humanPLayer} turn")
            self.show_board()
            
            #Human
            square = human.human_move(self.board)
            self.board[square] = self.humanPLayer

            new_node = str(self.board)########################################
            tree.node(new_node, new_node)########################################
            tree.edge(self.current_nodo, new_node)########################################
            self.game_tree.add_move(self.board.copy(), square)##########
            self.current_nodo = new_node########################################

            if self.checkWinner():
                break
            
            #Bot
            square = bot.machine_move(self.board)
            self.board[square] = self.botPlayer

            new_node = str(self.board)########################################
            tree.node(new_node, new_node)########################################
            tree.edge(self.current_nodo, new_node)########################################
            self.game_tree.add_move(self.board.copy(), square)##########
            self.current_nodo = new_node########################################

            if self.checkWinner():
                break

        # showing the final view of board
        print()
        self.show_board()

        print("\nArbol del juego:")#############################
        tic_tac_toe.game_tree.print_tree()#############################

        tree.render('Arbol',view=True, format='svg', cleanup=True)##########################

    

class humanPLayer:
    def __init__(self,letter):
        self.letter = letter
    
    def human_move(self,state):
        # taking user input
        while True:
            square =  int(input("Enter the square to fix spot(1-9): "))
            print()
            if state[square-1] == "-":
                break
        return square-1

class ComputerPlayer(TicTacToe):
    def __init__(self,letter):
        self.botPlayer = letter
        self.humanPlayer = "X" if letter == "O" else "O"
        self.tree = tree
        #self.game_tree = self.game_tree#!!!!!!!!!!!!!!!!!!!!!!!!

    def players(self,state):
        n = len(state)
        x = 0
        o = 0
        for i in range(9):
            if(state[i] == "X"):
                x = x+1
            if(state[i] == "O"):
                o = o+1
        
        if(self.humanPlayer == "X"):
            return "X" if x==o else "O"
        if(self.humanPlayer == "O"):
            return "O" if x==o else "X"
    
    def actions(self,state):
        return [i for i, x in enumerate(state) if x == "-"]
    
    def result(self,state,action):
        newState = state.copy()
        player = self.players(state)
        newState[action] = player
        return newState
    
    def terminal(self,state):
        if(self.is_player_win(state,"X")):
            return True
        if(self.is_player_win(state,"O")):
            return True
        return False

    def minimax(self, state, player):
        max_player = self.humanPlayer  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if self.terminal(state):
            return {'position': None, 'score': 1 * (len(self.actions(state)) + 1) if other_player == max_player else -1 * (
                        len(self.actions(state)) + 1)}
        elif self.is_board_filled(state):
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in self.actions(state):
            newState = self.result(state,possible_move)
            sim_score = self.minimax(newState, other_player)  # simulate a game after making that move

            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

    def machine_move(self,state):
        square = self.minimax(state,self.botPlayer)['position']
        return square

# starting the game
tic_tac_toe = TicTacToe()
while True:
    print("1. Iniciar juego.\n")
    print("2. Imprimir arbol.\n")
    print("3. Salir.")
    try:#utilizo el try como trato, para
        opc = int(input("Seleccione una opcion para continuar: "))#trato de leer el valor ingresado por el usuario, convertirlo en un entero
    except ValueError as e:#si no sale bien el proceso porque el usuario introdujo un valor erroneo entonces
        print("Error: Porfavor ingrese una opcion valida")#imprimo que hubo un error 
        print(f"Error: {e}")#imprimo el error en especifico
    if opc == 1:
        tic_tac_toe.start()
        print("Reiniciando...")
    elif opc == 2:
        print("\nArbol del juego:")#############################
        tic_tac_toe.game_tree.print_tree()#############################
    elif opc == 3:
        print("Saliendo....")
        break
    else:
        print("Opcion invalida.")
