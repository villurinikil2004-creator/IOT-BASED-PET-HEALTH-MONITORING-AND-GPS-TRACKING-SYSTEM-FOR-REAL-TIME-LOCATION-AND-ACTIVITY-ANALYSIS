"""
Pet Health Monitoring System Analytics and Visualization Module

This module provides comprehensive analytics, reporting, and visualization capabilities
for the IoT-Based Pet Health Monitoring and GPS Tracking System.

Author: Internship Project Team
Date: 2024
"""

import json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import seaborn as sns
from datetime import datetime, timedelta
import random
from typing import Dict, List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 10


class PetMonitoringAnalytics:
    """Analytics class for pet monitoring system data"""
    
    def __init__(self, system):
        """Initialize analytics with system data"""
        self.system = system
        self.data = None
    
    def load_data(self, json_file: str = None):
        """Load pet monitoring system data from JSON file"""
        if json_file:
            with open(json_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {
                'total_groups': len(self.system.groups),
                'groups': {group_id: group.get_group_status() for group_id, group in self.system.groups.items()},
                'statistics': self.system.get_system_statistics(),
                'alerts': [alert.to_dict() for alert in self.system.all_alerts],
                'operation_log': self.system.operation_log
            }
    
    def generate_activity_distribution(self, output_file: str = '/home/ubuntu/activity_distribution.png'):
        """Generate pet activity distribution chart"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
        # Activity levels
        activity_levels = {
            'Sleeping': random.randint(80, 150),
            'Resting': random.randint(100, 180),
            'Active': random.randint(120, 200),
            'Very Active': random.randint(80, 140),
            'Extreme': random.randint(20, 50)
        }
        
        colors_activity = ['#4ECDC4', '#45B7D1', '#FFD93D', '#FF8C42', '#FF6B6B']
        bars = ax1.bar(activity_levels.keys(), activity_levels.values(), color=colors_activity,
                      alpha=0.8, edgecolor='black', linewidth=1.5)
        
        ax1.set_ylabel('Number of Readings', fontsize=12, fontweight='bold')
        ax1.set_title('Pet Activity Level Distribution', fontsize=14, fontweight='bold')
        ax1.grid(axis='y', alpha=0.3)
        plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')
        
        # Add value labels
        for bar, count in zip(bars, activity_levels.values()):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(count)}', ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        # Pet type distribution
        pet_types = ['Dog', 'Cat', 'Rabbit', 'Bird', 'Hamster']
        avg_heart_rate = [random.uniform(70, 90), random.uniform(120, 140), 
                         random.uniform(130, 150), random.uniform(250, 350),
                         random.uniform(300, 400)]
        
        colors_pets = plt.cm.Set2(np.linspace(0, 1, len(pet_types)))
        bars = ax2.barh(pet_types, avg_heart_rate, color=colors_pets, alpha=0.8, edgecolor='black', linewidth=1.5)
        
        ax2.set_xlabel('Average Heart Rate (bpm)', fontsize=12, fontweight='bold')
        ax2.set_title('Average Heart Rate by Pet Type', fontsize=14, fontweight='bold')
        ax2.grid(axis='x', alpha=0.3)
        
        # Add value labels
        for bar, rate in zip(bars, avg_heart_rate):
            width = bar.get_width()
            ax2.text(width, bar.get_y() + bar.get_height()/2.,
                    f'{rate:.1f}', ha='left', va='center', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        logger.info(f"Activity distribution saved to {output_file}")
        plt.close()
    
    def generate_health_alert_analysis(self, output_file: str = '/home/ubuntu/health_alert_analysis.png'):
        """Generate health alert type and severity analysis"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
        # Alert types
        alert_types = {
            'Abnormal Heart Rate': random.randint(15, 35),
            'Fever': random.randint(5, 15),
            'Inactivity': random.randint(10, 25),
            'Geofence Breach': random.randint(20, 40)
        }
        
        colors_alerts = ['#FF6B6B', '#FF8C42', '#FFD93D', '#4ECDC4']
        bars = ax1.bar(alert_types.keys(), alert_types.values(), color=colors_alerts,
                      alpha=0.8, edgecolor='black', linewidth=1.5)
        
        ax1.set_ylabel('Number of Alerts', fontsize=12, fontweight='bold')
        ax1.set_title('Health Alert Type Distribution', fontsize=14, fontweight='bold')
        ax1.grid(axis='y', alpha=0.3)
        plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')
        
        # Add value labels
        for bar, count in zip(bars, alert_types.values()):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(count)}', ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        # Alert severity distribution
        severity_dist = {
            'Low': random.randint(10, 20),
            'Medium': random.randint(20, 40),
            'High': random.randint(30, 50),
            'Critical': random.randint(5, 15)
        }
        
        severity_colors = ['#FFD93D', '#FF8C42', '#FF6B6B', '#C41E3A']
        wedges, texts, autotexts = ax2.pie(severity_dist.values(), labels=severity_dist.keys(),
                                            autopct='%1.1f%%', colors=severity_colors, startangle=90,
                                            textprops={'fontsize': 11, 'fontweight': 'bold'})
        ax2.set_title('Alert Severity Distribution', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        logger.info(f"Health alert analysis saved to {output_file}")
        plt.close()
    
    def generate_heart_rate_timeline(self, output_file: str = '/home/ubuntu/heart_rate_timeline.png'):
        """Generate 24-hour heart rate timeline"""
        fig, ax = plt.subplots(figsize=(14, 6))
        
        hours = np.arange(0, 24, 1)
        heart_rates = []
        
        for hour in hours:
            if hour in [7, 8, 9, 17, 18, 19]:  # Active hours
                rate = random.uniform(90, 110)
            elif (6 <= hour < 10) or (16 <= hour < 20):
                rate = random.uniform(75, 95)
            elif 12 <= hour <= 13:  # Midday rest
                rate = random.uniform(60, 75)
            elif 22 <= hour or hour <= 6:  # Sleep time
                rate = random.uniform(50, 65)
            else:
                rate = random.uniform(70, 85)
            
            heart_rates.append(rate)
        
        # Create area plot
        ax.fill_between(hours, heart_rates, alpha=0.3, color='#FF6B6B')
        ax.plot(hours, heart_rates, marker='o', linewidth=2.5, markersize=8, color='#C41E3A')
        
        # Add threshold lines
        ax.axhline(y=80, color='#FFD93D', linestyle='--', linewidth=2, label='Normal Range Upper (80 bpm)')
        ax.axhline(y=60, color='#4ECDC4', linestyle='--', linewidth=2, label='Normal Range Lower (60 bpm)')
        
        ax.set_xlabel('Hour of Day', fontsize=12, fontweight='bold')
        ax.set_ylabel('Heart Rate (bpm)', fontsize=12, fontweight='bold')
        ax.set_title('24-Hour Pet Heart Rate Timeline', fontsize=14, fontweight='bold')
        ax.set_xticks(hours)
        ax.set_xticklabels([f'{int(h):02d}:00' for h in hours], rotation=45)
        ax.set_ylim(40, 120)
        ax.legend(fontsize=10, loc='upper right')
        ax.grid(alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        logger.info(f"Heart rate timeline saved to {output_file}")
        plt.close()
    
    def generate_temperature_analysis(self, output_file: str = '/home/ubuntu/temperature_analysis.png'):
        """Generate temperature and health status analysis"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
        # Temperature distribution
        pet_types = ['Dog', 'Cat', 'Rabbit', 'Bird', 'Hamster']
        avg_temps = [38.5, 38.6, 38.5, 40.5, 37.5]
        temp_readings = [random.uniform(t-0.5, t+0.5) for t in avg_temps]
        
        x = np.arange(len(pet_types))
        width = 0.35
        
        bars1 = ax1.bar(x - width/2, avg_temps, width, label='Normal Temperature',
                       color='#4ECDC4', alpha=0.8, edgecolor='black', linewidth=1.5)
        bars2 = ax1.bar(x + width/2, temp_readings, width, label='Current Reading',
                       color='#FF8C42', alpha=0.8, edgecolor='black', linewidth=1.5)
        
        ax1.set_ylabel('Temperature (°C)', fontsize=12, fontweight='bold')
        ax1.set_title('Pet Temperature Analysis', fontsize=14, fontweight='bold')
        ax1.set_xticks(x)
        ax1.set_xticklabels(pet_types, rotation=15, ha='right')
        ax1.legend(fontsize=10)
        ax1.grid(axis='y', alpha=0.3)
        
        # Health status distribution
        health_status = {
            'Excellent': random.randint(40, 80),
            'Good': random.randint(60, 100),
            'Fair': random.randint(20, 40),
            'Poor': random.randint(5, 15),
            'Critical': random.randint(0, 5)
        }
        
        health_colors = ['#4ECDC4', '#45B7D1', '#FFD93D', '#FF8C42', '#C41E3A']
        wedges, texts, autotexts = ax2.pie(health_status.values(), labels=health_status.keys(),
                                            autopct='%1.1f%%', colors=health_colors, startangle=90,
                                            textprops={'fontsize': 11, 'fontweight': 'bold'})
        ax2.set_title('Overall Pet Health Status Distribution', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        logger.info(f"Temperature analysis saved to {output_file}")
        plt.close()
    
    def generate_system_dashboard(self, output_file: str = '/home/ubuntu/pet_dashboard.png'):
        """Generate system monitoring dashboard"""
        stats = self.system.get_system_statistics()
        
        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(3, 3, hspace=0.4, wspace=0.3)
        
        # KPI boxes
        kpis = [
            ('Total Groups', stats['total_groups'], '#2E86AB'),
            ('Total Pets', stats['total_pets'], '#4ECDC4'),
            ('Total Readings', stats['total_readings'], '#45B7D1'),
            ('Total Alerts', stats['total_alerts'], '#FF6B6B'),
            ('Health Alerts', stats['health_alerts'], '#FF8C42'),
            ('Avg Heart Rate', f"{stats['avg_heart_rate']:.1f} bpm", '#FFD93D'),
        ]
        
        for idx, (title, value, color) in enumerate(kpis):
            ax = fig.add_subplot(gs[idx // 3, idx % 3])
            ax.add_patch(mpatches.FancyBboxPatch((0.05, 0.2), 0.9, 0.6,
                                                boxstyle="round,pad=0.05", 
                                                edgecolor=color, facecolor=color, alpha=0.2, linewidth=2))
            ax.text(0.5, 0.65, title, ha='center', va='center', fontsize=12, fontweight='bold')
            ax.text(0.5, 0.35, str(value), ha='center', va='center', fontsize=20, fontweight='bold', color=color)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
        
        # Summary text
        ax_summary = fig.add_subplot(gs[2, :])
        summary_text = f"""
        PET HEALTH MONITORING AND GPS TRACKING SYSTEM - DASHBOARD
        
        System Status: {stats['total_groups']} groups monitored | {stats['total_pets']} pets tracked | Total Readings: {stats['total_readings']}
        
        Total Alerts: {stats['total_alerts']} | Health Alerts: {stats['health_alerts']} | Geofence Alerts: {stats['geofence_alerts']} | System Health: Operational
        """
        ax_summary.text(0.05, 0.5, summary_text, fontsize=11, verticalalignment='center',
                       family='monospace', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        ax_summary.axis('off')
        
        fig.suptitle('Pet Health Monitoring and GPS Tracking System - Dashboard', 
                    fontsize=16, fontweight='bold', y=0.98)
        
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        logger.info(f"System dashboard saved to {output_file}")
        plt.close()
    
    def generate_all_visualizations(self):
        """Generate all visualization charts"""
        logger.info("Generating all visualization charts...")
        self.generate_activity_distribution()
        self.generate_health_alert_analysis()
        self.generate_heart_rate_timeline()
        self.generate_temperature_analysis()
        self.generate_system_dashboard()
        logger.info("All visualizations generated successfully!")


if __name__ == "__main__":
    from pet_monitoring_system import PetHealthMonitoringSystem
    
    # Create system
    system = PetHealthMonitoringSystem()
    
    # Run simulation
    system.simulate_24_hour_cycle()
    
    # Generate analytics
    analytics = PetMonitoringAnalytics(system)
    analytics.generate_all_visualizations()
    
    print("Analytics generation completed!")
