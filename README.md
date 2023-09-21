# PYTHON NETWORK SECURITY TOOLS
This is a compilation of network security tools derived from the book "Black Hat Python" with some slight adjustments. The collection encompasses a variety of tools, starting from a basic TCP client and progressing to more robust ones, designed for offensive use in identifying and monitoring security vulnerabilities within a system. It is important to note that these tools are solely intended for educational purposes and should never be employed for any malicious activities, as doing so may result in severe legal consequences.
## Arper
ARP spoofing, also known as ARP cache poisoning, is a well-established and highly effective technique. The Address Resolution Protocol (ARP) serves as a widely used communication protocol, responsible for translating internet layer addresses into corresponding link layer addresses.

Arper is a tool specifically designed for ARP spoofing. This technique involves an attacker sending spoofed ARP messages across a local area network. The primary objective is to associate the attacker's MAC address with the IP address of another host, such as the default gateway. Consequently, any traffic intended for that IP address will be directed to the attacker instead. Each computer within a network maintains an ARP cache, which stores the most recent Media Access Control (MAC) addresses associated with the IP addresses on the local network.

ARP spoofing enables an attacker to intercept data frames on the network, manipulate the traffic, or even halt all communication. This type of attack is often utilized as a launching pad for additional attacks, including Distributed Denial of Service (DDoS), man-in-the-middle, or session hijacking attacks. It's important to note that ARP spoofing can only be executed on networks that employ ARP and necessitates direct access to the targeted local network segment by the attacker.

## Burp Extension tool for Bing
In many cases, a single web server is responsible for hosting multiple web applications. When targeting such a server for an attack, it can be advantageous to identify these other hostnames. This knowledge might provide an easier path to gaining access to a shell. It's not uncommon to come across vulnerable web applications or even development resources that are located on the same machine as your primary target.

Microsoft's Bing search engine offers search capabilities that enable you to query for all websites associated with a specific IP address using the "IP" search modifier. By employing this feature, Bing will provide you with information on all subdomains associated with a given domain if you utilize the domain search modifier. This can be particularly useful in uncovering additional targets or potential entry points during an attack.
## Fuzzer
In certain scenarios, you may encounter a web application or service that restricts the use of conventional web application assessment tools. In such cases, it becomes crucial to establish a reliable baseline of HTTP traffic, including authentication cookies. This serves as a starting point for further analysis.

To tackle this situation, a custom fuzzer proves to be invaluable. It allows you to intercept and modify the body of incoming requests, providing the flexibility to manipulate the payload as desired. This custom fuzzer empowers you to fine-tune the payload and perform targeted assessments tailored to the specific requirements of the situation.

## WordList Generator
User passwords often play a critical role in security. Particularly with web applications, especially those that are customized, it is unfortunately quite common to find that they lack mechanisms to lock users out after multiple failed authentication attempts. In such cases, conducting an online password guessing session can become a means to gain unauthorized access to the target site. 

The key to successful online password guessing lies in assembling an appropriate wordlist. This wordlist comprises a collection of potential passwords that are systematically tried in order to find the correct one. By utilizing a well-curated wordlist, you increase the chances of guessing the right password and potentially gaining access to the targeted site. 

## Bruter
When targeting a custom web application or a complex e-commerce system, it's common to be unaware of all the files accessible on the webserver. To maximize your understanding of the web application's structure, you can employ a spider that systematically navigates through the target website, uncovering various components. However, in many instances, your goal will be to obtain configuration files or remnants of development that may contain sensitive information or expose unintended functionality.

To discover such content, you'll need to utilize a brute-forcing tool designed to search for commonly used filenames and directories. This tool allows you to systematically and exhaustively search for specific files or directories that may reveal valuable information or provide unexpected access to the system. By employing this approach, you increase your chances of finding hidden resources or configuration files that the software developer did not intend to expose.

## Mail Sniffer
This tool serves as a straightforward email sniffer designed to capture credentials for protocols like Simple Mail Transfer Protocol (SMTP), Post Office Protocol (POP3), and Internet Message Access Protocol (IMAP). By utilizing this mail sniffer, it becomes possible to intercept and acquire login information from these protocols.

For enhanced effectiveness, this mail sniffer can be combined with ARP poisoning and man-in-the-middle attacks. By executing ARP poisoning, the attacker can redirect network traffic through their machine, enabling them to intercept and retrieve credentials from other devices on the same network.

It's important to note that the usage of this tool, especially in conjunction with ARP poisoning and man-in-the-middle attacks, may involve unauthorized access and potentially illegal activities. It is crucial to comply with legal and ethical guidelines and obtain proper authorization before engaging in any such activities.
## Mapper
Content Management Systems (CMS) and blogging platforms have simplified the process of creating new websites and blogs. They are commonly used in shared hosting environments as well as enterprise networks. However, each system presents its own set of challenges when it comes to installation, configuration, and patch management. Content management systems are no exception in this regard. 

