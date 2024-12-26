# Report on Keylogger Project Exploiting Windows 1507 Vulnerabilities

## 1. Introduction

This report documents a controlled cybersecurity experiment designed to demonstrate the exploitation of human error and inadequate security measures. The experiment involves creating a custom keylogger disguised as a calculator application on a Windows 10 (version 1507) system. Through this analysis, we examine the vulnerabilities exploited, attack methodology, and essential risk mitigation strategies.

## 2. Objectives

The experiment focused on three primary objectives:
1. Demonstrating human error exploitation in a controlled environment
2. Analyzing deployment and activation methods of malicious software
3. Developing comprehensive recommendations for attack prevention

## 3. Vulnerability Analysis

### Introduction

As organizations increasingly rely on digital communication, the risk of cyberattacks has escalated. Email remains a primary vector for cybercriminals, who exploit human psychology to trick users into executing malicious files or divulging sensitive information. This report examines several vulnerabilities that can arise from email-based social engineering, including the execution of unsigned software, lack of endpoint protection, and the consequences of excessive user privileges.

### Vulnerabilities Involved

#### 3.1 Email-Based Social Engineering

**Vulnerability**: Execution of Malicious Files Delivered via Email

Email-based social engineering attacks often involve the delivery of malicious files disguised as legitimate attachments. Users may inadvertently execute these files, leading to severe security breaches.

**Root Cause**: Lack of Proper Email Filtering, Awareness, or Endpoint Protection

The primary reasons for this vulnerability include inadequate email filtering mechanisms, insufficient user awareness regarding phishing tactics, and ineffective endpoint protection solutions. Many organizations fail to implement robust email security measures, leaving users vulnerable to attacks.

**Fixes**:
1. Implement Robust Email Security Solutions: Organizations should deploy advanced email security solutions that include spam filters, attachment scanning, and URL filtering to detect and block malicious content.
2. User Education: Regular training sessions should be conducted to educate users on recognizing phishing attempts and malicious emails. Simulated phishing exercises can help reinforce this training.

#### 3.2 Execution of Unsigned or Untrusted Software

**Vulnerability**: Execution of Untrusted or Unsigned Software

Once a malicious file is executed, it may install additional malware, such as keyloggers, that can compromise sensitive information.

**Root Cause**: Insufficient Application Control Policies

Many organizations lack stringent application control policies, allowing users to execute untrusted or unsigned software without proper checks.

**Fixes**:
1. Enable Application Control: Implement application control solutions, such as Microsoft AppLocker, to restrict the execution of unauthorized applications.
2. Software Integrity Verification: Ensure that all software is digitally signed and verify its integrity before execution.

#### 3.3 Lack of Endpoint Protection

**Vulnerability**: Failure to Detect or Block Keyloggers

**Root Cause**: Ineffective or Outdated Antivirus/Antimalware Solutions

**Fixes**:
1. Install and Update Robust Antivirus Software
2. Implement Real-Time Threat Detection

#### 3.4 Outbound Communication to Command and Control (C2) Server

**Vulnerability**: Successful Communication with Remote Servers

**Root Cause**: Lack of Outbound Network Traffic Monitoring

**Fixes**:
1. Configure Firewalls: Implement strict outbound connection rules
2. Use DNS Filtering and IDS/IPS: Deploy comprehensive monitoring systems

## 4. Methodology

### 4.1 Malicious File Development

The team developed a Python-based keylogger with the following capabilities:
1. Keystroke recording utilizing the pyinput library
2. Functional calculator interface serving as camouflage
3. Azure-hosted remote server communication
4. Executable conversion through pyinstaller

### 4.2 Payload Delivery

The attack vector followed a straightforward path:
1. Initial file upload to OneDrive
2. Distribution via Outlook email attachment
3. Local machine download by the target

### 4.3 Payload Execution

Upon execution, the application presented a fully functional calculator interface while simultaneously activating the keylogger component. The malware maintained persistent keystroke logging and server communication, continuing operation even after application closure.

## 5. Tools and Technical Implementation

### 5.1 Technical Stack

The experiment utilized the following tools:
1. Python for core development
2. PyInstaller for executable creation
3. Azure Virtual Machine for C2 server hosting

### 5.2 Core Functionality

The application integrated three primary components:
1. Keystroke capture through pynput
2. Server communication via the requests library
3. Calculator interface implementation using tkinter

## 6. Key Observations

The experiment revealed several critical findings:
1. The payload successfully exploited user trust through effective disguise
2. Windows SmartScreen (version 1507) failed to detect the threat
3. The keylogger maintained undetected server communication
4. Real-time keystroke transmission persisted beyond application termination

## 7. Mitigation Strategies

### 7.1 User-Level Protection

Individual users should implement basic security practices:
1. Strict avoidance of untrusted executable files
2. Thorough file authentication before execution

### 7.2 Organizational Security

Organizations should establish comprehensive security measures:
1. Implementation of email attachment scanning
2. Group Policy restrictions on unverified executables
3. Regular user security awareness training

### 7.3 Administrative Controls

System administrators should deploy multiple layers of protection:
1. Regular Windows security updates
2. Comprehensive network traffic monitoring
3. Strict firewall configuration
4. DNS filtering and IDS/IPS implementation
5. EDR solution deployment

## 8. Conclusion

This experiment effectively demonstrates the critical intersection of user awareness and security measures in cybersecurity defense. The successful exploitation of user trust, combined with outdated security features and inadequate traffic monitoring, enabled the attack's success in our controlled environment. Organizations can significantly enhance their security posture by implementing the recommended mitigation strategies.
https://github.com/muhammadmaazabbasi/Keylogger/


