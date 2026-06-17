# Project Overview / نظرة عامة على المشروع

## Project Name | اسم المشروع
**Chair Location - Workspace & Co-working Space Booking Platform** (Database Name: `chair_location`)
*(منصة تشير لوكيشن لإدارة وحجز مساحات العمل المشتركة، المكاتب الخاصة، وقاعات الاجتماعات)*

---

## Short Description | وصف قصير
A comprehensive workspace booking and space management platform built with Laravel 9. It provides seamless reservation capabilities for co-working spaces, private offices, meeting rooms, and dedicated desks. Key features include Al Rajhi Bank hosted payment gateway integration, dynamic calendar scheduling with slot conflict check, a referral affiliate system with gamified loyalty reward points, and a robust admin CRM panel for lead activity, financial ledgers, and employee KPI/HR metrics.

نظام متكامل لإدارة وحجز مساحات العمل المشتركة والمكاتب وقاعات الاجتماعات تم بناؤه باستخدام Laravel 9. يوفر النظام إمكانية حجز مساحات العمل المشتركة، المكاتب الخاصة، قاعات الاجتماعات، والمكاتب المخصصة بسلاسة. ويتميز بدمج بوابة دفع بنك الراجحي، وجدولة المواعيد الذكية لمنع تداخل الحجوزات، ونظام إحالة (Affiliate) متكامل مع نقاط مكافآت مرنة، ولوحة تحكم إدارية شاملة لمتابعة العملاء المحتملين (CRM)، والتدقيق المالي للمصروفات والإيرادات، وتقييم مؤشرات الأداء (KPIs) للموظفين.

---

## Medium Description | وصف متوسط
Chair Location is an enterprise-grade booking SaaS and workspace management application specifically developed for the Saudi & Gulf market. Built using Laravel 9 and PHP 8.0/8.2, the platform connects users with flexible workspace solutions categorised under four distinct models: shared areas, meeting rooms, private offices, and dedicated desks. Each workspace has dynamic pricing models (hourly, daily, monthly, etc.) with custom tax calculations and additional service addons. The backend features a real-time reservation scheduling algorithm that prevents booking overlaps and manages physical seat constraints dynamically. It includes an HR/KPI tracking suite that calculates employee performance based on attendance, leads, calls, and meetings. It also includes an affiliate referral system that rewards users with loyalty points, which can be redeemed for promo codes. The platform is localized (Arabic/English) at the database level (using `spatie/laravel-translatable`) and request headers, while push notifications are driven via Firebase Cloud Messaging (FCM). The admin dashboard handles CRM, income/expense auditing, permissions, and roles using Spatie Laravel Permission.

تطبيق تشير لوكيشن هو منصة متكاملة لحجز وإدارة مساحات العمل المشتركة (SaaS) موجهة خصيصاً للسوق السعودي والخليجي. تم بناء النظام باستخدام Laravel 9 و PHP 8.2، ويربط المستخدمين بحلول مساحات العمل المرنة المصنفة تحت أربعة نماذج حجز رئيسية: المساحات المشتركة، قاعات الاجتماعات، المكاتب الخاصة، والمكاتب المخصصة. يدعم النظام نماذج تسعير ديناميكية (بالساعة، اليوم، الشهر، إلخ) مع احتساب الضرائب وإضافة الخدمات الإضافية (Addons). يحتوي النظام على خوارزمية ذكية لمنع تداخل الحجوزات وإدارة السعة الاستيعابية للمساحات لحظياً، ونظام تقييم مؤشرات أداء الموظفين (KPIs) بناءً على الحضور والمكالمات والاجتماعات والعملاء المحتملين. بالإضافة إلى ذلك، يتضمن التطبيق نظام إحالة متكامل يمنح المستخدمين نقاط ولاء عند التسجيل أو الحجز، ويمكن استبدالها بأكواد خصم مولدة تلقائياً. المنصة مهيأة بالكامل للغتين العربية والإنجليزية على مستوى قواعد البيانات باستخدام حزمة `spatie/laravel-translatable` والـ Request Headers، وتدعم الإشعارات اللحظية عبر Firebase Cloud Messaging (FCM)، مع نظام حماية وصلاحيات متقدم للمشرفين والمديرين باستخدام Spatie Laravel Permission.

---

## Technologies & Packages | التقنيات والحزم المستخدمة

### **Backend (الباك إند):**
*   **Framework:** Laravel 9 (PHP 8.0+)
*   **Databases & Cache:**
    *   **MySQL 8.0+**: Primary relational database with structured tables for spaces, appointments, orders, points, and KPIs.
*   **Core Packages (الحزم الأساسية):**
    *   `laravel/sanctum`: Secure token-based API authentication for mobile and web frontends.
    *   `spatie/laravel-permission`: Advanced Role-Based Access Control (RBAC) managing permissions for admins, sub-admins, HR, and managers.
    *   `spatie/laravel-translatable`: Multi-language database translations for spaces details, categories, descriptions, and tags.
    *   `laravel-notification-channels/fcm` & Kreait Firebase SDK: Drives real-time push notifications to mobile devices.
    *   `yajra/laravel-datatables-oracle`: High-performance server-side data tables rendering for administrative modules.
    *   `maatwebsite/excel`: Exporting and importing accounting ledgers, lead lists, and system logs.
    *   `league/flysystem-aws-s3-v3`: Cloud storage provider integration for hosting high-quality images and media files.
    *   `realrashid/sweet-alert`: Native styled flash notifications inside the admin panel.

