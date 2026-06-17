# Project Overview / نظرة عامة على المشروع

## Project Name | اسم المشروع
**Amtalek Real Estate & CRM Platform** (Database Name: `amtalek_v2`)
*(منصة أمتلك العقارية ونظام إدارة علاقات العملاء CRM)*

---

## Short Description | وصف قصير
A high-performance, modular, multi-vendor real estate management and CRM platform built with Laravel 12, featuring AI-powered client guidance/matching using images (Manus AI), automated property scraping/onboarding via n8n integration, and real-time communications using Laravel Reverb (WebSockets).

*(منصة عقارية وإدارة علاقات العملاء متكاملة ومتعددة الشركات/البائعين (Multi-Vendor)، مبنية بإطار العمل Laravel 12، وتتميز بنظام توجيه وإرشاد العملاء وتوصيات العقارات باستخدام الصور والمدعوم بالذكاء الاصطناعي (Manus AI)، وأتمتة جلب العقارات عبر سير عمل n8n، والاتصال الفوري باستخدام Laravel Reverb).*

---

## Medium Description | وصف متوسط
Amtalek is an enterprise-grade real estate platform designed to orchestrate property management, multi-company vendor operations (multi-vendor), and customer relationship management (CRM) under a unified Modular Monolith architecture. The backend, powered by Laravel 12 and PHP 8.2+, manages over 30+ custom modules. It supports end-to-end CRM pipelines including lead tracking, deals, follow-ups, and sales activity reports. To automate operations, the system integrates **Manus AI** to analyze uploaded images to assist in guiding clients and recommending matching properties based on visual tastes, and features an **n8n scraping workflow** that ingests raw property details, automatically downloads/watermarks listing media, and populates relational database models. Additionally, real-time client interactions are driven by **Laravel Reverb (WebSockets)** and **Firebase Cloud Messaging**. Performance is a core pillar, with response times optimized to 50-100ms using Spatie Response Cache, tag-based Redis caching, and fine-tuned database indexing.

*(تعد منصة أمتلك العقارية نظاماً بمواصفات مؤسسية لإدارة العقارات والشركات العقارية (Vendors) وإدارة علاقات العملاء (CRM) تحت هيكلية برمجية موحدة (Modular Monolith) تضم أكثر من 30 وحدة مخصصة. يعتمد النظام على Laravel 12 و PHP 8.2+ لإدارة تدفق العمليات بالكامل من تتبع العملاء المحتملين (Leads) والصفقات إلى تقارير المبيعات. لتعزيز الكفاءة التشغيلية، تم دمج محرك الذكاء الاصطناعي **Manus AI** لتحليل الصور المرفوعة للمساعدة في توجيه وإرشاد العملاء واقتراح العقارات المطابقة لتفضيلاتهم بصرياً، بالإضافة إلى أتمتة عبر **n8n** لجلب العقارات تلقائياً وتحميل الصور ووضع العلامات المائية (Watermarks) وربط البيانات علائقياً. يدعم النظام الإشعارات والدردشة الفورية عبر **Laravel Reverb (WebSockets)** وتنبيهات **Firebase**. وتمت تهيئة الأداء الفائق ليصل زمن الاستجابة إلى 50-100 مللي ثانية بفضل استراتيجيات التخزين المؤقت المتقدمة باستخدام Redis و Spatie Response Cache).*

---

## Technologies & Packages | التقنيات والحزم المستخدمة

### **Backend (الباك إند):**
*   **Framework:** Laravel 12 (PHP 8.2+)
*   **Databases & Search Engines:**
    *   **MySQL 8.0+**: Primary relational database with optimized custom indexes.
    *   **Redis 6.0+**: Used for high-speed response caching and queue/job management.
    *   **Elasticsearch 9.2**: Powers advanced, fuzzy, and fast property searches.
*   **Core Packages (الحزم الأساسية):**
    *   `nwidart/laravel-modules`: Powers the modular monolith architecture (30+ separate modules).
    *   `spatie/laravel-responsecache`: For request-level response caching to bypass database queries.
    *   `spatie/laravel-permission`: Granular Role-Based Access Control (RBAC).
    *   `spatie/laravel-translatable`: Bilingual translation support (Arabic/English) inside database models.
    *   `spatie/laravel-activitylog`: Auditing admin actions and HR tracking.
    *   `laravel/reverb`: In-app real-time WebSocket protocol.
    *   `laravel/sanctum`: Secure API token-based authentication.
    *   `kreait/laravel-firebase`: For push notifications on mobile and web client channels.
    *   `intervention/image-laravel`: For image processing, resizing, and watermarking.
    *   `maatwebsite/excel`: Exporting and importing CRM data, leads, and financials.
    *   `google/apiclient`: Integration with Google Cloud services.

### **Frontend & APIs (الفرونت إند والواجهات):**
*   **Web Frontend**: Built using **React** and **Next.js** for a modern, high-performance, and SEO-friendly user interface.
*   **API-First Design**: Complete RESTful APIs supporting mobile applications (Flutter/iOS/Android) and the Next.js web application.
*   **Asset Management**: Powered by Vite.

---

## Key Features | الميزات الأساسية

