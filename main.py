 
import ctypes,threading
import os,json ,sys,subprocess
import time

sys.path.append(os.getcwd()) 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
from datetime import datetime,timedelta
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

try:
    from helpers.configHandlerFile import configHandler
    from helpers.workerThreadFile import workerThread,launchNewInstanceThread
    from helpers.workerActivationThread import serverThread
    from helpers.workerRemainingBalanceThread  import remainingBalanceThread
    from helpers.sharedMemory  import sharedMemory
except:
    try:
        from helpers.configHandlerFile import configHandler
        
    except:
        from helpers.configHandlerFile import configHandler
    try:
        from helpers.sharedMemory  import sharedMemory  
    except:
        from helpers.sharedMemory  import sharedMemory

    try:
        from helpers.workerThreadFile import workerThread,launchNewInstanceThread
        from helpers.workerActivationThread import serverThread
        from helpers.workerRemainingBalanceThread  import remainingBalanceThread
    except:
        from helpers.workerActivationThread import serverThread
        from helpers.workerRemainingBalanceThread  import remainingBalanceThread
        ...
    # from workerThreadFile import workerThread




def getArgumentValue(key):
    args = sys.argv 
    parameter = [x for x in args if key in x]
    if parameter:
        parameter = parameter[0]
        return str(parameter).split(key)[-1]
    return None
     

class contactFileReaderThreadClass(QThread): 
    def __init__(self,file_name):
        super().__init__()
        self.file_name  = file_name 
        
    file_reader_signal_slot = pyqtSignal(str)
    def run(self): 
        try:
            with open(self.file_name,'r',encoding="utf-8") as file:
                contacts = [str(x).strip() for x in file.readlines()]
                contacts = [x for x in contacts if len(str(x))>1]
                contacts = "\n".join(contacts) 
                self.file_reader_signal_slot.emit(f"{contacts}") 
 
        except  UnicodeDecodeError:
            self.file_reader_signal_slot.emit("error")
             



 
