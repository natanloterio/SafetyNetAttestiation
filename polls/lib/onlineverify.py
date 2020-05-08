from verificationrequest import VerificationRequest
import base64
import io
import json

class OnlineVerify:
    API_KEY = "AIzaSyBZ8wNUgDrM331iTTMiA-9WpqQaMbhNoXY"
    URL = "https://www.googleapis.com/androidcheck/v1/attestations/verify?key="+API_KEY
    is_valid_signature = False
    error = ''
    
    def online_verify(self,request: VerificationRequest):
        payload = json.dumps(request.__dict__)
        result = requests.post(self.URL,data=payload)
        verificationResponse = json.loads(result.content)
        return verificationResponse

    def extract_jws_data(jws):
        parts = jws.split('.')

        if(len(parts) != 3):
            print("Failure: Illegal JWS signature format. The JWS consists of "
                    + len(parts) + " parts instead of 3.")
            return

        return base64.decodestring(parts[1])

    def parse_and_verify(self, signed_attestation_statement):
        request = VerificationRequest(signed_attestation=signed_attestation_statement)
        response = self.online_verify(signed_attestation_statement)

        if(response is None):
            return null
        

        if(response.error is not None):
            print("Failure: The API encountered an error processing this request:"+
            response.error)
            return
        
        if(response.isValidSignature is not None):
            if(response.isValidSignature != True):
                print("Failure: The cryptographic signature of the attestation statement" +
                " couldn't be verified")
                return
            
            #successfuly verified
            print("Sucessfully verified the signature of the attestation statement.")

            data = extract_jws_data(signed_attestation_statement)
            str_data = io.BytesIO(data)
            return str_data





