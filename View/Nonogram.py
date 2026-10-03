import pygame
from View.Images import Images
from View.ArrayCell import ArrayCell
from View.Lives import Lives
from View.Consts import Consts
from View.ColorSelection import ColorSelection

# from View.Button import Button
# from View.Digit import Digit
# from View.DigitClock import DigitClock
from Controller.Controller import Controller
from random import randint, choice



TIMER_LINE = pygame.USEREVENT + 1
TIMER_COLUMN = pygame.USEREVENT + 2
TIMER_END = pygame.USEREVENT + 3


class Nonogram:
    # Animation des lignes / colonnes
    # Les cellules sont dessinées par paire (début, fin)
    _animate_lines: list[tuple[int, int]]
    _animate_columns: list[tuple[int, int]]

    # Tableau des cellules graphiques
    _arrayCells: ArrayCell | None

    # Permet de visualiser les cellules cachées
    _cheatCode: bool

    # Gestion/affichage graphique des coeurs de vie
    _lives: Lives

    # Sélection graphique des couleurs
    _selected_color: ColorSelection

    # Mémorisation de l'image de fond du jeu
    img_background: pygame.Surface | None

    # Taille des bords sur le jeu
    bord: int

    # Taille des fontes
    font_size: int

    # Fontes par défaut
    bold_fonte : pygame.font.Font
    fonte : pygame.font.Font

    # Taille de la fenêtre
    size: tuple[int, int]

    # Booléen permettant de marquer la fin du jeu
    ended: bool
    # Booléen permettant de savoir si la partie est gagnée
    won_game: bool

    # Contrôleur gérant le modèle du jeu
    controller: Controller

    def __init__(self, controller: Controller):

        self.bord = Consts.Border
        self._cheatCode = False

        self._animate_lines = []
        self._animate_columns = []
        self._monochrome: bool


        pygame.init()
        pygame.font.init()
        self.font_size = 20
        # Initialisation des fontes
        self.bold_fonte = pygame.font.SysFont('Arial', self.font_size, bold=True)
        self.fonte = pygame.font.SysFont('Times New Roman', self.font_size)


        # Chargement des images
        Images.load_images()

        # Taille de l'écran (de la fenêtre principale)
        self.size = Images.get_window_size()
        self.screen = pygame.display.set_mode((self.size[0], self.size[1]))
        Images.convert(self.screen)
        pygame.display.set_caption('Nonogram')
        pygame.display.set_icon(Images.caption)
        Images.convert(self.screen)

        # Fin du jeu
        self.ended = False
        self.won_game = False
        self.end_timer_on = False

        # Récupération du contrôleur
        # et initialisation de la fenêtre du contrôleur
        self.controller = controller
        self.controller.set_win(self)

        # Déterminer la taille de chaque carré de la grille
        self.w_border = Consts.DigitHorizontalSize + 2*Consts.Border
        self.h_border = Consts.DigitVerticalSize + 2*self.bord

        self.img_background = None

        self._arrayCells = None

        self._monochrome = False


        self.initialise_background()

        self.do_refresh = True

    def animate_line(self, li: int):
        if len(self._animate_lines) == 0:
            # On démarre l'animation
            # print("Initialise Line Animation")
            pygame.time.set_timer(TIMER_LINE, 50)
        self._animate_lines.append((li, 0))
        # print("Added Line Animation", self._animate_lines)

    def animate_column(self, col: int):
        if len(self._animate_columns) == 0:
            # print("Initialise Column Animation")
            pygame.time.set_timer(TIMER_COLUMN, 50)
        self._animate_columns.append((0, col))
        # print("Added Column Animation", self._animate_columns)

    def initialise_background(self):
        # On récupère la taille de la fenêtre
        (w, h) = self.size
        # On récupère la taille de l'image de fond
        (w_img, h_img) = Images.img_background.get_size()
        # On calcule le rapport img / fenetre
        w_r = w_img / w
        h_r = h_img / h
        surf = Images.img_background.convert()
        if w_r > h_r: # La réduction est plus importante en largeur qu'en hauteur
            # On réduit donc la hauteur
            w_i2 = w * h_r
            x = (w_img - w_i2) // 2
            # print(f"Dimensions de l'image : {w_img} x {h_img}")
            # print(f"Extraction de la zone de l'image : ({x}, 0, {w_i2}, {h_img - 1})")
            surf = Images.img_background.subsurface((x, 0, w_i2, h_img - 1))
        elif h_r > w_r:
            h_i2 = h * w_r
            y = (h - h_i2) // 2
            surf = Images.img_background.subsurface((0, y, w_img, h_i2))

        self.img_background = pygame.transform.scale(surf, self.size)

    def init_game(self):
        self._monochrome = self.display_message("Voulez un jeu avec des cellules monochromes ou en couleur ?",
                                          ["Monochrome", "Couleur"]) == 0
        dim = [5, 10, 15]
        c_dim = dim[self.display_message("Quelle dimension voulez-vous ?", [str(d) for d in dim])]
        self.controller.initialise_game(c_dim, self._monochrome)

        (w, h) = self.size
        w_r = (w - self.w_border - Consts.Border) // self.controller.get_size()
        h_r = (h - self.h_border - Consts.Border) // self.controller.get_size()
        _size = w_r
        if h_r < w_r:
            _size = h_r

        dim = [2, 3, 4]
        c_dim = dim[self.display_message("Combien de vies voulez-vous ?", [str(d) for d in dim])]
        self._lives = Lives(c_dim, Consts.Border, Consts.Border, Consts.DigitHorizontalSize, Consts.DigitVerticalSize)
        self._arrayCells = ArrayCell(self.controller,
            self.controller.get_size(), self.w_border, self.h_border, _size,
            self.controller.get_image(), self._lives)

        r = self._arrayCells.get_rect()
        x = r.topright[0] + Consts.Border
        y = r.topright[1] + Consts.Border

        w = Consts.WindowWidth - r.topright[0] - 2 * Consts.Border
        self._selected_color = ColorSelection(self._arrayCells.get_colors(), x, y, w,
                                              Consts.DigitVerticalSize - 2 * Consts.Border)
        self.set_refresh(True)



    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if self.ended:
                        continue
                    elif self._arrayCells is None:
                        self.init_game()
                    elif event.key == pygame.K_1:
                        suggestions = self.controller.get_mono_blocs_suggestions() if self._monochrome \
                            else self.controller.get_blocs_suggestions()
                        if len(suggestions) == 0:
                            self.display_message("Aucune suggestion proposée...")
                        else:
                            self._arrayCells.set_suggestions(suggestions)
                            self.set_refresh(True)
                    elif event.key == pygame.K_2:
                        suggestions = self.controller.get_mono_glue_suggestions() if self._monochrome \
                            else self.controller.get_glue_suggestions()
                        if len(suggestions) == 0:
                            self.display_message("Aucune suggestion proposée...")
                        else:
                            self._arrayCells.set_suggestions(suggestions)
                            self.set_refresh(True)
                    elif event.key == pygame.K_3:
                        suggestions = self.controller.get_empty_holes_suggestions()
                        if len(suggestions) == 0:
                            self.display_message("Aucune suggestion proposée...")
                        else:
                            self._arrayCells.set_suggestions(suggestions)
                            self.set_refresh(True)
                    elif event.key == pygame.K_4:
                        suggestions = self.controller.get_more_mono_suggestions() if self._monochrome \
                            else self.controller.get_more_suggestions()
                        if len(suggestions) == 0:
                            self.display_message("Aucune suggestion proposée...")
                        else:
                            self._arrayCells.set_suggestions(suggestions)
                            self.set_refresh(True)
                    elif event.key == pygame.K_c:
                        self._cheatCode = True
                        self.do_refresh = True
                    elif event.key == pygame.K_UP:
                        if self._selected_color.decrease():
                            self.do_refresh = True
                    elif event.key == pygame.K_DOWN:
                        if self._selected_color.increase():
                            self.do_refresh = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_c:
                        self._cheatCode = False
                        self.do_refresh = True
                    elif event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3\
                            or event.key == pygame.K_4:
                        self._arrayCells.set_suggestions({})
                        self.do_refresh = True
                elif event.type == pygame.MOUSEBUTTONDOWN and self._arrayCells is not None and not self.ended:
                    if not event.button == 1:
                        continue
                    pos = event.pos
                    if self._selected_color.contains(pos):
                        if self._selected_color.mouse_clicked(pos):
                            self.do_refresh = True
                    else:
                        coord = self._arrayCells.mouse_clicked(pos)
                        if coord is not None:
                            self.controller.mouse_clicked(coord, self.get_selected_color_index())
                            self._selected_color.update_solved_colors(self.controller.get_solved_colors())
                elif event.type == pygame.MOUSEMOTION and self._arrayCells is not None and not self.ended:
                    pos = event.pos
                    if self._arrayCells.mouse_moved(pos):
                        self.do_refresh = True
                        if event.buttons[0]:
                            coord = self._arrayCells.mouse_clicked(pos)
                            if coord is not None:
                                self.controller.mouse_clicked(coord, self.get_selected_color_index())
                                self._selected_color.update_solved_colors(self.controller.get_solved_colors())
                elif event.type == TIMER_LINE or event.type == TIMER_COLUMN:
                    # print("Animation !")
                    self.do_refresh = True
                elif event.type == TIMER_END:
                    self.end_timer_on = False
                    # print("End Timer")
                    self.play_again()
            if self.do_refresh:
                self.refresh()
            if self.controller.is_ended():
                self.ended = True
                self.won_game = True
            if self._arrayCells is not None and self._lives.get_active_lives() == 0:
                self.ended = True
            if not self.end_timer_on and (self.ended or self.won_game):
                # print("Activating End Timer")
                pygame.time.set_timer(TIMER_END, 800, 1)
                self.end_timer_on = True

    def play_again(self):
        self.ended = True
        self._arrayCells.set_suggestions({})
        if self.won_game:
            if self.display_message("Bravo !! Partie gagnée !!  Voulez-vous faire une nouvelle partie ?",
                                    ["Oui", "Non"]) == 0:
                self.init_game()
                self.ended = False
                self.won_game = False
        else:
            n = self.display_message("Perdu !! Voulez-vous recommencer la partie ?",
                                     ["Recommencer", "Nouvelle", "Quitter"])
            if n == 0:
                self.ended = False
                self._lives.reset_active_lives()
                self.controller.reset_image()
                self._arrayCells.reset_image()
                self.set_refresh(True)
            elif n == 1:
                self.ended = False
                self.init_game()

        if self.ended:
            pygame.quit()
            exit()

    def set_refresh(self, b: bool = True):
        self.do_refresh = b

    def set_won_game(self, b: bool = True):
        self.won_game = b

    def set_cell_visible(self, pos: tuple[int, int]):
        self._arrayCells.set_cell_visible(pos)

    def set_cell_error(self, pos: tuple[int, int]):
        self._arrayCells.set_cell_error(pos)

    def get_selected_color_index(self) -> int:
        return self._selected_color.get_selected_color_index()

    def update_digit_line(self, li: int, vus: list[bool]):
        self._arrayCells.update_digit_line(li, vus)

    def update_digit_column(self, co: int, vus: list[bool]):
        self._arrayCells.update_digit_column(co, vus)

    def refresh(self):
        # Dessin de l'image de fond
        background = pygame.Surface(self.size, pygame.SRCALPHA)
        background.fill((0, 0, 0, 0))
        if self._arrayCells is not None:
            self._arrayCells.draw(background, self._cheatCode)
            self._lives.draw(background)
            self._selected_color.draw(background)
        else:
            texte = self.bold_fonte.render("Appuyez sur une touche pour commencer", True, (47, 71, 137))
            pos = texte.get_rect(center=(self.size[0] / 2, self.size[1] / 2))
            background.blit(texte, pos)

        if len(self._animate_lines) > 0:
            items_to_keep = []
            # print("Line animation", self._animate_lines)
            for li, co in self._animate_lines:
                self.animate_cell(background, li, co)
                co += 1
                if co < self.controller.get_size():
                    items_to_keep.append((li, co))
            self._animate_lines = items_to_keep
            if len(self._animate_lines) == 0:
                # print("Stop Line animation !")
                pygame.time.set_timer(TIMER_LINE, 100, 1)

        if len(self._animate_columns) > 0:
            # print("Column animation", self._animate_columns)
            items_to_keep = []
            for li, co in self._animate_columns:
                self.animate_cell(background, li, co)
                li += 1
                if li < self.controller.get_size():
                    items_to_keep.append((li, co))
            self._animate_columns = items_to_keep
            if len(self._animate_columns) == 0:
                # print("Stop Column animation !")
                pygame.time.set_timer(TIMER_COLUMN, 100, 1)

        self.screen.blit(self.img_background, (0, 0))
        self.screen.blit(background, (0, 0))
        self.do_refresh = False

        pygame.display.flip()

    def animate_cell(self, background: pygame.Surface, li: int, co: int):
        color = pygame.Color(154, 245, 239, 160)
        background.fill(color, self._arrayCells.get_rect_cell(li, co))

    def display_message(self, message: str, boutons: list[str] = ["Ok"]) -> int:
        """
        Affiche une boîte de dialogue et retourne le numéro de bouton (commençant à 0) cliqué

        :param message: Message de la boîte de dialogue
        :param boutons: Liste des boutons (chaînes de caractères)
        :return: Numéro du bouton cliqué
        """

        # Largeur maximale de la boîte de dialogue : 4/5 de la largeur de la fenêtre
        w_max = 3*self.size[0]//4
        # Premier rendu du message
        txt = self.bold_fonte.render(message, True, (0, 0, 0))
        message_list = [txt]
        if txt.get_width() > w_max:
            # Il faut découper le message !
            # Nombre de caractères :
            nb = (w_max * len(message)) // txt.get_width()
            txt = None
            # Découpe du message
            msgs = message.split(' ')
            # Construction des découpes
            s = ""
            message_list = []
            for m in msgs:
                if len(s) + len(m) <= nb:
                    s = m if len(s) == 0 else s + " " + m
                else:
                    message_list.append(self.bold_fonte.render(s, True, (0, 0, 0)))
                    s = m
            if s is not None:
                message_list.append(self.bold_fonte.render(s, True, (0, 0, 0)))
        # Calcul de la largeur max des textes
        w_t = max([m.get_width() for m in message_list]) + 2*self.bord
        # Création des boutons
        btns = []
        for s in boutons:
            btns.append(self.bold_fonte.render(s, True, (0, 0, 0)))
        # Calcul de la largeur totale des boîtes des boutons
        w = sum([s.get_width() + 2*self.bord for s in btns]) + self.bord*len(btns)
        # print("w =", w, "w_max =", w_max)
        bouton_list = []
        if w > w_max:
            # Il faut découper les boutons sur plusieurs lignes
            w = 0
            lst = []
            for btn in btns:
                _w = btn.get_width() + 3*self.bord
                if w + _w < w_max:
                    lst.append(btn)
                    w += _w
                else:
                    bouton_list.append(lst)
                    w = _w
                    lst = [btn]
            bouton_list.append(lst)
        else:
            bouton_list.append(btns)
        # print("len(bouton_list) =", len(bouton_list))
        # Calcul de la largeur max des boutons
        w_b = max([sum([b.get_width() for b in lst]) + self.bord*(len(lst)+1) for lst in bouton_list])
        # Largeur de la boîte de dialogue
        w_boite = max(w_t, w_b)
        # Calcul de la hauteur de la boîte de dialogue
        h_boite = len(message_list)*self.font_size + (len(message_list)+1)*self.bord + \
            len(bouton_list)*(self.font_size + 3*self.bord) + self.bord
        # On peut maintenant dessiner la boîte de dialogue
        x_boite = (self.size[0] - w_boite) // 2
        y_boite = (self.size[1] - h_boite) // 2
        # Dessin du fond de la boîte
        self.screen.fill((255, 255, 255), (x_boite, y_boite, w_boite, h_boite))
        # Dessin du cadre de la boîte
        pygame.draw.rect(self.screen, (0, 0, 0), (x_boite, y_boite, w_boite, h_boite), 1)
        # Affichage du texte
        y = y_boite + self.bord
        for m in message_list:
            self.screen.blit(m, (x_boite + (w_boite - m.get_width())//2, y))
            y += self.font_size + self.bord
        # Affichage des boutons
        # On construit en même temps les cadres des boutons
        y += self.bord
        btn_cadre = []
        for lst in bouton_list:
            w = sum([btn.get_width() for btn in lst]) + 3*len(lst)*self.bord
            space = (w_boite - w) // 2
            x = space + x_boite
            for btn in lst:
                # Calcul de la largeur du bouton
                w = btn.get_width() + 2*self.bord
                # Calcul de la hauteur du bouton
                h = self.font_size+ 2*self.bord
                # Stockage du cadre et du "texte" du bouton
                btn_cadre.append((x, y, x+w, y+h, btn))
                # Dessin du bouton
                self._display_button(btn_cadre[-1])
                x += w + self.bord
            y += 3*self.bord + self.font_size
        # Mise a jour de la fenêtre
        pygame.display.flip()
        # On attend que l'utilisateur clique sur un bouton...
        # On empêche la sortie de l'application ?...
        clicked_btn = -1
        # Animation du bouton lorsque la souris est dessus
        over_btn = -1
        while clicked_btn == -1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                    (x, y) = event.pos
                    # On recherche si la position se trouve sur un des boutons
                    over = -1
                    for (n, (x1, y1, x2, y2, _)) in enumerate(btn_cadre):
                        if x1 <= x <= x2 and y1 <= y <= y2:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                clicked_btn = n
                            else:
                                over = n
                    if event.type == pygame.MOUSEMOTION:
                        # On regarde s'il faut redessiner le bouton
                        refresh = False
                        if over != over_btn:
                            if over_btn != -1:
                                # On remet le bouton dans son état normal
                                self._display_button(btn_cadre[over_btn])
                                refresh = True
                            over_btn = over
                            if over_btn != -1:
                                # On active le nouveau bouton
                                self._display_button(btn_cadre[over_btn], actif=True)
                                refresh = True
                        if refresh:
                            pygame.display.flip()
        # On efface la boîte de dialogue
        self.refresh()
        return clicked_btn

    def _display_button(self, cadre: tuple, actif: bool = False, actualise: bool = False):
        """
        Usage interne uniquement : Dessine un bouton avec son texte

        :param cadre: tuple (x1, y1, x2, y2, btn) définissant le cadre du bouton (pt sup gauche, pt inf droit) et le
        contenu (btn) de type pygame.Surface
        :param actif: True si la souris est au-dessus du bouton
        :param actualise: True s'il faut rafraîchir la fenêtre immédiatement
        :return: Rien
        """
        # Récupération du cadre et du contenu
        (x1, y1, x2, y2, btn) = cadre
        w = x2 - x1
        h = y2 - y1
        # Dessin du fond du bouton
        col = (134, 255, 13) if actif else (192, 192, 192)
        self.screen.fill(col, (x1, y1, w, h))
        # Dessin du cadre
        pygame.draw.rect(self.screen, (0, 0, 0), (x1, y1, w, h), 2 if actif else 1)
        # Dessin du texte
        self.screen.blit(btn, (x1 + self.bord, y1 + self.bord))
        if actualise:
            pygame.display.flip()

