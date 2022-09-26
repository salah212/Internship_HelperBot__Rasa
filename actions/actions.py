from __future__ import absolute_import , division , print_function , unicode_literals
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker # tracker permet de rtourner les msges 
from rasa_sdk.executor import CollectingDispatcher # permer de 
from rasa_sdk.events import SlotSet # permet de garder les infos dans la memoire pour les reutiliser
from sklearn.utils import resample # permet le stockage des slots dans la memoire
import os
class ActionGiveName(Action):
    def name(self) -> Text:
       return "action_give_name"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dernier_message = tracker.latest_message
    

        # if dernier_message['entities']:
        #     for entite in dernier_message['entities']:
        #         if entite['entity'] == 'nom':
        #              nom = entite['value']
                     #print(f'************** {name}**********')

        ## deuxieme façon de recupere
        nom = next(tracker.get_latest_entity_values("nom"))
        message = f"So **{nom}**, What subject are you studying and where❓"

        dispatcher.utter_message(text=message)

        return []

class ActionSearchIntern(Action):
    def name(self) -> Text:
       return "action_search_intern"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # school = next(tracker.get_latest_entity_values("school"))
        # option = next(tracker.get_latest_entity_values("option"))
        # intern = next(tracker.get_latest_entity_values("intern"))
        dernier_message = tracker.latest_message
        if dernier_message['entities']:
            for entite in dernier_message['entities']:
                if entite['entity'] == 'school':
                     school = entite['value']
                if entite['entity'] == 'option':
                     option = entite['value']
                if entite['entity'] == 'intern':
                     intern = entite['value']
                     
        try:
            message = f"I will save your following informations :\n\rSchool :**{school}**\n\rOption :**{option}**\n\rCity :**{intern}**\n\rHow can i help you?"
        except UnboundLocalError as e:
            if 'school' in str(e):
                message = "This **school** does not exist! "
            if 'option' in str(e):
                message = "This **option** does not exist! "
            if 'intern' in str(e):
                message = f"This **city** does not exist! "
       
        dispatcher.utter_message(text=message)

        return []

class ActionStage(Action):

     def name(self) -> Text:
         return "action_stage"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        stage =""
        with open('C:\\Users\\Salaheddin\\OneDrive\\Documents\\Projets\\Rasa_chatbot\\fold\\stage.txt', 'r',encoding='UTF-8') as f:
            stage+=f.read()

        dispatcher.utter_message(text=stage) # returner les actions

        return [] 


#*********************************************************************************************


class ActionGererStage(Action): # le but de cette classe c'est de stocker les infos


     def name(self) -> Text:
         return "action_gerer_stage"

     def run(self, dispatcher: CollectingDispatcher, # dans cette cas on n'est utilier dispatcher par ce que on est just stocker les donnnés dans le slot
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        gerer_stage = Tracker.get_slot("stage")
        print("-----------------",gerer_stage)

        dispatcher.utter_message(text=gerer_stage) # returner les actions

        return [SlotSet("stage",gerer_stage)] # stocker dans la memoire



class ActionConfirmation(Action):

     def name(self) -> Text:
         return "action_confirmation"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        gerer_stage = tracker.latest_message['text']
        
        type_stage =open('C:\\Users\\Salaheddin\\OneDrive\\Documents\\Projets\\Rasa_chatbot\\fold\\test.txt', 'r',encoding='UTF-8').readlines()
        choix = int(gerer_stage)
        result_choix = "{}".format(type_stage[choix])
        if choix ==1:
            test_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [{
                    "title": "Data Science Intern",
                    "image_url": os.getcwd()+"\\actions\\im_1.jpg",
                    "buttons": [{
                        "title": "Click Here",
                        "url": result_choix,
                        "type": "web_url" } ]
                        }]
                    }
                }

        if choix ==2:
            test_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [{
                    "title": "Data Analytics Intern",
                    "image_url": os.getcwd()+"\\actions\\im_2.jpg",
                    "buttons": [{
                        "title": "Click Here",
                        "url": result_choix,
                        "type": "web_url" } ]
                        }]
                    }
                }
        if choix ==3:
            test_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [{
                    "title": "Business Intelligence Intern",
                    "image_url": os.getcwd()+"\\actions\\im_3.jpg",
                    "buttons": [{
                        "title": "Click Here",
                        "url": result_choix,
                        "type": "web_url" } ]
                        }]
                    }
                }
        if choix ==4:
            test_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [{
                    "title": "Web Developpement Intern",
                    "image_url": os.getcwd()+"\\actions\\im_4.jpg",
                    "buttons": [{
                        "title": "Click Here",
                        "url": result_choix,
                        "type": "web_url" } ]
                        }]
                    }
                }

        dispatcher.utter_message(attachment=test_carousel)
        #dispatcher.utter_message(text=result_choix) # returner les actions
        return []