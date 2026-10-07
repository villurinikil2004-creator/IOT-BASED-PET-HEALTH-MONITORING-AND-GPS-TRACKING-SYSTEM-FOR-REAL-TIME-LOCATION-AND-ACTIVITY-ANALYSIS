"""
IoT-Based Pet Health Monitoring and GPS Tracking System
Main Module: Real-Time Pet Location, Activity, and Health Monitoring

This module implements a comprehensive pet monitoring system that simulates
real-time health tracking and GPS location monitoring for pets.

Author: Internship Project Team
Date: 2024
"""

import json
import random
import datetime
import math
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, asdict
from enum import Enum
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PetType(Enum):
    """Types of pets"""
    DOG = "Dog"
    CAT = "Cat"
    RABBIT = "Rabbit"
    BIRD = "Bird"
    HAMSTER = "Hamster"


class ActivityLevel(Enum):
    """Pet activity levels"""
    SLEEPING = "Sleeping"
    RESTING = "Resting"
    ACTIVE = "Active"
    VERY_ACTIVE = "Very Active"
    EXTREME = "Extreme"


class HealthStatus(Enum):
    """Pet health status"""
    EXCELLENT = "Excellent"
    GOOD = "Good"
    FAIR = "Fair"
    POOR = "Poor"
    CRITICAL = "Critical"


@dataclass
class GPSLocation:
    """GPS location data"""
    latitude: float
    longitude: float
    altitude: float = 0.0
    accuracy: float = 5.0  # meters
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'latitude': round(self.latitude, 6),
            'longitude': round(self.longitude, 6),
            'altitude': round(self.altitude, 2),
            'accuracy': round(self.accuracy, 2)
        }
    
    def distance_to(self, other: 'GPSLocation') -> float:
        """Calculate distance to another location in meters"""
        # Simplified distance calculation
        lat_diff = (self.latitude - other.latitude) * 111000
        lon_diff = (self.longitude - other.longitude) * 111000 * math.cos(math.radians(self.latitude))
        return math.sqrt(lat_diff**2 + lon_diff**2)


@dataclass
class HealthReading:
    """Data class representing a pet health reading"""
    reading_id: str
    timestamp: datetime.datetime
    pet_id: str
    pet_name: str
    pet_type: PetType
    heart_rate: int  # beats per minute
    body_temperature: float  # Celsius
    activity_level: ActivityLevel
    steps_count: int
    gps_location: GPSLocation
    battery_level: float
    signal_strength: int  # 0-5 bars
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'reading_id': self.reading_id,
            'timestamp': self.timestamp.isoformat(),
            'pet_id': self.pet_id,
            'pet_name': self.pet_name,
            'pet_type': self.pet_type.value,
            'heart_rate': self.heart_rate,
            'body_temperature': round(self.body_temperature, 2),
            'activity_level': self.activity_level.value,
            'steps_count': self.steps_count,
            'gps_location': self.gps_location.to_dict(),
            'battery_level': round(self.battery_level, 2),
            'signal_strength': self.signal_strength
        }


@dataclass
class HealthAlert:
    """Data class representing a pet health alert"""
    alert_id: str
    pet_id: str
    pet_name: str
    alert_type: str  # 'ABNORMAL_HEART_RATE', 'FEVER', 'INACTIVITY', 'GEOFENCE_BREACH'
    severity: str  # 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL'
    message: str
    timestamp: datetime.datetime
    value: float = 0.0
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'alert_id': self.alert_id,
            'pet_id': self.pet_id,
            'pet_name': self.pet_name,
            'alert_type': self.alert_type,
            'severity': self.severity,
            'message': self.message,
            'timestamp': self.timestamp.isoformat(),
            'value': round(self.value, 2)
        }


