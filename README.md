# Job Listings Scraper & Analysis

##  Project Description
This project collects job listing data from online job portals and performs data analysis to understand job market trends such as role demand, location demand, and required skills.

##  Tools & Technologies
- Python
- BeautifulSoup
- Requests
- Pandas
- Matplotlib

##  Project Structure
- scraper/ → Scrapes job listings
- data/ → Stores raw and cleaned CSV files
- analysis/ → Data analysis and visualization
- README.md → Project documentation

##  Analysis Performed
- Job role distribution
- Location-wise job demand
- Skill demand analysis
- Data cleaning and preprocessing

##  Output
- Cleaned CSV datasets
- Bar charts showing job and skill trends
- Insights into in-demand job roles and skills

##  Visualizations

### Job Locations Distribution
![Location Chart](charts/location_chart.png)

### Job Roles Distribution
![Role Chart](charts/role_chart.png)

##  How to Run

1. Install libraries
pip install requests beautifulsoup4 pandas matplotlib

2. Run scraper
python scraper/job_scraper.py

3. Run analysis
python analysis/analysis.py

##  Conclusion
This project helps understand current job market requirements and supports data-driven career planning.

##  Author
Bhargavi Chinnaparapu
