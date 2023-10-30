from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox, QScrollArea, QTextEdit
from logic import howConstruct

class FileInputView(QWidget):
    def __init__(self, show_main_menu_callback):
        super().__init__()
        
        self.show_main_menu_callback = show_main_menu_callback
        self.starting_key = ""
        self.grammar_map = {}
        
        self.file_input_layout = QVBoxLayout()
        self.file_input_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.file_input_layout = QVBoxLayout()
        self.file_input_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.file_input_layout_label = QLabel("<h2>Descricao Formal</h2>")
        self.file_input_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.file_input_layout.addWidget(self.file_input_layout_label)
        
        self.text_input = QTextEdit()
        self.text_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_input.setPlaceholderText("Cole aqui as regras de construcao")
        self.file_input_layout.addWidget(self.text_input)
                
        self.test_word_layout = QHBoxLayout()
        self.test_word_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.test_word_layout_label = QLabel("<h3>Palavra</h3>")
        self.test_word_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.test_word_layout.addWidget(self.test_word_layout_label)
        
        self.test_word_layout_input = QLineEdit()
        self.test_word_layout_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.test_word_layout_input.setPlaceholderText("Insira a palavra a ser testada")
        self.test_word_layout.addWidget(self.test_word_layout_input)
        
        self.file_input_layout.addLayout(self.test_word_layout)

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
        
        
        self.file_input_layout.addLayout(self.output_layout)
                
        self.continue_button_layout = QHBoxLayout()
        self.continue_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_script_validate_input = (QPushButton("Testar"))
        self.button_script_validate_input.clicked.connect(self.validate_input)
        self.continue_button_layout.addWidget(self.button_script_validate_input)
        self.file_input_layout.addLayout(self.continue_button_layout)
        
        ## Footer
        self.choices_bottom = QHBoxLayout()
        self.choices_bottom.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_script_show_options_menu = (QPushButton("Resetar"))
        self.button_script_show_options_menu.clicked.connect(self.resetar)
        self.choices_bottom.addWidget(self.button_script_show_options_menu)
        self.file_input_layout.addLayout(self.choices_bottom)
        
        self.back_button_layout = QHBoxLayout()
        self.back_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.file_input_layout_back_button = (QPushButton("Voltar"))
        self.file_input_layout_back_button.clicked.connect(self.show_main_menu_callback)
        self.back_button_layout.addWidget(self.file_input_layout_back_button)
        self.file_input_layout.addLayout(self.back_button_layout)
        
        
        self.scroll_container_layout = QVBoxLayout()
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        scroll_content = QWidget()
        scroll_content.setLayout(self.file_input_layout)
        
        scroll_area.setWidget(scroll_content)
        
        self.scroll_container_layout.addWidget(scroll_area)
        
        
        self.setLayout(self.scroll_container_layout)
        
    def validate_input(self):
        raw_text_input = self.text_input.toPlainText()
        lines = raw_text_input.split('\n')
        
        self.starting_key == ""
        self.grammar_map.clear()
        valid_input = True
        
        try:
            for line in lines:
                line = line.strip()
                key, value = line.split(">")
                if key in self.grammar_map:
                    QMessageBox.warning(self, "Valores repetidos", "Valores repetidos detectados! Por favor insira valores unicos para cada variavel.")
                    valid_input = False
                values = value.split(",")
                if len(values) != len(set(values)):
                    QMessageBox.warning(self, "Valores repetidos", "Valores repetidos detectados! Por favor insira valores unicos para cada símbolo do alfabeto.")
                    valid_input = False
                self.grammar_map[key] = set(values)
                
                if self.starting_key == "":
                    self.starting_key = key
        except:
            QMessageBox.warning(self, "Valores invalidos", "Valores invalidos detectados! Por favor siga o padrao correto do arquivo de entrada.")
            valid_input = False
        
        if(valid_input):    
            test_word_input = self.test_word_layout_input.text()
            
            if test_word_input == "":
                QMessageBox.warning(self, "Teste Invalido", f"Por favor, insira uma palavra para ser testada.")
            else:
                result = howConstruct(self.grammar_map, self.starting_key, test_word_input, "", 1)

                if(result is not None):
                    self.output_contents_layout_label.setText('\n'.join(result))
                else:
                    self.output_contents_layout_label.setText(''.join("Impossivel contruir a palavra com essas regras."))
                    
    def resetar(self):
        self.starting_key = ""
        self.grammar_map.clear()
        
        self.text_input.setText("")
        self.test_word_layout_input.setText("")
        self.output_contents_layout_label.setText("")