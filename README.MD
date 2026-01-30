# 🔮 Habit/Addiction Predictor Dashboard

An AI-powered habit tracking and prediction dashboard that helps identify patterns, predict risk factors, and provide actionable insights for behavior change. Built with **Power BI** and **React** for comprehensive data analysis and visualization.

![Dashboard Preview](screenshots/dashboard_overview.png)

---

## 🚀 **Live Demo**

- **Interactive Dashboard**: [View on Vercel](https://habit-predictor-app.vercel.app/) ⚡
- **Power BI File**: Download `Habit-Predictor_pbi.pbix` to explore in Power BI Desktop
- **GitHub Repository**: [View Source](https://github.com/JackDatanerd/Habit-Predictor)

---

## ✨ **Features**

### 📊 **Overview Dashboard**
- **Success Rate Tracking**: Real-time calculation of habit success percentage
- **Current Streak Counter**: GitHub-style streak tracking for motivation
- **Risk Score Calculator**: Predictive risk assessment based on severity and patterns
- **Trigger Analysis**: Identify which triggers lead to failure
- **Time-of-Day Risk Mapping**: Discover when you're most vulnerable

### 📅 **GitHub-Style Heatmap Calendar**
- Visual representation of success/failure patterns over time
- Week-by-week breakdown with color-coded indicators
- Quick identification of streaks and relapse patterns

### 🎯 **Deep Analysis**
- **Severity Distribution**: Understand the intensity of urges over time
- **Habit Performance Matrix**: Cross-analysis of habits vs triggers
- **Monthly Trends**: Track improvement or decline over months
- **Duration Analysis**: Correlation between time spent and success rate

### 🔮 **Predictive Insights**
- **Risk Prediction**: AI-powered scoring based on historical patterns
- **Trend Indicators**: Improving vs declining performance signals
- **Most Dangerous Triggers**: Data-driven identification of high-risk factors
- **Optimal Success Times**: When you're most likely to succeed

---

## 🛠️ **Tech Stack**

### **Power BI Version**
- **Power BI Desktop**: Advanced data modeling and DAX calculations
- **DAX Formulas**: Custom measures for streak calculation, risk scoring, and trend analysis
- **Power Query**: Data transformation and cleaning
- **Custom Visuals**: Heatmap calendar, matrix visualizations, gauge charts

### **React Version**
- **React 18**: Modern component-based UI
- **Recharts**: Interactive, responsive charts
- **Tailwind CSS**: Utility-first styling
- **Lucide Icons**: Clean, modern iconography
- **Vite**: Fast build tool and dev server

### **Data Generation**
- **Python Script**: Automated sample data generator with realistic patterns
- **CSV Export**: Standard format for easy import

---

## 📁 **Project Structure**

```
Habit-Predictor/
├── data/
│   └── habit_predictor_data.csv                 # Sample dataset
├── scripts/
│   └── generate_habit_data.py         # Python data generator
├── screenshots/
│   ├── dashboard_overview.png
│   ├── deep_analysis.png
│   ├── predictive_insights.png
│   └── streak_tracker.png
├── habit_predictor_pbi.pbix               # Power BI file
├── habit_predictor_dashboard_pdf.pdf                # Exported PDF for quick preview
└── README.md                          # This file
```

---

## 🎯 **How to Use**
4. **Filter** by habit type to focus on specific behaviors
```bash
# Install Python (if not already installed)
# Navigate to project folder
python scripts/generate_habit_data.py

# Upload the generated habit_data.csv to the dashboard
```

---

## 📊 **Data Format**

|--------------|---------|--------------------------------------|----------------------|
| Date         | Date    | Date of the attempt                  | 2025-11-15           |
| Habit        | Text    | Type of habit being tracked          | Phone Overuse        |
| Trigger      | Text    | What triggered the urge              | Boredom              |
| Severity     | Number  | Intensity of urge (1-10)             | 7                    |
| Duration     | Number  | Minutes spent on habit               | 45                   |
| Result       | Text    | Outcome (Success/Fail)               | Fail                 |
| Time_of_Day  | Text    | When it occurred                     | Evening              |
| Notes        | Text    | Additional context (optional)        | Scrolled TikTok      |

**Habit Types**: Phone Overuse, Social Media, Gaming, Junk Food, Smoking, etc.  
**Result Values**: `Success`, `Fail`  
**Time Values**: `Morning`, `Afternoon`, `Evening`, `Night`

---

## 🔬 **Key Metrics & Calculations**

### **DAX Measures (Power BI)**

**Success Rate:**
```dax
Success Rate = 
DIVIDE(
    COUNTROWS(FILTER('habit_data', 'habit_data'[Result] = "Success")),
    COUNTROWS('habit_data'),
    0
)
```

**Risk Score:**
```dax
Risk Score = 
VAR AvgSeverity = AVERAGE('habit_data'[Severity])
VAR FailRate = 1 - [Success Rate]
RETURN
    (AvgSeverity / 10) * 0.6 + FailRate * 0.4
```

**Most Dangerous Trigger:**
```dax
Most Dangerous Trigger = 
VAR TriggerTable = 
    ADDCOLUMNS(
        VALUES('habit_data'[Trigger]),
        "@FailRate", 
            DIVIDE(
                CALCULATE(COUNTROWS('habit_data'), 'habit_data'[Result] = "Fail"),
                CALCULATE(COUNTROWS('habit_data'))
            )
    )
VAR MaxFailRate = MAXX(TriggerTable, [@FailRate])
RETURN
    MAXX(FILTER(TriggerTable, [@FailRate] = MaxFailRate), 'habit_data'[Trigger])
```

---

## 🎓 **Use Cases**

- **Personal Habit Tracking**: Monitor and improve daily habits
- **Addiction Recovery**: Track progress and identify relapse triggers
- **Behavioral Analysis**: Understand patterns in habit formation
- **Psychology Research**: Analyze behavioral data with advanced metrics
- **Portfolio Project**: Demonstrate data analysis and visualization skills

---

## 📸 **Screenshots**

### Overview Dashboard
![Overview](screenshots/dashboard_overview.png)

### Deep Analysis
![Heatmap](screenshots/deep_analysis.png)

### Streak Tracker
![Triggers](screenshots/streak_tracker.png)

### Predictive Insights
![Predictions](screenshots/predictive_insights.png)

---

## 🔧 **Customization**

### **Adding Your Own Data**

**Power BI:**
1. Open `habit_predictor_pbi.pbix`
2. Go to **Home → Transform Data**
3. Replace the data source with your CSV file
4. **Close & Apply**

**Web Dashboard:**
- Simply upload your CSV through the web interface
- Data is processed client-side (private and secure)

### **Modifying Visualizations**

- **Power BI**: Drag and drop fields to customize visuals
- **React**: Modify components in the source code

---

## 🐍 **Python Data Generator**

The included Python script generates realistic habit tracking data with:

- **Weighted probabilities** for time-of-day patterns
- **Severity-based fail rates** (higher severity = higher fail rate)
- **Contextual triggers** specific to each habit type
- **Realistic notes** based on success/failure
- **90 days of data** with ~3 entries per day

**Usage:**
```bash
python scripts/generate_habit_data.py
```

**Output:** `habit_data.csv` ready for immediate use

---

## 🤝 **Contributing**

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 **License**

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 **Author**

**Jack Ongogo**
- GitHub: [@JackDatanerd](https://github.com/JackDatanerd)
- LinkedIn: [Jack Omondi](https://linkedin.com/in/jack-ongogo-735015132/)

---

## 🙏 **Acknowledgments**

- Inspired by behavioral psychology research on habit formation
- GitHub contribution calendar design for streak visualization
- Power BI community for DAX formula insights
- React and Recharts documentation

---

## 📚 **Related Projects**

- [Performance Dashboard](https://github.com/JackDatanerd/Performance-Dashboard) - Employee performance analytics with Power BI and React

---

## 💡 **Future Enhancements**

- [ ] Machine learning prediction model for relapse risk
- [ ] Mobile app version for on-the-go tracking
- [ ] Social accountability features (anonymous groups)
- [ ] Gamification with achievements and rewards
- [ ] Export reports to PDF
- [ ] Integration with health tracking APIs

---

**⭐ If you found this project helpful, please consider giving it a star!**

---

## 🔗 **Quick Links**

- **Live Demo**: https://habit-predictor-app.vercel.app/
- **Source Code**: https://github.com/JackDatanerd/Habit-Predictor
- **Performance Dashboard**: https://github.com/JackDatanerd/Performance-DashboardYour CSV file should follow this structure:

| Column       | Type    | Description                          | Example              |
cd Habit-Predictor

# Run the data generator

### **Option 3: Generate Sample Data**


### **Option 1: Power BI Desktop**
3. **Explore** real-time analytics and insights

1. **Download Power BI Desktop** (free): [Download Here](https://powerbi.microsoft.com/desktop/)
2. **Upload your CSV** file with the required format (see below)
### **Option 2: Interactive Web Dashboard**

1. **Visit** [https://habit-predictor-app.vercel.app/](https://habit-predictor-app.vercel.app/)