class PetHealthSensor:
    """Class representing a pet health monitoring sensor (wearable device)"""
    
    def __init__(self, pet_id: str, pet_name: str, pet_type: PetType, owner_name: str):
        """
        Initialize a pet health sensor
        
        Args:
            pet_id: Unique pet identifier
            pet_name: Pet's name
            pet_type: Type of pet
            owner_name: Owner's name
        """
        self.pet_id = pet_id
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.owner_name = owner_name
        self.readings: List[HealthReading] = []
        self.battery_level = 100.0
        self.is_functional = True
        self.reading_count = 0
        self.current_location = GPSLocation(40.7128 + random.uniform(-0.05, 0.05), 
                                           -74.0060 + random.uniform(-0.05, 0.05))
        
        # Set pet-specific health parameters
        self._set_pet_parameters()
    
    def _set_pet_parameters(self):
        """Set baseline health parameters based on pet type"""
        if self.pet_type == PetType.DOG:
            self.normal_heart_rate_min = 60
            self.normal_heart_rate_max = 100
            self.normal_temp = 38.5
            self.activity_factor = 0.8
        elif self.pet_type == PetType.CAT:
            self.normal_heart_rate_min = 110
            self.normal_heart_rate_max = 140
            self.normal_temp = 38.6
            self.activity_factor = 0.6
        elif self.pet_type == PetType.RABBIT:
            self.normal_heart_rate_min = 120
            self.normal_heart_rate_max = 150
            self.normal_temp = 38.5
            self.activity_factor = 0.7
        elif self.pet_type == PetType.BIRD:
            self.normal_heart_rate_min = 200
            self.normal_heart_rate_max = 400
            self.normal_temp = 40.5
            self.activity_factor = 0.9
        else:  # HAMSTER
            self.normal_heart_rate_min = 200
            self.normal_heart_rate_max = 500
            self.normal_temp = 37.5
            self.activity_factor = 0.7
    
    def take_reading(self, time_of_day: int = 12, activity_factor: float = 0.5) -> HealthReading:
        """
        Take a pet health reading
        
        Args:
            time_of_day: Hour of day (0-23)
            activity_factor: Factor representing activity level (0.0 = sleeping, 1.0 = very active)
            
        Returns:
            HealthReading object
        """
        timestamp = datetime.datetime.now()
        reading_id = f"PET_{self.pet_id}_{self.reading_count + 1}"
        
        # Determine activity level based on time and factor
        if activity_factor < 0.2:
            activity_level = ActivityLevel.SLEEPING
            steps = random.randint(0, 50)
        elif activity_factor < 0.4:
            activity_level = ActivityLevel.RESTING
            steps = random.randint(50, 200)
        elif activity_factor < 0.6:
            activity_level = ActivityLevel.ACTIVE
            steps = random.randint(200, 500)
        elif activity_factor < 0.8:
            activity_level = ActivityLevel.VERY_ACTIVE
            steps = random.randint(500, 1000)
        else:
            activity_level = ActivityLevel.EXTREME
            steps = random.randint(1000, 2000)
        
        # Calculate heart rate based on activity
        base_hr = (self.normal_heart_rate_min + self.normal_heart_rate_max) / 2
        hr_variation = (self.normal_heart_rate_max - self.normal_heart_rate_min) / 2
        heart_rate = int(base_hr + (activity_factor * hr_variation * 0.5) + random.uniform(-5, 5))
        
        # Calculate body temperature
        base_temp = self.normal_temp
        # Slight increase with activity
        temp_increase = activity_factor * 0.5
        body_temp = base_temp + temp_increase + random.uniform(-0.3, 0.3)
        
        # Update GPS location (simulate movement)
        movement_distance = steps * 0.5  # meters
        if movement_distance > 0:
            angle = random.uniform(0, 2 * math.pi)
            lat_change = (movement_distance / 111000) * math.cos(angle)
            lon_change = (movement_distance / (111000 * math.cos(math.radians(self.current_location.latitude)))) * math.sin(angle)
            self.current_location.latitude += lat_change
            self.current_location.longitude += lon_change
        
        # Create reading
        reading = HealthReading(
            reading_id=reading_id,
            timestamp=timestamp,
            pet_id=self.pet_id,
            pet_name=self.pet_name,
            pet_type=self.pet_type,
            heart_rate=heart_rate,
            body_temperature=body_temp,
            activity_level=activity_level,
            steps_count=steps,
            gps_location=self.current_location,
            battery_level=self.battery_level,
            signal_strength=random.randint(3, 5)
        )
        
        self.readings.append(reading)
        self.reading_count += 1
        
        # Update battery
        self.battery_level -= random.uniform(0.1, 0.3)
        if self.battery_level < 0:
            self.battery_level = 0
            self.is_functional = False
        
        return reading
    
    def get_sensor_status(self) -> Dict:
        """Get current sensor status"""
        return {
            'pet_id': self.pet_id,
            'pet_name': self.pet_name,
            'pet_type': self.pet_type.value,
            'owner_name': self.owner_name,
            'is_functional': self.is_functional,
            'battery_level': round(self.battery_level, 2),
            'total_readings': self.reading_count,
            'current_location': self.current_location.to_dict() if self.readings else None,
            'last_reading': self.readings[-1].to_dict() if self.readings else None
        }