### **Frontend & APIs (الفرونت إند والواجهات):**
*   **Web Admin Panel**: Rendered using Laravel Blade views, Bootstrap 5, jQuery, and Yajra Datatables.
*   **API-First Design**: Unified RESTful APIs serving mobile applications and modern web portals.

---

## Key Features | الميزات الأساسية

1.  **Multi-Format Space Booking Engine (محرك حجز المساحات متعدد النماذج)**: 
    Supports scheduling for:
    *   `shared_area`: Priced per hour/day/month, checking physical chair capacity in real-time.
    *   `meeting_room`: Exclusive slot-based reservations booked per hour.
    *   `private_office`: Long-term monthly/yearly leasing with automatic range suggestion logic.
    *   `dedicated_disk`: Daily desk bookings.
2.  **Conflict-Free Slot Validation Algorithm (خوارزمية حجز بدون تداخل)**: 
    A reservation engine that evaluates date ranges and active timeslots, ensuring zero overlaps. For shared areas, it dynamically tracks the remaining seat capacity (`max_people - active_bookings`) to prevent overbooking.
3.  **Al Rajhi Bank Payment Gateway (بوابة دفع بنك الراجحي)**: 
    Native hosted payment page integration tailored for Saudi Riyal (SAR). It encrypts payload structures (`trandata`), securely communicates with the bank hosted endpoints, processes IPN callbacks, and redirects users based on payment status.
4.  **Loyalty Points & Redemption Catalog (نقاط الولاء ونظام الاستبدال)**: 
    A gamified loyalty module where users earn reward points for performing platform actions (bookings, referral code shares). Users can redeem points for dynamically generated 30-day coupon codes mapped to rewards criteria.
5.  **Affiliate & Invitation Program (برنامج الإحالة ودعوة الأصدقاء)**: 
    Automatic generation of unique affiliate registration codes (`ChairLocation-<Name>@<Random>`). Includes package-aware guest invitation passes where members can invite friends to join them in co-working spaces under invitation caps.
6.  **HR & KPI Calculation Suite (تقييم مؤشرات الأداء للموظفين)**: 
    Internal tracking of admin/manager performance by compiling attendance, calls, meetings, and leads counts against target credentials to yield performance achievement scores. Handles salaries, bonuses, and penalties.
7.  **Accounting Ledger & Financial Logging (التدقيق المالي والمحاسبي)**: 
    Integrated bookkeeping. Confirmed bookings automatically trigger an income ledger entry (`IncomeExpense` of type `income`), while refunds or cancellations register an expense ledger log.
8.  **Multi-Channel FCM Push Notifications (نظام الإشعارات اللحظية)**: 
    Firebase API integration targeting user device tokens to deliver contextual alerts about orders, meeting requests, and marketing promotions.
9.  **Database-Level Bilingual Localization (التعريب والترجمة ثنائية اللغة)**: 
    Deep internationalization routing system translating API response messages, validation errors, and translatable database columns (Arabic/English).

---

## Challenges & Solutions | التحديات والحلول

*   **Challenge 1 (Overlapping Reservations & Overbooking):** Managing real-time slot availability for meeting rooms and shared spaces without double bookings or exceeding physical seat limits.
    *   **Solution:** Built a verification algorithm inside `OrderController` that calculates slot overlaps within requested time frames and aggregates capacity constraints (`sum(num_of_persons + num_of_friends)`). It strictly blocks checkout requests if the total count exceeds the maximum capacity of the space.
*   **Challenge 2 (Secure Al Rajhi Hosted Checkout & Decryption):** Safely passing sensitive payment variables to Al Rajhi bank systems and handling response callbacks to verify transaction integrity.
    *   **Solution:** Integrated an isolated `AlRajhiPaymentService` utilizing the bank's encryption algorithm to package data buffers (`trandata`). Created callback endpoints that decrypt transaction parameters on IPN receipt, update databases securely, and redirect users to target pages on mobile or web.
*   **Challenge 3 (Disposable Coupon Code Collisions):** Preventing race conditions and coupon duplication when users redeem points for discount codes.
    *   **Solution:** Created a secure validation loop in `RedemptionController` that checks database code uniqueness before generation and sets strict limits (`limit_of_usage = 1` and `limit_per_user = 1`) to guarantee promo codes are single-use and disposable.
*   **Challenge 4 (staff Performance Calculation Load):** Querying massive tables to calculate monthly employee performance targets for KPI reviews.
    *   **Solution:** Designed an optimized SQL query utilizing conditional aggregates (`SUM(CASE WHEN type = '...' THEN 1 ELSE 0 END)`) grouped by the employee ID and target month, obtaining attendance, calls, meetings, and lead figures in a single database trip.

---

## Key Takeaways | النقاط الرئيسية المستفادة

1.  **Strict validation is vital for resources (أهمية التحقق الصارم للحجوزات):** Double-booking prevention must happen programmatically at the transaction level before database persistence to maintain client trust.
2.  **Gamification drives growth (التحفيز يدفع عجلة النمو):** Linking referral actions and user bookings to loyalty points that redeem as real monetary discounts encourages organic user acquisition.
3.  **Financial logs must be event-driven (أتمتة القيود المالية):** Automating accounting records via model hooks (`assignIncome` and `assignExpense`) during order state transitions prevents bookkeeping discrepancies.
4.  **Regional systems demand deep localization (متطلبات التخصيص المحلي):** Providing database-level multi-language support (Arabic/English) is crucial for Gulf workspace marketplaces to support bilingual clients and local admins.
