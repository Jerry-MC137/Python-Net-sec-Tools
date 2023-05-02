from burp import IBurpExtender
from burp import IIntruderPayloadGeneratorFactory
from burp import IIntruderPayloadGenerator

from java.util import List, ArrayList

import random

class BurpExtender(IBurpExtender, IIntruderPayloadGeneratorFactory):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()

        callbacks.registerIntruderPayloadGeneratorFactory(self)

        return

    def getGeneratorName(self):
        return "BHP Payload  Generator"

    def createNewInstance(self, attack):
        return BHPFuzzer(self, attack)

class BHPFuzzer(IIntruderPayloadGenerator):
    def __init__(self, extension, attack):
        self._extension = extension
        self._helpers = extension._helpers
        self._attack = attack
        self.max_payloads = 10
        self.num_iterations = 0

        return

    def hasMorePayloads(self):
        if self.num_iterations == self.max_payloads:
            return False
        else:
            return True

    def getNextPayload(self,current_payload):
        # CONVERT INTO A STRING.
        payload = "".join(chr(x) for x in current_payload)

        # CALL SIMPLE MUTATOR TO FUZZ THE POST.
        payload = self.mutate_payload(payload)

        # INCREASE THE NUMBER OF FUZZING ATTEMPTS.
        self.num_iterations += 1

        return payload

    def reset(self):
        self.num_iterations = 0
        return

    def mutate_payload(self, original_payload):
        # PICK A SIMPLE MUTATOR OR CALL AN EXTERNAL SCRIPT
        picker = random.randint(1,3)

        # SELECT A RANDOM OFFSET IN THE PAYLOAD TO MUTATE
        offset = random.randint(0, len(original_payload)-1)

        front, back = original_payload[:offset], original_payload[offset:]

        # RANDOM OFFSET INSERT A SQL INJECTION ATTEMPT
        if picker == 1:
            front += "'"

        # JAM AN XSS ATTEMPT IN
        elif picker == 2:
            front += "<script>alert('BHP!');</script>"

        # REPEAT A RANDOM CHUNK OF THE ORIGINAL PAYLOAD
        elif picker == 3:
            chunk_length = random.randint(0, len(back)-1)
            repeater = random.randint(1,10)
            for _ in range(repeater):
                front += original_payload[:offset + chunk_length]
            front += back

        return front
