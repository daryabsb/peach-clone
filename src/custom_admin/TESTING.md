# Custom Admin Testing Guide

This document provides a guide for manually testing the custom admin functionality.

## Prerequisites

- Django server running (`python manage.py runserver`)
- A staff user account created
- Some sample data in the database (companies, users, items, transactions)

## Login Testing

1. **Staff User Login**
   - Navigate to `/custom-admin/login/`
   - Enter staff user credentials
   - Verify redirection to dashboard
   - Verify welcome message

2. **Regular User Login**
   - Navigate to `/custom-admin/login/`
   - Enter regular (non-staff) user credentials
   - Verify redirection away from admin area
   - Verify warning message

3. **Invalid Login**
   - Navigate to `/custom-admin/login/`
   - Enter invalid credentials
   - Verify error message
   - Verify staying on login page

## Dashboard Testing

1. **Dashboard Access**
   - Login as staff user
   - Navigate to `/custom-admin/`
   - Verify dashboard loads correctly

2. **Dashboard UI Elements**
   - Verify dashboard header with date range picker and refresh button
   - Verify stat cards for Sales, Purchases, Users, and Items
   - Verify financial summary section
   - Verify transaction statistics with chart/table toggle
   - Verify recent transactions section with filter dropdown
   - Verify recent activities section

3. **Dashboard Interactivity**
   - Test refresh button (should spin and reload page)
   - Test financial period dropdown (This Month, Last Month, etc.)
   - Test transaction chart/table toggle
   - Test transaction filter dropdown (All, Sales Only, Purchases Only)

## Sidebar Testing

1. **Sidebar Navigation**
   - Verify all sidebar links work correctly
   - Verify active state for current page
   - Test sidebar collapse toggle
   - Verify sidebar collapse state persists across page loads

2. **Mobile Sidebar**
   - Resize browser to mobile width
   - Verify mobile header appears
   - Test mobile sidebar toggle
   - Verify sidebar closes when clicking outside

## Theme Testing

1. **Theme Toggle**
   - Locate theme toggle button
   - Test switching between light and dark themes
   - Verify theme state persists across page loads

## CRUD Operations Testing

1. **Company Management**
   - Navigate to company list
   - Verify existing companies display correctly
   - Test adding a new company
   - Test editing an existing company
   - Test deleting a company

2. **Item Management**
   - Navigate to item list
   - Verify existing items display correctly
   - Test adding a new item
   - Test editing an existing item
   - Test deleting an item

3. **Transaction Management**
   - Test each transaction type (Invoice, Purchase, Sale, Payment, Receive)
   - Verify list views display correctly
   - Test adding new transactions
   - Test editing existing transactions
   - Test deleting transactions

## User Management Testing

1. **User List**
   - Navigate to user list
   - Verify existing users display correctly

2. **User Operations**
   - Test adding a new user
   - Test editing an existing user
   - Test changing user permissions

## Activity Logging Testing

1. **Login/Logout Logging**
   - Login and logout several times
   - Navigate to dashboard
   - Verify login/logout activities appear in recent activities

2. **CRUD Operation Logging**
   - Perform various CRUD operations
   - Verify these operations are logged in recent activities

## Browser Compatibility Testing

1. **Desktop Browsers**
   - Test in Chrome, Firefox, Safari, Edge
   - Verify UI renders correctly
   - Verify all functionality works

2. **Mobile Browsers**
   - Test in mobile Chrome, Safari
   - Verify responsive design works
   - Verify all functionality works

## Performance Testing

1. **Page Load Times**
   - Verify dashboard loads in a reasonable time
   - Verify list views with many items load in a reasonable time

2. **Chart Rendering**
   - Verify transaction chart renders correctly and quickly

## Accessibility Testing

1. **Keyboard Navigation**
   - Test navigating the admin interface using only keyboard
   - Verify all interactive elements are accessible

2. **Screen Reader Compatibility**
   - Test with a screen reader
   - Verify all important information is announced

## Security Testing

1. **Permission Enforcement**
   - Verify non-staff users cannot access admin pages
   - Verify logout works correctly
   - Verify session expiration works

## Issues and Reporting

If you encounter any issues during testing, please document them with the following information:

- Page/feature being tested
- Steps to reproduce
- Expected behavior
- Actual behavior
- Browser/device information
- Screenshots (if applicable)