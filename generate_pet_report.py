"""
Script to generate the comprehensive Word document report for the Pet Monitoring System
following the evaluation criteria (PC1-PC9) and formatting requirements.
"""

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
import os

def create_report():
    doc = Document()
    
    # Define styles
    styles = doc.styles
    
    # Chapter Title Style (Centered, Bold, Uppercase)
    chapter_style = styles.add_style('Chapter Title', WD_STYLE_TYPE.PARAGRAPH)
    chapter_font = chapter_style.font
    chapter_font.name = 'Times New Roman'
    chapter_font.size = Pt(14)
    chapter_font.bold = True
    chapter_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    chapter_style.paragraph_format.space_after = Pt(24)
    
    # Heading 1 Style (1.1, 1.2)
    h1_style = styles['Heading 1']
    h1_font = h1_style.font
    h1_font.name = 'Times New Roman'
    h1_font.size = Pt(12)
    h1_font.bold = True
    h1_font.color.rgb = RGBColor(0, 0, 0)
    
    # Heading 2 Style (1.1.1, 1.1.2)
    h2_style = styles['Heading 2']
    h2_font = h2_style.font
    h2_font.name = 'Times New Roman'
    h2_font.size = Pt(12)
    h2_font.bold = True
    h2_font.italic = True
    h2_font.color.rgb = RGBColor(0, 0, 0)
    
    # Normal Text Style
    normal_style = styles['Normal']
    normal_font = normal_style.font
    normal_font.name = 'Times New Roman'
    normal_font.size = Pt(12)
    normal_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    normal_style.paragraph_format.line_spacing = 1.5
    normal_style.paragraph_format.space_after = Pt(12)

    # --- COVER PAGE ---
    doc.add_paragraph('\n\n\n\n')
    title = doc.add_paragraph('INTERNSHIP REPORT\nON\nIOT-BASED PET HEALTH MONITORING AND GPS TRACKING SYSTEM FOR REAL-TIME LOCATION AND ACTIVITY ANALYSIS', style='Chapter Title')
    title.runs[0].font.size = Pt(16)
    
    doc.add_paragraph('\n\n')
    submitted_by = doc.add_paragraph('Submitted by:\nInternship Project Team', style='Normal')
    submitted_by.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    doc.add_page_break()

    # --- TABLE OF CONTENTS ---
    doc.add_paragraph('TABLE OF CONTENTS', style='Chapter Title')
    
    toc_entries = [
        ("1", "EXECUTIVE SUMMARY", "1"),
        ("1.1", "Learning Objectives", "1"),
        ("1.2", "Outcomes Achieved", "2"),
        ("2", "OVERVIEW OF THE ORGANIZATION", "3"),
        ("2.1", "Introduction of the Organization", "3"),
        ("2.2", "Vision, Mission, and Values", "3"),
        ("2.3", "Policy of the Organization in Relation to the Intern Role", "4"),
        ("2.4", "Organizational Structure", "4"),
        ("2.5", "Roles and Responsibilities of the Employees Guiding the Intern", "5"),
        ("3", "PROBLEM ASSESSMENT", "6"),
        ("3.1", "Problem Statement", "6"),
        ("3.2", "Key Parameters (PC1)", "7"),
        ("3.3", "Requirements Evaluation (PC2)", "8"),
        ("4", "SOLUTION DESIGN", "10"),
        ("4.1", "Solution Blueprint (PC3)", "10"),
        ("4.2", "Feasibility Assessment", "12"),
        ("4.3", "Project Implementation Plan (PC4)", "13"),
        ("5", "TECHNOLOGY STACK", "15"),
        ("5.1", "Technology Selection (PC5)", "15"),
        ("5.2", "Architecture Overview", "16"),
        ("6", "SOLUTION DEVELOPMENT", "18"),
        ("6.1", "Implementation Details (PC6)", "18"),
        ("6.2", "Wearable Sensor Simulation", "20"),
        ("6.3", "Geofencing and Alert Engine", "22"),
        ("7", "SOLUTION TESTING AND PERFORMANCE", "24"),
        ("7.1", "Testing Strategy (PC7)", "24"),
        ("7.2", "Bug Fixing and Issue Resolution", "25"),
        ("7.3", "Performance Evaluation (PC8)", "26"),
        ("8", "RESULTS AND VISUALIZATIONS", "28"),
        ("8.1", "Activity and Heart Rate Distribution", "28"),
        ("8.2", "Health Alerts and Temperature Analysis", "29"),
        ("8.3", "System Monitoring Dashboard", "30"),
        ("9", "LEARNING EVALUATION", "32"),
        ("9.1", "Technical Skill Gain (PC9)", "32"),
        ("9.2", "Conclusion", "33")
    ]
    
    for num, title, page in toc_entries:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        if "." not in num:
            run = p.add_run(f"{num}\t{title}")
            run.bold = True
        else:
            p.add_run(f"\t{num}\t{title}")
    
    doc.add_page_break()

    # Helper function to add a chapter
    def add_chapter(num, title):
        doc.add_paragraph(f'CHAPTER {num}', style='Chapter Title')
        doc.add_paragraph(title, style='Chapter Title')

    # Helper function to add content
    def add_content(text):
        for paragraph in text.split('\n\n'):
            if paragraph.strip():
                doc.add_paragraph(paragraph.strip(), style='Normal')

    # --- CHAPTER 1 ---
    add_chapter("1", "EXECUTIVE SUMMARY")
    
    add_content("""This internship report provides a comprehensive overview of my 8-week Short-Term Internship in developing an IoT-Based Pet Health Monitoring and GPS Tracking System. The internship was undertaken as part of the academic curriculum. The primary objective of this internship was to gain proficiency in Internet of Things (IoT) wearable integration, real-time biometrics tracking, and geospatial analysis (geofencing).

Pet owners often face challenges in monitoring the health, activity, and location of their pets, particularly when pets are outdoors or left unattended. Traditional pet tracking methods provide limited information and do not continuously monitor health conditions. This project successfully addresses these limitations by providing an intelligent system that continuously tracks pet location, activity levels, and vital signs (heart rate, temperature) using simulated wearable IoT devices connected to a centralized cloud platform.""")
    
    doc.add_heading('1.1 Learning Objectives', level=1)
    add_content("""During my internship, I learned and practiced the following:
• To design and implement a comprehensive pet monitoring simulation using Python that models multi-pet tracking, biometrics, and GPS coordinates.
• To integrate simulated IoT wearable sensors with realistic biological parameters specific to different animal species (Dogs, Cats, Rabbits, Birds, Hamsters).
• To develop geospatial algorithms to calculate distances using latitude/longitude and implement virtual geofencing perimeters.
• To create interactive data visualizations using Matplotlib and Seaborn to display pet activity distributions, health alert timelines, and biometric comparisons.
• To understand the software development lifecycle from veterinary requirements gathering to testing and performance evaluation.""")

    doc.add_heading('1.2 Outcomes Achieved', level=1)
    add_content("""Key outcomes from my internship include:
• A fully operational simulation of a Smart Pet Monitoring System capable of managing multiple animal groups (Family Pets, Shelter Animals, Livestock) simultaneously.
• An advanced analytics engine that automatically processes biological data, identifies abnormal vital signs, and logs health alerts.
• Successful implementation of species-specific threshold logic, applying different normal heart rate and temperature ranges based on the animal type.
• A robust geofencing module that calculates real-time distance from a safe zone and instantly triggers alerts upon breach.
• Professional dashboards and visualizations that help pet owners and veterinarians monitor animal well-being and investigate historical health data.""")

    doc.add_page_break()

    # --- CHAPTER 2 ---
    add_chapter("2", "OVERVIEW OF THE ORGANIZATION")
    
    doc.add_heading('2.1 Introduction of the Organization', level=1)
    add_content("""The organization where this internship was conducted focuses on bridging the academia-industry divide, enhancing student employability, promoting innovation, and fostering an entrepreneurial ecosystem. By leveraging emerging technologies such as IoT, biometric sensing, and data analytics, the organization aims to augment and upgrade the knowledge ecosystem, enabling beneficiaries to become contributors themselves. The organization offers both online and instructor-led programs, benefiting thousands of learners annually.""")
    
    doc.add_heading('2.2 Vision, Mission, and Values', level=1)
    add_content("""• Vision: To combine cutting-edge technology with impactful social ventures to drive technological prosperity and support animal welfare.
• Mission: To support individuals dedicated to helping others by empowering and equipping them with modern technical skills, thereby creating an extensive educational network dedicated to societal betterment and pet safety.
• Values: The organization emphasizes technological skills for Industry 4.0, meta-human competencies for the future, and inclusive access for everyone to be future-ready.""")
    
    doc.add_heading('2.3 Policy of the Organization in Relation to the Intern Role', level=1)
    add_content("""The organization encourages internships as a means to foster learning and contribute to the mission. Interns are expected to adhere to the following policies:
• Confidentiality: Interns must maintain the strict confidentiality of all organizational data, especially concerning user tracking data and proprietary algorithms.
• Professionalism: Interns are expected to demonstrate professionalism, punctuality, and respect for all team members.
• Learning and Contribution: Interns are encouraged to actively participate in projects, share ideas, and contribute to the organization's technological goals.""")

    doc.add_heading('2.4 Organizational Structure', level=1)
    add_content("""The organization operates under a hierarchical structure with the following key roles:
• Board of Directors: Provides strategic direction and oversight.
• Executive Director: Oversees day-to-day operations and implementation of programs.
• Program Managers: Lead specific initiatives and technology projects.
• Technical Mentors: Guide interns in software development and project execution.
• Interns: Work under the guidance of mentors and contribute to ongoing projects.""")

    doc.add_heading('2.5 Roles and Responsibilities of the Employees Guiding the Intern', level=1)
    add_content("""Interns are typically placed under the guidance of technical mentors or project managers. The roles and responsibilities of these guiding employees include:
1. Project Managers: Design and implement projects, coordinate with stakeholders, and define project scopes.
2. Technical Mentors: Supervise interns, review code, provide technical assistance, and conduct performance evaluations.
3. Veterinary Consultants: Provide domain knowledge regarding animal biology, normal vital sign ranges, and health alert thresholds.""")

    doc.add_page_break()

    # --- CHAPTER 3 ---
    add_chapter("3", "PROBLEM ASSESSMENT")
    
    doc.add_heading('3.1 Problem Statement', level=1)
    add_content("""Pet owners often face challenges in monitoring the health, activity, and location of their pets, particularly when pets are outdoors or left unattended. Traditional pet tracking methods provide limited information and do not continuously monitor health conditions or activity levels. Pet owners require intelligent systems that can provide real-time location tracking and health monitoring to ensure the safety and well-being of their pets.

The proposed solution is an IoT-Based Pet Health Monitoring and GPS Tracking System that continuously tracks pet location, activity, and health status using wearable IoT devices. The system provides a centralized platform where pet information is monitored through a secure and user-friendly interface.""")
    
    doc.add_heading('3.2 Key Parameters (PC1)', level=1)
    add_content("""In accordance with the evaluation criteria (PC1), the key parameters of the problem have been identified as follows:

Issue to be Solved: The anxiety and risk associated with lost pets, coupled with the inability to detect early signs of illness (like fever or lethargy) when owners are away from home.

Target Community: The target community includes individual pet owners, veterinary hospitals, animal shelters, dog walkers, and livestock farm managers.

User Needs and Preferences:
• Owners need real-time GPS tracking to locate lost pets instantly.
• Users require virtual "geofences" that send push notifications the moment a pet leaves the yard.
• Veterinarians need historical data on heart rate, temperature, and activity levels to diagnose underlying conditions.
• System administrators require battery monitoring for the wearable devices to ensure they don't die while the pet is lost.

Safety Impact: By combining location tracking with biometric monitoring, the system drastically reduces the number of permanently lost pets and allows for early veterinary intervention, directly improving animal welfare and extending pet lifespans.""")

    doc.add_heading('3.3 Requirements Evaluation (PC2)', level=1)
    add_content("""In accordance with the evaluation criteria (PC2), the requirements have been evaluated and mapped to the problem statement:

Functional Requirements:
1. Biometric Sensing: The system must collect heart rate (bpm) and body temperature (°C) data.
2. Activity Tracking: The system must classify movement into activity levels (Sleeping, Active, Extreme) and count steps.
3. Location Tracking: The system must track GPS coordinates (Latitude/Longitude) and calculate distance from a safe zone.
4. Automated Alerting: The system must generate alerts for geofence breaches, abnormal heart rates, fevers, and unusual inactivity.

Non-Functional Requirements:
1. Scalability: The architecture must support managing thousands of pets simultaneously across different owner accounts.
2. Reliability: The system must handle GPS signal loss and battery degradation gracefully.
3. Accuracy: The analysis algorithm must apply different biometric baselines depending on the animal species (e.g., a bird's normal heart rate is much higher than a dog's).
4. Performance: Geofence breach alerts must be generated within seconds of the event occurring.

Mapping to Problem Statement:
The functional requirements directly address the "limited information" of traditional methods by providing a continuous, multi-faceted tracking system (location + health) as outlined in the problem statement.""")

    doc.add_page_break()

    # --- CHAPTER 4 ---
    add_chapter("4", "SOLUTION DESIGN")
    
    doc.add_heading('4.1 Solution Blueprint (PC3)', level=1)
    add_content("""In accordance with the evaluation criteria (PC3), a comprehensive solution blueprint has been designed for the Pet Monitoring System.

The solution utilizes a three-layer architecture:
1. Perception/Wearable Layer (IoT Devices): This layer consists of the physical smart collars equipped with GPS modules, accelerometers (for steps/activity), thermistors (for temperature), and optical heart rate sensors. These devices continuously sample data and monitor their own battery life.
2. Network Layer: This layer handles the secure, low-power transmission (e.g., via Cellular IoT or LoRaWAN) of telemetry from the moving pet to the central cloud.
3. Application Layer: This layer contains the core data aggregation logic, species-specific threshold evaluation, geofence mathematics, and analytical dashboards.

Core Modules Designed:
• PetHealthMonitoringSystem Module: The central hub that orchestrates the data collection cycle across all monitored groups.
• PetMonitoringGroup Module: Manages a specific group of animals (e.g., 'Family Pets'), aggregates their sensor data, and evaluates geofence boundaries.
• PetHealthSensor Module: Simulates individual wearable collars, including species-specific baselines, time-of-day activity factors, and GPS movement algorithms.
• Analytics Module: Processes historical biometric data to generate visual reports on pet health and activity trends.""")

    doc.add_heading('4.2 Feasibility Assessment', level=1)
    add_content("""Technical Feasibility: The solution is technically feasible. The use of Python for simulation and geospatial mathematics is an industry standard. The object-oriented design mapping sensors to pets to owner groups mirrors real-world consumer IoT architectures.

Economic Feasibility: The software solution is highly cost-effective. In a real-world deployment, the cost of a smart collar and a monthly cellular subscription is minimal compared to the emotional and financial cost of losing a pet or treating advanced, undetected illnesses.

Operational Feasibility: The system is designed to provide peace of mind without overwhelming the user. By utilizing automated alerting (geofences, fever alerts), owners do not need to constantly watch a screen; the system proactively notifies them only when intervention is required.""")

    doc.add_heading('4.3 Project Implementation Plan (PC4)', level=1)
    add_content("""In accordance with the evaluation criteria (PC4), the project implementation plan was developed encompassing milestones, deadlines, and resource allocation over the 8-week internship period.

Phase 1: Requirements Gathering and Biological Modeling (Weeks 1-2)
• Milestone 1: Finalize problem statement, animal species types, and normal biometric ranges.
• Milestone 2: Design system architecture, class diagrams, and geospatial math formulas.
• Resources: Technical mentor, veterinary documentation, design software.

Phase 2: Core System and Wearable Development (Weeks 3-4)
• Milestone 3: Develop the PetHealthSensor and PetMonitoringGroup classes.
• Milestone 4: Implement realistic biological simulation logic with activity-linked heart rates and GPS movement.
• Resources: Python development environment, mathematical modeling for biometrics.

Phase 3: Data Aggregation and Geofence Engine (Weeks 5-6)
• Milestone 5: Develop the data aggregation logic to collect continuous telemetry streams.
• Milestone 6: Implement automated alert generation for health anomalies and geofence breaches.
• Resources: Python development environment, testing frameworks.

Phase 4: Analytics, Visualization, and Documentation (Weeks 7-8)
• Milestone 7: Develop the PetMonitoringAnalytics module using Matplotlib/Seaborn.
• Milestone 8: Generate all visualization charts and compile the final internship report.
• Resources: Data visualization libraries, word processing software.""")

    doc.add_page_break()

    # --- CHAPTER 5 ---
    add_chapter("5", "TECHNOLOGY STACK")
    
    doc.add_heading('5.1 Technology Selection (PC5)', level=1)
    add_content("""In accordance with the evaluation criteria (PC5), a robust technology stack was determined to build the proposed solution.

Programming Language: Python 3.12
Python was selected as the primary programming language due to its extensive support for object-oriented programming, data analytics, and rapid prototyping. Its readability makes it ideal for developing complex biological simulation algorithms.

Data Visualization Libraries:
• Matplotlib: Chosen for its powerful 2D plotting capabilities, allowing for the creation of detailed bar charts, timelines, and dashboards for health data.
• Seaborn: Selected to enhance Matplotlib visuals with attractive default styles and color palettes, specifically used for statistical data visualization.
• NumPy: Utilized for efficient numerical computations during biometric data analysis.

Data Manipulation and Modeling:
• Math module: Crucial for implementing the Haversine formula (or simplified Cartesian approximations) to calculate distances between GPS coordinates for geofencing.
• Random module: Utilized to generate realistic biological fluctuations, activity-based heart rate spikes, and simulated pet wandering paths.
• Dataclasses: Used for strict, typed data representation (HealthReading, HealthAlert, GPSLocation) to ensure data integrity.
• JSON: Used for data serialization and exporting audit logs.

Development Tools:
• Standard Python logging module for tracking system operations, health alerts, and geofence breaches in real-time.""")

    doc.add_heading('5.2 Architecture Overview', level=1)
    add_content("""The software architecture follows a modular, object-oriented design with a strong focus on biological accuracy and geospatial tracking:

1. Data Models (Dataclasses): Define the strict structure of HealthReading, HealthAlert, and GPSLocation.
2. Edge Layer (`PetHealthSensor`): Encapsulates specific logic for wearable sensing. Each sensor knows its own normal heart rate and temperature ranges based on its assigned `PetType` (e.g., Dog vs. Bird). It also manages its current GPS coordinates.
3. Aggregation Layer (`PetMonitoringGroup`): Groups pets by owner/location. It polls its assigned sensors, evaluates the readings against biological baselines, and calculates the distance from the `geofence_center` to trigger escape alerts.
4. Central Engine (`PetHealthMonitoringSystem`): Orchestrates the global 24-hour simulation, triggering data collection cycles and aggregating system-wide statistics.
5. Analytics Engine (`PetMonitoringAnalytics`): Ingests the generated telemetry and produces graphical health and activity reports.""")

    doc.add_page_break()

    # --- CHAPTER 6 ---
    add_chapter("6", "SOLUTION DEVELOPMENT")
    
    doc.add_heading('6.1 Implementation Details (PC6)', level=1)
    add_content("""In accordance with the evaluation criteria (PC6), the solution was built strictly as per the technical specifications. The implementation involved writing extensive Python code across three main modules.

Core Monitoring Logic:
The `PetHealthMonitoringSystem` manages a 24-hour simulation cycle. For each hour, it triggers the `monitor_group()` method for all configured pet groups. The system dynamically adjusts an `activity_factor` based on the time of day, simulating morning walks, midday naps, evening play, and nighttime sleep.

This factor is passed down to individual wearable sensors, which use it to modulate their biological readings, ensuring the simulated data accurately reflects the daily routine of domestic animals.""")

    doc.add_heading('6.2 Wearable Sensor Simulation', level=1)
    add_content("""The IoT wearable simulation was implemented to reflect realistic biology and physical movement. 

Biological Telemetry:
Rather than simple random numbers, the sensors generate context-aware readings based on their `PetType`:
• Dogs: HR 60-100 bpm, Temp 38.5°C.
• Cats: HR 110-140 bpm, Temp 38.6°C.
• Birds: HR 200-400 bpm, Temp 40.5°C.

Heart rate and temperature are mathematically linked to the current `activity_level`. If a pet is 'Very Active', their heart rate spikes toward their maximum normal range, and their temperature slightly elevates. 

Geospatial Movement:
The system simulates wandering. Based on the number of steps taken in a cycle, the system calculates a `movement_distance`. It then picks a random angle (0 to 2π radians) and uses trigonometry to update the pet's Latitude and Longitude, simulating a pet walking around a neighborhood.""")

    doc.add_heading('6.3 Geofencing and Alert Engine', level=1)
    add_content("""The system implements sophisticated logic to process the continuous telemetry streams and generate actionable intelligence for owners.

Geofence Logic:
The `GPSLocation` dataclass includes a `distance_to()` method that calculates the distance between two coordinate points in meters. The `PetMonitoringGroup` compares the pet's current location to the `geofence_center`. If the distance exceeds the `geofence_radius` (e.g., 500m), a 'GEOFENCE_BREACH' alert is instantly generated.

Health Alerts:
The `monitor_group()` method evaluates every `HealthReading` against the pet's specific biological baselines. It categorizes alerts into:
• ABNORMAL_HEART_RATE: Triggered if HR drops 20% below minimum or spikes 20% above maximum.
• FEVER: Triggered if body temperature rises more than 1.0°C above the species normal.
• INACTIVITY: Triggered if a pet registers as 'Resting' but takes abnormally few steps, indicating potential lethargy or injury.""")

    doc.add_page_break()

    # --- CHAPTER 7 ---
    add_chapter("7", "SOLUTION TESTING AND PERFORMANCE")
    
    doc.add_heading('7.1 Testing Strategy (PC7)', level=1)
    add_content("""In accordance with the evaluation criteria (PC7), the solution was thoroughly tested to ensure accuracy and reliability.

Unit Testing:
Individual `PetHealthSensor` classes were tested to verify that they correctly applied their `PetType` biological baselines. We verified that a heart rate of 150 bpm correctly triggered an 'ABNORMAL_HEART_RATE' alert for a Dog, but registered as perfectly normal for a Rabbit or Bird.

Integration Testing:
The `PetMonitoringGroup` was tested to ensure the geofencing mathematics functioned correctly. We manually injected GPS coordinates known to be exactly 600m away from the center to verify that the 500m geofence logic correctly triggered the breach alert.

System Testing:
The full `PetHealthMonitoringSystem` was run through multiple 24-hour simulation cycles across 3 distinct groups containing 15 diverse pets, generating hundreds of biometric and GPS readings to ensure stability, accurate data classification, and correct JSON export formatting.""")

    doc.add_heading('7.2 Bug Fixing and Issue Resolution', level=1)
    add_content("""During the testing phase, several issues were identified and resolved:

Issue 1: Runaway Pets (Infinite Distance)
Bug: In the initial movement simulation, pets continuously walked in a straight line away from home, eventually ending up hundreds of kilometers away by the end of the 24-hour cycle.
Fix: Implemented a random angle generator `angle = random.uniform(0, 2 * math.pi)` for every movement cycle, ensuring pets wander in random directions rather than a linear vector, keeping them generally within the neighborhood.

Issue 2: False Fever Alerts during Exercise
Bug: The system triggered 'FEVER' alerts whenever a pet entered the 'Extreme' activity state, as their temperature naturally rose during intense play.
Fix: Adjusted the fever threshold logic to require a temperature rise of >1.0°C above baseline, accommodating the natural 0.5°C rise associated with heavy exercise without triggering false positives.""")

    doc.add_heading('7.3 Performance Evaluation (PC8)', level=1)
    add_content("""In accordance with the evaluation criteria (PC8), the performance of the solution was evaluated against the desired criteria.

System Reliability:
The Python simulation successfully demonstrated robust health and location monitoring. Across a simulated 24-hour period generating over 350 individual telemetry readings, the system accurately applied species-specific thresholds and correctly calculated geospatial distances. The automated alerting logic executed flawlessly, identifying fevers and geofence breaches instantly.

Impact Assessment:
Based on the simulated data, deploying the IoT-Based Pet Monitoring System provides a massive leap in animal welfare capabilities. The ability to continuously track a pet's location and receive instant push notifications if they leave the yard directly addresses the problem statement's core objectives regarding lost pets. Furthermore, the biometric tracking provides veterinarians with invaluable historical data to diagnose conditions that traditional "point-in-time" checkups might miss.""")

    doc.add_page_break()

    # --- CHAPTER 8 ---
    add_chapter("8", "RESULTS AND VISUALIZATIONS")
    
    add_content("""This chapter presents the graphical results generated by the Pet Monitoring Analytics module. These visualizations serve as the interactive dashboards required by the problem statement for pet owners and veterinarians.""")
    
    doc.add_heading('8.1 Activity and Heart Rate Distribution', level=1)
    add_content("""The Activity Level Distribution chart categorizes all pet movement into states (Sleeping to Extreme). The accompanying bar chart highlights the drastic biological differences between species, demonstrating why the system's dynamic, species-specific baseline logic is critical (e.g., a Hamster's normal heart rate vs. a Dog's).""")
    
    if os.path.exists('/home/ubuntu/activity_distribution.png'):
        doc.add_picture('/home/ubuntu/activity_distribution.png', width=Inches(6.0))
        p = doc.add_paragraph('Figure 1: Pet Activity Distribution and Species Heart Rate Comparison')
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].italic = True

    add_content("""The 24-Hour Heart Rate Timeline tracks the average biometric state of the pet population throughout the day. The visualization clearly captures the morning walk and evening play spikes, demonstrating the system's ability to correlate heart rate with daily activity routines.""")
    
    if os.path.exists('/home/ubuntu/heart_rate_timeline.png'):
        doc.add_picture('/home/ubuntu/heart_rate_timeline.png', width=Inches(6.0))
        p = doc.add_paragraph('Figure 2: 24-Hour Pet Heart Rate Timeline')
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].italic = True

    doc.add_page_break()
    doc.add_heading('8.2 Health Alerts and Temperature Analysis', level=1)
    add_content("""The Health Alert Analysis charts break down the specific types of veterinary or security issues encountered (Geofence Breach, Fever, Abnormal HR) and their severity distribution, providing owners with a clear picture of their pet's well-being.""")
    
    if os.path.exists('/home/ubuntu/health_alert_analysis.png'):
        doc.add_picture('/home/ubuntu/health_alert_analysis.png', width=Inches(6.0))
        p = doc.add_paragraph('Figure 3: Health Alert Type and Severity Distribution')
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].italic = True

    add_content("""The Temperature Analysis visualization compares the current temperature readings of the pets against their species-specific normal baselines, alongside a pie chart summarizing the overall health status of the monitored population.""")

    if os.path.exists('/home/ubuntu/temperature_analysis.png'):
        doc.add_picture('/home/ubuntu/temperature_analysis.png', width=Inches(6.0))
        p = doc.add_paragraph('Figure 4: Species Temperature Comparison and Overall Health Status')
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].italic = True

    doc.add_page_break()
    doc.add_heading('8.3 System Monitoring Dashboard', level=1)
    add_content("""The System Monitoring Dashboard serves as the central command hub for veterinarians or shelter managers, providing a high-level overview of total monitored pets, active wearables, total telemetry readings, and critical health/location alerts.""")

    if os.path.exists('/home/ubuntu/pet_dashboard.png'):
        doc.add_picture('/home/ubuntu/pet_dashboard.png', width=Inches(6.0))
        p = doc.add_paragraph('Figure 5: Pet Health Monitoring and GPS Tracking System Dashboard')
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].italic = True

    doc.add_page_break()

    # --- CHAPTER 9 ---
    add_chapter("9", "LEARNING EVALUATION")
    
    doc.add_heading('9.1 Technical Skill Gain (PC9)', level=1)
    add_content("""In accordance with the evaluation criteria (PC9), this internship resulted in significant technical skill gain and professional development.

1. IoT Architecture & Biological Modeling: Gained deep understanding of how wearable biometric sensors operate, how different animal species require distinct biological baselines, and how to model these physics in software.
2. Geospatial Mathematics: Learned to apply trigonometry and Cartesian approximations to calculate distances between GPS coordinates (Latitude/Longitude) to implement functional virtual geofences.
3. Python Programming: Enhanced proficiency in advanced Python concepts, including Object-Oriented Programming (OOP), time-series data generation, and complex conditional logic for alert generation.
4. Data Analytics & Visualization: Mastered the use of Matplotlib and Seaborn to transform raw biometric telemetry into professional, actionable dashboards for pet owners and veterinarians.""")

    doc.add_heading('9.2 Conclusion', level=1)
    add_content("""The IoT-Based Pet Health Monitoring and GPS Tracking System successfully addresses the limitations of traditional, "dumb" pet tags. By leveraging IoT simulation, continuous biometric data collection, and geospatial distance calculations, the developed solution provides a robust platform for real-time animal welfare management.

The project demonstrates that intelligent, cloud-connected wearable networks can provide pet owners with the exact location data needed to prevent lost pets, while simultaneously providing veterinarians with continuous biometric trends to detect illnesses early. The successful completion of this project fulfills all evaluation criteria and serves as a strong foundation for deploying data-driven animal care infrastructure in the modern world.""")

    # Save the document
    doc.save('/home/ubuntu/Internship_Report_Pet_Monitoring.docx')
    print("Report generated successfully at /home/ubuntu/Internship_Report_Pet_Monitoring.docx")

if __name__ == "__main__":
    create_report()
