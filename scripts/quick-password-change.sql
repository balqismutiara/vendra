-- Quick SQL script untuk mengganti password SuperAdmin
-- Jalankan di MySQL Workbench atau command line

-- 1. Lihat user yang ada
SELECT id, email, name, role, status FROM users WHERE role = 'SUPERADMIN';

-- 2. Update password SuperAdmin (password: "PASSWORD_BARU_ANDA")
-- Hash bcrypt untuk "PASSWORD_BARU_ANDA" dengan salt rounds 12
UPDATE users 
SET password = '$2a$12$REPLACE_WITH_NEW_BCRYPT_HASH'
WHERE email = 'superadmin@vendra.com' AND role = 'SUPERADMIN';

-- 3. Verifikasi perubahan
SELECT id, email, name, role, status, 
       SUBSTRING(password, 1, 20) as password_hash_preview
FROM users 
WHERE role = 'SUPERADMIN';

-- 4. Jika SuperAdmin belum ada, buat yang baru
INSERT INTO users (id, email, name, password, role, status, createdAt, updatedAt)
SELECT 
    'superadmin001' as id,
    'superadmin@vendra.com' as email,
    'Super Administrator' as name,
    '$2a$12$REPLACE_WITH_NEW_BCRYPT_HASH' as password,
    'SUPERADMIN' as role,
    'APPROVED' as status,
    NOW() as createdAt,
    NOW() as updatedAt
WHERE NOT EXISTS (
    SELECT 1 FROM users WHERE email = 'superadmin@vendra.com'
);

-- Login credentials setelah script ini dijalankan:
-- Email: superadmin@vendra.com
-- Password: PASSWORD_BARU_ANDA
