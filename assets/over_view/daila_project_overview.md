# Project Overview / نظرة عامة على المشروع

## Project Name | اسم المشروع
**Daila - E-commerce & CRM Platform** 
*(دايلا - منصة التجارة الإلكترونية وإدارة علاقات العملاء)*

---

## Short Description | وصف قصير
A comprehensive bilingual (Arabic/English) web application that serves as both an e-commerce platform and a dedicated CRM. It allows customers to easily order products via a cookie-based cart system, while providing administrators with a robust dashboard to manage content, track orders through various shipping stages, and leverage AI to auto-generate corporate content.

*(تطبيق ويب شامل ثنائي اللغة (عربي/إنجليزي) يعمل كمنصة للتجارة الإلكترونية ونظام لإدارة علاقات العملاء (CRM). ويتيح للعملاء طلب المنتجات بسهولة عبر نظام سلة مشتريات يعتمد على ملفات تعريف الارتباط (Cookies)، بينما يوفر للمسؤولين لوحة تحكم قوية لإدارة المحتوى، وتتبع الطلبات عبر مراحل الشحن المختلفة، والاستفادة من الذكاء الاصطناعي لتوليد محتوى الشركات تلقائيًا.)*

---

## Medium Description | وصف متوسط
Daila is an advanced E-commerce and CRM system built with Laravel to streamline online sales and customer relations. The platform features a guest-friendly shopping experience where cart data is preserved via cookies, allowing seamless browsing and checkout without mandatory account creation. During checkout, shipping costs are dynamically calculated based on the selected Governorate, and orders are assigned unique 10-digit tracking numbers. The backend CRM empowers admins to categorize and process orders across multiple statuses (New, Shipped, Delivered). Furthermore, the platform integrates Google Gemini AI to assist administrators in generating dynamic content for the "About Us", "Vision", and "Mission" sections, significantly reducing administrative overhead. The entire system has native bilingual support to cater to both Arabic and English speaking audiences.

*(دايلا هو نظام متطور للتجارة الإلكترونية وإدارة علاقات العملاء مبني باستخدام Laravel لتسهيل المبيعات عبر الإنترنت وعلاقات العملاء. تتميز المنصة بتجربة تسوق سلسة للزوار حيث يتم حفظ بيانات السلة عبر ملفات تعريف الارتباط (Cookies)، مما يتيح التصفح وإتمام الشراء دون الإلزام بإنشاء حساب. أثناء الدفع، يتم حساب تكاليف الشحن ديناميكيًا بناءً على المحافظة المحددة، ويُمنح كل طلب رقم تتبع فريد مكون من 10 أرقام. تُمكّن لوحة تحكم CRM المسؤولين من تصنيف ومعالجة الطلبات عبر حالات متعددة (جديد، مشحون، تم التوصيل). علاوة على ذلك، تدمج المنصة تقنية الذكاء الاصطناعي Google Gemini لمساعدة المسؤولين في توليد محتوى ديناميكي لأقسام "من نحن"، و"الرؤية"، و"المهمة"، مما يقلل بشكل كبير من العبء الإداري. يدعم النظام اللغة العربية والإنجليزية بشكل متأصل لخدمة جمهور واسع.)*

---

## Technologies & Packages | التقنيات والحزم المستخدمة

### **Backend (الباك إند):**
*   **Framework:** Laravel 10 (PHP 8.1+)
*   **Database:** MySQL
*   **Core Packages:**
    *   `google-gemini-php/laravel`: For integrating AI capabilities to auto-generate content directly within the dashboard.
    *   `laravel/sanctum`: For API authentication (if required for mobile/external integrations).
    *   `laravel/ui`: For legacy/custom UI scaffolding and authentication routes.
    *   **Native Bilingual Strategy:** Database tables (e.g., Products, Offers, Blogs) distinctively utilize `_ar` and `_en` suffixes (e.g., `title_ar`, `title_en`) to serve localized content natively without additional translatable packages.

### **Frontend (الفرونت إند):**
*   **Core:** Blade Templates, HTML5, CSS3, JavaScript.
*   **Styling:** Bootstrap 5 & Sass.
*   **Build Tool:** Vite (`laravel-vite-plugin`).
*   **Features:** DOM-based cart management, interactive UI.

---

## Key Features | الميزات الأساسية
1.  **Cookie-Based Shopping Cart**: Guests can browse products, add items to their cart, and adjust quantities; all data persists locally via browser Cookies (expiring securely), preventing data loss during sessions.
2.  **Dynamic Checkout & Governorate Shipping**: Automatic calculation of shipping fees based on the user's governorate selection, factored alongside a standard 15% VAT and the total product cost.
3.  **Comprehensive CRM Dashboard**: Admins can manage the entire lifecycle of an order (`NewOrder`, `ShippedOrder`, `DeliveredOrder`) and efficiently track changes via an `OrderHistory` model.
4.  **Google Gemini AI Content Generation**: The [AboutUsController](file:///c:/xampp/htdocs/daila/app/Http/Controllers/Dashboard/AboutUsController.php#11-148) uses `GeminiService` to pass specific prompts ("about", "vision", "mission") to auto-generate corporate textual content in real-time for the website.
5.  **Multi-Module Content Management System (CMS)**: Out-of-the-box management for Blogs, Sliders, Portfolios, Menus, Offers, Features, and Tracking Tools.
6.  **WhatsApp Integration**: Verifies customers via WhatsApp numbers during the checkout phase to streamline communication and link historical purchases.

---

## Challenges & Solutions | التحديات والحلول
*   **Challenge 1 (Guest Cart Retention):** Retaining a user's shopping cart items effectively without forcing them to register or login upfront.
    *   **Solution:** Engineered a robust [CartController](file:///c:/xampp/htdocs/daila/app/Http/Controllers/Front/CartController.php#18-387) that accurately stores array-based cart structures (Product IDs, Quants, Prices) strictly within Laravel Cookies for 120 minutes/2 hours, seamlessly reading and modifying the array directly from HTTP request headers.
*   **Challenge 2 (Automated Copywriting):** Administrators lacking the time or expertise to constantly update corporate texts (Vision, Mission, etc.).
    *   **Solution:** Integrated `gemini-1.5-flash-latest` model to accept targeted parameters/prompts from the Blade view. The CRM now generates highly relevant, creative content arrays dynamically.
*   **Challenge 3 (Tracking Disparate Orders):** Managing customer orders from various regions while ensuring correct shipping values and trackable history without manual math.
    *   **Solution:** Implemented regional `Governorate` models that hold set `shipping_price` values. The `OrderSubmit` logic programmatically generates a unique `10-digit Order Number` and logs all initial states instantly into an `OrderHistory` table for secure CRM tracking.

---

## Key Takeaways | النقاط الرئيسية المستفادة
1.  **AI is a Practical Dashboard Tool:** Embedding tools like Google Gemini deeply within admin panel controllers proves that AI is no longer a gimmick, but a functional asset for dynamic CMS maintenance.
2.  **Frictionless E-Commerce Converts Better:** Relying on Cookie-state carts and utilizing WhatsApp numbers as primary identifiers drastically reduces the barrier for user checkout. 
3.  **Monolithic Architectures Still Thrive:** Combining E-Commerce, CRM, and CMS into a single highly-structured Laravel application reduces external API latency and keeps data relationships (Customer ↔ Order ↔ Governorate) perfectly rigid and secure.