class PetMonitoringGroup:
    """Class representing a group of pets being monitored"""
    
    def __init__(self, group_id: str, group_name: str):
        """
        Initialize a pet monitoring group
        
        Args:
            group_id: Group identifier
            group_name: Group name
        """
        self.group_id = group_id
        self.group_name = group_name
        self.pets: Dict[str, PetHealthSensor] = {}
        self.alerts: List[HealthAlert] = []
        self.geofence_center = GPSLocation(40.7128, -74.0060)
        self.geofence_radius = 500  # meters
        
        self._initialize_pets()
    
    def _initialize_pets(self):
        """Initialize pets for the group"""
        pet_configs = [
            ('DOG_001', 'Max', PetType.DOG, 'John Smith'),
            ('CAT_001', 'Whiskers', PetType.CAT, 'Jane Doe'),
            ('RABBIT_001', 'Fluffy', PetType.RABBIT, 'Bob Johnson'),
            ('BIRD_001', 'Tweety', PetType.BIRD, 'Alice Brown'),
            ('HAMSTER_001', 'Nibbles', PetType.HAMSTER, 'Charlie Wilson'),
        ]
        
        for pet_id, pet_name, pet_type, owner_name in pet_configs:
            sensor = PetHealthSensor(pet_id, pet_name, pet_type, owner_name)
            self.pets[pet_id] = sensor
    
    def monitor_group(self, hour: int = 12):
        """
        Monitor the group by reading all pet sensors
        
        Args:
            hour: Current hour of day (0-23)
        """
        activity_factor = 0.5
        
        # Adjust activity based on time of day
        if 7 <= hour <= 9:  # Morning activity
            activity_factor = 0.8
        elif 12 <= hour <= 14:  # Midday rest
            activity_factor = 0.3
        elif 17 <= hour <= 20:  # Evening activity
            activity_factor = 0.9
        elif 22 <= hour or hour <= 6:  # Night sleep
            activity_factor = 0.1
        else:
            activity_factor = 0.5
        
        for pet_id, sensor in self.pets.items():
            reading = sensor.take_reading(hour, activity_factor)
            
            # Check for health alerts
            self._check_health_alerts(sensor, reading)
            
            # Check for geofence breach
            self._check_geofence(sensor, reading)
    
    def _check_health_alerts(self, sensor: PetHealthSensor, reading: HealthReading):
        """Check for health-related alerts"""
        alert_id = f"ALERT_{len(self.alerts) + 1}"
        
        # Check heart rate
        if reading.heart_rate < sensor.normal_heart_rate_min * 0.8 or reading.heart_rate > sensor.normal_heart_rate_max * 1.2:
            alert = HealthAlert(
                alert_id=alert_id,
                pet_id=sensor.pet_id,
                pet_name=sensor.pet_name,
                alert_type='ABNORMAL_HEART_RATE',
                severity='HIGH' if reading.heart_rate > sensor.normal_heart_rate_max * 1.3 else 'MEDIUM',
                message=f"Abnormal heart rate detected for {sensor.pet_name}: {reading.heart_rate} bpm",
                timestamp=reading.timestamp,
                value=reading.heart_rate
            )
            self.alerts.append(alert)
            logger.warning(f"Health Alert: {alert.message}")
        
        # Check temperature
        if reading.body_temperature > sensor.normal_temp + 1.0:
            alert = HealthAlert(
                alert_id=alert_id,
                pet_id=sensor.pet_id,
                pet_name=sensor.pet_name,
                alert_type='FEVER',
                severity='CRITICAL' if reading.body_temperature > sensor.normal_temp + 2.0 else 'HIGH',
                message=f"Fever detected for {sensor.pet_name}: {reading.body_temperature}°C",
                timestamp=reading.timestamp,
                value=reading.body_temperature
            )
            self.alerts.append(alert)
            logger.warning(f"Health Alert: {alert.message}")
        
        # Check inactivity
        if reading.activity_level == ActivityLevel.SLEEPING and reading.steps_count < 10:
            # This is normal, no alert
            pass
        elif reading.activity_level == ActivityLevel.RESTING and reading.steps_count < 20:
            alert = HealthAlert(
                alert_id=alert_id,
                pet_id=sensor.pet_id,
                pet_name=sensor.pet_name,
                alert_type='INACTIVITY',
                severity='MEDIUM',
                message=f"Unusual inactivity detected for {sensor.pet_name}",
                timestamp=reading.timestamp,
                value=reading.steps_count
            )
            self.alerts.append(alert)
            logger.info(f"Activity Alert: {alert.message}")
    
    def _check_geofence(self, sensor: PetHealthSensor, reading: HealthReading):
        """Check for geofence breach"""
        distance = reading.gps_location.distance_to(self.geofence_center)
        
        if distance > self.geofence_radius:
            alert_id = f"ALERT_{len(self.alerts) + 1}"
            alert = HealthAlert(
                alert_id=alert_id,
                pet_id=sensor.pet_id,
                pet_name=sensor.pet_name,
                alert_type='GEOFENCE_BREACH',
                severity='HIGH',
                message=f"Geofence breach: {sensor.pet_name} is {distance:.1f}m away from home",
                timestamp=reading.timestamp,
                value=distance
            )
            self.alerts.append(alert)
            logger.warning(f"Geofence Alert: {alert.message}")
    
    def get_group_status(self) -> Dict:
        """Get current group status"""
        return {
            'group_id': self.group_id,
            'group_name': self.group_name,
            'total_pets': len(self.pets),
            'total_readings': sum(s.reading_count for s in self.pets.values()),
            'total_alerts': len(self.alerts),
            'health_alerts': len([a for a in self.alerts if a.alert_type in ['ABNORMAL_HEART_RATE', 'FEVER']]),
            'geofence_alerts': len([a for a in self.alerts if a.alert_type == 'GEOFENCE_BREACH'])
        }


