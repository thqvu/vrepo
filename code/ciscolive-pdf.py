from concurrent.futures import ThreadPoolExecutor
import requests
pool = ThreadPoolExecutor(100)

url = "http://d2zmdbbm9feqrf.cloudfront.net/2016/usa/pdf/{}.pdf"

sessions = [
dict(name = "ACI 1.2 CLI Configuration",
session_id = "LABACI-1010"),

dict(name = "ACI - Application Deployment with External Connectivity",
session_id = "LTRCRT-2611"),

dict(name = "ACI L4-L7 Practice Lab",
session_id = "LTRACI-2226"),

dict(name = "ACI L4-L7 Service Insertion with Unmanaged Mode",
session_id = "LABACI-2009"),

dict(name = "ACI Troubleshooting Hands On",
session_id = "LTRACI-3010"),

dict(name = "Add coding to networking skills and program REST API with Cisco and IoT",
session_id = "LTRCRT-2225"),

dict(name = "Advanced Enterprise WAN Design and Deployment",
session_id = "TECCRS-2500"),

dict(name = "Advanced Enterprise WLAN Deployment",
session_id = "TECEWN-3002"),

dict(name = "Advanced IWAN PfR w/QoS Hands on Lab",
session_id = "LTRRST-3015"),

dict(name = "Advanced Remote Access and Site-to-Site VPN design with IOS",
session_id = "TECSEC-3725"),

dict(name = "Advancing Your Network Management Architecture",
session_id = "TECNMS-2006"),

dict(name = "All your hypervisors are belong to ACI",
session_id = "TECACI-2400"),

dict(name = "An Immersive Journey into IPv6",
session_id = "TECRST-2166"),

dict(name = "APIC Enterprise Module - SDN in the Enterprise",
session_id = "TECSDN-3600"),

dict(name = "Application Centric Infrastructure (ACI) - The Policy Driven Data Center",
session_id = "TECACI-2009"),

dict(name = "Enterprise Module (APIC-EM): Hands-On Lab",
session_id = "LTRNMS-2500"),

dict(name = "Expressway 8.X",
session_id = "TECCOL-2223"),

dict(name = "Architecture Big Data and Analytics: From the IoT Edge to Data Center",
session_id = "TECAPP-1201"),

dict(name = "ASA Hands-on Troubleshooting Lab",
session_id = "LTRSEC-3021"),

dict(name = "ASA version 9.1 (and later) NAT Hands-on Configuration Lab",
session_id = "LTRSEC-3022"),

dict(name = "ASR 9000 Network Virtualization - nV Edge (Cluster)",
session_id = "LABARC-1011"),

dict(name = "ASR 9000 Network Virtualization - nV Satellite",
session_id = "LABARC-1012"),

dict(name = "ASR 9000 Operation and Troubleshooting",
session_id = "TECSPG-3001"),

dict(name = "BGP in the Enterprise for Fun and (fake) Profit: A Hands-On Lab",
session_id = "LTRRST-1179"),

dict(name = "Building and Migrating to Cisco's Intelligent WAN (IWAN)",
session_id = "LTRCRS-2005"),

dict(name = "CCDE Lab",
session_id = "LTRCCDE-3006"),

dict(name = "CCDE: The Cisco Certified Design Expert",
session_id = "TECCCDE-3005"),

dict(name = "CCIE Collaboration Lab",
session_id = "LTRCCIE-3504"),

dict(name = "CCIE Collaboration Techtorial",
session_id = "TECCCIE-3503"),

dict(name = "Express (UCCX)",
session_id = "LABCCIE-3020"),

dict(name = "Features",
session_id = "LABCCIE-3021"),

dict(name = "CCIE Collaboration - Troubleshooting UCM Call Routing",
session_id = "LABCCIE-3023"),

dict(name = "CCIE Collaboration - Troubleshooting Jabber Login",
session_id = "LABCCIE-3022"),

dict(name = "CCIE DC Techtorial",
session_id = "TECCCIE-3644"),

dict(name = "CCIE Routing and Switching - Configuration Assessment Lab",
session_id = "LABCCIE-2001"),

dict(name = "CCIE Routing and Switching - Diagnostic Practice Lab",
session_id = "LABCCIE-3015"),

dict(name = "CCIE Routing and Switching - Diagnostic Assessment Lab",
session_id = "LABCCIE-3016"),

dict(name = "CCIE Routing and Switching - DMVPN Technologies Practice Lab",
session_id = "LABCCIE-2014"),

dict(name = "CCIE Routing and Switching - IPv4 Technologies Practice Lab",
session_id = "LABCCIE-2009"),

dict(name = "CCIE Routing and Switching - IPv6 Technologies Practice Lab",
session_id = "LABCCIE-2010"),

dict(name = "CCIE Routing and Switching - Layer 2 Technologies Practice Lab",
session_id = "LABCCIE-2012"),

dict(name = "CCIE Routing and Switching - MPLS Technologies Practice Lab",
session_id = "LABCCIE-2013"),

dict(name = "CCIE Routing and Switching - Multicast Technologies Practice Lab",
session_id = "LABCCIE-2016"),

dict(name = "CCIE Routing and Switching Techtorial",
session_id = "TECCCIE-3000"),

dict(name = "CCIE Routing and Switching - Troubleshooting Practice Lab",
session_id = "LABCCIE-3014"),

dict(name = "CCIE Routing and Switching - Troubleshooting Assessment Lab",
session_id = "LABCCIE-1000"),

dict(name = "CCIE Routing & Switching - Infrastructure & Security Technologies",
session_id = "LABCCIE-2015"),

dict(name = "CCIE R&S v5 - Skills Evaluation and Preparation Approaches for the Lab Exam",
session_id = "LTRCCIE-3532"),

dict(name = "CCIE Security Techtorial",
session_id = "TECCCIE-3202"),

dict(name = "CCIE Service Provider",
session_id = "TECCCIE-3406"),

dict(name = "CCIE SP DIAG module",
session_id = "LABCCIE-3008"),

dict(name = "CCIE SP Practice Lab",
session_id = "LTRCCIE-3401"),

dict(name = "CCIE SP Troubleshoot - IPv4 and IPv6 Routing",
session_id = "LABCCIE-3009"),

dict(name = "CCIE SP Troubleshoot - MPLS",
session_id = "LABCCIE-3007"),

dict(name = "CCIE Wireless: Configure and Troubleshoot Wireless Security Policies",
session_id = "LABCCIE-1013"),

dict(name = "CCIE Wireless Techtorial",
session_id = "TECCCIE-3106"),

dict(name = "CCNP to CCIE Routing and Switching Bridge Labs",
session_id = "LABCCIE-2020"),

dict(name = "Troubleshooting Labs",
session_id = "LTRCCIE-3900"),

dict(name = "Cisco ASR 9000 vDDoS Protection Solution",
session_id = "LABSPG-2011"),

dict(name = "Cisco Collaboration Clients - Architecture and Design",
session_id = "TECCOL-2900"),

dict(name = "Cisco Contact Center Enterprise: Design, Deployment, and Troubleshooting",
session_id = "LTRCCT-3051"),

dict(name = "Troubleshooting",
session_id = "LTRCCT-2010"),

dict(name = "Cisco Data Center Instructor-Led Lab",
session_id = "LTRDCT-3077"),

dict(name = "digitalized business",
session_id = "TECCRS-2700"),

dict(name = "Cisco Enterprise NFV Deep Dive and Hands-On Lab",
session_id = "TECCRS-3006"),

dict(name = "Cisco IOS XR Programmability",
session_id = "LTRSPG-2601"),

dict(name = "Cisco Multiparty Video Design Guidance",
session_id = "TECCOL-2224"),

dict(name = "Cisco Open SDN Controller Hands-on Lab",
session_id = "LTRSDN-1913"),

dict(name = "Cisco Prime Collaboration Provisioning - Provisioning methods",
session_id = "LABUCC-2011"),

dict(name = "Cisco Prime Collaboration Provisioning Deployment and Best Practices",
session_id = "LTRUCC-3305"),

dict(name = "Cisco Security for Traditional and ACI Data Centers",
session_id = "TECSEC-4273"),

dict(name = "replication",
session_id = "LTRUCC-2150"),

dict(name = "Cisco Unified Communications Manager Serviceability and Troubleshooting",
session_id = "TECUCC-3000"),

dict(name = "Cisco Unified Computing System",
session_id = "TECCOM-2001"),

dict(name = "Cisco Virtualized Packet Core Installation on Openstack",
session_id = "LABSPM-2012"),

dict(name = "Cisco Virtualized Packet Core Installation on VMware",
session_id = "LABSPM-2011"),

dict(name = "Cloud Orchestration Tools to deploy applications on ACI",
session_id = "LABACI-1102"),

dict(name = "Configure and troubleshoot Unified CM/CME Mobility",
session_id = "LABCRT-1011"),

dict(name = "UCCX",
session_id = "LABCRT-1012"),

dict(name = "and WLC.",
session_id = "LABSEC-1011"),

dict(name = "Configuring Cisco Finesse IP Phone Agent Feature on UCCX 11.0.",
session_id = "LABCCT-2011"),

dict(name = "Controller (APIC)",
session_id = "LABACI-1003"),

dict(name = "Contact Center Enterprise Architecture & Design Workshop",
session_id = "TECCCT-3002"),

dict(name = "CUIC Scheduled reports with Email integration for UCCX",
session_id = "LABCCT-1011"),

dict(name = "Deep Dive Lab on ASA, FTD, and Firepower in ACI",
session_id = "LTRSEC-3001"),

dict(name = "APIC)",
session_id = "LABACI-1002"),

dict(name = "Deploying Call Manager Express for Jabber",
session_id = "LABUCC-1013"),

dict(name = "Deploying Cisco Cloud Services Router (CSR 1000V) in Public and Private Clouds",
session_id = "LTRVIR-2100"),

dict(name = "Deploying PKI for Today's Advanced Networks",
session_id = "TECSEC-2053"),

dict(name = "Communications Infrastructure",
session_id = "LTRCOL-1100"),

dict(name = "Deployment and Operation of BGP",
session_id = "TECRST-2310"),

dict(name = "Deployment Considerations for Interconnecting Distributed Virtual Data Centers",
session_id = "TECDCT-2181"),

dict(name = "Designing Fabric Based Networks",
session_id = "TECDCT-2405"),

dict(name = "Cisco IOS Routers",
session_id = "LABNMS-2400"),

dict(name = "DMVPN overlay routing for IWAN deployments",
session_id = "LABRST-2013"),

dict(name = "Dr. Evil's secret VIRL hands-on Lab",
session_id = "LTRRST-3003"),

dict(name = "Easy Network Virtualization using EVN",
session_id = "LABRST-2011"),

dict(name = "EIGRP Fundamentals: A Hands-On Lab",
session_id = "LTRRST-1178"),

dict(name = "Enhancing VXLAN/EVPN Fabrics with LISP",
session_id = "LTRDCT-2224"),

dict(name = "Enterprise Branch Threat Defense",
session_id = "LABSEC-2012"),

dict(name = "Enterprise High Availability Design and Architecture",
session_id = "TECCRS-2001"),

dict(name = "Enterprise MPLS Lab: Advanced Level",
session_id = "LTRMPL-3102"),

dict(name = "Enterprise SDN: Advanced Network Programming Hands-On Lab",
session_id = "LTRNMS-3602"),

dict(name = "Enterprise SDN: Architecture and Key Concepts",
session_id = "TECNMS-2602"),

dict(name = "Evolution in Catalyst Access Switching Technology - Hands On Lab",
session_id = "LTRCRS-2007"),

dict(name = "Evolution of Integrated Security with Cisco Threat Defense..",
session_id = "LABSEC-1012"),

dict(name = "Evolve your Datacenter with ACI",
session_id = "LTRACI-1210"),

dict(name = "Familiarize with HTML 5 - Cisco UCS New User Interface",
session_id = "LABDCT-1021"),

dict(name = "Firepower Tuning: Improving Detection and Performance",
session_id = "TECSEC-3000"),

dict(name = "FNF with multi vendors collectors",
session_id = "LABNMS-2300"),

dict(name = "Getting started with NfV using the CSP 2100",
session_id = "LABCLD-2011"),

dict(name = "Hacking in the Attack Kill Chain",
session_id = "LTRSEC-3002"),

dict(name = "automation",
session_id = "TECDCT-2941"),

dict(name = "Hunting for Evil: Security Monitoring with Cisco StealthWatch",
session_id = "LTRSEC-8421"),

dict(name = "Identity Services Engine 2.1 Best Practices",
session_id = "TECSEC-3672"),

dict(name = "IMC Supervisor - An introduction to managing standalone C-series servers",
session_id = "LABDCT-1006"),

dict(name = "Implementing and Understanding SIP Profiles",
session_id = "LABCOL-2011"),

dict(name = "Implementing Dynamic Multipoint VPN",
session_id = "LABIOT-2012"),

dict(name = "Implementing Inter-AS MPLS L3VPN Solutions",
session_id = "LABMPL-3011"),

dict(name = "Implementing Multicast Routing in Enterprise Network",
session_id = "LABIPM-1011"),

dict(name = "Implementing the Intelligent WAN (IWAN)",
session_id = "TECCRS-2004"),

dict(name = "Implementing VXLAN in a Data Center",
session_id = "LTRDCT-2223"),

dict(name = "Integrated Threat Defense - Solving for Time",
session_id = "TECSEC-2000"),

dict(name = "Introduction to IOS XR Operating System",
session_id = "LABRST-2000"),

dict(name = "Introduction to Performance Management with Cisco Prime NAM",
session_id = "LABNMS-1005"),

dict(name = "Introduction to Programming Cisco ACI with Python",
session_id = "LABACI-1011"),

dict(name = "Introduction to Programming Cisco ACI with REST and XML",
session_id = "LABACI-1012"),

dict(name = "Intro IPv6 Addressing and Routing Lab",
session_id = "LABCRS-1000"),

dict(name = "IOS FlexVPN Hands-on Lab",
session_id = "LTRSEC-2050"),

dict(name = "IPv6 in the Enterprise for Fun and (fake) Profit: A Hands-On Lab",
session_id = "LTRRST-2016"),

dict(name = "Learning BGP and RPL on IOS XR Operating System",
session_id = "LABRST-2001"),

dict(name = "Managing UCS environments with Cisco UCS Python SDK",
session_id = "LTRINI-2020"),

dict(name = "DC Tasks, Step-by-step.",
session_id = "TECACI-2000"),

dict(name = "Mastering Enterprise QoS 5.0 with the Four-Horsemen of the QoS-Apocalypse!",
session_id = "TECRST-2387"),

dict(name = "Infrastructure 3",
session_id = "LTRNMS-3002"),

dict(name = "Network Function Virtualization Seminar",
session_id = "TECSPG-2300"),

dict(name = "Next Generation Data Center Infrastructure",
session_id = "TECDCT-2002"),

dict(name = "Next Generation multicast - mVPN Rosen over P2MP TE",
session_id = "LABIPM-2011"),

dict(name = "Next Generation Service Provider Network using Segment Routing & BIER",
session_id = "LABSPG-2012"),

dict(name = "Nexus 9000 DevOps & Programmability Options",
session_id = "LTRDCT-1225"),

dict(name = "NFV Hands-on Deployment Lab",
session_id = "LTRSPG-2311"),

dict(name = "NX-OS Programming Lab",
session_id = "LABNMS-1023"),

dict(name = "Operating and Deploying NX-OS Nexus Devices in an evolving world",
session_id = "TECDCT-2821"),

dict(name = "Performance Management with Cisco Prime Infrastructure",
session_id = "LABNMS-2005"),

dict(name = "PFR-3 Lab Demo",
session_id = "LABRST-2003"),

dict(name = "PFRv3 troubleshooting techniques",
session_id = "LABRST-2012"),

dict(name = "Programmable VXLAN Fabric using VTS with OpenStack/VMware Integration",
session_id = "LTRDCN-2001"),

dict(name = "Protecting the Network with Firepower NGFW",
session_id = "LTRSEC-2101"),

dict(name = "QoS Policy propagation via BGP",
session_id = "LABRST-1011"),

dict(name = "SCYBER",
session_id = "LTRCRT-2910"),

dict(name = "SDN WAN Orchestration Principles and Solutions",
session_id = "TECMPL-3200"),

dict(name = "Security in Collaboration end to end",
session_id = "TECCOL-2345"),

dict(name = "Segment Routing in Datacenter using Nexus 9000/3000",
session_id = "LABRST-2020"),

dict(name = "Architecture",
session_id = "TECSAN-2301"),

dict(name = "Sun Tzu: CCIE R&S and the Art of Troubleshooting Lab - The Battlev5",
session_id = "LTRCCIE-3333"),

dict(name = "Test Drive MPLS and its Applications",
session_id = "LABMPL-2011"),

dict(name = "Tetration Analytics - Industry’s Powerful Analytics Platform",
session_id = "LABACI-3020"),

dict(name = "The Next Generation CCIE",
session_id = "TECCCIE-3352"),

dict(name = "Tools and Resources for IoT Embedded Systems",
session_id = "LABIOT-2011"),

dict(name = "Tools in Troubleshooting VoIP issues",
session_id = "LABCOL-1011"),

dict(name = "Troubleshooting & debugging OTV issues on N7K switch and ASR routers",
session_id = "LTRDCN-2200"),

dict(name = "UCSD-ACI 101",
session_id = "LABUCS-2018"),

dict(name = "UCS-D + ACI Advance Deployment Lab",
session_id = "LTRACI-2100"),

dict(name = "UCS Manager - Pools, Policies, and Profiles at scale.",
session_id = "LABUCC-2004"),

dict(name = "performance of Converged Infrastructure with UCSPM.",
session_id = "LABDCT-1005"),

dict(name = "Understanding OpenStack",
session_id = "TECCLD-2000"),

dict(name = "Understanding SIP and SDP Protocol",
session_id = "LABUCC-1011"),

dict(name = "Understanding VoIP Protocols",
session_id = "LABCOL-1012"),

dict(name = "Unified Collaboration Architecture",
session_id = "TECCOL-2982"),

dict(name = "Managing, and Deploying devices and Services",
session_id = "LTRSPG-2515"),

dict(name = "Virtual Packet Core Orchestration: Spring to Life Gateways and Services",
session_id = "LTRSPM-2022"),

dict(name = "Visibility Driven Secure Segmentation - Hands-on Lab",
session_id = "LTRCRS-2006"),

dict(name = "VOIP Protocol Debugging : Explore and Understand",
session_id = "LABUCC-1012"),

dict(name = "VxLAN Demo for extending vlans between datacenters",
session_id = "LABINI-2011"),

dict(name = "VXLAN on Nexus 1000v and CSR 1000v",
session_id = "LABRST-3016"),

dict(name = "Wireless Deployment and Design For Media-Rich Mobile Applications",
session_id = "TECEWN-3010"),
]

def dl(r):
    fn1 = '{}.pdf'.format(r['session_id'])
    fn2 = '{}-LG.pdf'.format(r['session_id'])
    d1 = requests.get(r['source'])
    d2 = requests.get(r['source_lg'])
    for name, data in [(fn1, d1), (fn2,d2)]:
        with open(name, 'wb') as fh:
            fh.write(data.content)
        print('done downloading {}'.format(name))

sess = pool.map(dl, sessions)
sess = list(sess)