# Project Overview / نظرة عامة على المشروع

## Project Name | اسم المشروع
**Bnaia Store & Multi-Vendor E-Commerce Platform** (Database Name: `eramo_db`)
*(منصة بناية للمتاجر المتعددة والتجارة الإلكترونية)*

---

## Short Description | وصف قصير
A high-performance, modular, multi-vendor e-commerce marketplace built with Laravel 12, featuring a dynamic product variants system, an AI-powered OCR Request For Quotation (RFQ) processing and matching pipeline, double-entry financial accounting, asynchronous Zoho Books ERP synchronization, and a scalable API-first design consumed by a Next.js 15 / React 19 frontend.

*(منصة تجارة إلكترونية متكاملة ومتعددة المتاجر (Multi-Vendor) عالية الأداء، مبنية بإطار العمل Laravel 12 بهيكلية برمجية موحدة (Modular Monolith)، وتتميز بنظام مرن لإدارة متغيرات المنتجات (Product Variants)، ونظام أتمتة معالجة ومطابقة طلبات عروض الأسعار (RFQ) المدعوم بالذكاء الاصطناعي وOCR، وربط خلفي ذكي مع Zoho Books وFirebase، مع واجهات برمجية (APIs) محسنة تخدم موقع فرونت إند مبني بـ Next.js 15 و React 19).*

---

## Medium Description | وصف متوسط
Bnaia is an enterprise-grade marketplace connecting multiple vendors with customers under a unified Modular Monolith architecture. The backend, powered by Laravel 12 and PHP 8.2+, manages 14 custom modules (including CatalogManagement, Order, Refund, and Accounting). It features a unique **Bank Product System** that allows vendors to adopt shared listings, set custom prices, manage region-specific stock, and customize multi-attribute **Product Variants** (sizes, colors, materials) dynamically localized using a unified database translation schema. To automate transactions, the platform implements an **AI-powered background OCR Request For Quotation (RFQ) pipeline**. When customers upload quote requests (images or PDFs), a background job using database queues (via n8n integration) extracts items and routes them to the matching engine (`RfqExtractionMatchingService`), which normalizes Arabic texts, adjusts for dialect spelling variations, scores candidates using similarity matching, and auto-pairs them with catalog products and variants. Admins review and route inquiries to selected vendors who submit bids; customer acceptance automatically triggers individual vendor orders, updates stock statuses, and posts ledger entries. The backend exposes secure, rate-limited Sanctum APIs tailored for a **Next.js 15 and React 19 frontend** built using RTK Query and Server Components, handling 1,000+ concurrent users/min. Integrations include a background **Zoho Books pipeline** to sync sales orders and invoices, as well as Firebase push notifications. The database layer features optimized indexes and Redis cache tagging, ensuring API response times remain under 50-100ms.

*(تعد منصة بناية نظاماً متطوراً للتجارة الإلكترونية متعددة المتاجر (Marketplace) يربط الموردين بالعملاء تحت بنية برمجية موحدة (Modular Monolith) تضم 14 وحدة متكاملة (منها إدارة الكتالوج، المبيعات، المرتجعات، والحسابات). يعتمد الباك إند على Laravel 12 و PHP 8.2+ ويتميز بنظام "بنك المنتجات" (Bank Product) لتبني المنتجات العامة وتخصيص أسعارها ومخزونها حسب المنطقة، مع نظام مرن لإدارة **متغيرات المنتجات (Product Variants)** متعددة المواصفات (الألوان، المقاسات، والمواد) المترجمة ديناميكياً على مستوى قاعدة البيانات. كما يدعم النظام **دورة معالجة ومطابقة طلبات عروض الأسعار (RFQ) المؤتمتة بالذكاء الاصطناعي وOCR** في الخلفية؛ حيث يقوم العميل برفع ملف عرض السعر (صورة أو PDF)، ليقوم جوب خلفي عبر طابور قاعدة البيانات (مدمج مع سير عمل n8n) باستخراج البنود وتمريرها لمحرك المطابقة الذكي (`RfqExtractionMatchingService`) الذي يقوم بمعالجة وتطبيع النصوص العربية والتعامل مع فروق الإملاء بلهجاتها المختلفة وحساب نقاط التشابه لاقتراح ومطابقة البنود تلقائياً مع المنتجات والمتغيرات المناسبة بقاعدة البيانات، ومن ثم توجيهها للتجار المحددين عبر إشعارات Firebase لتقديم عروضهم التي يراجعها العميل ويقبلها، مما يؤدي لإنشاء أوردر منفصل للتاجر المقبول فوراً وتحديث المخزون والقيود المحاسبية. يقدم الباك إند واجهات برمجية (APIs) مؤمنة بـ Sanctum لتغذية موقع الويب المبني بـ Next.js 15 و React 19 باستخدام RTK Query ومكونات الخادم (Server Components) لخدمة أكثر من 1000 مستخدم في الدقيقة مع سرعة استجابة تتراوح بين 50-100 مللي ثانية بفضل استراتيجيات التخزين المؤقت عبر Redis. كما تم دمج النظام مع **Zoho Books** عبر خط أنابيب خلفي لمزامنة الحسابات والفواتير).*