def main():
    sign = "eyJhbGciOiJSUzI1NiIsIng1YyI6WyJNSUlGa3pDQ0JIdWdBd0lCQWdJUkFOY1NramRzNW42K0NBQUFBQUFwYTBjd0RRWUpLb1pJaHZjTkFRRUxCUUF3UWpFTE1Ba0dBMVVFQmhNQ1ZWTXhIakFjQmdOVkJBb1RGVWR2YjJkc1pTQlVjblZ6ZENCVFpYSjJhV05sY3pFVE1CRUdBMVVFQXhNS1IxUlRJRU5CSURGUE1UQWVGdzB5TURBeE1UTXhNVFF4TkRsYUZ3MHlNVEF4TVRFeE1UUXhORGxhTUd3eEN6QUpCZ05WQkFZVEFsVlRNUk13RVFZRFZRUUlFd3BEWVd4cFptOXlibWxoTVJZd0ZBWURWUVFIRXcxTmIzVnVkR0ZwYmlCV2FXVjNNUk13RVFZRFZRUUtFd3BIYjI5bmJHVWdURXhETVJzd0dRWURWUVFERXhKaGRIUmxjM1F1WVc1a2NtOXBaQzVqYjIwd2dnRWlNQTBHQ1NxR1NJYjNEUUVCQVFVQUE0SUJEd0F3Z2dFS0FvSUJBUUNXRXJCUVRHWkdOMWlaYk45ZWhSZ2lmV0J4cWkyUGRneHcwM1A3VHlKWmZNeGpwNUw3ajFHTmVQSzVIemRyVW9JZDF5Q0l5Qk15eHFnYXpxZ3RwWDVXcHNYVzRWZk1oSmJOMVkwOXF6cXA2SkQrMlBaZG9UVTFrRlJBTVdmTC9VdVp0azdwbVJYZ0dtNWpLRHJaOU54ZTA0dk1ZUXI4OE5xd1cva2ZaMWdUT05JVVQwV3NMVC80NTIyQlJXeGZ3eGMzUUUxK1RLV2tMQ3J2ZWs2V2xJcXlhQzUyVzdNRFI4TXBGZWJ5bVNLVHZ3Zk1Sd3lLUUxUMDNVTDR2dDQ4eUVjOHNwN3dUQUhNL1dEZzhRb3RhcmY4T0JIa25vWjkyWGl2aWFWNnRRcWhST0hDZmdtbkNYaXhmVzB3RVhDdnFpTFRiUXRVYkxzUy84SVJ0ZFhrcFFCOUFnTUJBQUdqZ2dKWU1JSUNWREFPQmdOVkhROEJBZjhFQkFNQ0JhQXdFd1lEVlIwbEJBd3dDZ1lJS3dZQkJRVUhBd0V3REFZRFZSMFRBUUgvQkFJd0FEQWRCZ05WSFE0RUZnUVU2REhCd3NBdmI1M2cvQzA3cHJUdnZ3TlFRTFl3SHdZRFZSMGpCQmd3Rm9BVW1OSDRiaERyejV2c1lKOFlrQnVnNjMwSi9Tc3daQVlJS3dZQkJRVUhBUUVFV0RCV01DY0dDQ3NHQVFVRkJ6QUJoaHRvZEhSd09pOHZiMk56Y0M1d2Eya3VaMjl2Wnk5bmRITXhiekV3S3dZSUt3WUJCUVVITUFLR0gyaDBkSEE2THk5d2Eya3VaMjl2Wnk5bmMzSXlMMGRVVXpGUE1TNWpjblF3SFFZRFZSMFJCQll3RklJU1lYUjBaWE4wTG1GdVpISnZhV1F1WTI5dE1DRUdBMVVkSUFRYU1CZ3dDQVlHWjRFTUFRSUNNQXdHQ2lzR0FRUUIxbmtDQlFNd0x3WURWUjBmQkNnd0pqQWtvQ0tnSUlZZWFIUjBjRG92TDJOeWJDNXdhMmt1WjI5dlp5OUhWRk14VHpFdVkzSnNNSUlCQkFZS0t3WUJCQUhXZVFJRUFnU0I5UVNCOGdEd0FIY0E5bHlVTDlGM01DSVVWQmdJTUpSV2p1Tk5FeGt6djk4TUx5QUx6RTd4Wk9NQUFBRnZudXkwWndBQUJBTUFTREJHQWlFQTdlLzBZUnUzd0FGbVdIMjdNMnZiVmNaL21ycCs0cmZZYy81SVBKMjlGNmdDSVFDbktDQ0FhY1ZOZVlaOENDZllkR3BCMkdzSHh1TU9Ia2EvTzQxaldlRit6Z0IxQUVTVVpTNnc3czZ2eEVBSDJLaitLTURhNW9LKzJNc3h0VC9UTTVhMXRvR29BQUFCYjU3c3RKTUFBQVFEQUVZd1JBSWdFWGJpb1BiSnA5cUMwRGoyNThERkdTUk1BVStaQjFFaVZFYmJiLzRVdk5FQ0lCaEhrQnQxOHZSbjl6RHZ5cmZ4eXVkY0hUT1NsM2dUYVlBLzd5VC9CaUg0TUEwR0NTcUdTSWIzRFFFQkN3VUFBNElCQVFESUFjUUJsbWQ4TUVnTGRycnJNYkJUQ3ZwTVhzdDUrd3gyRGxmYWpKTkpVUDRqWUZqWVVROUIzWDRFMnpmNDluWDNBeXVaRnhBcU9SbmJqLzVqa1k3YThxTUowajE5ekZPQitxZXJ4ZWMwbmhtOGdZbExiUW02c0tZN1AwZXhmcjdIdUszTWtQMXBlYzE0d0ZFVWFHcUR3VWJHZ2wvb2l6MzhGWENFK0NXOEUxUUFFVWZ2YlFQVFliS3hZait0Q05sc3MwYlRTb0wyWjJkL2ozQnBMM01GdzB5eFNLL1VUcXlrTHIyQS9NZGhKUW14aStHK01LUlNzUXI2MkFuWmF1OXE2WUZvaSs5QUVIK0E0OFh0SXlzaEx5Q1RVM0h0K2FLb2hHbnhBNXVsMVhSbXFwOEh2Y0F0MzlQOTVGWkdGSmUwdXZseWpPd0F6WHVNdTdNK1BXUmMiLCJNSUlFU2pDQ0F6S2dBd0lCQWdJTkFlTzBtcUdOaXFtQkpXbFF1REFOQmdrcWhraUc5dzBCQVFzRkFEQk1NU0F3SGdZRFZRUUxFeGRIYkc5aVlXeFRhV2R1SUZKdmIzUWdRMEVnTFNCU01qRVRNQkVHQTFVRUNoTUtSMnh2WW1Gc1UybG5iakVUTUJFR0ExVUVBeE1LUjJ4dlltRnNVMmxuYmpBZUZ3MHhOekEyTVRVd01EQXdOREphRncweU1URXlNVFV3TURBd05ESmFNRUl4Q3pBSkJnTlZCQVlUQWxWVE1SNHdIQVlEVlFRS0V4VkhiMjluYkdVZ1ZISjFjM1FnVTJWeWRtbGpaWE14RXpBUkJnTlZCQU1UQ2tkVVV5QkRRU0F4VHpFd2dnRWlNQTBHQ1NxR1NJYjNEUUVCQVFVQUE0SUJEd0F3Z2dFS0FvSUJBUURRR005RjFJdk4wNXprUU85K3ROMXBJUnZKenp5T1RIVzVEekVaaEQyZVBDbnZVQTBRazI4RmdJQ2ZLcUM5RWtzQzRUMmZXQllrL2pDZkMzUjNWWk1kUy9kTjRaS0NFUFpSckF6RHNpS1VEelJybUJCSjV3dWRnem5kSU1ZY0xlL1JHR0ZsNXlPRElLZ2pFdi9TSkgvVUwrZEVhbHROMTFCbXNLK2VRbU1GKytBY3hHTmhyNTlxTS85aWw3MUkyZE44RkdmY2Rkd3VhZWo0YlhocDBMY1FCYmp4TWNJN0pQMGFNM1Q0SStEc2F4bUtGc2JqemFUTkM5dXpwRmxnT0lnN3JSMjV4b3luVXh2OHZObWtxN3pkUEdIWGt4V1k3b0c5aitKa1J5QkFCazdYckpmb3VjQlpFcUZKSlNQazdYQTBMS1cwWTN6NW96MkQwYzF0Skt3SEFnTUJBQUdqZ2dFek1JSUJMekFPQmdOVkhROEJBZjhFQkFNQ0FZWXdIUVlEVlIwbEJCWXdGQVlJS3dZQkJRVUhBd0VHQ0NzR0FRVUZCd01DTUJJR0ExVWRFd0VCL3dRSU1BWUJBZjhDQVFBd0hRWURWUjBPQkJZRUZKalIrRzRRNjgrYjdHQ2ZHSkFib090OUNmMHJNQjhHQTFVZEl3UVlNQmFBRkp2aUIxZG5IQjdBYWdiZVdiU2FMZC9jR1lZdU1EVUdDQ3NHQVFVRkJ3RUJCQ2t3SnpBbEJnZ3JCZ0VGQlFjd0FZWVphSFIwY0RvdkwyOWpjM0F1Y0d0cExtZHZiMmN2WjNOeU1qQXlCZ05WSFI4RUt6QXBNQ2VnSmFBamhpRm9kSFJ3T2k4dlkzSnNMbkJyYVM1bmIyOW5MMmR6Y2pJdlozTnlNaTVqY213d1B3WURWUjBnQkRnd05qQTBCZ1puZ1F3QkFnSXdLakFvQmdnckJnRUZCUWNDQVJZY2FIUjBjSE02THk5d2Eya3VaMjl2Wnk5eVpYQnZjMmwwYjNKNUx6QU5CZ2txaGtpRzl3MEJBUXNGQUFPQ0FRRUFHb0ErTm5uNzh5"
    online = OnlineVerify()
    stmt = online.parse_and_verify(sign)

    if(stmt is None):
        print("Failure: Failed to parse and verify the attestation statement.")
        return
    
    print("The content of the attestation statement is:")
    print(stmt)
    return

if __name__ == '__main__':
    main()
