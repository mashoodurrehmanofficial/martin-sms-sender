 
 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys,random,uuid,json,time
from PyQt5.QtGui import QTextCursor
try:
    from configHandler import configHandler
    from workerThread import workerThread
except:
    from .configHandler import configHandler
    from .workerThread import workerThread
    
    

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
        
        self.prepareHomeTab()
        self.prepareConfigurationTab()
        self.prepareCredentialsTab()
        self.tab_container.setCurrentIndex(0)
        
    def showWarningBox(self,text):
        QMessageBox.about(self, 'Error',str(text))
        
    def onHomeTabServiceComboBoxChange(self, value):
        self.home_tab_available_service_credentials_dropdown.clear()    
        available_credentials = configHandler().getServiceCredentialsList(service=value)      
        for credentials in available_credentials:
            self.home_tab_available_service_credentials_dropdown.addItem(str(credentials))
       

    def onClickContactListImportButton(self):
        file_name = QFileDialog.getOpenFileNames(self, "Select File", "", "*.txt")
        if file_name[0]:
            file_name = file_name[0][0]
            with open(file_name,'r',encoding="utf-8") as file:
                contacts = [str(x).strip() for x in file.readlines()]
                contacts = [x for x in contacts if len(str(x))>1]
                self.home_page_import_receivers_input_box.setText("\n".join(contacts))
            print(contacts) 

    def onClickMessageBodyLoadButton(self):
        self.home_page_import_message_input_box
        file_name = QFileDialog.getOpenFileNames(self, "Select File", "", "*.txt")
        if file_name[0]:
            file_name = file_name[0][0]
            with open(file_name,'r',encoding="utf-8") as file:
                message_body = file.read()
                self.home_page_import_message_input_box.setText(message_body)
                
                
    def prepareHomeTab(self):
        pass
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
        self.home_tab_available_service_credentials_dropdown = QComboBox()
        # self.home_tab_available_service_credentials_dropdown.currentTextChanged.connect(self.on_combobox_changed)
        # self.home_tab_available_service_credentials_dropdown.addItem(str(uuid.uuid4())+str(uuid.uuid4())+str(uuid.uuid4())) 
        
        self.home_tab_available_service_dropdown = QComboBox()
        self.home_tab_available_service_dropdown.currentTextChanged.connect(self.onHomeTabServiceComboBoxChange)
        self.availavle_services_list = configHandler().getAllServices()
        for service in self.availavle_services_list:
            self.home_tab_available_service_dropdown.addItem(str(service))


        self.home_page_service_selection_panel_layout.addWidget(self.home_tab_available_service_dropdown,1)  
        self.home_page_message_title = QLineEdit()
        self.home_page_service_selection_panel_layout.addWidget(self.home_tab_available_service_credentials_dropdown,5)
        self.home_page_service_selection_panel_layout.addWidget(self.home_page_message_title,1)
        self.home_main_frame_layout.addWidget(self.home_page_service_selection_panel,1) 
        # Horizontal -> Vertical  bar for input
        self.home_page_data_import_panel = QGroupBox("Import Data")
        self.home_page_data_import_panel_layout = QHBoxLayout()
        self.home_page_data_import_panel.setMaximumHeight(200)
        self.home_page_data_import_panel_layout.setAlignment(Qt.AlignTop)
        self.home_page_data_import_panel.setLayout(self.home_page_data_import_panel_layout)
        # Load contacts
        self.home_page_import_receivers_panel = QGroupBox("Import Contacts / Receivers")
        self.home_page_import_receivers_panel_layout = QVBoxLayout()
        self.home_page_import_receivers_panel.setAlignment(Qt.AlignTop)
        self.home_page_import_receivers_panel.setLayout(self.home_page_import_receivers_panel_layout)
        self.home_page_import_receivers_input_box = QTextEdit()
        self.home_page_import_receivers_panel_layout.addWidget(self.home_page_import_receivers_input_box,1)
        
        
        self.home_page_import_receivers_list_btn = QPushButton("Load Contact File")
        self.home_page_import_receivers_list_btn.clicked.connect(self.onClickContactListImportButton) 
        self.home_page_import_receivers_panel_layout.addWidget(self.home_page_import_receivers_list_btn,1)
        
        
        # self.home_page_import_receivers_panel_layout.addWidget(QPushButton("Load Contact File"),1)
        self.home_page_import_receivers_panel_layout.addStretch()
        # Load message
        self.home_page_import_message_panel = QGroupBox("Import Message")
        self.home_page_import_message_panel_layout = QVBoxLayout()
        self.home_page_import_message_panel.setAlignment(Qt.AlignTop)
        self.home_page_import_message_panel.setLayout(self.home_page_import_message_panel_layout)
        self.home_page_import_message_input_box = QTextEdit()
        self.home_page_import_message_panel_layout.addWidget(self.home_page_import_message_input_box,1)
        self.home_page_import_message_btn = QPushButton("Load Contact File")
        self.home_page_import_message_btn.clicked.connect(self.onClickMessageBodyLoadButton) 
        
        
        self.home_page_import_message_panel_layout.addWidget(self.home_page_import_message_btn,1)
        self.home_page_import_message_panel_layout.addStretch()
        self.home_page_data_import_panel_layout.addWidget(self.home_page_import_receivers_panel,1)
        self.home_page_data_import_panel_layout.addWidget(self.home_page_import_message_panel,1)
        # self.home_page_message_title = QLineEdit()
        # self.home_main_frame_layout.addWidget(self.home_page_message_title,1)
        self.home_main_frame_layout.addWidget(self.home_page_data_import_panel,1)
        self.home_main_frame_start_btn  =QPushButton("Start sending Messages")
        self.home_main_frame_start_btn.clicked.connect(self.onClickStartButton)
        self.home_main_frame_layout.addWidget(self.home_main_frame_start_btn,1)
        # Load message
        self.home_page_log_panel = QGroupBox("Log Messages")
        self.home_page_log_panel_layout = QVBoxLayout()
        self.home_page_log_panel.setAlignment(Qt.AlignTop)
        self.home_page_log_panel.setLayout(self.home_page_log_panel_layout)
        # self.home_page_log_input_box = QTextBrowser()
        self.home_page_log_input_box = QTextEdit()
        self.home_page_log_panel_layout.addWidget(self.home_page_log_input_box,1) 
        self.home_page_log_panel_layout.addStretch()
        self.home_main_frame_layout.addWidget(self.home_page_log_panel,1)
        self.home_tab_layout.addWidget(self.home_main_frame,1) 
        self.home_main_frame_layout.addStretch()
        
     
    def longRunningTask(self,service,credentials,message_title,contact_list,message_body): 
        try: 
            from workerThread import workerThread
        except: 
            from .workerThread import workerThread
        
        
        
        self.worker = workerThread(service,credentials,message_title,contact_list,message_body)
        self.worker.start()
        self.worker.finished.connect(self.customSlot)
        self.worker.update_component.connect(self.customSlot2)
        
    def customSlot2(self,val): 
        self.home_page_log_input_box.textCursor().insertText(str(val)+'\n')
        self.home_page_log_input_box.verticalScrollBar().setValue(self.home_page_log_input_box.verticalScrollBar().maximum())
        
        print("signal - update - ", val)
        
        
    def customSlot(self):
        pass
    
    def onClickStartButton(self):
        service = str(self.home_tab_available_service_dropdown.currentText())
        
        contact_list = ['923167 81 5639','923476026649','12057404127']
        contact_list = ["".join([y for y in str(x) if str(y).isnumeric()])  for x in contact_list ]

        self.home_page_message_title.setText("Alert")
        self.home_page_import_receivers_input_box.setText("\n".join(contact_list))
        self.home_page_import_message_input_box.setText(f"Hello this is message from {service}")


        credentials = eval(self.home_tab_available_service_credentials_dropdown.currentText())
        message_title = str(self.home_page_message_title.text())[:8]
        contact_list = str(self.home_page_import_receivers_input_box.toPlainText())
        message_body = str(self.home_page_import_message_input_box.toPlainText()) 
        contact_list = contact_list.replace("\n",',').split(",")
        
        # if not message_title or  message_title.isspace():
        #     self.showWarningBox("Please enter a Message Title (Sender ID)")
    
        # elif not contact_list or contact_list.isspace():
        #     self.showWarningBox("Please enter valid Contacts / Receivers' phone number list")
        
        # elif not message_body or message_body.isspace():
        #     self.showWarningBox("Please enter Message body to be sent")
        
        # credentials = str(credentials).replace("\'", "\"")
        # credentials = json.loads(credentials)
        # print("Service = ", service)
        # print("credentials = ", (credentials)) 
        self.home_page_log_input_box.setText("")
        self.longRunningTask(service,credentials,message_title,contact_list,message_body)
         
        
        
        
        
    def on_combobox_changed(self, value):
        print("combobox changed", value)  
        
    def onClickAddNewCredentialsButton(self):
        new_crendential_value = str(self.new_crendetials_insert_box.toPlainText())
        service = self.available_service_dropdown.currentText()
        try:
            new_crendential_value = eval(new_crendential_value)
            res = configHandler().addServiceCredentials(service=service,creds=new_crendential_value)
            if type(res) is dict:
                self.showWarningBox(text=f"Wrong credentials Layout.\nMake sure credentials have layout like follpwing\n{str(res)}")
            else:
                self.showWarningBox(text="Successfully added new credentials ")
                self.new_crendetials_insert_box.setPlainText("")
        except:
            self.showWarningBox(text="Invalid JSON struture for new Credentials")
        
        try:self.populateCrentialsTable()
        except:pass
    
 
    def populateCrentialsTable(self): 
        table_data = configHandler().getServiceCredentialsList(service=self.available_service_dropdown.currentText())
        
        print(table_data)
        
        # self.populateCrentialsTable()
        self.rows = len(table_data)
        self.tableWidget.setRowCount(self.rows)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1,QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeaderItem(0,QTableWidgetItem("Credentials"))
        self.tableWidget.setHorizontalHeaderItem(1,QTableWidgetItem("Operation"))
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # self.tableWidget.itemClicked.connect(self.deleteCredentialsRecord)
        
        for x in range(self.rows): 

            self.tableWidget.setItem(x,0, QTableWidgetItem(  str(table_data[x]) )) 
            btn = QPushButton(self.tableWidget)
            btn.setText(f'Delete - {x+1}')
            btn.clicked.connect(self.deleteCredentialsRecord)
            self.tableWidget.setCellWidget(x,1, btn) 
            # self.tableWidget.setItem(x,1, QTableWidgetItem(f"   Cell ({x},2)    ",)) 
        
        
    def deleteCredentialsRecord(self):
        service=self.available_service_dropdown.currentText()
        record_index = int(str(self.sender().text()).split(" - ")[-1])-1
        print (f"-> Deleting credentials for {service} with index {record_index}")
        configHandler().removeServiceCredentials(service=service,credential_index=int(record_index))
        self.populateCrentialsTable()
        
    
    def onChangeAvailableService(self,value):
        try:self.populateCrentialsTable()
        except:pass
    
    def prepareCredentialsTab(self):
        
        self.credentails_tab_layout.setAlignment(Qt.AlignTop)
        self.credentails_main_frame = QGroupBox("Manage Credentials")
        self.credentails_main_frame_layout = QHBoxLayout()
        self.credentails_main_frame.setFixedHeight(200)  
        # LEFT panel - New credentials Insertion panel
        self.service_credentials_insertion_panel = QGroupBox("Add Service Credentials")
        self.service_credentials_insertion_panel_layout = QVBoxLayout()
        self.service_credentials_insertion_panel_layout.setAlignment(Qt.AlignTop)
        self.service_credentials_insertion_panel.setLayout(self.service_credentials_insertion_panel_layout)
        self.available_service_dropdown = QComboBox()
        self.available_service_dropdown.currentTextChanged.connect(self.onChangeAvailableService) 
        # self.available_service_dropdown.currentText.connect(self.on_combobox_changed) 
        for service in self.availavle_services_list:
            self.available_service_dropdown.addItem(str(service))
        self.service_credentials_insertion_panel_layout.addWidget(self.available_service_dropdown,1)
        self.new_crendetials_insert_box = QPlainTextEdit()
        self.new_crendetials_save_btn = QPushButton("Add new Credentials")
        self.new_crendetials_save_btn.clicked.connect(self.onClickAddNewCredentialsButton)
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
        
        self.tableWidget = QTableWidget()
        self.populateCrentialsTable()
        # self.rows =100
        # self.tableWidget.setRowCount(self.rows)
        # self.tableWidget.setColumnCount(2)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(1,QHeaderView.ResizeToContents)
        # self.tableWidget.setHorizontalHeaderItem(0,QTableWidgetItem("Credentials"))
        # self.tableWidget.setHorizontalHeaderItem(1,QTableWidgetItem("Operation"))
        # self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # # self.tableWidget.itemClicked.connect(self.deleteCredentialsRecord)
        
        # for x in range(self.rows): 

        #     self.tableWidget.setItem(x,0, QTableWidgetItem( str(uuid.uuid4())+str(uuid.uuid4())+str(uuid.uuid4())+str(uuid.uuid4())+str(uuid.uuid4())  )) 
        #     btn = QPushButton(self.tableWidget)
        #     btn.setText(f'Delete - {x+1}')
        #     btn.clicked.connect(self.deleteCredentialsRecord)
        #     self.tableWidget.setCellWidget(x,1, btn) 
        #     # self.tableWidget.setItem(x,1, QTableWidgetItem(f"   Cell ({x},2)    ",)) 
        
        
        self.credentails_listing_table_layout.addWidget(self.tableWidget)  
        self.credentails_tab_layout.addWidget(self.credentails_listing_table,12) 

        self.credentails_tab_layout.addStretch()




    def save_configuration_thread_threshold(self):
        number = self.configuration_thread_input.text()
        try:
            number = int(number)
            configHandler().setThreadsThreshold(number)
            self.showWarningBox("Thread threshold update")
        except Exception:
            self.showWarningBox("Threads / sec can only be a number") 
        pass
        
    def prepareConfigurationTab(self):
        self.configuration_tab_layout.setAlignment(Qt.AlignTop)
        self.configuration_frame = QGroupBox("Set Threads / sec")
        self.group_box_layout = QHBoxLayout()
        self.configuration_save_btn = QPushButton("Save settings",)
        self.configuration_save_btn.clicked.connect(self.save_configuration_thread_threshold)
        self.configuration_thread_input = QLineEdit()
        self.configuration_thread_input.setText(str(configHandler().getThreadsThreshold()))
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