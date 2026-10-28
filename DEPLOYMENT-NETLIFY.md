# 🚀 Panduan Deploy Vendra CRM ke Netlify

## ⚠️ PENTING - Netlify & Next.js

**CATATAN:** Netlify memiliki keterbatasan untuk Next.js dibandingkan Vercel:
- Server-side rendering (SSR) terbatas
- API routes memerlukan konfigurasi tambahan
- Performa mungkin tidak seoptimal Vercel

**Rekomendasi:** Gunakan Vercel untuk hasil terbaik.

## 📋 Persiapan

### 1. Push Code ke GitHub
```bash
git add .
git commit -m "Setup for Netlify deployment"
git push origin main
```

## 🎯 Cara Deploy ke Netlify

### Langkah 1: Buka Netlify
1. Buka https://app.netlify.com
2. Login dengan GitHub
3. Klik "Add new site" → "Import an existing project"

### Langkah 2: Connect Repository
1. Pilih "GitHub"
2. Authorize Netlify (jika belum)
3. Pilih repository: `Galang0304/vendra_kasir`

### Langkah 3: Build Settings
Netlify akan auto-detect dari `netlify.toml`, tapi pastikan:

- **Base directory:** (kosongkan)
- **Build command:** `prisma generate && npm run build`
- **Publish directory:** `.next`
- **Node version:** 20

### Langkah 4: Environment Variables
Tambahkan environment variables berikut:

```env
DATABASE_URL=mysql://username:password@localhost:3306/vendra_crm

NEXTAUTH_SECRET=your-nextauth-secret

VENDRA_AI_PROVIDER=gemini
VENDRA_AI_ENABLED=true
VENDRA_AI_MODEL=gemini-2.0-flash

VENDRA_GEMINI_API_KEY_1=your-gemini-api-key

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=vendracrm@gmail.com
EMAIL_PASS=your-email-app-password
EMAIL_FROM=Vendra CRM <vendracrm@gmail.com>

SUPERADMIN_EMAIL=admin@example.com

VENDRA_OPENAI_API_KEY=sk-your-openai-api-key

WEBHOOK_API_KEY=your-webhook-api-key
```

**JANGAN ISI `NEXTAUTH_URL` DULU** - akan diisi setelah deploy!

### Langkah 5: Deploy
1. Klik "Deploy site"
2. Tunggu proses build (3-5 menit)
3. ☕ Minum kopi...

### Langkah 6: Update NEXTAUTH_URL
1. Setelah deploy berhasil, copy site URL (contoh: `https://vendra-crm-xxx.netlify.app`)
2. Masuk ke Site settings → Environment variables
3. Tambahkan:
   ```
   NEXTAUTH_URL=https://vendra-crm-xxx.netlify.app
   ```
4. Klik "Trigger deploy" untuk redeploy

## ⚙️ Konfigurasi Tambahan

### Custom Domain (Opsional)
1. Site settings → Domain management
2. Add custom domain
3. Update DNS sesuai instruksi
4. Update `NEXTAUTH_URL` dengan domain baru

### Functions (untuk API Routes)
Netlify Functions akan auto-handle Next.js API routes via plugin.

## 🐛 Troubleshooting

### Build Error: "Prisma not found"
**Solusi:**
- Pastikan `prisma generate` ada di build command
- Check DATABASE_URL sudah benar

### NextAuth Error
**Solusi:**
- Pastikan NEXTAUTH_URL sama persis dengan URL site
- Pastikan NEXTAUTH_SECRET sudah di-set

### Database Connection Timeout
**Solusi:**
- Netlify serverless function ada timeout 10 detik
- Pastikan database accessible dari internet
- Consider using connection pooling

### API Routes Not Working
**Solusi:**
- Pastikan `@netlify/plugin-nextjs` terinstall
- Check `netlify.toml` configuration

## 📊 Monitoring

- **Netlify Dashboard:** https://app.netlify.com
- **Deploy logs:** Check di dashboard untuk debug
- **Analytics:** Available in Netlify dashboard

## 🔄 Auto Deployment

Setiap push ke branch `main`:
- Netlify otomatis build & deploy
- Preview deployment untuk pull requests
- Rollback mudah via dashboard

---

## ⚠️ Perbandingan: Vercel vs Netlify untuk Next.js

| Feature | Vercel | Netlify |
|---------|--------|---------|
| Next.js Support | ⭐⭐⭐⭐⭐ Native | ⭐⭐⭐ Via Plugin |
| SSR Performance | Excellent | Good |
| API Routes | Seamless | Limited |
| Deployment Speed | Fast | Fast |
| Free Tier | 100GB bandwidth | 100GB bandwidth |
| Database Edge | Support Vercel Postgres | Manual setup |

**Rekomendasi Final:** Untuk Next.js app dengan database & API routes seperti Vendra CRM, **Vercel tetap pilihan terbaik**.

---

**Ready to deploy?** Push to GitHub dan connect ke Netlify! 🚀