if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "2"
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class Main(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.title = 'QuickSMS'
        self.left = 0
        self.top = 0
        self.width = 1000
        self.height = 600
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)      
        self.setWindowIcon( QIcon(QApplication.style().standardIcon(QStyle.SP_DesktopIcon))  )
        self.IS_STOP_FUNCTIONALITY_ALLOWED = False

        # self.showMaximized()
        # Initialize tab screen
        self.tab_container = QTabWidget()
        self.tab_container.setContentsMargins(0,0,0,0)
        
        
        self.home_tab = QWidget()
        self.credentails_tab = QWidget()
        self.configuration_tab = QWidget()
        self.activation_tab = QWidget()
        self.templates_macros_tab = QWidget()

        self.home_tab_layout = QVBoxLayout()    
        self.credentails_tab_layout = QVBoxLayout()   
        self.configuration_tab_layout = QVBoxLayout()
        self.activation_tab_layout = QVBoxLayout()
        self.templates_macros_tab_layout = QVBoxLayout()

        self.home_tab.setLayout(self.home_tab_layout)
        self.credentails_tab.setLayout(self.credentails_tab_layout)
        self.activation_tab.setLayout(self.activation_tab_layout)
        self.configuration_tab.setLayout(self.configuration_tab_layout)
        self.templates_macros_tab.setLayout(self.templates_macros_tab_layout)

        self.home_tab_label = QLabel()
        self.credentails_tab_label = QLabel()
        self.configuration_tab_label = QLabel()
        self.activation_tab_label = QLabel()
        self.templates_macros_tab_label = QLabel()

 
        self.home_tab_layout.addWidget(self.home_tab_label)
        self.credentails_tab_layout.addWidget(self.credentails_tab_label)
        self.configuration_tab_layout.addWidget(self.templates_macros_tab_label)
        self.activation_tab_layout.addWidget(self.configuration_tab_label)




        self.toolbar = QToolBar("Toolbar")
        self.addToolBar(self.toolbar) 
        self.toolbar.setContentsMargins(0,0,0,0)
        self.setCentralWidget(self.tab_container)
        self.button_action = QAction("Launch New Instance ???", self)
        self.button_action.setStatusTip("Launch New Instance Button")
        self.toolbar.setMovable(False)
        self.button_action.triggered.connect(self.onClickLaunchNewInstanceButton)
        self.toolbar.addAction(self.button_action)


        # Add tabs 
        self.tab_container.addTab(self.activation_tab,"Activation")     
 
          
        # self.center()
        self.show() 
        self.prepareActivationTab()
        # self.tab_container.setCurrentIndex(3)
    
    def manageVisibleTabs(self):
        self.tab_container.removeTab(0)
        self.tab_container.addTab(self.home_tab,"Home")
        self.tab_container.addTab(self.credentails_tab,"Credentials")
        self.tab_container.addTab(self.templates_macros_tab,"Templates / Macros")     
        self.tab_container.addTab(self.configuration_tab,"Configuration")     
        self.prepareHomeTab()
        self.prepareConfigurationTab()
        self.prepareCredentialsTab()
        self.prepareTemplatesMacrosTabe()
    

    def updateNewInstanceButtonText(self,val):
        val = str(val)
        self.button_action.setText(val)


    def onClickLaunchNewInstanceButton(self):
        file_path = os.path.abspath(__file__)
        file_path = os.path.join(os.getcwd(),"dist","QuickSMS.exe") 
        if not os.path.exists(file_path):
            file_path = os.path.join(os.getcwd(),"QuickSMS.exe") 
             
        
        self.newInstanceWorker = launchNewInstanceThread(file_path)
        self.newInstanceWorker.start()
        # self.newInstanceWorker.finished.connect(self.threadFinishedSlot)
        self.newInstanceWorker.log_input_box_component.connect(self.updateNewInstanceButtonText)
    
        
      
    def showWarningBox(self,text,title='Error'):
        QMessageBox.about(self, title,str(text))
        
    def onHomeTabServiceComboBoxChange(self, value):
        self.home_tab_request_mode_dropdown.clear()
        api_service_configuration = configHandler().getServiceConfiguration(service=value)
        api_service_configuration = eval(str(api_service_configuration))
        
        self.home_tab_request_mode_dropdown.addItem("Singleton")
        if api_service_configuration['allow_bulk'] in [True,"True"] : 
            self.home_tab_request_mode_dropdown.addItem("Bulk")
            
        
        
        
        self.home_tab_available_service_credentials_dropdown.clear()    
        available_credentials = configHandler().getServiceCredentialsList(service=value)      
        for credentials in available_credentials:
            self.home_tab_available_service_credentials_dropdown.addItem(str(credentials))
       

         
    


    def onClickContactListImportButton(self):
        file_name = QFileDialog.getOpenFileNames(self, "Select File", "", "*.txt")
        if file_name[0]:
            file_name = file_name[0][0]
            print("file_name = ",file_name)
            self.longRunningContactFileReaderTask(file_name) 




    def onClickMessageBodyLoadButton(self):
        self.home_page_import_message_input_box
        file_name = QFileDialog.getOpenFileNames(self, "Select File", "", "*.txt")
        if file_name[0]:
            file_name = file_name[0][0]
            try:
                with open(file_name,'r',encoding="utf-8") as file:
                    message_body = file.read()
                    self.home_page_import_message_input_box.setText(message_body)
            except UnicodeDecodeError:
                self.showWarningBox("Can't read text file due to UnicodeDecodeError")
                
                
                
    def onHomeTabImportTemplateComboBoxChange(self,value):
        if value!='Choose Template':
            self.home_page_import_message_input_box.setText(str(configHandler().getTemplatesBody(key=value)))
            
            
            
    def loadTemplatesIntoDropdownList(self):
        self.home_page_import_template_dropdown.clear()
        self.home_page_import_template_dropdown.addItems(["Choose Template"]+configHandler().getAvailableTemplates())
       
    
    def onClickCheckBalanceButton(self):
        service = self.home_tab_available_service_dropdown.currentText()
        credentials = self.home_tab_available_service_credentials_dropdown.currentText()
        try:
            eval(str(credentials))
        except :
            return self.showWarningBox(text="Credentials not selected !")
        self.home_page_balance_check_btn.setText("Checking ... ")
        print(service, " - ",credentials) 
        
        self.remaining_balance_worker = remainingBalanceThread(service=service,credentials=credentials)
        self.remaining_balance_worker.start()
        # self.remaining_balance_worker.finished.connect(self.threadFinishedSlot)
        self.remaining_balance_worker.balance_request_status.connect(self.displayRemainingBalance)
        
    
    def displayRemainingBalance(self, val):
        service = self.home_tab_available_service_dropdown.currentText().capitalize()
        print(f"-> {val}")
        self.home_page_balance_check_btn.setText("Check Balance")
        return self.showWarningBox(title="Message", text=f"{service} Cuurent Balance = {val}")
        
       
                
    def prepareHomeTab(self):
        pass
        # self.tab_container.setCurrentIndex(0)
        self.home_tab_layout.setAlignment(Qt.AlignTop)
        self.home_main_frame = QGroupBox("Main Panel")
        self.home_main_frame_layout = QVBoxLayout() 
        self.home_main_frame.setLayout(self.home_main_frame_layout)
        self.home_main_frame.setAlignment(Qt.AlignTop)
        # Horizontal bar for comboxes
        self.home_tab_request_mode_dropdown = QComboBox()
        self.home_page_service_selection_panel = QGroupBox("Select Credentials")
        self.home_page_service_selection_panel_layout = QHBoxLayout()
        self.home_page_service_selection_panel_layout.setAlignment(Qt.AlignTop)
        self.home_page_service_selection_panel.setLayout(self.home_page_service_selection_panel_layout)
        self.home_page_service_selection_panel.setFixedHeight(70) 
        self.home_tab_available_service_credentials_dropdown = QComboBox()   
        self.home_tab_available_service_dropdown = QComboBox()
        self.home_tab_available_service_dropdown.currentTextChanged.connect(self.onHomeTabServiceComboBoxChange)
        self.availavle_services_list = configHandler().getAllServices()
        for service in self.availavle_services_list:
            self.home_tab_available_service_dropdown.addItem(str(service))

        

        self.home_page_service_selection_panel_layout.addWidget(self.home_tab_available_service_dropdown,1)  
        
        

        
        
        
        
        currentTime = QDateTime.currentDateTime()
        self.home_page_timer_input_box = QDateTimeEdit()
        self.home_page_timer_input_box.setDateTime(currentTime) 
        self.home_page_message_title = QLineEdit()
        self.home_page_message_title.setPlaceholderText("Sender ID")
        
        
        self.home_page_balance_check_btn = QPushButton()
        self.home_page_balance_check_btn.setText("Check Balance")
        self.home_page_balance_check_btn.clicked.connect(self.onClickCheckBalanceButton) 
        
        
        
        self.home_page_service_selection_panel_layout.addWidget(self.home_tab_available_service_credentials_dropdown,5)
        self.home_page_service_selection_panel_layout.addWidget(self.home_tab_request_mode_dropdown,1)  
        self.home_page_service_selection_panel_layout.addWidget(self.home_page_timer_input_box,1)
        self.home_page_service_selection_panel_layout.addWidget(self.home_page_message_title,1)
        self.home_page_service_selection_panel_layout.addWidget(self.home_page_balance_check_btn,1)
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
        self.home_page_import_message_panel_buttons_panel = QGroupBox()
        self.home_page_import_message_panel_buttons_panel.setAlignment(Qt.AlignTop)
        self.home_page_import_message_panel_buttons_layout = QHBoxLayout() 
        self.home_page_import_message_panel_buttons_panel.setLayout(self.home_page_import_message_panel_buttons_layout)
        self.home_page_import_message_btn = QPushButton("Load Message File") 
        self.home_page_import_template_dropdown = QComboBox() 
        self.loadTemplatesIntoDropdownList() 
        self.home_page_import_template_dropdown.currentTextChanged.connect(self.onHomeTabImportTemplateComboBoxChange) 
        self.home_page_import_message_panel_buttons_layout.addWidget(self.home_page_import_message_btn,1)
        self.home_page_import_message_panel_buttons_layout.addWidget(self.home_page_import_template_dropdown,1)
        self.home_page_import_message_btn.clicked.connect(self.onClickMessageBodyLoadButton)  
        self.home_page_import_message_panel_layout.addWidget(self.home_page_import_message_panel_buttons_panel,1)  
        self.home_page_import_message_panel_layout.addStretch()
        self.home_page_data_import_panel_layout.addWidget(self.home_page_import_receivers_panel,1)
        self.home_page_data_import_panel_layout.addWidget(self.home_page_import_message_panel,1) 
        self.home_main_frame_layout.addWidget(self.home_page_data_import_panel,1)
        self.home_main_frame_start_btn  = QPushButton("Start sending Messages")
        self.changeStartSendingMessagesButtonStatus()
        self.home_main_frame_start_btn.clicked.connect(self.onClickStartButton)
        self.home_main_frame_layout.addWidget(self.home_main_frame_start_btn,1)
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
        
    def changeStartSendingMessagesButtonStatus(self,stop=False):
        if not stop:
            # start
            self.IS_STOP_FUNCTIONALITY_ALLOWED = False
            self.home_main_frame_start_btn.setText("Start sending Messages")
            self.home_main_frame_start_btn.setStyleSheet("background-color: ")
        else:
            self.IS_STOP_FUNCTIONALITY_ALLOWED = True
            self.home_main_frame_start_btn.setText("Stop SMS Sender")
            self.home_main_frame_start_btn.setStyleSheet("background-color: red")
            
            
        
        
        pass
    
    
    
    def longRunningTask(self,service,credentials,request_mode,message_title,contact_list,message_body,timer_difference):     
        self.appedLogInoutBoxText(str("Starting Main Thread / Parent Thread ..."))
        self.worker = workerThread(service,credentials,request_mode,message_title,contact_list,message_body,timer_difference)
        self.worker.start()
        self.worker.finished.connect(self.threadFinishedSlot)
        self.worker.log_input_box_component.connect(self.logUpdateSlot)
     
    
     
    def longRunningContactFileReaderTask(self,file_name):      
        self.file_reader_worker = contactFileReaderThreadClass(file_name)
        self.file_reader_worker.start()
        # self.file_reader_worker.finished.connect(self.threadFinishedSlot)
        self.file_reader_worker.file_reader_signal_slot.connect(self.fileReaderResponseSlot)
     
    def fileReaderResponseSlot(self,val):  
        is_error = "error" in str(val).lower()
        if is_error:
            return self.showWarningBox("Can't read text file due to UnicodeDecodeError") 
        else:
            contacts = val
            self.home_page_import_receivers_input_box.setText(contacts)
            
            
            
     
    def appedLogInoutBoxText(self,val):
        self.home_page_log_input_box.textCursor().insertText(str(val)+'\n')
        self.home_page_log_input_box.verticalScrollBar().setValue(self.home_page_log_input_box.verticalScrollBar().maximum())
        
    def logUpdateSlot(self,val):  
        val = str(val)
        if val == "ENABLE_STOP_BUTTON":
            self.changeStartSendingMessagesButtonStatus(stop=True)
            return
        if val == "DISABLE_STOP_BUTTON":
            self.changeStartSendingMessagesButtonStatus(stop=False)
            return
        
        
        
        
        if 'Message sent to' in str(val):
            self.messages_sent_index = self.messages_sent_index + 1
            self.messages_sent_index 
            val = f"{self.messages_sent_index}/{self.total_numbers_in_contact_list}" + str(val)
        self.appedLogInoutBoxText(str(val)) 
        # print("signal - update - ", val)
        
        
    def threadFinishedSlot(self): 
        log_plain_text = str(self.home_page_log_input_box.toPlainText())  
        total_messages_sent = sum([int(str(x).split("=")[-1].strip()) for x in log_plain_text.split('\n') if  "Message Sent For Current Request Session" in  str(x)] )
        self.appedLogInoutBoxText(str("-"*50))
        self.appedLogInoutBoxText(f"\nTotal messages sent =  {total_messages_sent}")
        self.showWarningBox(text=f"Total messages sent = {total_messages_sent}", title="Total Messages Sent")
    
    def onClickStartButton(self): 
        # Checking if Stop is enabled
        if self.IS_STOP_FUNCTIONALITY_ALLOWED:
            # write shared memory data
            print("-> STOP ALLOWED")
            print("-> Write Shared Memory Data")
            sharedMemory.stop_btn_pressed = True
            return 
        else:
            print("-> STOP NOT ALLOWED")
            sharedMemory.stop_btn_pressed = False
            
        
        
        
        
        service = str(self.home_tab_available_service_dropdown.currentText())
        
        # # Start - set dummy data
        # contact_list = ['447748347521',"923167815639","923476026649","923167815639","923167815639",][2:]
        # contact_list = ['447777347521',"447748347577"][:]
        # contact_list = [str(x) for x in contact_list]
        # self.home_page_message_title.setText("Stock Msg")
        # self.home_page_import_receivers_input_box.setText("\n".join(contact_list)) 
        # self.home_page_import_message_input_box.setText("Test") 
        # # END - set dummy data
        

        credentials = self.home_tab_available_service_credentials_dropdown.currentText()
        try:
            eval(str(credentials))
        except :
            return self.showWarningBox(text="Credentials not selected !")
        credentials = eval(credentials)
        message_title = str(self.home_page_message_title.text())
        contact_list = str(self.home_page_import_receivers_input_box.toPlainText())
        message_body = str(self.home_page_import_message_input_box.toPlainText()) 
        self.total_numbers_in_contact_list = len(contact_list) 
        self.messages_sent_index = 0
        
        if not message_title or  message_title.isspace():
            self.showWarningBox("Please enter a Message Title (Sender ID)")
            return
    
        elif not contact_list or contact_list.isspace():
            self.showWarningBox("Please enter valid Contacts / Receivers' phone number list")
            return
        
        contact_list = contact_list.replace("\n",',').split(",")
        contact_list = ["".join([y for y in str(x) if str(y).isnumeric()])  for x in contact_list ]
        if not message_body or message_body.isspace():
            self.showWarningBox("Please enter Message body to be sent")
            return
        
        self.total_numbers_in_contact_list = len(contact_list) 
        self.messages_sent_index = 0
        
        timer_value = self.home_page_timer_input_box.dateTime().toPyDateTime().replace(second=0, microsecond=0)
        current_time = datetime.today().replace(second=0, microsecond=0)
        timer_difference = 0
        if current_time >  timer_value:
            self.showWarningBox("Timer value cannot be less that current time of your machine")
            return
        else: 
            timer_difference = (timer_value - current_time).total_seconds()
            if timer_difference>0:
                self.showWarningBox(f"Quick SMS would start sending messages after {int(timer_difference/60)} minutes")
            # time.sleep(difference) 
            print(f"-> Waiting for {timer_difference} seconds")
        
        
        
        
        request_mode = self.home_tab_request_mode_dropdown.currentText()
        
        credentials = str(credentials).replace("\'", "\"")
        credentials = json.loads(credentials) 
        self.home_page_log_input_box.setText("")
        self.appedLogInoutBoxText(str("-"*50))
        self.appedLogInoutBoxText(str(f"Service = {service}",  ))
        self.appedLogInoutBoxText(str(f"Credentials = {credentials}",  ))
        self.appedLogInoutBoxText(str(f"Sederer ID / Message Title = {message_title}",  ))
        self.appedLogInoutBoxText(str(f"Message Body = {message_body}",  ))
        self.appedLogInoutBoxText(str(f"Receiver Phone number list = {contact_list}",  ))
        self.appedLogInoutBoxText(str("-"*50))
        self.appedLogInoutBoxText(str("SMS Sender is inintiating ..."))
        self.longRunningTask(service,credentials,request_mode,message_title,contact_list,message_body,timer_difference)
         
    
        
    def onClickAddNewCredentialsButton(self):
        new_crendential_value = str(self.new_crendetials_insert_box.toPlainText())
        service = self.available_service_dropdown.currentText()
        try:
            new_crendential_value = eval(new_crendential_value)
            res = configHandler().addServiceCredentials(service=service,creds=new_crendential_value)
            if type(res) is dict:
                self.showWarningBox(text=f"Wrong credentials Layout.\nMake sure credentials have layout like follpwing\n{str(res)}")
            else:
                self.showWarningBox(text="Successfully added new credentials ",title="Message")
                self.new_crendetials_insert_box.setPlainText("")
        except:
            self.showWarningBox(text="Invalid JSON struture for new Credentials")
        
        try:self.populateDataTable()
        except:pass
        
    def onClickAddNewTemplateMacroButton(self): 
        key = self.getTemplateMacrosTableKey()
        title = str(self.template_vs_macro_title_insert_box.toPlainText())
        if not title or title.isspace():
            self.showWarningBox(text=f"{key.capitalize()} Title / Short Name cannot be empty ! ")
            return
        
        body = str(self.template_vs_macro_body_insert_box.toPlainText())
        try:
            if key=="macros" :
                body = str(body).split(",")
                if type(body) is list and len(body)<1:
                    self.showWarningBox(text=f"Body values cannot be  empty ")
                    return 
                    
            
        except:
            self.showWarningBox(text=f"{key.capitalize()} Body has invalid layout  ")
            return
        value = {
            title:body
        }
        res = configHandler().addNewTemplateMacro(key=key,value=value)
        if  res=='duplicate':
            return self.showWarningBox(text=f"{key.capitalize()} has already a record with this title {title}   ")
        self.loadTemplatesIntoDropdownList()
        self.populateDataTable(key=key) 
        self.template_vs_macro_title_insert_box.setPlainText("")
        self.template_vs_macro_body_insert_box.setPlainText("")
    
        
        
    
 
    def populateDataTable(self,key='credentials',cols=[],row=[]): 
        self.target_table = None
        self.delete_function = None
        column_names = []
        table_data = []
        self.target_table = self.credentials_table_widget
        if key=='credentials':
            self.target_table = self.credentials_table_widget
            self.delete_function = self.deleteCredentialsRecord
            column_names = ["Credentials","Operation"]
            table_data = configHandler().getServiceCredentialsList(service=self.available_service_dropdown.currentText())
        elif key=='templates':
            self.target_table = self.template_macro_table_widget
            self.delete_function = self.deleteTemplateMacroRecord
            column_names = ["Templates","Operation"]
            table_data = configHandler().getTemplateMacroList(self.getTemplateMacrosTableKey())
            
            
        elif key=='macros':
            self.target_table = self.template_macro_table_widget
            column_names = ["Macros","Operation"]
            self.delete_function = self.deleteTemplateMacroRecord
            table_data = configHandler().getTemplateMacroList(self.getTemplateMacrosTableKey())
        
        
        # print(table_data)
        self.rows = len(table_data)
        self.target_table.setRowCount(self.rows)
        self.target_table.setColumnCount(2)
        self.target_table.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.target_table.horizontalHeader().setSectionResizeMode(1,QHeaderView.ResizeToContents)
        for column_index,column in enumerate(column_names):
            self.target_table.setHorizontalHeaderItem(column_index,QTableWidgetItem(column)) 
        self.target_table.setEditTriggers(QTableWidget.NoEditTriggers) 
        for x in range(self.rows):  
            self.target_table.setItem(x,0, QTableWidgetItem(  str(table_data[x]) )) 
            btn = QPushButton(self.target_table)
            btn.setText(f'Delete - {key} - {x+1}')
            btn.clicked.connect(self.delete_function)
            self.target_table.setCellWidget(x,1, btn)  
    
    
         
    def deleteTemplateMacroRecord(self):
        record_index = int(str(self.sender().text()).split(" - ")[-1])-1 
        key = self.getTemplateMacrosTableKey()
        self.populateDataTable()
        configHandler().deleteTemplateMacroRecord( key=key,index= record_index) 
        self.populateDataTable(key)
         
    
        
    def deleteCredentialsRecord(self):
        service=self.available_service_dropdown.currentText()
        record_index = int(str(self.sender().text()).split(" - ")[-1])-1
        print (f"-> Deleting credentials for {service} with index {record_index}")
        configHandler().removeServiceCredentials(service=service,credential_index=int(record_index))
        self.populateDataTable()
        
    
    def onChangeAvailableService(self,value):
        
        credential_prototype = configHandler().getCredentialsPrototype(service=value)
        credential_prototype = json.dumps(credential_prototype)
        self.new_crendetials_insert_box.setPlainText(credential_prototype)
        # print(value)
        # print(credential_prototype)
        
        
        try:
            self.populateDataTable()
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
        self.new_crendetials_insert_box = QPlainTextEdit()
        self.available_service_dropdown = QComboBox()
        self.available_service_dropdown.currentTextChanged.connect(self.onChangeAvailableService)  
        for service in self.availavle_services_list:
            self.available_service_dropdown.addItem(str(service))
        self.service_credentials_insertion_panel_layout.addWidget(self.available_service_dropdown,1)
        self.new_crendetials_insert_box.setFixedHeight(80)
        self.new_crendetials_save_btn = QPushButton("Add new Credentials")
        self.new_crendetials_save_btn.setFont(QFont('Times', 9))
        self.new_crendetials_save_btn.clicked.connect(self.onClickAddNewCredentialsButton)
        self.service_credentials_insertion_panel_layout.addWidget(self.new_crendetials_insert_box,1)
        self.service_credentials_insertion_panel_layout.addWidget(self.new_crendetials_save_btn,1)
        self.credentails_main_frame_layout.addWidget(self.service_credentials_insertion_panel,3) 
        self.credentails_main_frame.setLayout(self.credentails_main_frame_layout)
        self.credentails_main_frame.setAlignment(Qt.AlignTop)
        self.credentails_tab_layout.addWidget(self.credentails_main_frame,1) 
        self.credentails_listing_table = QGroupBox("Credentials Listing")
        self.credentails_listing_table_layout = QHBoxLayout()  
        self.credentails_listing_table.setLayout(self.credentails_listing_table_layout)
        self.credentials_table_widget = QTableWidget()
        self.populateDataTable() 
        self.credentails_listing_table_layout.addWidget(self.credentials_table_widget)  
        self.credentails_tab_layout.addWidget(self.credentails_listing_table,12)  
        self.credentails_tab_layout.addStretch()


    def getTemplateMacrosdDropdownText(self):
        return self.template_vs_macros_dropdown.currentText()
    def getTemplateMacrosTableKey(self):
        current_text = str(self.template_vs_macros_dropdown.currentText())
        key = "templates" if current_text == 'Templates' else "macros"
        return key
    
    def onChangeTemplateMacrosDropdown(self):
        current_text = str(self.template_vs_macros_dropdown.currentText()) 
        self.template_vs_macro_title_insert_box.setPlaceholderText(f"Insert Title / Key / Short Name for {self.getTemplateMacrosdDropdownText()}")
        self.template_vs_macro_body_insert_box.setPlaceholderText(f"Insert Body / Message for {self.getTemplateMacrosdDropdownText()}")
        self.templates_macros_listing_table.setTitle ( f"{self.getTemplateMacrosdDropdownText()} Listing")
        self.new_templates_macros_save_btn.setText(f"Add new {self.getTemplateMacrosdDropdownText()}")
        self.templates_macros_listing_table_layout = QHBoxLayout()  
        self.populateDataTable(key = self.getTemplateMacrosTableKey())
  
    
    
    def prepareTemplatesMacrosTabe(self):
        self.templates_macros_tab_layout.setAlignment(Qt.AlignTop)
        self.templates_macros_main_frame = QGroupBox("Manage Templates / Macros")
        self.templates_macros_main_frame_layout = QHBoxLayout()
        self.templates_macros_main_frame.setFixedHeight(250)  
        # LEFT panel - New credentials Insertion panel
        self.templates_macros_insertion_panel = QGroupBox("Add Templates / Macros")
        self.templates_macros_insertion_panel_layout = QVBoxLayout()
        self.templates_macros_insertion_panel_layout.setAlignment(Qt.AlignTop)
        self.templates_macros_insertion_panel.setLayout(self.templates_macros_insertion_panel_layout)
        self.template_vs_macros_dropdown = QComboBox()
        self.template_vs_macros_dropdown.addItem("Templates")
        self.template_vs_macros_dropdown.addItem("Macros")
        self.template_vs_macros_dropdown.currentTextChanged.connect(self.onChangeTemplateMacrosDropdown)  
        self.templates_macros_insertion_panel_layout.addWidget(self.template_vs_macros_dropdown,1)
        self.template_vs_macro_title_insert_box = QPlainTextEdit() 
        self.template_vs_macro_title_insert_box.setPlaceholderText(f"Insert Title / Key / Short Name for {self.getTemplateMacrosdDropdownText()}")
        self.template_vs_macro_body_insert_box = QPlainTextEdit()
        self.template_vs_macro_body_insert_box.setPlaceholderText(f"Insert Body / Message for {self.getTemplateMacrosdDropdownText()}")
        # self.template_vs_macro_body_insert_box.setFixedHeight(80)
        self.templates_macros_title_body_insertion_panel = QLabel()
        self.templates_macros_title_body_insertion_panel_layout = QHBoxLayout()
        self.templates_macros_title_body_insertion_panel_layout.setAlignment(Qt.AlignTop)
        self.templates_macros_title_body_insertion_panel_layout.setContentsMargins(0,0,0,0)
        self.templates_macros_title_body_insertion_panel.setLayout(self.templates_macros_title_body_insertion_panel_layout)
        self.templates_macros_title_body_insertion_panel_layout.addWidget(self.template_vs_macro_title_insert_box,1)
        self.templates_macros_title_body_insertion_panel_layout.addWidget(self.template_vs_macro_body_insert_box,3) 
        self.templates_macros_insertion_panel_layout.addWidget(self.templates_macros_title_body_insertion_panel,1) 
        self.new_templates_macros_save_btn = QPushButton(f"Add new {self.getTemplateMacrosdDropdownText()}")
        self.new_templates_macros_save_btn.setFont(QFont('Times', 9))
        # self.new_crendetials_save_btn.clicked.connect(self.onClickAddNewCredentialsButton)
        self.new_templates_macros_save_btn.clicked.connect(self.onClickAddNewTemplateMacroButton)
        # self.templates_macros_insertion_panel_layout.addWidget(self.new_crendetials_insert_box,1)
        self.templates_macros_insertion_panel_layout.addWidget(self.new_templates_macros_save_btn,1)
        
        self.templates_macros_main_frame_layout.addWidget(self.templates_macros_insertion_panel,3)
        self.templates_macros_main_frame.setLayout(self.templates_macros_main_frame_layout)
        self.templates_macros_main_frame.setAlignment(Qt.AlignTop)
        self.templates_macros_tab_layout.addWidget(self.templates_macros_main_frame,1) 
        self.templates_macros_listing_table = QGroupBox(f"{self.getTemplateMacrosdDropdownText()} Listing")
        self.templates_macros_listing_table_layout = QHBoxLayout()  
        self.templates_macros_listing_table.setLayout(self.templates_macros_listing_table_layout)
        
        self.template_macro_table_widget = QTableWidget()
        self.populateDataTable(key="templates") 
        self.templates_macros_listing_table_layout.addWidget(self.template_macro_table_widget)  
        self.templates_macros_tab_layout.addWidget(self.templates_macros_listing_table,12)  
        self.templates_macros_tab_layout.addStretch()

    def save_configuration_thread_threshold(self):
        number = self.configuration_thread_input.text()
        try:
            number = int(number)
            if number < 1:
                self.showWarningBox("Threads / sec must be greater than Zero (0)")
            else:
                configHandler().setThreadsThreshold(number)
                self.showWarningBox("Thread threshold updated")
        except Exception:
            self.showWarningBox("Threads / sec can only be a number") 
        pass
        
    def prepareConfigurationTab(self):
        self.configuration_tab_layout.setAlignment(Qt.AlignTop)
        self.configuration_frame = QGroupBox("Set Threads / sec")
        self.group_box_layout = QHBoxLayout()
        self.configuration_save_btn = QPushButton("Save",)
        self.configuration_save_btn.clicked.connect(self.save_configuration_thread_threshold)
        self.configuration_thread_input = QLineEdit()
        self.configuration_thread_input.setText(str(configHandler().getThreadsThreshold()))
        self.group_box_layout.addWidget(self.configuration_thread_input,11)
        self.group_box_layout.addWidget(self.configuration_save_btn,1)
        self.configuration_frame.setLayout(self.group_box_layout)
        self.configuration_frame.setAlignment(Qt.AlignTop) 
        
 
        self.configuration_frame.setAlignment(Qt.AlignTop) 
        self.configuration_tab_request_load_waitpanel = QGroupBox("Manage Request Load / Wait")
        self.configuration_tab_request_load_waitpanel_layout = QVBoxLayout()
        self.configuration_tab_request_load_waitpanel_layout.setAlignment(Qt.AlignTop)
        self.configuration_tab_request_load_waitpanel.setLayout(self.configuration_tab_request_load_waitpanel_layout)
        self.configuration_tab_available_service_dropdown = QComboBox()
        

        
        
        
        for service in self.availavle_services_list:
            self.configuration_tab_available_service_dropdown.addItem(str(service))  
        self.request_load_insert_box = QLineEdit() 
        self.request_load_insert_box.setPlaceholderText(f"Set Messages per Request")
        self.configuration_tab_available_service_dropdown.currentTextChanged.connect(self.onConfigurationTabAvailableServiveChange)
        self.request_interval_wait_insert_box = QLineEdit()
        self.request_interval_wait_insert_box.setPlaceholderText(f"Set wait between Requests")
        self.configuration_tab_request_load_wait_panel = QLabel()
        self.configuration_tab_request_load_wait_panel_layout = QHBoxLayout()
        self.configuration_tab_request_load_wait_panel_layout.setAlignment(Qt.AlignTop)
        self.configuration_tab_request_load_wait_panel_layout.setContentsMargins(0,0,0,0)
        self.configuration_tab_request_load_wait_panel.setLayout(self.configuration_tab_request_load_wait_panel_layout)
        self.configuration_tab_request_load_wait_panel_layout.addWidget(self.configuration_tab_available_service_dropdown,2)
        self.configuration_tab_request_load_wait_panel_layout.addWidget(self.request_load_insert_box,3)
        self.configuration_tab_request_load_wait_panel_layout.addWidget(self.request_interval_wait_insert_box,3) 
        self.configuration_tab_request_load_waitpanel_layout.addWidget(self.configuration_tab_request_load_wait_panel,5)   
        self.new_configuration_tab_request_load_wait_save_btn = QPushButton(f"Save") 
        self.new_configuration_tab_request_load_wait_save_btn.clicked.connect(self.onClickSaveRequestLoadWaitButton) 
        self.configuration_tab_request_load_wait_panel_layout.addWidget(self.new_configuration_tab_request_load_wait_save_btn,1)  
        self.configuration_tab_layout.addWidget(self.configuration_frame)  
        self.configuration_tab_layout.addWidget(self.configuration_tab_request_load_waitpanel)  
        
        selected_service = self.configuration_tab_available_service_dropdown.currentText()
        selected_service_configuration = configHandler().getServiceConfiguration(selected_service) 
        self.request_load_insert_box.setText(str(selected_service_configuration['request_load']))
        self.request_interval_wait_insert_box.setText(str(selected_service_configuration['request_interval_wait']))
        
     
     
     
    def onConfigurationTabAvailableServiveChange(self):
        selected_service = self.configuration_tab_available_service_dropdown.currentText()
        selected_service_configuration = configHandler().getServiceConfiguration(selected_service)
        self.request_load_insert_box.setText(str(selected_service_configuration['request_load']))
        self.request_interval_wait_insert_box.setText(str(selected_service_configuration['request_interval_wait']))
        

    def onClickSaveRequestLoadWaitButton(self):
        load = str(self.request_load_insert_box.text())
        wait = str(self.request_interval_wait_insert_box.text())
        service = self.configuration_tab_available_service_dropdown.currentText()
        try:
            load = int(load)
            wait = int(wait)
            if load<1:
                return self.showWarningBox(text="Request Load can't be less than 1 ")     
            else:
                configHandler().setServiceConfiguration(service,load,wait)
                return self.showWarningBox(title="Message", text="Configuration Saved", )
 
        except:
            return self.showWarningBox(text="Request Load and Request Wait must be number ")
        






    def prepareActivationTab(self):
        self.activation_tab_layout.setAlignment(Qt.AlignTop)
        self.activation_frame = QGroupBox("Product Key")
        self.group_box_layout = QHBoxLayout()
        self.activation_save_btn = QPushButton("Verify",)
        self.activation_save_btn.clicked.connect(self.verifyProductKeyFromServer)
        self.activation_key_input = QLineEdit()
        self.activation_key_input.setText(configHandler().getProductKey())
        # self.activation_thread_input.setText(str(configHandler().getThreadsThreshold()))
        self.group_box_layout.addWidget(self.activation_key_input,11)
        self.group_box_layout.addWidget(self.activation_save_btn,1)
        self.activation_frame.setLayout(self.group_box_layout)
        self.activation_frame.setAlignment(Qt.AlignTop)
        self.activation_tab_request_status = QLabel("")
        self.activation_tab_layout.addWidget(self.activation_frame) 
        self.activation_tab_layout.addWidget(self.activation_tab_request_status)  
 
        ## Auto - Activation Checking  
        print("getArgumentValue")
        if getArgumentValue("--ask_product_key=") in ['True', True, None]: 
            if  len(configHandler().getProductKey()) >10 :
                print("Auto connecting to server for key validation ... ")
                self.activation_save_btn.setEnabled(False)
                self.verifyProductKeyFromServer() 
        else:
            self.manageVisibleTabs()
        
        


    def verifyProductKeyFromServer(self):
        configHandler().setMachineId()
        machine_id = configHandler().getMachineId()
        key = str(self.activation_key_input.text())
        # print(key)
        if not key or str(key).isspace():
            self.showWarningBox("Product key can't be empty")
            return 
        self.activation_tab_request_status.setText("Status: Verifying Product Key from server ... ")
        self.activation_worker = serverThread(key,machine_id)
        self.activation_worker.start()
        # self.worker.finished.connect(self.activationKeyServerFinishedSlot)
        self.activation_worker.activation_request_status.connect(self.activationKeyServerResponseSlot)
 


 
     
  
    def activationKeyServerResponseSlot(self,val):  
        self.activation_save_btn.setEnabled(True)
        key = str(self.activation_key_input.text())
        self.activation_tab_request_status.setText("")
        val = eval(val)
        if val['is_valid'] is False:
            return self.showWarningBox(title="Server Response",text=f"Product key {key} is Invalid")
            
        elif val['used'] is True:
            return self.showWarningBox(title="Server Response",text=f"Product key {key} is already being used on another machine")
        
        elif val['allowed'] is False:
            return self.showWarningBox(title="Server Response",text=f"Product key {key} has been deactivated by Server Admin")
  
        elif val['is_valid'] is True and val['used'] is False and val['allowed'] is True :
            # self.showWarningBox(title="Server Response",text="Software Activated :) ")
            configHandler().setproductKey(new_key=key)
            self.manageVisibleTabs() 
            return 
            
        
    def activationKeyServerFinishedSlot(self,val):  
        pass  

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