class PetHealthMonitoringSystem:
    """Central pet health monitoring system"""
    
    def __init__(self):
        """Initialize the pet monitoring system"""
        self.groups: Dict[str, PetMonitoringGroup] = {}
        self.all_readings: List[HealthReading] = []
        self.all_alerts: List[HealthAlert] = []
        self.operation_log: List[Dict] = []
        
        self._initialize_groups()
        logger.info("Pet Health Monitoring System initialized")
    
    def _initialize_groups(self):
        """Initialize monitoring groups"""
        group_configs = [
            ('GROUP_01', 'Family Pets'),
            ('GROUP_02', 'Shelter Animals'),
            ('GROUP_03', 'Farm Livestock'),
        ]
        
        for group_id, group_name in group_configs:
            group = PetMonitoringGroup(group_id, group_name)
            self.groups[group_id] = group
    
    def simulate_24_hour_cycle(self):
        """Simulate a 24-hour pet monitoring cycle"""
        logger.info("Starting 24-hour pet monitoring simulation")
        
        for hour in range(24):
            for group_id, group in self.groups.items():
                group.monitor_group(hour)
                
                # Collect readings and alerts
                for pet_id, sensor in group.pets.items():
                    if sensor.readings:
                        self.all_readings.append(sensor.readings[-1])
                
                for alert in group.alerts:
                    if alert not in self.all_alerts:
                        self.all_alerts.append(alert)
            
            # Log hourly status
            self.operation_log.append({
                'timestamp': datetime.datetime.now().isoformat(),
                'hour': hour,
                'total_readings': len(self.all_readings),
                'total_alerts': len(self.all_alerts),
                'avg_heart_rate': self._calculate_avg_heart_rate()
            })
            
            logger.info(f"Hour {hour:02d}:00 - Readings: {len(self.all_readings)}, "
                       f"Alerts: {len(self.all_alerts)}")
        
        logger.info("24-hour simulation completed")
    
    def _calculate_avg_heart_rate(self) -> float:
        """Calculate average heart rate across all pets"""
        if not self.all_readings:
            return 0.0
        return sum(r.heart_rate for r in self.all_readings) / len(self.all_readings)
    
    def get_system_statistics(self) -> Dict:
        """Get system-wide statistics"""
        total_groups = len(self.groups)
        total_pets = sum(len(g.pets) for g in self.groups.values())
        
        # Count alert types
        alert_distribution = {}
        for alert in self.all_alerts:
            alert_distribution[alert.alert_type] = alert_distribution.get(alert.alert_type, 0) + 1
        
        # Activity distribution
        activity_dist = {}
        for reading in self.all_readings:
            activity = reading.activity_level.value
            activity_dist[activity] = activity_dist.get(activity, 0) + 1
        
        return {
            'total_groups': total_groups,
            'total_pets': total_pets,
            'total_readings': len(self.all_readings),
            'total_alerts': len(self.all_alerts),
            'health_alerts': len([a for a in self.all_alerts if a.alert_type in ['ABNORMAL_HEART_RATE', 'FEVER']]),
            'geofence_alerts': len([a for a in self.all_alerts if a.alert_type == 'GEOFENCE_BREACH']),
            'avg_heart_rate': round(self._calculate_avg_heart_rate(), 2),
            'alert_distribution': alert_distribution,
            'activity_distribution': activity_dist
        }
    
    def export_to_json(self, filename: str):
        """Export system data to JSON"""
        data = {
            'system_name': 'Pet Health Monitoring and GPS Tracking System',
            'total_groups': len(self.groups),
            'groups': {group_id: group.get_group_status() for group_id, group in self.groups.items()},
            'statistics': self.get_system_statistics(),
            'alerts': [alert.to_dict() for alert in self.all_alerts[-50:]],
            'operation_log': self.operation_log
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        logger.info(f"Data exported to {filename}")


if __name__ == "__main__":
    # Create pet monitoring system
    system = PetHealthMonitoringSystem()
    
    # Run simulation
    system.simulate_24_hour_cycle()
    
    # Get statistics
    stats = system.get_system_statistics()
    
    # Print report
    print("\n" + "="*60)
    print("PET HEALTH MONITORING SYSTEM - SIMULATION REPORT")
    print("="*60)
    print(json.dumps(stats, indent=2))
    
    # Export data
    system.export_to_json('/home/ubuntu/pet_monitoring_system_data.json')
