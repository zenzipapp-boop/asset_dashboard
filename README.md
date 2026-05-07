# Asset Audit System

A web-based IT asset management and audit system built with FastAPI (Python) and a single-page HTML/JS frontend, backed by SQLite.

---

## Features

- **Dashboard** — Asset statistics, status breakdown, and distribution charts
- **Add Assets** — Form-based entry with auto-suggestions for vendors, locations, and types
- **Asset Registry** — Searchable, filterable table with inline edit and delete
- **Maintenance Log** — Track repairs, inspections, and servicing per asset
- **Excel Export** — Download all assets as a formatted `.xlsx` spreadsheet
- **GST Support** — Auto-calculates CGST/SGST (intra-state) or IGST (inter-state)

---

## Architecture

```
┌──────────────────────────────┐
│   Web Browser (Client)       │
│   index.html                 │
│   HTML / CSS / JavaScript    │
└──────────────┬───────────────┘
               │  HTTP / JSON
               ▼
┌──────────────────────────────┐
│   FastAPI Server (Backend)   │
│   app.py                     │
│   Async Python, auto-docs    │
└──────────────┬───────────────┘
               │  SQLAlchemy ORM
               ▼
┌──────────────────────────────┐
│   SQLite Database            │
│   assets.db                  │
└──────────────────────────────┘
```

**Stack:** FastAPI · SQLAlchemy 2 · SQLite · openpyxl · Vanilla JS

---

## Setup Guide

### Prerequisites

- **Python 3.8 or higher** — [Download](https://www.python.org/downloads/)
- **pip** — Included with Python 3.4+
- A modern web browser (Chrome, Firefox, Edge)

Verify your Python version:
```bash
python --version
```

---

### Step 1 — Clone or Download the Project

If you have the project as a zip, extract it to a folder of your choice. Then open a terminal in that folder.

```bash
cd path/to/excel
```

---

### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:

| Package | Version | Purpose |
|---|---|---|
| fastapi | >=0.100.0 | Web framework and REST API |
| uvicorn | >=0.20.0 | ASGI server to run FastAPI |
| sqlalchemy | >=2.0.0 | ORM for database access |
| openpyxl | >=3.1.5 | Excel file generation |
| python-multipart | >=0.0.6 | Form data parsing |

---

### Step 3 — Start the Server

**Option A — Automatic (recommended):**
Opens the browser automatically.
```bash
python run.py
```

**Option B — Windows batch file:**
Double-click `START_SERVER.bat`, or run:
```bash
START_SERVER.bat
```

**Option C — Manual with uvicorn:**
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

---

### Step 4 — Open the App

Once the server is running, open your browser and go to:

```
http://localhost:8000
```

To stop the server, press `Ctrl + C` in the terminal.

---

### Optional — API Documentation

FastAPI generates interactive API docs automatically:

| Interface | URL |
|---|---|
| Swagger UI | `http://localhost:8000/docs` |
| ReDoc | `http://localhost:8000/redoc` |

---

## Usage

### Adding an Asset
1. Click the **New Asset** tab in the sidebar.
2. Fill in the required fields (name, type, date of purchase, value, status, location).
3. Add serial numbers if the quantity is greater than one.
4. Click **Save Asset**.

### Browsing Assets
1. Click the **All Assets** tab.
2. Use the search bar to find assets by name or serial number.
3. Filter by **Status**, **Type**, or **Location** using the dropdowns.
4. Use the **Edit** or **Delete** buttons on any row to modify records.

### Exporting to Excel
1. Click the **Export** tab.
2. Click **Export to Excel**.
3. The file `exported_assets.xlsx` will be downloaded with formatted headers, alternating row colours, frozen panes, and auto-filters.

### Maintenance Log
1. Navigate to the **Maintenance** tab.
2. Create entries for repairs, inspections, or scheduled servicing.
3. Each entry links to an asset and tracks date, technician, cost, and status.

---

## API Reference

### Assets

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/assets` | List all assets (supports search, filter, pagination) |
| `GET` | `/api/assets/{id}` | Get a single asset by ID |
| `POST` | `/api/assets` | Create a new asset |
| `PUT` | `/api/assets/{id}` | Update an existing asset |
| `DELETE` | `/api/assets/{id}` | Delete an asset |

**Query parameters for `GET /api/assets`:**

| Parameter | Type | Description |
|---|---|---|
| `search` | string | Filter by asset name or serial number |
| `status` | string | Filter by status (Functional / Non-Functional / Condemned) |
| `asset_type` | string | Filter by asset type |
| `location` | string | Filter by location |
| `skip` | integer | Pagination offset (default: 0) |
| `limit` | integer | Page size (default: 50) |

### Statistics & Options

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/stats` | Dashboard statistics (counts, totals, distributions) |
| `GET` | `/api/options` | Dropdown option lists (vendors, locations, types) |
| `POST` | `/api/export-excel` | Generate and download the Excel export |

### Maintenance

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/maintenance` | List all maintenance entries |
| `GET` | `/api/assets/{id}/maintenance` | Get maintenance history for a specific asset |
| `POST` | `/api/maintenance` | Create a maintenance entry |
| `PUT` | `/api/maintenance/{id}` | Update a maintenance entry |
| `DELETE` | `/api/maintenance/{id}` | Delete a maintenance entry |

---

## Database Schema

### Asset Table

| Column | Type | Description |
|---|---|---|
| id | Integer | Primary key (auto-increment) |
| sl_no | Integer | Serial list number (unique) |
| asset_name | String | Equipment name |
| asset_type | String | Type (Laptop, Desktop, Tab, etc.) |
| si_no | String | Manufacturer serial / model number |
| dop | String | Date of purchase (DD/MM/YYYY) |
| age | String | Calculated age (e.g., "3 yrs 4 mo") |
| quantity | Integer | Number of units |
| vendor | String | Vendor / supplier name |
| value | Float | Purchase value (₹) |
| base_price | Float | Pre-GST price |
| location | String | Physical location |
| department | String | Department or project |
| purchased_from | String | Fund source |
| status | String | Functional / Non-Functional / Condemned |
| disposed | Boolean | Whether the asset has been disposed |
| disposal_reason | String | Reason for disposal |
| gst_applicable | Boolean | Whether GST applies |
| gst_mode | String | Intra-state or Inter-state |
| gst_rate | Float | GST rate (%) |
| gst_amount | Float | Total GST amount (₹) |
| created_at | DateTime | Record creation timestamp |
| updated_at | DateTime | Last updated timestamp |

### MaintenanceLog Table

| Column | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| asset_id | Integer | Foreign key → Asset |
| entry_type | String | Repair / Inspection / Scheduled / Discarded |
| date | String | Date of maintenance |
| technician | String | Technician or vendor name |
| notes | String | Description of work done |
| cost | Float | Cost of maintenance (₹) |
| scrap_value | Float | Scrap value if disposed |
| status | String | Pending / In Progress / Completed |
| created_at | DateTime | Record creation timestamp |
| updated_at | DateTime | Last updated timestamp |

---

## Troubleshooting

**Port 8000 already in use:**
```bash
uvicorn app:app --host 0.0.0.0 --port 8001
```
Then access the app at `http://localhost:8001`.

**`assets.db` not found:**
Ensure `assets.db` is present in the same directory as `app.py`. The database file must exist before starting the server.

**Database locked error:**
Close any other process that may have the database open (e.g., a database browser), then restart the server.

**CORS errors in browser:**
CORS is enabled for all origins in `app.py`. If you are accessing the app from a different host, ensure the `API_URL` constant in `index.html` matches the server address.

**Dependencies not installing:**
Try upgrading pip first:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
