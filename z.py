from configHandlerFile import configHandler


def getMessagePrototypes(message,total_contacts):
    message_prototypes = [] 
    if '##' not in message: 
        message_prototypes.append(message)  
    else:
        # detected_macros = [x for x in message.split() if "#" in str(x) ]
        # detected_macros = [x for x in message.split() if x.startswith("##") and x.endswith("##")]
        
        
        detected_macros = [max(x.split("##"),key=len) for x in message.split() if str(x).count("#")==4]
        detected_macros = ["##"+x+"##" for x in detected_macros]
        # print("detected_macros = ",detected_macros)
        detected_macros = [x for x in detected_macros if x.replace("#","") in configHandler().getAvailableMacros()]
        iterable_macros = [x for x in detected_macros  if type(configHandler().getMacroBody(key=str(x).replace("#",""))) is list]
        non_iterable_macros = [x for x in detected_macros  if type(configHandler().getMacroBody(key=str(x).replace("#",""))) is not list]
        # print("all = ", configHandler().getAvailableMacros())
        # print("detected_macros = ",detected_macros)
        # print("iterable_macros = ",iterable_macros)
        # print("non_iterable_macros = ",non_iterable_macros)
        for non_iterable_macro in non_iterable_macros:    
            message = message.replace(non_iterable_macro,configHandler().getMacroBody(key=str(non_iterable_macro).replace("#","")))
        
        if len(iterable_macros)>0:
            temp_iterable_macros_dict = [{x: configHandler().getMacroBody(key=str(x).replace("#",""))  } for x in iterable_macros]
            iterable_macros_dict = {}
            [iterable_macros_dict.update(x) for x in temp_iterable_macros_dict]
            # print("-"*10)
            # print("iterable_macros_dict = ", iterable_macros_dict)
            
            
            max_counter = max([len(x) for x in list(iterable_macros_dict.values())]) 
            
            print("max_counter = ", max_counter)
            
            for counter in range(max_counter):
                temp_message = message 
                for iterable_macro in iterable_macros: 
                    current_macro_value = iterable_macros_dict[iterable_macro][counter%len(iterable_macros_dict[iterable_macro])]
                    # print("iterable_macro = ", iterable_macro)
                    # print("current_macro_value = ", current_macro_value)
                    temp_message = str(temp_message).replace(str(iterable_macro),str(current_macro_value))     
                    # print("temp_message = ", temp_message)
                    # print("temp_message = ", temp_message)
                print("-"*5)
                message_prototypes.append(temp_message)
                # temp_message = message
                
        else:
            message_prototypes.append(message)
            
    # print("orignal message_prototypes len = ", len(message_prototypes))
    if total_contacts>len(message_prototypes):      
        message_prototypes = message_prototypes * (total_contacts - len(message_prototypes) + 1)
    message_prototypes = message_prototypes[:total_contacts]
    return message_prototypes     




message_prototypes = getMessagePrototypes("##TestAlert##. Go to ##LINK##",10)
print(message_prototypes)