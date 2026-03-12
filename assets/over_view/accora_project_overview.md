# Project Overview / نظرة عامة على المشروع

## Project Name | اسم المشروع
**Accora - Development & Real Estate CRM**
*(نظام إدارة علاقات العملاء العقارية والتطوير - أكورا)*

---

## Short Description | وصف قصير
A comprehensive bilingual Customer Relationship Management (CRM) web application designed specifically for the real estate and automotive sectors. It empowers admin and sales teams to manage leads, track interactions, handle inventory (properties and vehicles), and schedule appointments, featuring robust data import tools and analytics.

---

## Medium Description | وصف متوسط
Accora is a specialized CRM platform tailored for real estate developers and automotive dealerships to streamline their sales processes. The system provides role-based access control (Admin, Sales) to manage the entire sales funnel from lead acquisition to closing. It features advanced lead management capabilities including bulk import with duplicate resolution, detailed interaction tracking, and appointment scheduling via an integrated FullCalendar. Additionally, it offers comprehensive inventory management for real estate units (types, finishing, delivery status) and automotive models (brands, cars, trims), alongside financial configurations like banks, payment methods, and installment systems. The platform is fully bilingual (Arabic/English) to serve the MENA market effectively, complete with interactive sales dashboards and PDF report generation.

---

## Technologies & Packages | التقنيات والحزم المستخدمة

### **Backend (الباك إند):**
*   **Framework:** Laravel 10 (PHP 8.1+)
*   **Database:** MySQL
*   **Core Packages:**
    *   `spatie/laravel-permission`: For Role-Based Access Control (Admin, Sales).
    *   `maatwebsite/excel`: For importing and exporting Leads data.
    *   `barryvdh/laravel-dompdf`: For generating PDF reports and analytics exports.
    *   `silviolleite/laravelpwa`: For Progressive Web App (PWA) capabilities.
    *   `gemini-api-php/client`: For AI integration and smart features.
    *   `laravel/sanctum`: For secure API authentication.

### **Frontend (الفرونت إند):**
*   **Core:** HTML5, CSS3, JavaScript.
*   **Styling:** Bootstrap 5 & Custom CSS styling (Admin Dashboard theme).
*   **Build Tool:** Vite.
*   **Calendar:** FullCalendar.js for interactive appointment scheduling.
*   **Icons:** FontAwesome & Bootstrap Icons.

### **Integrations & Automation (التكامل والأتمتة):**
*   **Automated Duplicate Resolution:** Smart logic to handle lead duplicate conflicts during bulk Excel imports.
*   **Email Sending:** Configurable email system via SMTP for notifications.
*   **Calendar API:** Custom API endpoints feeding real-time events to the frontend calendar.

---

## Key Features | الميزات الأساسية
1.  **Lead Management & Import**: Advanced lead tracking, interaction logging, and an intelligent Excel import tool with a duplicate resolution center.
2.  **Dual Inventory System**: Seamlessly manage real estate properties (Units, Finishing Types) and automotive inventory (Brands, Cars, Trims) in one unified system.
3.  **Interactive Master Calendar**: Integrated FullCalendar for sales representatives and admins to track meetings, site visits, and client appointments.
4.  **Sales & Admin Dashboards**: Dedicated UI dashboards providing real-time analytics, metrics, and PDF reporting capabilities for performance tracking.
5.  **Financial & Booking Configurations**: Flexible setup for Banks, Installment Systems, Offer Types, and Delivery Statuses to accommodate diverse sales operations.
6.  **Role-Based Access Control**: Securely partitions workflows between Root/Admins and Sales Reps using Spatie Permissions.
7.  **Bilingual Enterprise Interface**: Fully localized interface holding dynamic session-based language switching (Arabic/English).

---

## Challenges & Solutions | التحديات والحلول
*   **Challenge 1 (Data Duplication & Integrity):** Importing large lists of leads from various sources often results in redundant data, creating confusion for the sales team.
    *   **Solution:** Built a dedicated `LeadImportController` with a preview phase and a conflict resolution interface (`resolveDuplicates`) to safely merge or update records before final insertion.
*   **Challenge 2 (Diverse Inventory Types):** Handling completely different assets (Real Estate Units vs. Cars) without cluttering the interface or database.
    *   **Solution:** Separated the domains cleanly into dedicated grouped modules (Cars, Trims vs. Units, Unit Types, Finishing) while keeping the lead interactions modular enough to link to any asset type or offer.
*   **Challenge 3 (Sales Activity Tracking):** Ensuring sales representatives stay on top of their tasks and managers have visibility over appointments.
    *   **Solution:** Integrated FullCalendar linked directly to the `AppointmentController` allowing visual management of client meetings natively within the CRM dashboard.
*   **Challenge 4 (Bilingual UX):** Providing a seamless, easy-to-use interface for Arab and expat employees operating simultaneously.
    *   **Solution:** Implemented dynamic route-based language switching retaining user preferences in the session, flipping the UI from LTR to RTL using Bootstrap 5 RTL features natively.

---

## Key Takeaways | النقاط الرئيسية المستفادة
1.  **Robust Lead Ingestion is Vital:** A CRM's value relies heavily on data quality; implementing a duplicate-resolution tool early on saves countless hours of cleanup.
2.  **Modular Permissions Scale Well:** Separating Admin configurations (Settings, Banks, Lead Sources) from day-to-day Sales activities ensures data security and focused workflows.
3.  **Visual Tools Enhance Productivity:** Embedding a full calendar directly into the dashboard makes scheduling interactions intuitive compared to standard tabular lists.
4.  **Bilingual Support by Design:** Building the RTL and LTR support into the core layout (`header.blade.php`) from day one prevents costly refactoring later when targeting the MENA region.
