# Business Card Data Extraction using EasyOCR and Streamlit

## Overview

This project is an **OCR-based Business Card Data Extraction System** that automatically extracts information from business card images using **EasyOCR**. The extracted information is processed using regular expressions, structured into meaningful fields, and stored in an **SQLite database**.

The application is developed using **Streamlit**, providing an interactive interface for:

- Uploading business card images
- Extracting text using OCR
- Storing extracted information
- Viewing saved records
- Updating existing records
- Deleting records

---

# Problem Statement

Business cards contain valuable contact information, but manually entering this information into databases is time-consuming and prone to errors.

This project automates the process by:

- Extracting text from business card images
- Identifying important fields
- Storing structured information
- Allowing users to manage records efficiently

---

# Features

- OCR-based business card text extraction
- Automatic information parsing using Regular Expressions
- SQLite database integration
- Interactive Streamlit dashboard
- Update existing records
- Delete unwanted records
- Display extracted information in tabular format

---

# Technologies Used

### Programming Language

- Python

### OCR

- EasyOCR

### Database

- SQLite

### Web Framework

- Streamlit

### Data Processing

- Pandas
- Regular Expressions (Regex)

### Image Processing

- Pillow (PIL)

---

# Project Workflow

## 1. Image Upload

The user provides a business card image.

↓

## 2. OCR Extraction

EasyOCR extracts text from the image.

↓

## 3. Information Parsing

Regular expressions identify:

- Company Name
- Card Holder Name
- Designation
- Mobile Number
- Email Address
- Website
- Area
- City
- State
- PIN Code

↓

## 4. Database Storage

The structured information is stored in SQLite.

↓

## 5. Data Management

Users can:

- View records
- Update records
- Delete records

---

# System Architecture

```text
                 Business Card Image
                         │
                         ▼
                EasyOCR Text Extraction
                         │
                         ▼
              Text Preprocessing & Regex
                         │
                         ▼
              Structured Information
                         │
                         ▼
                  SQLite Database
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
    View Records     Update Data    Delete Data
                         │
                         ▼
                 Streamlit Dashboard
```

---

# Application Modules

## Home

Displays sample business card images and instructions for using the application.

---

## Extract & Upload

Functions:

- Read business card image
- Extract text using EasyOCR
- Parse extracted text
- Display structured information
- Save data into SQLite database

---

## Data Modification

Allows users to:

- View stored business card records
- Update selected fields
- Delete unwanted records

---

# Database Schema

## Table: biz1_details

| Column | Description |
|----------|-------------|
| company_name | Company Name |
| card_holder | Card Holder Name |
| designation | Job Title |
| mobile_number | Contact Number |
| email | Email Address (Primary Key) |
| website | Website |
| area | Area |
| city | City |
| state | State |
| pin_code | PIN Code |
| image | Business Card Image |

---

# OCR Extraction Pipeline

```text
Business Card Image
        │
        ▼
EasyOCR Reader
        │
        ▼
Extracted Text
        │
        ▼
Regex Pattern Matching
        │
        ▼
Structured Fields
        │
        ▼
SQLite Database
```

---

# Project Structure

```text
Business-Card-Data-Extraction

│
├── app.py
├── bizD.db
├── requirements.txt
├── README.md
├── images/
│
└── assets/
```

---

# Key Functionalities

### OCR Extraction

- Reads business card images
- Detects English text
- Extracts complete card information

### Information Parsing

Automatically identifies:

- Company Name
- Person Name
- Designation
- Phone Number
- Email
- Website
- Address Details

### Database Operations

- Insert
- Read
- Update
- Delete (CRUD)

---

# User Interface

The Streamlit application consists of three pages:

### Home

- Application introduction
- Sample business card images

### Extract & Upload

- Image input
- OCR extraction
- SQL upload

### Data Modification

- View database
- Update records
- Delete records

---

# Technology Stack

- Python
- Streamlit
- EasyOCR
- SQLite
- Pandas
- Pillow
- Regular Expressions

---

# Future Improvements

- Drag-and-drop image upload
- Multi-language OCR support
- Support for multiple business cards in one image
- Export data to CSV and Excel
- Cloud database integration (MySQL/PostgreSQL)
- REST API using FastAPI
- Business card image preprocessing for higher OCR accuracy

---

# Key Learning Outcomes

- Optical Character Recognition (OCR)
- Image Processing
- Text Parsing using Regex
- SQLite Database Management
- CRUD Operations
- Streamlit Application Development
- Data Extraction Automation

---

# Author

**SRISHHA**
