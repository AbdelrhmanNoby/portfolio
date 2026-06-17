# Project Overview / نظرة عامة على المشروع

## Project Name | اسم المشروع
**iTashteeb Finishing & Interior Design Marketplace** (Database Name: `itashteeb_v2`)
*(منصة إي تشطيب للتشطيبات والتصميم الداخلي ونظام إدارة المقاولين والموردين)*

---

## Short Description | وصف قصير
A high-performance, modular, multi-vendor home finishing, renovation, and interior design SaaS marketplace built with Laravel 12. It features AI-powered interactive client and vendor guidance based on site screenshots and visual aids (Manus AI), automated lead routing and workflow systems, real-time communications via Laravel Reverb (WebSockets), and a comprehensive subscription and package limits engine.



---

## Medium Description | وصف متوسط
iTashteeb is an enterprise-grade multi-tenant digital marketplace designed to connect property owners with verified construction, finishing, renovation, architecture, and interior design professionals in Egypt. The platform is structured under a clean Modular Monolith architecture using Laravel 12 and PHP 8.2, encompassing over 30+ isolated business modules. Each professional company (vendor) operates in strict isolation (Multi-Tenancy) with its own branch settings, portfolios, employees, expense ledgers, and sales activity trackers (CRM). To optimize client and vendor onboarding, the platform integrates **Manus AI** to analyze screenshots and visual queries, automatically guiding users and professional companies step-by-step on how to interact with the marketplace, manage dashboards, and handle platform functionalities through visual aids. Additionally, automated background services and scrapers coordinate lead generation, while **Laravel Reverb (WebSockets)** powers instant notifications and in-app communications for sales agents. Platform performance is highly optimized using Spatie Response Cache and tagged Redis cache, achieving response times of 50-100ms.



---

## Technologies & Packages | التقنيات والحزم المستخدمة

### **Backend (الباك إند):**
*   **Framework:** Laravel 12 (PHP 8.2+)
*   **Databases & Cache:**
    *   **MySQL 8.0+**: Primary relational database with tailored composite indexes for tenant-scoped queries.
    *   **Redis**: High-speed memory store utilized for application cache, response caching, and background job queue management.
*   **Core Packages (الحزم الأساسية):**
    *   `nwidart/laravel-modules`: Powers the modular monolith architecture to keep business domains separated.
    *   `laravel/reverb`: In-app real-time WebSocket protocol for dashboards and notifications.
    *   `laravel/sanctum`: Secure token-based authentication API.
    *   `spatie/laravel-translatable`: Bilingual translation support (Arabic/English) inside database models.
    *   `spatie/laravel-activitylog`: Complete audit trail tracking user and admin activities across the dashboard.
    *   `maatwebsite/excel`: Exporting and importing accounting ledgers, expenses, and CRM data.
    *   `league/flysystem-aws-s3-v3`: For cloud file storage of high-resolution project images and media.

### **Frontend & APIs (الفرونت إند والواجهات):**
*   **Web Frontend**: Built using **React** and **Next.js** to deliver a premium, fast, and SEO-friendly web marketplace.
*   **API-First Design**: RESTful APIs mapping distinct dashboards (Platform Administration, Company/Vendor Console) and public web channels.
*   **Asset Management**: Powered by Vite.

---

## Key Features | الميزات الأساسية

1.  **Multi-Vendor Architecture**: Advanced database-level and query-level isolation (Multi-Tenancy) where professional finishing companies and designers manage their own branch scopes, sales teams, project showcases, and customer leads securely without data leaks.
2.  **Advanced CRM & Sales Pipeline**: Complete deals pipeline tracking leads from initial request (web request/consultation booking) to meeting schedules, sales rep assignment, commission logging, and final contract signing.
3.  **AI Image-Based User Guidance (Manus AI)**: Integrates Manus AI to analyze screenshots and visual queries uploaded by clients and vendors, providing interactive visual step-by-step guidance on how to use the site, configure settings, and interact with the marketplace features.

