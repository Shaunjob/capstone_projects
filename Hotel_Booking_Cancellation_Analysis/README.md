# 🏨 Hotel Booking Cancellations — Exploratory Data Analysis

> An end-to-end Python EDA project uncovering the drivers behind high cancellation rates at City Hotel and Resort Hotel, with data-backed strategic recommendations.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Analysis Walkthrough](#analysis-walkthrough)
- [Key Findings](#key-findings)
- [Strategic Recommendations](#strategic-recommendations)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

---

## Project Overview

Both City Hotel and Resort Hotel have been experiencing persistently high booking cancellation rates, leading to significant revenue loss and poor room utilisation. This project performs a full exploratory data analysis (EDA) on historical reservation data to:

- Identify the key variables that drive cancellations
- Quantify the relationship between pricing (ADR) and cancellation behaviour
- Surface patterns by hotel type, month, country, and booking channel
- Deliver actionable business recommendations grounded in the data

---

## Dataset

**File:** `hotel_booking.csv`

The dataset covers hotel reservations from **2015 to 2017** across two property types: City Hotel and Resort Hotel.

| Column | Description |
|---|---|
| `hotel` | Hotel type — `City Hotel` or `Resort Hotel` |
| `is_canceled` | Cancellation flag — `0` = not cancelled, `1` = cancelled |
| `adr` | Average Daily Rate (room price per night) |
| `reservation_status_date` | Date the reservation status was last updated |
| `country` | Country of origin of the guest |
| `market_segment` | Booking channel — e.g. Online TA, Offline TA, Direct, Groups |
| `month` | Month derived from `reservation_status_date` |

> **Note:** PII columns (`name`, `email`, `phone-number`, `credit_card`) and sparse columns (`company`, `agent`) are dropped during preprocessing. Rows with fewer than ~500 missing values are removed as the dataset is large enough to absorb the loss.

---

## Project Structure

```
hotel-booking-analysis/
│
├── Hotel_Data_Analysis.ipynb   # Main analysis notebook
├── hotel_booking.csv           # Source dataset (not included — see Dataset section)
├── README.md                   # This file
```

---

## Installation & Setup

### Prerequisites

- Python 3.8+
- Jupyter Notebook or JupyterLab

### 1. Clone the repository

```bash
git clone https://github.com/your-username/hotel-booking-analysis.git
cd hotel-booking-analysis
```

### 2. Install dependencies

```bash
pip install pandas matplotlib seaborn
```

Or with a virtual environment:

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
pip install pandas matplotlib seaborn
```

### 3. Add the dataset

Place `hotel_booking.csv` in the project root directory.

### 4. Launch the notebook

```bash
jupyter notebook Hotel_Data_Analysis.ipynb
```

---

## Analysis Walkthrough

The notebook is organised into three main stages:

### Stage 1 — Data Loading & Cleaning
- Load `hotel_booking.csv` with pandas
- Drop PII and low-coverage columns (`company`, `agent`)
- Parse `reservation_status_date` to datetime
- Handle missing values and remove outliers in `adr` (cap at 5,000)
- Profile the dataset using `.info()`, `.describe()`, and `.isnull().sum()`

### Stage 2 — Exploratory Data Analysis & Visualisation

Seven analyses are performed, each paired with a visualisation:

| # | Analysis | Chart Type |
|---|---|---|
| 1 | Overall reservation status | Bar chart |
| 2 | Cancellation rate by hotel type | Count plot |
| 3 | Average Daily Rate over time — City vs. Resort | Line chart |
| 4 | Reservation status by month | Count plot |
| 5 | ADR for cancelled bookings by month | Bar chart |
| 6 | Top 10 countries by cancellations | Pie chart |
| 7 | ADR: cancelled vs. non-cancelled bookings | Line chart |

### Stage 3 — Insights & Recommendations
- Findings are synthesised against the three original hypotheses
- Business recommendations are derived directly from the data

---

## Key Findings

**37%** of all reservations are cancelled — a material revenue risk for both properties.

### 1. Price is the primary cancellation driver
Cancelled bookings consistently show a higher Average Daily Rate (ADR) than completed ones. Periods of peak pricing correlate directly with spikes in cancellation volume.

### 2. City Hotel has a higher cancellation rate
City Hotel cancellations reach **~41%**, compared to a lower rate for Resort Hotel — despite city hotels generally having lower ADR. Volume, not just price, amplifies the problem.

### 3. January is the highest-risk month
January records the highest cancellation-to-booking ratio. Resort Hotel spikes in ADR during weekends and holidays also create predictable cancellation windows.

### 4. Portugal leads all countries in cancellations
Among the top 10 source countries, Portugal accounts for the largest share of cancelled reservations.

### 5. Online Travel Agencies (OTAs) dominate — and cancel most
~46% of bookings come through OTAs. Cancelled reservations show a similar pattern, with ~47% originating from online channels — suggesting OTA listings or guest expectations may be misaligned with the actual product.

---

## Strategic Recommendations

| Recommendation | Rationale |
|---|---|
| **Implement dynamic pricing** — offer targeted discounts during high-ADR windows | Directly addresses the price–cancellation correlation |
| **Introduce weekend/holiday packages at Resort Hotel** | Counters ADR spikes that drive leisure cancellations |
| **Run a January demand campaign** | January has the highest cancellation ratio; marketing/promotions can stimulate commitment |
| **Develop a Portugal retention strategy** | Highest cancellation volume nationally; warrants localised service improvements and loyalty incentives |
| **Audit OTA listings** | 47% of cancellations come from online bookings — inaccurate representations may be inflating cancellation intent |

---

## Technologies Used

| Tool | Purpose |
|---|---|
| `pandas` | Data loading, cleaning, transformation |
| `matplotlib` | Base visualisation |
| `seaborn` | Statistical plots and styled visuals |
| `Jupyter Notebook` | Interactive analysis environment |

---

## Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

*Data covers the period 2015–2017. Findings are intended to inform strategic decisions rather than serve as a definitive causal study.*
