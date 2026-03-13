# Project Overview / نظرة عامة على المشروع

## Project Name | اسم المشروع
**Sila - Family Kinship & Networking Platform** (Database Name: `sla-r7m`)
*(منصة صلة - لإدارة التواصل وصلة الرحم)*

---

## Short Description | وصف قصير
A robust mobile-focused API backend built to manage personal relationships, family networks, and social groups. It features secure multi-platform authentication (including Google and Apple), OTP-based verification, and multi-language support.

---

## Medium Description | وصف متوسط
This project is a specialized networking backend API designed to strengthen family ties ("Silat Al-Rahm") and manage personal contacts. It provides complete endpoints for users to securely add relatives (individuals) with detailed contact and social media profiles, categorize them into relational groups, and organize social family events. Tailored seamlessly for mobile frontend frameworks like Flutter, the system features robust authentication supporting traditional email login with OTP verification, alongside seamless social login integrations (Google and Apple) via Socialite and JWT. It also handles dynamic multilingual translations for a localized and highly accessible user experience.

---

## Technologies & Packages | التقنيات والحزم المستخدمة

### **Backend (الباك إند):**
*   **Framework:** Laravel 10 (PHP 8.1+)
*   **Database:** MySQL
*   **Core Packages:**
    *   `tymon/jwt-auth`: For secure, stateless JSON Web Token API authentication.
    *   `laravel/socialite` & `socialiteproviders/google`: For handling Google and Apple social login SSO integrations.
    *   `ichtrojan/laravel-otp`: For generating and verifying One-Time Passwords (OTPs) during password resets and email verification.
    *   `laravel/sanctum`: Lightweight authentication framework for APIs.

### **Frontend / Client (الفرونت إند / العميل):**
*   **Target Client:** Flutter Mobile Application (Integrated via specialized API endpoints like `AuthFlutterController`).
*   **Web Assets:** Basic Vite & Bootstrap scaffolding available for internal administrative purposes or landing pages.

---

## Key Features | الميزات الأساسية
1.  **Individual & Relationship Management**: Users can add relatives and contacts, specifying their relationship type, phone numbers, locations, and multiple social media links (Facebook, X, LinkedIn, Snapchat).
2.  **Group Categorization**: The ability to organize individuals into logical, customizable groups (e.g., Immediate Family, Cousins, Friends).
3.  **Event Organization**: Manage family gatherings and events, with the capability to link specific individuals and locations to these events.
4.  **Comprehensive Authentication System**: Supports traditional email registration with OTP verification, robust JWT-based session management, and integrated Apple & Google Single Sign-On (SSO).
5.  **Multi-language Support**: Dynamic structure utilizing `languages` and `translations` tables to seamlessly serve content to users in their preferred locale.
6.  **API-First Architecture**: Routes and controllers explicitly optimized for a Flutter mobile frontend, providing fast and standardized JSON responses.

---

## Challenges & Solutions | التحديات والحلول
*   **Challenge 1 (Cross-Platform Authentication):** Ensuring secure, unified authentication for mobile users who prefer different login methods (Email, Google, Apple) without relying on traditional web-session states.
    *   **Solution:** Implemented a hybrid authentication strategy combining JWT for standard logins and Laravel Socialite for managing external OAuth providers, all passing through highly customized Flutter API endpoints.
*   **Challenge 2 (Mobile Account Recovery & Verification):** Verifying user emails and handling password resets securely on mobile devices without relying on traditional web-based email reset links, which often break mobile UX flows.
    *   **Solution:** Integrated `ichtrojan/laravel-otp` to send and verify secure 4-6 digit numeric OTP codes via email, providing a much smoother, mobile-native experience for account verification and recovery.
*   **Challenge 3 (Complex Relationship Mapping):** Users needed a systematic way to manage not just simple contacts, but the *type* of relationship, group them logically, and invite them to specific events.
    *   **Solution:** Designed a highly flexible relational database schema featuring isolated `individuals`, `groups`, and `events` tables, utilizing pivot tables (`group_individual`, `event_individual`) to dynamically link members across the entire platform.

---

## Key Takeaways | النقاط الرئيسية المستفادة
1.  **OTPs Enhance Mobile UX:** Utilizing OTPs instead of traditional reset links drastically improves the user experience and completion rate for mobile-first applications.
2.  **Robust Relational Models:** Properly structuring the database to separate individuals, groups, and events allows the application to smoothly scale and perform fast queries as a user's family tree or social network grows.
3.  **Unified JWT & SSO Integration:** Combining Laravel Socialite with JWT ensures a highly secure, stateless API backend perfectly suited to handle the demands of modern mobile frameworks like Flutter.