1.  **Multi-Vendor Architecture**: Complete database data-isolation between different real estate companies (vendors), allowing each vendor to manage their own properties, projects, sales teams, and CRM leads in a multi-vendor setup.
2.  **Advanced CRM & Lead Tracking**: Track potential clients through custom pipelines, schedule follow-ups, and generate comprehensive performance reports for sales teams.
3.  **AI Image-Based Client Guidance (Manus AI)**: Utilizes Manus AI to analyze property images and visual inputs to guide users and match/recommend properties to clients based on their visual tastes.
    *(إرشاد وتوجيه العملاء بالذكاء الاصطناعي: استخدام Manus AI لتحليل صور العقارات والمدخلات البصرية لمساعدة وإرشاد المستخدمين ومطابقة العملاء مع العقارات الملائمة لتفضيلاتهم البصرية).*
4.  **n8n Workflow Automation**: Automated property scraping and guest property creation. Incoming webhooks from n8n supply raw property details, which are processed, and the system automatically downloads, processes, watermarks, and relationally binds listing images, sliders, amenities, and dynamic specs.
5.  **High-Performance Caching System**: Achieved response times of 50-100ms (90% faster) and reduced database query overhead by 95% using a multi-layer cache (Spatie Response Cache + tagged Redis caching + request-level auth user caching).
6.  **Real-Time Real-Time Reverb WebSockets**: Native WebSocket support (configured on production and cPanel environments) for instant message delivery and real-time update triggers.
7.  **HR & Attendance Systems**: Built-in HR module with automated features like late-attendance penalties, task assignment tracking, and an auto-logout system for inactive admins/users to prevent security breaches.
8.  **Bilingual Support (Arabic/English)**: The platform natively supports Arabic and English at the database level using translation models and interface-level switching.
9.  **Subscriptions & Addons Lifecycle**: A comprehensive billing and subscription engine for companies (vendors) to purchase pricing packages and standalone addons (e.g., extra property listings, additional sales team slots). The system manages the entire operational lifecycle: order generation, Kashier payment gateway integration, automatic transitions from pending to active status, real-time constraint enforcement (restricting listings or masking leads when package limits are exceeded), automated notifications warning of upcoming expiration, and automatic expiration handling.


---

## Challenges & Solutions | التحديات والحلول

*   **Challenge 1 (API Performance Bottlenecks):** The main property list and show APIs were experiencing high memory usage (~70MB) and slow response times (~1000ms) due to 30+ database queries (many N+1 duplicates) per request.
    *   **Solution:** Restructured the database query pipeline with eager loading (`withCount`, `exists()`), added 10 strategic database indexes, cleaned up duplicate indexes, and introduced a request-level authentication caching middleware. This reduced queries by 64%, eliminated duplicate queries completely, and dropped response times to 50-100ms.
*   **Challenge 2 (Automated Listing Scrapers):** Building a reliable way to import raw properties scraped from external sources (like Dubizzle) without database schema fragmentation.
    *   **Solution:** Integrated a guest onboarding API (`/api/add-property-as-guest`) with n8n. Instead of storing complex data inside unsearchable JSON fields, the API translates incoming n8n data into proper relational models (`property_sliders`, `property_amenities`, `property_inputs`) and automates media downloads with watermarking.
*   **Challenge 3 (Visual Client Guidance & Recommendations):** Finding the perfect property recommendation based on client visual tastes and photo inputs can be subjective and slow.
    *   **Solution:** Built a direct integration with **Manus AI** (`/api/crm/ocr/extract-rfq-upload` endpoint repurposed for visual analysis) to process client-uploaded images of design/layout preferences, allowing the system to match and guide clients to properties sharing those aesthetics.
*   **Challenge 4 (Real-Time Communication in Shared Hosting):** Setting up WebSockets on standard cPanel environments without high overhead costs.
    *   **Solution:** Deployed and configured **Laravel Reverb**, a first-party WebSocket server built for Laravel, optimizing proxy rules and configuration scripts to run lightweight, real-time chat and notifications.
*   **Challenge 5 (Security and Vendor Isolation):** Managing a complex system with different company admins, sales agents, and normal users while maintaining data privacy.
    *   **Solution:** Implemented Spatie Permission for Role-Based Access Control combined with global vendor scopes that automatically isolate company-specific properties, reports, and leads based on the authenticated user's company context.

---

## Key Takeaways | النقاط الرئيسية المستفادة

1.  **Relational Quality over JSON Shortcuts:** When scraping data via automation (n8n), mapping data relationally (using tables like `property_amenities` and `property_inputs`) preserves the system's indexing power and Elasticsearch compatibility, unlike storing raw JSON strings in the database.
2.  **Performance is a Core Feature:** Caching should be designed at multiple levels (response cache, Redis tag cache, and request-level user caching) to sustain high traffic, especially in mobile-app-heavy real estate portals.
3.  **AI & Automation Create Competitive Edge:** Offloading client recommendation workflows to Manus AI image analysis and property importing to n8n workflows significantly reduces time-to-market for listing platforms and increases sales productivity.
4.  **Modular Monolith Maintainability:** Splitting a large application into 30+ separate modules ensures that development teams can work on isolated domains (like HR, CRM, or Properties) without breaking core application features.
