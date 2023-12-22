![FPKIPA Federal Public Key Infrastructure Policy Authority ](media/image1.emf){width="3.7604166666666665in" height="0.75in"}


**X.509 Certificate Policy**


**For The**


**U.S. Federal PKI**


**Common Policy Framework**


Version 3647 - 1.17


December 13, 2011


**Signature Page**


\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_


Chair, Federal Public Key Infrastructure Policy Authority DATE


**Revision History**


-----------------------------------------------------------------------------------------------------------------------------------------------------------------
**Document Version**   **Document Date**    **Revision Details**
----------------------
--------------------
---------------------------------------------------------------------------------------------------------------------
1.0                    May 7, 2007          Revised Common Policy (RFC 3647 format)




FOREWORD


This is the policy framework governing the public key infrastructure (PKI) component of the Federal Enterprise Architecture.
The policy framework incorporates seven specific certificate policies: a policy for users with software cryptographic modules, a policy for users with hardware cryptographic modules, a policy for devices with software cryptographic modules, a policy for devices with hardware cryptographic modules, a high assurance user policy, a user authentication policy, and a card authentication policy.
There are two Certification Authorities associated with the Common Policy Framework: The Federal Common Policy Root CA and the SHA-1 Federal Root CA.


# Table of Contents {#table-of-contents .TOC-Heading}





#  Introduction



This certificate policy (CP) includes seven distinct certificate policies: a policy for users with software cryptographic modules, a policy for users with hardware cryptographic modules, a policy for devices with software cryptographic modules, a policy for devices with hardware cryptographic modules, a high assurance user policy, a user authentication policy, and a card authentication policy.
In this document, the term "device" means a non-person entity, i.e., a hardware device or software application.
Where a specific policy is not stated, the policies and procedures in this specification apply equally to all seven policies.


The use of SHA-1 to create digital signatures is deprecated beginning January 1, 2011.
However, there are some applications in use within the federal government that cannot process certificates or certificate revocation information signed using SHA-256.
Therefore this CP also includes five additional distinct certificate policies which indicate the use of the deprecated SHA-1 after December 31, 2010.
These id-fpki-sha1 policies adhere to all the requirements of the associated id-common policy with the exception that the certificate is generated with a SHA-1 signature and the issuing CA may use SHA-1 for generation of PKI objects such as CRLs and OCSP responses until December 31, 2013.
It should be noted that certificates issued on or after January 1, 2011 are not FIPS 201 compliant, and therefore do not meet the requirements of HSPD-12.
CAs that issue SHA-1 certificates after December 31, 2010 may not also issue FIPS 201 compliant certificates.


The user policies apply to certificates issued to Federal employees, contractors, and other affiliated personnel for the purposes of authentication, signature, and confidentiality.
This CP was explicitly designed to support access to Federal systems that have not been designated national security systems.


A PKI that uses this CP will provide the following security management services:


-   Key generation/storage


-   Certificate generation, modification, re-key, and distribution


-   Certificate revocation list (CRL) generation and distribution


-   Directory management of certificate related items


-   Certificate token initialization/programming/management


-   System management functions (e.g., security audit, configuration management, archive.)


The user policies require Federal employees, contractors, and other affiliated personnel to use FIPS 140 validated cryptographic modules for cryptographic operations and the protection of trusted public keys.
The device policy also requires use of FIPS 140 validated cryptographic modules for cryptographic operations and the protection of trusted public keys.


This policy does not presume any particular PKI architecture.
The policy may be implemented through a hierarchical PKI, mesh PKI, or a single certification authority (CA).
Any CA that asserts this policy in certificates must obtain prior approval from the Federal PKI Policy Authority.
CAs that issue certificates under this policy may operate simultaneously under other policies.
Such CAs must not assert the OIDs in this policy in certificates unless they are issued in accordance with all the requirements of this policy.


This policy establishes requirements for the secure distribution of self-signed certificates for use as trust anchors.
These constraints apply only to CAs that chose to distribute self-signed certificates, such as a hierarchical PKI's root CA.


This CP is consistent with request for comments (RFC) 3647, the Internet Engineering Task Force (IETF) Public Key Infrastructure X.509 (IETF PKIX) Certificate Policy and Certification Practices Framework.