---

## Technologies & Packages | التقنيات والحزم المستخدمة

### **Backend (الباك إند):**
*   **Framework:** Laravel 12 (PHP 8.2+)
*   **Databases & Caching:**
    *   **MySQL 8.0+**: Primary relational database with optimized custom indexes and constraints.
    *   **Redis 6.0+**: Used for high-speed response caching, sessions, and queue/job management.
*   **Core Packages (الحزم الأساسية):**
    *   `nwidart/laravel-modules`: Powers the modular monolith architecture (14 active modules).
    *   `laravel/sanctum`: Secure API token-based authentication.
    *   `predis/predis`: Redis client for high-performance caching.
    *   `kreait/firebase-php`: Firebase Cloud Messaging for push notifications on mobile and web client channels.
    *   `yajra/laravel-datatables`: Server-side rendering of tables.
    *   `maatwebsite/excel`: Exporting and importing catalog, order, and financial records.
    *   `mcamara/laravel-localization`: For bilingual routing and language preferences.

### **Frontend & APIs (الفرونت إند والواجهات):**
*   **Web Frontend**: Built using **React 19** and **Next.js 15** (App Router) with Redux Toolkit Query (RTK Query), server components, and ISR-ready route handlers for maximum performance.
*   **API-First Design**: Complete RESTful API architecture supporting mobile applications (Flutter/iOS/Android) and the Next.js web application.
*   **Asset Management**: Powered by Vite.

---

## Key Features | الميزات الأساسية

1.  **Multi-Vendor Architecture & Order Splitting**: Complete separation between vendors. When a customer places a checkout order with items from multiple vendors, the system automatically splits the order into vendor-specific orders, calculates independent shipping costs, and routes them to their respective vendor dashboards.
2.  **Bank Product System (نظام بنك المنتجات)**: A shared product catalog created by admins that vendors can adopt. Multiple vendors can sell the exact same product definition while defining their own pricing, taxes, commission, and regional stock.
3.  **Dynamic Product Variants System (نظام متغيرات المنتجات المرن)**: Supports multi-attribute options (colors, sizes, materials) at the database level with a translatable scheme mapped via the unified `value` field in the translation table. This ensures clean API returns (e.g. `get-variants-ai` and category tree endpoints) for frontends, coupled with optimized queries to prevent database overhead.
    *(نظام متغيرات المنتجات المرن: يدعم خيارات متعددة الخصائص (الألوان، المقاسات، والمواد) على مستوى قاعدة البيانات باستخدام نموذج ترجمة موحد عبر حقل `value` بجدول التراجم، مما يضمن عرض البيانات بدقة في واجهات API للفرونت إند وتطبيقات الموبايل، مع تحسين الاستعلامات لتجنب الأعباء الإضافية على الخادم).*
4.  **Automated AI-Powered Multi-Vendor RFQ System (أتمتة عروض الأسعار واستخراج البيانات بالذكاء الاصطناعي)**: Customers can upload quote files (images/PDFs) which triggers an asynchronous background OCR queue job (`SendQuotationToOcrJob`, `ProcessRfqOcrJob`) via n8n. The system's matching engine (`RfqExtractionMatchingService`) normalizes Arabic text (handling dialect typos like ة/ه and ي/ى), scores candidates via similarity matching, and pairs them to database products/variants with statuses (`matched`, `ambiguous`, `undefined`). Accepted offers automatically split into individual vendor orders.
    *(نظام عروض الأسعار (RFQ) المؤتمت بالذكاء الاصطناعي: يتيح للعملاء رفع طلبات عروض الأسعار كملفات أو صور، ليقوم جوب خلفي بمعالجتها بالـ OCR عبر سير عمل n8n، ثم يطابق محرك البحث الذكي البنود المستخرجة مع منتجات ومتغيرات المتجر بحساب نقاط التشابه اللفظي والتعامل مع أخطاء الإملاء العربية الشائعة، لتُقسم الطلبات المقبولة تلقائياً لأوردرات تجار منفصلة).*