When security best practices and proper installation procedures are not followed, these systems can become vulnerable and serve as easy attack vectors for gaining unauthorized access to web servers. 

This tool is specifically designed as a scanner to identify and locate all accessible files on the wordpress framework  on a remote target. It effectively searches for remnants of installation files, unprotected directories, and other valuable resources that can provide an attacker with a foothold on the web server. By utilizing this tool, an attacker can identify potential weaknesses and exploit them to gain unauthorized access or control over the targeted web server.

## Netcat
Netcat is widely regarded as a versatile networking tool that can perform a multitude of functions, making it akin to a swiss army knife for network operations. Consequently, savvy system administrators often opt to remove it from their systems to prevent potential misuse. However, if an attacker manages to gain access to a system, having Netcat installed would provide them with significant capabilities. With Netcat, an attacker can read and write data across the network, enabling them to execute remote commands, transfer files, or even establish a remote shell.

In many instances, you may encounter servers that lack Netcat but have Python installed. To overcome this limitation, this tool serves as a straightforward network client and server, designed to mimic the functionality of Netcat. It allows you to accomplish tasks such as pushing files or establishing a listener that provides command-line interface (CLI) access. By leveraging this tool, you can achieve similar functionality to Netcat even on systems where it is not present.

## TCP Client
A TCP client is responsible for initiating a connection request to a TCP server, enabling the establishment of a connection between the client and server. In the context of penetration testing, there are numerous occasions where there is a need to quickly create a TCP client for various purposes. These can include testing services, sending random or malformed data (fuzzing), or performing other tasks relevant to the assessment.

However, when operating within large enterprise environments, certain restrictions may apply. Access to networking tools or compilers might be limited or unavailable. Additionally, basic functionalities like copy/paste or internet connectivity may not be accessible. In such scenarios, the ability to swiftly create a TCP client becomes exceptionally valuable.

Having the capability to rapidly generate a TCP client allows penetration testers to work efficiently, even in constrained environments. It provides the flexibility to perform essential tasks without relying on external tools or internet connectivity, ensuring the testing process can proceed effectively.

## TCP Proxy
A TCP proxy server acts as a mediator between a client and a destination server, facilitating communication between them. Clients establish connections with the TCP proxy server, which in turn establishes connections with the destination server. Including a TCP proxy in your set of tools offers several advantages. For example, it can be used to forward traffic, enabling it to hop from one host to another. It is also useful for assessing network-based software.

During penetration tests conducted in enterprise environments, there are limitations that restrict the use of robust tools like Wireshark. Additionally, running drivers to capture loopback traffic on Windows may not be feasible. Furthermore, network segmentation prevents direct execution of tools against the target host.

In such situations, having a TCP proxy becomes invaluable. It allows you to overcome these limitations and perform essential tasks by serving as an intermediary between your testing tools and the target host. By redirecting traffic through the TCP proxy, you can effectively assess the network and software without being hindered by the constraints imposed by the environment.
## TCP Server
A TCP server is an application that waits for incoming TCP connections from TCP clients. Once a connection is established, both the server and the client can exchange data in any desired sequence. The utilization of a custom TCP server is particularly useful when developing command shells or creating a proxy.

By implementing your own TCP server, you have full control over the communication process. This enables you to design command shells that facilitate remote interaction or construct proxies that mediate connections between clients and other servers. The flexibility offered by a custom TCP server allows for tailored solutions to meet specific requirements in terms of functionality and data exchange.
## UDP Client
 UDP (User Datagram Protocol) is a networking procedure utilized for transferring data between two computers connected over a network, similar to other networking protocols. However, UDP operates differently compared to other protocols. It follows a direct approach by delivering packets (data units) directly to the destination computer without establishing a connection beforehand, specifying the order of the packets, or ensuring their intended arrival. These packets are referred to as "datagrams" in the context of UDP.

UDP finds extensive usage on the Internet, particularly for time-sensitive transmissions like DNS lookups and video playback. By omitting the need to establish a connection before transmitting data, UDP facilitates faster communication. This allows for rapid delivery of data. However, this speed comes with the trade-off of potential packet loss during transmission. As a result, UDP can be vulnerable to attacks such as DDoS (Distributed Denial of Service), where an attacker intentionally floods the network with UDP packets, causing disruptions or exploitation of vulnerabilities.

## Wordpress Killer
This tool is a straightforward brute force attack tool designed for targeting WordPress websites. While modern WordPress systems implement some basic anti-brute-force techniques, they still commonly lack features like account lockouts or strong CAPTCHAs by default. This makes them susceptible to attacks and serves as a prime target for exploiting vulnerabilities through brute force methods.
