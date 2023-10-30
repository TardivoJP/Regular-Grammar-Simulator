from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox, QScrollArea
from logic import howConstruct

class ManualInputView(QWidget):
    def __init__(self, show_main_menu_callback):
        super().__init__()
        
        self.show_main_menu_callback = show_main_menu_callback
        self.state = 0
        self.variables_set = {}
        self.alphabet_set = {}
        self.starting_key = ""
        self.grammar_map = {}
        self.derivation_inputs = {}
        
        self.manual_input_layout = QVBoxLayout()
        self.manual_input_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.manual_input_layout_label = QLabel("<h2>Descricao Formal</h2>")
        self.manual_input_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.manual_input_layout.addWidget(self.manual_input_layout_label)
        
        self.variables_layout = QHBoxLayout()
        self.variables_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.variables_layout_label = QLabel("<h3>V</h3>")
        self.variables_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.variables_layout.addWidget(self.variables_layout_label)
        
        self.variables_layout_input = QLineEdit()
        self.variables_layout_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.variables_layout_input.setPlaceholderText("Insira as variáveis separadas por virgulas")
        self.variables_layout.addWidget(self.variables_layout_input)
        
        self.manual_input_layout.addLayout(self.variables_layout)
        
        
        self.alphabet_layout = QHBoxLayout()
        self.alphabet_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.alphabet_layout_label = QLabel("<h3>T</h3>")
        self.alphabet_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.alphabet_layout.addWidget(self.alphabet_layout_label)
        
        self.alphabet_layout_input = QLineEdit()
        self.alphabet_layout_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.alphabet_layout_input.setPlaceholderText("Insira o alfabeto da linguagem separado por virgulas")
        self.alphabet_layout.addWidget(self.alphabet_layout_input)
        
        self.manual_input_layout.addLayout(self.alphabet_layout)
        
        # alphabet_layout items start invisible
        for i in range(self.alphabet_layout.count()):
            item = self.alphabet_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)
        
        
        self.start_symbol_layout = QHBoxLayout()
        self.start_symbol_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.start_symbol_layout_label = QLabel("<h3>S</h3>")
        self.start_symbol_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.start_symbol_layout.addWidget(self.start_symbol_layout_label)
        
        self.start_symbol_layout_input = QLineEdit()
        self.start_symbol_layout_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.start_symbol_layout_input.setPlaceholderText("Insira o simbolo de partida para as derivacoes")
        self.start_symbol_layout.addWidget(self.start_symbol_layout_input)
        
        self.manual_input_layout.addLayout(self.start_symbol_layout)
        
        # start_symbol_layout items start invisible
        for i in range(self.start_symbol_layout.count()):
            item = self.start_symbol_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)
                
                
        self.rules_layout = QVBoxLayout()
        self.rules_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.rules_layout_label = QLabel("<h2>Derivacoes</h2>")
        self.rules_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rules_layout.addWidget(self.rules_layout_label)
        self.manual_input_layout.addLayout(self.rules_layout)
        
        # rules_layout items start invisible
        for i in range(self.rules_layout.count()):
            item = self.rules_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)
                
                
        self.test_word_layout = QHBoxLayout()
        self.test_word_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.test_word_layout_label = QLabel("<h3>Palavra</h3>")
        self.test_word_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.test_word_layout.addWidget(self.test_word_layout_label)
        
        self.test_word_layout_input = QLineEdit()
        self.test_word_layout_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.test_word_layout_input.setPlaceholderText("Insira a palavra a ser testada")
        self.test_word_layout.addWidget(self.test_word_layout_input)
        
        self.manual_input_layout.addLayout(self.test_word_layout)
        
        # teste_word_layout items start invisible
        for i in range(self.test_word_layout.count()):
            item = self.test_word_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)
                
                
        self.output_layout = QVBoxLayout()
        self.output_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.output_layout_label = QLabel("<h2>Regras de Construcao Utilizadas</h2>")
        self.output_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_layout.addWidget(self.output_layout_label)
        
        self.output_contents_layout = QHBoxLayout()
        self.output_contents_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.output_contents_layout_label = QLabel("")
        self.output_contents_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_contents_layout.addWidget(self.output_contents_layout_label)

        self.output_layout.addLayout(self.output_contents_layout)
        
        
        self.manual_input_layout.addLayout(self.output_layout)
        
        # output_layout items start invisible
        for i in range(self.output_layout.count()):
            item = self.output_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)
                
        ## Footer
        self.continue_button_layout = QHBoxLayout()
        self.continue_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_script_validate_input = (QPushButton("Continuar"))
        self.button_script_validate_input.clicked.connect(self.validate_input)
        self.continue_button_layout.addWidget(self.button_script_validate_input)
        self.manual_input_layout.addLayout(self.continue_button_layout)
        
        self.choices_bottom = QHBoxLayout()
        self.choices_bottom.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_script_show_options_menu = (QPushButton("Resetar"))
        self.button_script_show_options_menu.clicked.connect(self.reset)
        self.choices_bottom.addWidget(self.button_script_show_options_menu)
        self.manual_input_layout.addLayout(self.choices_bottom)
        
        self.back_button_layout = QHBoxLayout()
        self.back_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.manual_input_layout_back_button = (QPushButton("Voltar"))
        self.manual_input_layout_back_button.clicked.connect(self.show_main_menu_callback)
        self.back_button_layout.addWidget(self.manual_input_layout_back_button)
        self.manual_input_layout.addLayout(self.back_button_layout)
        
        
        self.scroll_container_layout = QVBoxLayout()
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        scroll_content = QWidget()
        scroll_content.setLayout(self.manual_input_layout)
        
        scroll_area.setWidget(scroll_content)
        
        self.scroll_container_layout.addWidget(scroll_area)
        
        
        self.setLayout(self.scroll_container_layout)
    
    def validate_input(self):
        match self.state:
            case 0: 
                user_input = self.variables_layout_input.text()
                values_array = user_input.split(",")
                
                if len(values_array) != len(set(values_array)):
                    QMessageBox.warning(self, "Valores repetidos", "Valores repetidos detectados! Por favor insira valores unicos para cada variavel.")
                    self.variables_set.clear()
                elif any(len(variable) != 1 for variable in values_array):
                    QMessageBox.warning(self, "Valores invalidos", "Pelo menos um valor inserido é invalido. Por favor, com no máximo um caractere para o variavel.")
                    self.variables_set.clear()
                else:
                    self.variables_set = set(values_array)
                    
                    self.variables_layout_input.setDisabled(True)
                    self.state = 1
                    
                    for i in range(self.alphabet_layout.count()):
                        item = self.alphabet_layout.itemAt(i)

                        if isinstance(item.widget(), QWidget):
                            item.widget().setVisible(True)
            
            case 1:
                user_input = self.alphabet_layout_input.text()
                values_array = user_input.split(",")
                
                if len(values_array) != len(set(values_array)):
                    QMessageBox.warning(self, "Valores repetidos", "Valores repetidos detectados! Por favor insira valores unicos para cada símbolo do alfabeto.")
                    self.alphabet_set.clear()
                elif any(len(alphabet_symbol) != 1 for alphabet_symbol in values_array):
                    QMessageBox.warning(self, "Valores invalidos", "Pelo menos um valor inserido e invalido. Por favor, insira valores com no máximo um caractere para cada simbolo do alfabeto.")
                    self.alphabet_set.clear()
                elif any(variable in self.variables_set for variable in values_array):
                    QMessageBox.warning(self, "Valores ja existentes", "Pelo menos um valor inserido ja existe nos valores de variaveis. Por favor, insira valores unicos para o alfabeto.")
                    self.alphabet_set.clear()
                else:
                    self.alphabet_set = set(values_array)
                    
                    self.alphabet_layout_input.setDisabled(True)
                    self.state = 2
                    
                    for i in range(self.start_symbol_layout.count()):
                        item = self.start_symbol_layout.itemAt(i)

                        if isinstance(item.widget(), QWidget):
                            item.widget().setVisible(True)
                            
            case 2:
                user_input = self.start_symbol_layout_input.text()
                
                if(len(user_input) > 1):
                    QMessageBox.warning(self, "Valor invalido", "Por favor insira um valor existente das variaveis.")
                elif(user_input not in self.variables_set):
                    QMessageBox.warning(self, "Valor invalido", "Por favor insira um valor existente das variaveis.")
                else:
                    self.starting_key = user_input
                    
                    self.start_symbol_layout_input.setDisabled(True)
                    self.state = 3
                    
                    for i in range(self.rules_layout.count()):
                        item = self.rules_layout.itemAt(i)

                        if isinstance(item.widget(), QWidget):
                            item.widget().setVisible(True)
                            
                    starting_derivacao_layout = QHBoxLayout()
                    starting_derivacao_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

                    starting_derivacao_layout_label = QLabel("<h3>" + self.starting_key + " - </h3>")
                    starting_derivacao_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    starting_derivacao_layout.addWidget(starting_derivacao_layout_label)

                    starting_derivacao_layout_input = QLineEdit()
                    starting_derivacao_layout_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    starting_derivacao_layout_input.setPlaceholderText("Insira as regras separadas por virgula")
                    starting_derivacao_layout.addWidget(starting_derivacao_layout_input)

                    self.rules_layout.addLayout(starting_derivacao_layout)
                    
                    self.derivation_inputs = {self.starting_key: starting_derivacao_layout_input}

                    variables_set_copy = self.variables_set.copy()
                    variables_set_copy.discard(self.starting_key)

                    for variable in variables_set_copy:
                        derivacao_layout = QHBoxLayout()
                        derivacao_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

                        derivacao_layout_label = QLabel("<h3>" + variable + " - </h3>")
                        derivacao_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        derivacao_layout.addWidget(derivacao_layout_label)

                        derivacao_layout_input = QLineEdit()
                        derivacao_layout_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        derivacao_layout_input.setPlaceholderText("Insira as regras separadas por virgula")
                        derivacao_layout.addWidget(derivacao_layout_input)

                        self.rules_layout.addLayout(derivacao_layout)
                        
                        self.derivation_inputs[variable] = derivacao_layout_input
                    
            case 3:
                valid_input = True
                self.grammar_map.clear()
                combined_set = self.variables_set.union(self.alphabet_set)
                
                for variable, line_edit in self.derivation_inputs.items():
                    inputs = line_edit.text().split(",")
                    
                    if any(not input_str.strip() for input_str in inputs):
                        QMessageBox.warning(self, "Campo Vazio", f"Campo vazio detectado para a variavel '{variable}'. Por favor, insira valores validos.")
                        valid_input = False
                        break
                    
                    if len(inputs) != len(set(inputs)):
                        QMessageBox.warning(self, "Regras repetidas", f"Regras repetidas detectadas para a variavel '{variable}'. Por favor, insira regras unicas.")
                        valid_input = False
                        break
                    
                    for input in inputs:
                        if not self.validate_string(input, combined_set):
                            QMessageBox.warning(self, "Símbolo Invalido", f"Símbolo invalido '{input}' detectado para a variavel '{variable}'. Por favor, insira valores validos.")
                            valid_input = False
                            break

                    else:
                        self.grammar_map[variable] = set(inputs)
                
                if valid_input:
                    print(self.grammar_map)
                    
                    self.state = 4
                    
                    for line_edit in self.derivation_inputs.values():
                        line_edit.setDisabled(True)
                        
                    for i in range(self.test_word_layout.count()):
                        item = self.test_word_layout.itemAt(i)

                        if isinstance(item.widget(), QWidget):
                            item.widget().setVisible(True)
                            
                    self.button_script_validate_input.setText("Testar")
                            
            case 4:
                user_input = self.test_word_layout_input.text()
                
                if user_input == "":
                    QMessageBox.warning(self, "Teste Invalido", f"Por favor, insira uma palavra para ser testada.")
                else:
                    for i in range(self.output_layout.count()):
                        item = self.output_layout.itemAt(i)

                        if isinstance(item.widget(), QWidget):
                            item.widget().setVisible(True)
                    
                    result = howConstruct(self.grammar_map, self.starting_key, user_input, "", 1)

                    if(result is not None):
                        self.output_contents_layout_label.setText('\n'.join(result))
                    else:
                        self.output_contents_layout_label.setText(''.join("Impossivel contruir a palavra com essas regras."))
                
                    
    def reset(self):
        self.state = 0
        self.variables_set.clear()
        self.alphabet_set.clear()
        self.starting_key = ""
        self.derivation_inputs.clear()
        self.grammar_map.clear()
        
        self.variables_layout_input.setText("")
        self.alphabet_layout_input.setText("")
        self.start_symbol_layout_input.setText("")
        self.test_word_layout_input.setText("")
        self.output_contents_layout_label.setText("")
        
        self.variables_layout_input.setDisabled(False)
        self.alphabet_layout_input.setDisabled(False)
        self.start_symbol_layout_input.setDisabled(False)
        
        self.button_script_validate_input.setText("Continuar")
        
        for i in range(self.alphabet_layout.count()):
            item = self.alphabet_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)
                
        for i in range(self.start_symbol_layout.count()):
            item = self.start_symbol_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)
                
        while self.rules_layout.count():
            layout_item = self.rules_layout.takeAt(0)
            if layout_item:
                item_layout = layout_item.layout()
                if item_layout:
                    while item_layout.count():
                        item = item_layout.takeAt(0)
                        widget = item.widget()
                        if widget:
                            widget.deleteLater()
                        else:
                            pass
                    item_layout.deleteLater()
                else:
                    widget = layout_item.widget()
                    if widget:
                        widget.deleteLater()

        self.rules_layout_label = QLabel("<h3>Derivacoes</h3>")
        self.rules_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rules_layout.addWidget(self.rules_layout_label)
        self.manual_input_layout.addLayout(self.rules_layout)
        
        for i in range(self.rules_layout.count()):
            item = self.rules_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)
                
        for i in range(self.test_word_layout.count()):
            item = self.test_word_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)
                
        for i in range(self.output_layout.count()):
            item = self.output_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)
    
    def validate_string(self, input_string, char_set):
        if "*" not in input_string:
            return all(char in char_set for char in input_string)
        elif input_string == "**":
            return True
        else:
            return False