5.  **Zoho Books ERP Integration (الربط مع Zoho Books)**: Auto-synchronizes checkout orders, customers, and invoices to Zoho Books in the background using an async queue job with automatic retries and exponential backoff.
6.  **Double-Entry Accounting System (نظام المحاسبة مزدوج القيد)**: Auto-generates journal entries and charts of accounts, calculating platform commission and updating vendor balances dynamically upon order delivery or refunds.
7.  **Advanced Regional Stock Booking (حجز المخزون الإقليمي)**: Manages regional inventory levels dynamically (`total`, `booked`, `allocated`, `fulfilled`, `remaining`), preventing overselling during high-traffic checkouts.
8.  **Point & Rewards System (نظام النقاط والمكافآت)**: Customers earn, use, and refund loyalty points automatically, with transaction logging and cron-based expiration.
9.  **Bilingual Support (Arabic/English)**: Full Arabic and English database translation layer with RTL compatibility.

---

## Challenges & Solutions | التحديات والحلول

*   **Challenge 1 (RFQ Multi-Vendor Routing and Automated Order Splitting):** Designing a system that allows customers to request custom quotes and routes them to multiple vendors, managing independent offers, and converting the accepted offer into a standard order without manual admin interference.
    *   **Solution:** Built the `request_quotation_vendors` pivot engine. When the admin selects vendors, the system creates pivot records with a `pending` status and triggers Firebase notifications. Vendors reply with price and notes via their dashboard, updating the status to `offer_sent` (triggering customer notifications). Upon customer acceptance, the system automatically routes the data to a transaction service, creates a corresponding `order` record, allocates stock, and creates a Zoho Books sync job.
*   **Challenge 2 (Next.js 15 High QPS Fan-Out & Rate Protection):** Next.js 15 page rendering generates multiple concurrent API requests (departments, categories, products, filters, footer). At 1,000 users/minute, this caused extreme fan-out hitting the database, leading to performance degradation.
    *   **Solution:** Added `Cache::remember()` tags for guest routes (10-min TTL) in the `ProductApiRepository`, optimized MySQL indexes, and configured realistic rate-limit thresholds (600/min global API, 300/min products, 15/min checkout) preventing server exhaustion.
*   **Challenge 3 (N+1 Query Regression & Variant Translation Bugs in Complex Catalog Models):** Retrieving products with multiple nested relationships (variants, translation attributes, attachments) often caused slow response times (~1000ms) due to hidden N+1 queries. Additionally, variant option name translations were failing to load in guest-facing APIs (returning empty values) due to mapping errors.
    *   **Solution:** Restructured the repository query pipeline with eager loading, and enabled strict model guards (`Model::preventLazyLoading(!app()->isProduction())`) during development. Fixed the translation bug by mapping variant attributes to the unified translatable `value` field in the `VariantsConfiguration` model, correcting endpoints like `get-variants-ai` and `get-main-categories-with-tree` to return correct Arabic and English variant translations (e.g. أبيض / White).
*   **Challenge 4 (Asynchronous Zoho ERP Sync Failures):** Syncing customer checkouts to Zoho Books synchronously slowed down response times by 2-5 seconds and could fail checkouts if the Zoho API was down.
    *   **Solution:** Built a non-blocking background queue job (`SyncOrderToZohoJob`) using Redis queues with 3 automatic retries and exponential backoff (1min, 5min, 15min) in the checkout pipeline.
*   **Challenge 5 (Production Debugging & Log Correlation):** Tracing errors across 14 modules in high-traffic production logs was extremely difficult.
    *   **Solution:** Implemented a `RequestCorrelationId` middleware sharing a unique request UUID (`X-Request-Id`) across all log instances, allowing developers to trace the entire lifecycle of a request in logs.
*   **Challenge 6 (Unstructured RFQ Uploads & Arabic Typo Matching):** Standard OCR returns raw, unstructured text from uploaded quote files (images/PDFs) with unpredictable formatting and spelling variations (e.g. using ه instead of ة or ي instead of ى), making direct database lookup impossible.
    *   **Solution:** Built an asynchronous background queue system (`ocr-processing` using database drivers) that routes uploaded files to an n8n webhook for OCR extraction. The returned data passes to the `RfqExtractionMatchingService`, which normalizes Arabic text (cleaning symbols and standardizing letters), scores candidate database products and variants using a word-level similarity match algorithm, and classifies them into `matched`, `ambiguous`, or `undefined` statuses for fast admin validation.

---

## Key Takeaways | النقاط الرئيسية المستفادة

1.  **Architecture Modularity is Key**: Splitting the system into 14 distinct modules prevents code rot and allows seamless addition of complex workflows (like RFQ or Accounting) without affecting checkout.
2.  **API Optimization for Next.js is Critical**: Decoupled frontends require robust caching strategies (Redis tags + client-side RTK Query) to handle traffic without crashing the API backend.
3.  **Background Queues for ERP Integrations**: Third-party API integrations (like Zoho Books) must be asynchronous and queue-based to protect user checkout performance.
4.  **Dev-Time Warnings Prevent Production Bugs**: Strict guards like `preventLazyLoading` catch N+1 regressions before they reach code review.
