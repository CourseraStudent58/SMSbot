from setupform import SetupForm
from logger import log

from cpaassdk import Client
from flask import request
import sys

# projectTN = '+17327376809'

class Cpaas:
    status = "Not Ready"
    projectTN = "unk"

    def __init__(self,  bot):
        log('cpaas init')
        # Initialize
        self.bot = bot
        setup = SetupForm()
        setup.loadSetup()

        try:
            self.client = Client({
                'client_id': setup.private_key.data,
                'client_secret': setup.client_secret.data,
                'base_url': setup.apim_url.data
            })
            log('type of Client ', type(self.client))
            log(self.client)

            self.projectTN = setup.project_TN.data
            response = self.client.conversation.subscribe({
                'webhook_url': setup.public_url.data + '/inbound-sms/webhook',
                'type': 'sms',
                'destination_address': self.projectTN
            })
            log(response)
            self.status = "Ready"
        except Exception as e:
            print(e)
            self.status = "Not Ready"


    def getStatus(self):
        return self.status

    def sendMsg(self, to, msg):
        log('sending msg: ' + msg)
        response = self.client.conversation.create_message(
            dict(type='sms', destination_address=to, sender_address=self.projectTN, message=msg))
        log(response)

    def post(self):
        log("post");
        sys.stdout.flush()
        log(request.json)
        try:
            inboundNotification = request.json['inboundSMSMessageNotification']

            if inboundNotification is not None:
                parsed_response = inboundNotification['inboundSMSMessage']

                log(parsed_response)
                reply = self.bot.determineReply(parsed_response['message'])
                self.sendMsg(parsed_response['senderAddress'], reply)
                return '{"success":"true"}'
        except Exception as e:
            print(e)
        return '{"success":"false"}'


