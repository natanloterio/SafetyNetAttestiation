import base64

class AttestationStatement:
    nonce = ""
    timestampMs = 0
    apkPackageName = ""
    apkCertificateDigestSha256 = []
    apkDigestSha256 = []
    ctsProfileMatch = False
    basicIntegrity = False
    def get_nonce(self):
        return base64.decode(self.nonce)
    
    def get_timestamp_ms(self):
        return self.timestampMs

    def get_apk_package_name(self):
        return self.apkPackageName

    def get_apk_digest_sha256(self):
        return base64.decodebytes(self.apkDigestSha256)

    def get_apk_certificate_digest_sha258(self):

        w, h = 2, len(self.apkCertificateDigestSha256)
        certs = [[0 for x in range(w)] for y in range(h)]

        for i in range(len):
            certs[i] = base64.decodebytes(self.apkCertificateDigestSha256[i])
        return certs

    def is_cts_profile_match(self):
        return self.ctsProfileMatch
    
    def has_basic_integrity(self):
        return self.basicIntegrity


