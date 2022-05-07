 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys,random,uuid
try:
    from configHandler import configHandler
except:
    from .configHandler import configHandler
    


class Main(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.title = 'SMS Sender'
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 600
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)       
          
        # self.showMaximized()
        # Initialize tab screen
        self.tab_container = QTabWidget()
        
        self.home_tab = QWidget()
        self.credentails_tab = QWidget()
        self.configuration_tab = QWidget()

        self.home_tab_layout = QVBoxLayout()    
        self.credentails_tab_layout = QVBoxLayout()   
        self.configuration_tab_layout = QVBoxLayout()

        self.home_tab.setLayout(self.home_tab_layout)
        self.credentails_tab.setLayout(self.credentails_tab_layout)
        self.configuration_tab.setLayout(self.configuration_tab_layout)

        self.home_tab_label = QLabel()
        self.credentails_tab_label = QLabel()
        self.configuration_tab_label = QLabel()

 
        self.home_tab_layout.addWidget(self.home_tab_label)
        self.credentails_tab_layout.addWidget(self.credentails_tab_label)
        self.configuration_tab_layout.addWidget(self.configuration_tab_label)

        # Add tabs
        self.tab_container.addTab(self.home_tab,"Home")
        self.tab_container.addTab(self.credentails_tab,"Credentials")
        self.tab_container.addTab(self.configuration_tab,"Configuration")     


        self.setCentralWidget(self.tab_container)
        # self.center()
        self.show()
        
        self.tab_container.setCurrentIndex(2)
        self.prepareHomeTab()
        self.prepareConfigurationTab()
        self.prepareCredentialsTab()
        

        
    def onHomeTabServiceComboBoxChange(self, value):
        self.available_service_credentials_dropdown.clear()        
        print("onHomeTabServiceComboBoxChange", value)      
        

    def prepareHomeTab(self):
        
        self.tab_container.setCurrentIndex(0)
        self.home_tab_layout.setAlignment(Qt.AlignTop)
 
        self.home_main_frame = QGroupBox("Main Panel")
        self.home_main_frame_layout = QVBoxLayout() 
        self.home_main_frame.setLayout(self.home_main_frame_layout)
        self.home_main_frame.setAlignment(Qt.AlignTop)
        
        # Horizontal bar for comboxes
        self.home_page_service_selection_panel = QGroupBox("Select Credentials")
        self.home_page_service_selection_panel_layout = QHBoxLayout()
        self.home_page_service_selection_panel_layout.setAlignment(Qt.AlignTop)
        self.home_page_service_selection_panel.setLayout(self.home_page_service_selection_panel_layout)
        self.home_page_service_selection_panel.setFixedHeight(70) 
        
        self.available_service_dropdown = QComboBox()
        self.available_service_dropdown.currentTextChanged.connect(self.onHomeTabServiceComboBoxChange)
        
        
        self.availavle_services_list = configHandler().getAllServices()
        for service in self.availavle_services_list:
            self.available_service_dropdown.addItem(str(service))
            
            
        self.available_service_credentials_dropdown = QComboBox()
        self.available_service_credentials_dropdown.currentTextChanged.connect(self.on_combobox_changed)
        self.available_service_credentials_dropdown.addItem(str(uuid.uuid4())+str(uuid.uuid4())+str(uuid.uuid4()))
        self.available_service_credentials_dropdown.addItem(str(uuid.uuid4())+str(uuid.uuid4())+str(uuid.uuid4()))
        self.home_page_service_selection_panel_layout.addWidget(self.available_service_dropdown,1)
        
        self.home_page_message_title = QLineEdit()
        
        self.home_page_service_selection_panel_layout.addWidget(self.available_service_credentials_dropdown,5)
        self.home_page_service_selection_panel_layout.addWidget(self.home_page_message_title,1)
         
    
       
        self.home_main_frame_layout.addWidget(self.home_page_service_selection_panel,1) 
        
        # Horizontal -> Vertical  bar for input
        
        self.home_page_data_import_panel = QGroupBox("Import Data")
        self.home_page_data_import_panel_layout = QHBoxLayout()
        self.home_page_data_import_panel.setMaximumHeight(200)
        self.home_page_data_import_panel_layout.setAlignment(Qt.AlignTop)
        self.home_page_data_import_panel.setLayout(self.home_page_data_import_panel_layout)
        # self.home_page_data_import_panel.setFixedHeight(100) 
        
        # Load contacts
        self.home_page_import_receivers_panel = QGroupBox("Import Contacts / Receivers")
        self.home_page_import_receivers_panel_layout = QVBoxLayout()
        self.home_page_import_receivers_panel.setAlignment(Qt.AlignTop)
        self.home_page_import_receivers_panel.setLayout(self.home_page_import_receivers_panel_layout)
        self.home_page_import_receivers_input_box = QTextEdit()
        self.home_page_import_receivers_panel_layout.addWidget(self.home_page_import_receivers_input_box,1)
        self.home_page_import_receivers_panel_layout.addWidget(QPushButton("Load Contact File"),1)
        self.home_page_import_receivers_panel_layout.addStretch()
        
        
        
        # Load message
        self.home_page_import_message_panel = QGroupBox("Import Message")
        self.home_page_import_message_panel_layout = QVBoxLayout()
        self.home_page_import_message_panel.setAlignment(Qt.AlignTop)
        self.home_page_import_message_panel.setLayout(self.home_page_import_message_panel_layout)
        self.home_page_import_message_input_box = QTextEdit()
        self.home_page_import_message_panel_layout.addWidget(self.home_page_import_message_input_box,1)
        self.home_page_import_message_panel_layout.addWidget(QPushButton("Load Messge File"),1)
        self.home_page_import_message_panel_layout.addStretch()
        
        
        
        
        self.home_page_data_import_panel_layout.addWidget(self.home_page_import_receivers_panel,1)
        self.home_page_data_import_panel_layout.addWidget(self.home_page_import_message_panel,1)
        # self.home_page_message_title = QLineEdit()
        # self.home_main_frame_layout.addWidget(self.home_page_message_title,1)
        self.home_main_frame_layout.addWidget(self.home_page_data_import_panel,1)
        
        
        
        self.home_main_frame_layout.addWidget(QPushButton("Start sending Messages"),1)
         
         
        # Load message
        self.home_page_log_panel = QGroupBox("Log Messages")
        self.home_page_log_panel_layout = QVBoxLayout()
        self.home_page_log_panel.setAlignment(Qt.AlignTop)
        self.home_page_log_panel.setLayout(self.home_page_log_panel_layout)
        self.home_page_log_input_box = QTextEdit()
        self.home_page_log_panel_layout.addWidget(self.home_page_log_input_box,1) 
        self.home_page_log_panel_layout.addStretch()
         
        self.home_main_frame_layout.addWidget(self.home_page_log_panel,1)
         
         
         
        self.home_tab_layout.addWidget(self.home_main_frame,1) 
        
        
        
        
        self.home_main_frame_layout.addStretch()
        
        
        
        
        
        
        
        
        
    def on_combobox_changed(self, value):
        print("combobox changed", value)  
        
    def prepareCredentialsTab(self):
        
        self.credentails_tab_layout.setAlignment(Qt.AlignTop)

 
        self.credentails_main_frame = QGroupBox("Manage Credentials")
        self.credentails_main_frame_layout = QHBoxLayout()
        self.credentails_main_frame.setFixedHeight(200) 


        # self.credentails_save_btn.clicked.connect(self.save_credentails_thread_threshold)
        # self.credentails_thread_input = QLineEdit()
        # self.group_box_layout.addWidget(self.credentails_thread_input,11)
        
        # Create QBOX for dropdown and adding new credentials
        # - BQGroupBox
        # |__ Layout
        #    |__ Widgets
        
        # LEFT panel - New credentials Insertion panel
        self.service_credentials_insertion_panel = QGroupBox("Add Service Credentials")
        self.service_credentials_insertion_panel_layout = QVBoxLayout()
        self.service_credentials_insertion_panel_layout.setAlignment(Qt.AlignTop)
        self.service_credentials_insertion_panel.setLayout(self.service_credentials_insertion_panel_layout)
        
        self.available_service_dropdown = QComboBox()
        self.available_service_dropdown.currentTextChanged.connect(self.on_combobox_changed)
        self.available_service_dropdown.addItem('clicksend.com')
        self.available_service_dropdown.addItem('clickatell.com')
        self.available_service_dropdown.addItem('vonage.co.uk')
        self.available_service_dropdown.addItem('messagebird.com')
        
        self.service_credentials_insertion_panel_layout.addWidget(self.available_service_dropdown,1)
        
        
        self.new_crendetials_insert_box = QPlainTextEdit()
        self.new_crendetials_save_btn = QPushButton("Add new Credentials")
        self.service_credentials_insertion_panel_layout.addWidget(self.new_crendetials_insert_box,1)
        self.service_credentials_insertion_panel_layout.addWidget(self.new_crendetials_save_btn,1)
        self.credentails_main_frame_layout.addWidget(self.service_credentials_insertion_panel,3)
        
        
        
        
        # Right panel - New service Insertion panel
        
        # self.service_insertion_panel = QGroupBox("Add service")
        # self.service_insertion_panel_layout = QVBoxLayout()
        # self.service_insertion_panel_layout.setAlignment(Qt.AlignTop) 
        # self.new_crendetials_insert_box = QLineEdit() 
        # self.new_crendetials_save_btn = QPushButton("Add new Credentials")
        # self.service_insertion_panel_layout.addWidget(self.new_crendetials_insert_box,1)
        # self.service_insertion_panel_layout.addWidget(self.new_crendetials_save_btn,1)
        # self.service_insertion_panel.setLayout(self.service_insertion_panel_layout)
        # self.credentails_main_frame_layout.addWidget(self.service_insertion_panel,1)

        self.credentails_main_frame.setLayout(self.credentails_main_frame_layout)
        self.credentails_main_frame.setAlignment(Qt.AlignTop)
        
        self.credentails_tab_layout.addWidget(self.credentails_main_frame,1) 
        
        
        
        self.credentails_listing_table = QGroupBox("Credentials Listing")
        self.credentails_listing_table_layout = QHBoxLayout()  
        self.credentails_listing_table.setLayout(self.credentails_listing_table_layout)
        # self.credentails_listing_table_scroll_area = QScrollArea
        
        
        self.tableWidget = QTableWidget()
        self.rows =100
        self.tableWidget.setRowCount(self.rows)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1,QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeaderItem(0,QTableWidgetItem("Credentials"))
        self.tableWidget.setHorizontalHeaderItem(1,QTableWidgetItem("Operation"))
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # self.tableWidget.itemClicked.connect(self.editItem)
        
        for x in range(self.rows): 

            self.tableWidget.setItem(x,0, QTableWidgetItem( str(uuid.uuid4())+str(uuid.uuid4())+str(uuid.uuid4())+str(uuid.uuid4())+str(uuid.uuid4())  )) 
            btn = QPushButton(self.tableWidget)
            btn.setText(f'Delete - {x+1}')
            btn.clicked.connect(self.editItem)
            self.tableWidget.setCellWidget(x,1, btn) 
            # self.tableWidget.setItem(x,1, QTableWidgetItem(f"   Cell ({x},2)    ",)) 
        
        
        self.credentails_listing_table_layout.addWidget(self.tableWidget)  
        self.credentails_tab_layout.addWidget(self.credentails_listing_table,12) 

        self.credentails_tab_layout.addStretch()

    def editItem(self):
        record_index = int(str(self.sender().text()).split(" - ")[-1])-1
        print ( record_index)


    def save_configuration_thread_threshold(self):
        number = self.configuration_thread_input.text()
        try:
            number = int(number)
        except Exception:
            QMessageBox.about(self, 'Error','Threads / sec can only be a number')
            
        pass
        
    def prepareConfigurationTab(self):
        self.configuration_tab_layout.setAlignment(Qt.AlignTop)
        self.configuration_frame = QGroupBox("Set Threads / sec")
        self.group_box_layout = QHBoxLayout()
        self.configuration_save_btn = QPushButton("Save settings",)
        self.configuration_save_btn.clicked.connect(self.save_configuration_thread_threshold)
        self.configuration_thread_input = QLineEdit()
        self.group_box_layout.addWidget(self.configuration_thread_input,11)
        self.group_box_layout.addWidget(self.configuration_save_btn,1)
        self.configuration_frame.setLayout(self.group_box_layout)
        self.configuration_frame.setAlignment(Qt.AlignTop)
        self.configuration_tab_layout.addWidget(self.configuration_frame) 





    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_()) 