# Project Overview / نظرة عامة على المشروع

## Project Name | اسم المشروع
**Office Hub - Multi-Tenant Workspace & CRM SaaS Platform**
*(أوفيس هب - منصة سحابية لإدارة مساحات العمل للشركات وخدمات العملاء)*

---

## Short Description | وصف قصير
A comprehensive, multi-tenant B2B SaaS platform designed to operate co-working spaces, serviced offices, and service-oriented clinics. "Office Hub" serves as the Host SaaS (Admin Center), providing independent workspace operators (Tenants) with a fully integrated Workspace Operating System. Each tenant gains access to exhaustive modules spanning HR, payroll, real-estate operations, granular inventory, CRM pipelines, and a mobile-first PWA Portal specifically built for their end-clients to book rooms, request kitchen hospitality, track printing, and monitor packages.

---

## Medium Description | وصف متوسط
"Office Hub" is a dual-layered architectural masterpiece built on a Central Admin Host and a multitude of isolated Tenant Subsystems. 

**Host Level (Office Hub / Central Admin):** The central dashboard handles incoming tenant registration requests, provisioning secure sub-domains and completely isolated database environments on approval.

**Tenant Level (WorkspaceOS):** Once provisioned, a tenant has a 360-degree control panel. The system dives exceptionally deep into organizational structuring—handling Roles (Job Titles), Departments, Sections, Branches, Shifts, and even Weekend/Holiday configurations. The **HR Core** features QR code Manual Attendance via a Kiosk interface, Payroll generation, Advance Requests (Loans), and a robust Leave Management matrix. 

For **Sales and CRM**, the system features Kanban boards to manage Leads with dynamic stages, Google Sheets mass-import integration, Lead interaction tracking, and specialized Sales Targets and Performance dashboards.

The **Operations & Facility** side is heavily specialized, including Room Bookings, Contracts monitor, Digital Archives per employee, Kitchen Board operations directly tied to Inventory and Invoices, a dedicated Print Queue Kanban, and Incoming Mails logging. 

Finally, a **Client PWA Portal** offers end-clients a branded mobile application to track their contracts, book rooms seamlessly with history tracking, request on-demand hospitality (digital menu), interact with print queues, and set up their passwords securely. The entire tenant landscape is stitched together via an interactive Visual Calendar managing both internal operations and external public visitor bookings, with smart Fallback localization strings (Arabic/English) bridging incomplete inputs.

---

## Technologies & Packages | التقنيات والحزم المستخدمة

### **Backend (الباك إند):**
*   **Framework:** Laravel 10 (PHP 8.1+)
*   **Database:** MySQL
*   **Core Packages & Architecture:**
    *   `stancl/tenancy`: For advanced Multi-Tenant data isolation, domain mapping, and dynamic database provisioning.
    *   `spatie/laravel-permission`: For dynamic Role-Based Access Control tied to "Job Titles" and "Departments".
    *   `spatie/laravel-activitylog`: For tracking modifications and auditing logs across diverse modules.
    *   `maatwebsite/excel`: To power massive data imports (Leads, Employee Attendance Sheets).
    *   `laravel/sanctum`: Dedicated token-based API and PWA Client authentication routes.

### **Frontend (الفرونت إند):**
*   **Core:** HTML5, CSS3, JavaScript.
*   **Styling & UI:** Bootstrap 5 (Admin Dashboard).
*   **Client PWA:** Custom Progressive Web App implementation acting as a mobile portal for quick access to workspace services.
*   **Calendar:** FullCalendar.js powering internal room bookings and external visitor schedules dynamically.
*   **Build Tool:** Vite.

### **Integrations & Automation (التكامل والأتمتة):**
*   **Google Sheets API:** Integrated `GoogleSheetIntegrationController` to fetch multiple headers and sync externally sourced leads instantly into the CRM.
*   **QR Code Kiosk Attendance:** Built-in scanner functionality for 'Manual Attendance' tracking linked natively to shifts.
*   **Intelligent Frontend Localization Fallback:** Dynamically maps missing Arabic inputs (`description_ar`) to their English counterpart before rendering broken UI spaces to the end user.

---

## Key Features (Exhaustive List) | الميزات الشاملة

### 1. Host SaaS (Office Hub Central Admin)
*   **Tenant Provisioning**: Real-time evaluation and approval/rejection of workspace creation requests.
*   **Domain & Tenant Monitoring**: Central control over active isolated domains via strict middleware mapping.

### 2. HR & Employee Management (Tenant Side)
*   **Organizational Hierarchy**: Full management of Departments, Sections, and Job Titles mapped directly to user permissions.
*   **Digital Archives**: Deep personnel files attaching financial docs, contracts, leave/shift change requests, and ID avatars per employee.
*   **Advanced Attendance Matrix**: Supports HR-uploaded Excel sheets (`AttendanceImportController`), or live QR Code terminal scanning via `ManualAttendanceController` kiosk functionality.
*   **Payroll & Advances**: Payroll processor logic sending slips via email; handling employee advance/loan requests (`AdvanceRequestController`).
*   **Leave Types & Holidays**: Managing customizable weekend shifts, official holidays tracking, and tardiness approvals.

