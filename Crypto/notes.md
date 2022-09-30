# Fundamental goals:  
1. Confidentiality  
No one else can understand it 

2. Data integrity  
Data is transferred in full  

3. Data origin authentication  
Data comes from correct source

4. Non-repudiation  
Prevent an entity from denying previous commitments  

Note: avoid security by obscurity

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

# Symmetric key
Consits of:  
1. $M$ - the plaintext space
2. $C$ - the ciphertext space
3. $K$ - the key spcae
4. a family of encryption functions $E_k: M -> C \; \forall \; k \in K$
5. a family of decryption functions $D_k: C -> M \; \forall \; k \in K$  

Such that $D_k(E_k(m)) = m$  

_e.g. substitution cypher_


# Defining Security
## Advesarial Goal
1. Recover secret key
2. Systematically recover plaintext from ciphertext
3. Learn some partial information about the plaintext from the ciphertext (other than its length)

If the adversary can achieve 1 or 2, the SKES is said to be totally insecure.

## Advesray's interaction
1. Passive attacks  
    - Ciphertext-only attack  
    - Known-plaintext attack: the adversary knows bits of plaintext and corresponding ciphertext  
2. Active attacks  
    - Chosen-plaintext attack: the adversary chooses bits of plaintext and finds corresponding ciphertext  
    - Chosen-ciphertext attack: the adversary chooses bits of ciphertext and finds corresponding plaintext  (most powerful)
3. Other attacks  
    - side-channel attacks: monitor the encryption and decryption equipment  
        - timing attacks
        - power analysis attacks
        - electromagnetic radiation analysis
    - Physical attacks
        - bribery
        - blackmail
        - gun
        - social engineering


# Week 4 wed
DES s-boxes
