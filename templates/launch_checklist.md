# Production Launch Checklist

Use this checklist to verify that your application is fully prepared for a production release.

## 1. Secrets & Configuration
- [ ] No secrets, keys, or private endpoints are hardcoded in version-controlled files.
- [ ] Environment variables (`.env`) are configured on the hosting providers (Vercel, Supabase, etc.).
- [ ] Development keys (e.g., Stripe sandbox) are replaced with production credentials.

## 2. API & Network
- [ ] CORS is configured on the backend to allow requests only from the production frontend domain.
- [ ] SSL/TLS is active (HTTPS is enforced across all routes).
- [ ] API routes return proper HTTP status codes for both success and error paths.

## 3. Security Audit
- [ ] The 5-Point Security Review Prompt has been run and passes completely.
- [ ] Input validation is verified on all API endpoints.
- [ ] Access controls and database row ownership checks are in place.

## 4. Verification & Testing
- [ ] All acceptance criteria in active feature specs are fully met.
- [ ] Manual walkthrough of unhappy paths (duplicate clicks, bad forms, expired sessions) passes.
- [ ] All automated tests run and pass without failures.

## 5. Version Control & Backup
- [ ] Git status is clean (all working modifications committed).
- [ ] Code is pushed to the remote GitHub repository.
- [ ] A Git release tag (e.g., `v1.0.0`) is created at the release commit.