4.  **Workflow Automation**: Background automation services that process incoming leads, handle image resizing and watermarking dynamically via Intervention Image, and synchronize vendor listings.
5.  **Subscriptions & Addons Lifecycle**: A strict subscription engine for professional companies (vendors) with package limit enforcement. The system checks active subscriptions, consumes addon quota (e.g., project listings, staff slots, idea book uploads), and automatically restricts dashboards or hides leads when limits are exceeded.
6.  **High-Performance Multi-Layer Caching**: Response times optimized to 50-100ms by bypassing database queries for public resources using tagged Redis caching, Spatie Response Cache, and request-level user auth caching.
7.  **Real-Time Communications (Laravel Reverb WebSockets)**: Native WebSocket infrastructure (managed via Supervisor on production Nginx) for instantaneous dashboard push notifications, CRM state transitions, and team chat alerts.
8.  **Multi-Vendor Financial Ledger & Commissions**: Internal accounting module tracking expense records, operational costs, balances, and auto-calculating employee commissions based on deal metrics.
9.  **Bilingual Support (Arabic/English)**: Deep database-level localization of model content (names, categories, project descriptions) managed by custom language middleware and Spatie Translatable.

---

## Challenges & Solutions | التحديات والحلول

*   **Challenge 1 (Tenant Data Leak & Isolation Risks):** In a complex marketplace with multiple competing construction companies, any query failing to filter by `company_id` represents a high-severity security risk.
    *   **Solution:** Built a tenant-aware repository layer enforcing the `queryForActor($actor)` pattern. Every query is filtered automatically at the data access level based on the authenticated actor's company context, making cross-tenant data leaks programmatically impossible.
*   **Challenge 2 (Enforcing Subscriptions & Addon Constraints):** Preventing companies from exceeding their subscribed limits (e.g. posting too many projects or viewing too many client leads) without polluting controllers with messy IF statements.
    *   **Solution:** Implemented a centralized `SubscriptionService` and middleware. Before executing write operations or lead disclosures, the system calls `consumeAddonOrFail($companyId, 'addon_key')`, which handles transaction-safe quota deduction and aborts with clear validation exceptions when limits are reached.
*   **Challenge 3 (Real-Time CRM & Lead Updates):** Keeping sales reps updated instantly on new leads or deal changes without constant client-side API polling that overloads the database.
    *   **Solution:** Configured **Laravel Reverb** as a native WebSocket server. Set up Nginx proxy rules on port 443 redirecting `/app` traffic to Reverb on port 8080 internally, and managed Reverb and queue processes using Supervisor. This allowed instant broadcast of events with zero polling overhead.
*   **Challenge 4 (Onboarding Complexity & Visual Guidance):** Educating non-technical clients and traditional finishing vendors on how to deal with complex SaaS features and dashboard flows.
    *   **Solution:** Developed an interactive guidance workflow leveraging **Manus AI**. Users upload screenshots or visual queries of the site, and the AI parses the image to guide them step-by-step on how to navigate, submit requests, or manage dashboard setups visually.

*   **Challenge 5 (Modular Monolith Performance Issues):** Eager loading too many relations (projects, galleries, translations, categories) causing database memory spikes and slow response times.
    *   **Solution:** Re-architected data structures to separate list views from detailed views (avoiding full gallery payloads in indexes), applied composite database indexing on tenant search fields, and layered Spatie Response Cache over Redis.

---

## Key Takeaways | النقاط الرئيسية المستفادة

1.  **Security boundaries must be systemic:** Isolation cannot rely on manual filters in controllers. Centralizing scoping inside repositories via `queryForActor()` guarantees safety across the entire application lifecycle.
2.  **Modular design protects large applications:** Breaking the system into 30+ separate modules ensures that development teams can work on isolated domains (like CRM, Account, or Subscriptions) without risk of breaking core platform functionality.
3.  **Relational Quality over JSON Shortcuts:** Normalizing tables like `project_uploads` and `catalog_services` instead of storing loose JSON arrays keeps database queries fast, indexable, and compatible with high-speed caching.
4.  **AI & Automation Drive Platform Value:** Offloading onboarding and navigation support to Manus AI image-based guidance and automating CRM lead routing significantly reduces user friction and increases platform adoption for both clients and vendors.
