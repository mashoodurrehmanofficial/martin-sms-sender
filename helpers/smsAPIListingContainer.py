import requests ,os,sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


try:
    from apis._1s2uApiSMSGateway import * 
    from apis.bsgWorldApiSMSGateway import * 
    from apis.bulkgateApiSMSGateway import * 
    from apis.burstsmsApiSMSGateway import * 
    from apis.clickSendApiSMSGateway import * 
    from apis.cmTextApiSMSGateway import * 
    from apis.d7networksApiSMSGateway import * 
    from apis.infobipApiSMSGateway import * 
    from apis.messageBirdApiSMSGateway import * 
    from apis.octopushApiSMSGateway import * 
    from apis.plivoApiSMSGateway import * 
    from apis.sinchApiSMSGateway import * 
    from apis.smsbroadcastApiSMSGateway import * 
    from apis.smsupApiSMSGateway import * 
    from apis.spryngApiSMSGateway import * 
    from apis.telnyxApiSMSGateway import * 
    from apis.textmagicApiSMSGateway import * 
    from apis.twilioApiSMSGateway import * 
    from apis.tyntecApiSMSGateway import * 
    from apis.vonagecApiSMSGateway import * 
    from apis.voodoosmsApiSMSGateway import *  
except: 
    from ..apis._1s2uApiSMSGateway import * 
    from ..apis.bsgWorldApiSMSGateway import * 
    from ..apis.bulkgateApiSMSGateway import * 
    from ..apis.burstsmsApiSMSGateway import * 
    from ..apis.clickSendApiSMSGateway import * 
    from ..apis.cmTextApiSMSGateway import * 
    from ..apis.d7networksApiSMSGateway import * 
    from ..apis.infobipApiSMSGateway import * 
    from ..apis.messageBirdApiSMSGateway import * 
    from ..apis.octopushApiSMSGateway import * 
    from ..apis.plivoApiSMSGateway import * 
    from ..apis.sinchApiSMSGateway import * 
    from ..apis.smsbroadcastApiSMSGateway import * 
    from ..apis.smsupApiSMSGateway import * 
    from ..apis.spryngApiSMSGateway import * 
    from ..apis.telnyxApiSMSGateway import * 
    from ..apis.textmagicApiSMSGateway import * 
    from ..apis.twilioApiSMSGateway import * 
    from ..apis.tyntecApiSMSGateway import * 
    from ..apis.vonagecApiSMSGateway import * 
    from ..apis.voodoosmsApiSMSGateway import *  
    
    
    
SERVICE_API_MAPPING = { 
    "clicksend"     : {"singleton": clickSendApiSMSGatewaySingleton},
    "d7networks"    : {"singleton": d7networksApiSMSGatewaySingleton , "bulk": d7networksApiSMSGatewayBulk },
    "messagebird"   : {"singleton": messageBirdApiSMSGatewaySingleton , "bulk": messageBirdApiSMSGatewayBulk},
    "sinch"         : {"singleton": sinchApiSMSGatewaySingleton , "bulk": sinchApiSMSGatewayBulk},
    "telnyx"        : {"singleton": telnyxApiSMSGatewaySingleton},
    # "twilio"      : {"singleton": twilio , "bulk": },
    "cmtext"        : {"singleton": cmTextApiSMSGatewaySingleton , "bulk":cmTextApiSMSGatewayBulk},
    "smsup"         : {"singleton": smsupApiSMSGatewaySingleton , "bulk":smsupApiSMSGatewayBulk },
    # "voodoosms"   : {"singleton": voodoosmsApiSMSGateway , "bulk": },
    "textmagic"     : {"singleton":textmagicApiSMSGatewaySingleton  , "bulk":textmagicApiSMSGatewayBulk },
    "1s2u"          : {"singleton": api_1s2uApiSMSGatewaySingleton , "bulk": api_1s2uApiSMSGatewayBulk },
    "smsbroadcast"      : {"singleton":smsbroadcastApiSMSGatewaySingleton  , "bulk":smsbroadcastApiSMSGatewayBulk },
    "octopush"      : {"singleton": octopushApiSMSGatewaySingleton, "bulk":octopushApiSMSGatewayBulk},
    "bsgworld"      : {"singleton": bsgWorldApiSMSGatewaySingleton},
    "bulkgate"      : {"singleton":bulkgateApiSMSGatewaySingleton},
    "infobip"       : {"singleton":infobipApiSMSGatewaySingleton , "bulk":infobipApiSMSGatewayBulk},
    "plivo"         : {"singleton":plivoApiSMSGatewaySingleton , "bulk":plivoApiSMSGatewayBulk},
    "spryng"        : {"singleton": spryngApiSMSGatewaySingleton, "bulk":spryngApiSMSGatewayBulk},
    "burstsms"      : {"singleton": burstsmsApiSMSGatewaySingleton, "bulk":burstsmsApiSMSGatewayBulk},
    "vonage.co.uk"  : {"singleton":  vonagecApiSMSGatewaySingleton},
    "tyntec"        : {"singleton":tyntecApiSMSGatewaySingleton},
    
}   
# vonage.co.uk
# tyntec.com
