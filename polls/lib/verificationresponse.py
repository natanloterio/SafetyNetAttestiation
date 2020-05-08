from .verificationrequest import VerificationRequest
import requests
import json

class VerificationResponse:
    API_KEY = "AIzaSyBZ8wNUgDrM331iTTMiA-9WpqQaMbhNoXY"
    URL = "https://www.googleapis.com/androidcheck/v1/attestations/verify?key="+API_KEY
    is_valid_signature = False
    error = ''
    
    def online_verify(self,request: VerificationRequest):
        payload = json.dumps(request.__dict__)
        result = requests.post(self.URL,data=payload)
        verificationResponse = json.loads(result.content)
        return verificationResponse