# Fundamental goals:  
1. Confidentiality  
No one else can understand it  
2. Data integrity  
Data is transferred in full  
3. Data origin authentication  
Data comes from correct source  
4. Non-repudiation  
Prevent an entity from denying previous commitments  

# TLS  
## Vulnerabilites
1. The crypto could be weak (e.g., AES, HMAC, RSA).  
2. Quantum attacks on the underlying cryptography.  
3. Weak random number generation.  
4. Issuance of fraudulent certificates  
5. Software bugs (both inadvertent and malicious).  
6. Phishing attacks.  
 Most users do not verify the security information by looking at the URL or clicking on the
padlock.  
7. Only protects data during transit.  
Many servers store large amounts of personal information.  