### 3. CRM & Sales Center
*   **Pipeline & Lead Interaction**: Kanban-style interactive pipeline. Detailed logging of calls/meetings (`InteractionSettingController`).
*   **Import/Resolution Center**: Excel and Google Sheets integration handling bulk imports with a visual duplicate resolution preview page.
*   **Sales Targets & Performance**: Visual analytics tracking branch/agent conversions and target fulfillment via data exportation (`SalesPerformanceController`).

### 4. Operations, Fleet & Facility Management
*   **Print Queue System**: A Kanban board for processing tenant printing orders (Downloadable files, tracking execution states).
*   **Kitchen & Inventory ERP**: Connecting Invoices to Purchases and actual Inventory items. A live `KitchenBoardController` processes client hospitality demands from the PWA, tracking product stock dynamically.
*   **Contract Monitoring**: End-to-end PDF contract creation, secure storage, tracking, and remote client downloading.
*   **Incoming Packages/Mails**: Reception desk tool logging parcel arrivals, assigning them to clients, and pushing status to delivered (`IncomingMailController`).
*   **Unified Master Calendar**: Integrates Public Visitor Bookings securely against Internal Operations (Room Settings), avoiding double booking overlaps with dynamic visual markers.

### 5. Task Management Subsystem
*   **Team Kanbans**: Collaborative task assignment among internal employees.
*   **Reporting & Comments**: Built-in reporting mechanism tied to individual tasks measuring job performance execution.

### 6. Client PWA Portal (End-User Experience)
*   **Mobile-First Setup**: Secure URL password setup tokens. Client logs in via native-like app interface out of the box.
*   **Service Requests Engine**: Separate routing mapping client requests directly to the Kitchen Board (Hospitality) or Print Queue dynamically (`ServiceOrderController`).
*   **Booking History**: Allowing clients to explore workspace meeting rooms, reserve timeslots, and track historical/cancelled bookings globally.

---

## Challenges & Solutions | التحديات والحلول
*   **Challenge 1 (Complex Tenancy Routing & Auth Domains):** Maintaining separate routes to prevent central administrators from cross-bleeding sessions into tenant domains, while supporting a third independent authentication layer for PWA End-Clients.
    *   **Solution:** Separated routes strictly via `web.php` and `tenant.php`, wrapping tenant functionality behind `InitializeTenancyByDomain` middleware. Assigned specific Guards (`auth:client` vs `auth`) protecting the endpoints independently.
*   **Challenge 2 (Service Request Management in PWA):** Clients needed a unified, mobile-friendly way to request and track diverse services (Meeting Rooms vs. Kitchen vs. Incoming Mail) without opening disjointed forms.
    *   **Solution:** Engineered a robust PWA portal utilizing Bootstrap Modals and visual feeds (Services/History) merging disparate module notifications into a fast sliding mobile feed.
*   **Challenge 3 (Bilingual Content Fallback):** When admins created products or departments and skipped the Arabic translation, the UI appeared broken or blank for Arab users.
    *   **Solution:** Built a smart Frontend Fallback string mapping system natively. If the `name_ar` or `description_ar` resolves to null in the blade template, it automatically reads the English attributes ensuring no visual UI components warp or disappear.
*   **Challenge 4 (Visitor vs. Internal Calendar Conflicts):** Merging external public visitor bookings with scheduled internal room operations on the same master calendar frequently caused overlapping database definitions.
    *   **Solution:** Created a dedicated `CalendarController` API that standardizes structurally differing models (Visitors vs. Internal Operations) into synchronized FullCalendar Event objects, augmented with color-coding and overlap-barring rule-sets.
*   **Challenge 5 (Integrating Live HR Attendance with Hardware Kiosks):** Syncing on-ground arrival times required a terminal approach that wasn't natively supported.
    *   **Solution:** Created the `ManualAttendanceController` which opens a fullscreen Kiosk mode routing to a QR Code 'Scan' interface mapping tokenized requests seamlessly back to shift data.

---

## Key Takeaways | النقاط الرئيسية المستفادة
1.  **Multi-Tier Auths Require Absolute Discipline:** Delineating `web`, `tenant-admins`, and `tenant-clients` dictates tight route grouping and middleware assignments from day one preventing devastating security leaks.
2.  **PWA Portals Drive Ecosystem Engagement:** Hooking the Kitchen, Printers, and Receptions directly to the Client's phone via a PWA eliminates operational friction dramatically compared to physical requesting.
3.  **Graceful Degradation is Vital in MENA:** Operating a B2B SaaS in the MENA region demands bulletproof translation fallbacks. Empty database columns cannot break the UI.
4.  **Granular HR Scaling:** Building comprehensive Employee files (Digital Archives for loans, shift changes, contract snapshots) ensures the SaaS can sustain larger 200+ employee complexes efficiently without needing separate third-party HR software.
