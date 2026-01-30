"""
Habit/Addiction Tracker - Sample Data Generator
Generates realistic habit tracking data with patterns for testing and demonstration
Author: Jack Omondi
"""

import csv
import random
from datetime import datetime, timedelta

# Configuration
HABITS = ['Phone Overuse', 'Social Media', 'Gaming', 'Junk Food', 'Smoking']
TRIGGERS = {
    'Phone Overuse': ['Boredom', 'Anxiety', 'FOMO', 'Procrastination', 'Morning Routine', 'Habit'],
    'Social Media': ['Loneliness', 'Comparison', 'FOMO', 'Boredom', 'Habit'],
    'Gaming': ['Escape', 'Avoidance', 'Boredom', 'Social', 'Reward'],
    'Junk Food': ['Stress', 'Emotional', 'Boredom', 'Hunger', 'Celebration'],
    'Smoking': ['Stress', 'Social', 'Routine', 'Trigger']
}
TIME_OF_DAY = ['Morning', 'Afternoon', 'Evening', 'Night']

# Weighted probabilities for realistic patterns
TIME_FAIL_WEIGHTS = {
    'Morning': 0.3,    # 30% fail rate in morning
    'Afternoon': 0.5,  # 50% fail rate in afternoon
    'Evening': 0.7,    # 70% fail rate in evening
    'Night': 0.85      # 85% fail rate at night (highest risk)
}

SEVERITY_FAIL_CORRELATION = {
    range(1, 4): 0.2,   # Low severity (1-3): 20% fail
    range(4, 7): 0.5,   # Medium severity (4-6): 50% fail
    range(7, 11): 0.85  # High severity (7-10): 85% fail
}

def get_fail_probability(severity, time_of_day):
    """Calculate fail probability based on severity and time"""
    severity_prob = next(prob for sev_range, prob in SEVERITY_FAIL_CORRELATION.items() if severity in sev_range)
    time_prob = TIME_FAIL_WEIGHTS[time_of_day]
    # Combine both factors (weighted average)
    return (severity_prob * 0.6) + (time_prob * 0.4)

def generate_entry(date, habit):
    """Generate a single habit tracking entry"""
    trigger = random.choice(TRIGGERS[habit])
    severity = random.randint(1, 10)
    
    # Weight severity toward medium-high for realism
    if random.random() < 0.6:
        severity = random.randint(5, 10)
    
    duration = random.randint(5, 120)
    time_of_day = random.choice(TIME_OF_DAY)
    
    # Determine success/fail based on patterns
    fail_prob = get_fail_probability(severity, time_of_day)
    result = 'Fail' if random.random() < fail_prob else 'Success'
    
    # Generate contextual notes
    notes_templates = {
        'Success': [
            'Resisted urge successfully',
            'Good control today',
            'Stayed disciplined',
            'Set boundaries',
            'Made good choice'
        ],
        'Fail': [
            f'Lost track of time',
            f'{trigger} was too strong',
            f'Couldn\'t resist',
            f'Need better strategies',
            f'High stress day'
        ]
    }
    notes = random.choice(notes_templates[result])
    
    return {
        'Date': date.strftime('%Y-%m-%d'),
        'Habit': habit,
        'Trigger': trigger,
        'Severity': severity,
        'Duration': duration,
        'Result': result,
        'Time_of_Day': time_of_day,
        'Notes': notes
    }

def generate_dataset(days=90, entries_per_day=3):
    """Generate full dataset with realistic patterns"""
    data = []
    start_date = datetime.now() - timedelta(days=days)
    
    print(f"Generating {days} days of habit tracking data...")
    print(f"Approximately {days * entries_per_day} total entries")
    print("-" * 50)
    
    for day in range(days):
        current_date = start_date + timedelta(days=day)
        
        # Vary entries per day (some days more active than others)
        num_entries = random.randint(entries_per_day - 1, entries_per_day + 2)
        
        # Select random habits for this day
        daily_habits = random.sample(HABITS, min(num_entries, len(HABITS)))
        
        for habit in daily_habits:
            entry = generate_entry(current_date, habit)
            data.append(entry)
    
    # Calculate statistics
    total_entries = len(data)
    success_count = sum(1 for entry in data if entry['Result'] == 'Success')
    success_rate = (success_count / total_entries) * 100
    
    print(f"\n✅ Dataset Generation Complete!")
    print(f"Total Entries: {total_entries}")
    print(f"Success Rate: {success_rate:.1f}%")
    print(f"Fail Rate: {100 - success_rate:.1f}%")
    print(f"Date Range: {data[0]['Date']} to {data[-1]['Date']}")
    
    return data

def save_to_csv(data, filename='habit_data.csv'):
    """Save dataset to CSV file"""
    fieldnames = ['Date', 'Habit', 'Trigger', 'Severity', 'Duration', 'Result', 'Time_of_Day', 'Notes']
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"\n💾 Data saved to: {filename}")
    print(f"Ready to upload to dashboard!")

def print_sample(data, n=5):
    """Print sample entries"""
    print(f"\n📋 Sample Entries (first {n}):")

if __name__ == "__main__":
    print("=" * 50)
    print("🔮 HABIT TRACKER - DATA GENERATOR")
    print("=" * 50)
    
    # Show sample
    save_to_csv(dataset)
    print("=" * 50)    
    print("\n🚀 Upload this file to the Habit Predictor Dashboard!")
    print("   Vercel: https://habit-predictor-app.vercel.app/")
    print_sample(dataset)
    
    # Save to CSV
    
    # Generate dataset
    dataset = generate_dataset(days=90, entries_per_day=3)
    print("-" * 100)
    for entry in data[:n]:
        print(f"{entry['Date']} | {entry['Habit']:15} | {entry['Trigger']:15} | Severity: {entry['Severity']:2} | {entry['Result']:7} | {entry['Time_of_Day']:10}")
