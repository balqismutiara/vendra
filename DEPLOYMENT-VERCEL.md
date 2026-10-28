# 🚀 Panduan Deploy Vendra CRM ke Vercel

## Persiapan Sebelum Deploy

### 1. Install Vercel CLI (Opsional)
```bash
npm install -g vercel
```

## 🎯 Cara Deploy ke Vercel

### Opsi 1: Deploy via GitHub (RECOMMENDED)

#### Langkah 1: Push ke GitHub
```bash
git add .
git commit -m "Ready for Vercel deployment"
git push origin main
```

#### Langkah 2: Connect ke Vercel
1. Buka https://vercel.com
2. Login dengan GitHub
3. Klik "Add New Project"
4. Import repository `vendra_kasir`
5. Framework Preset: Next.js (auto-detect)

#### Langkah 3: Setup Environment Variables
Di Vercel Dashboard, tambahkan environment variables berikut:

```env
DATABASE_URL=mysql://username:password@localhost:3306/vendra_crm

NEXTAUTH_URL=https://your-app-name.vercel.app
NEXTAUTH_SECRET=your-nextauth-secret

VENDRA_AI_PROVIDER=gemini
VENDRA_AI_ENABLED=true
VENDRA_AI_MODEL=gemini-2.0-flash

VENDRA_GEMINI_API_KEY_1=your-gemini-api-key
VENDRA_GEMINI_API_KEY_2=your-gemini-api-key-2-here
VENDRA_GEMINI_API_KEY_3=your-gemini-api-key-3-here
VENDRA_GEMINI_API_KEY_4=your-gemini-api-key-4-here
VENDRA_GEMINI_API_KEY_5=your-gemini-api-key-5-here

VENDRA_GEMINI_CURRENT_KEY_INDEX=1

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=vendracrm@gmail.com
EMAIL_PASS=your-email-app-password
EMAIL_FROM=Vendra CRM <vendracrm@gmail.com>

SUPERADMIN_EMAIL=admin@example.com

NODE_ENV=production

VENDRA_OPENAI_API_KEY=sk-your-openai-api-key

WEBHOOK_API_KEY=your-webhook-api-key
```

#### Langkah 4: Deploy!
- Klik "Deploy"
- Tunggu 2-3 menit
- Aplikasi online! 🎉

### Opsi 2: Deploy via Vercel CLI

```bash
# Login ke Vercel
vercel login

# Deploy
vercel

# Ikuti instruksi di terminal
# Pilih project settings yang sesuai

# Deploy ke production
vercel --prod
```

## 📝 Setelah Deploy

### Update NEXTAUTH_URL
1. Setelah deploy, copy URL aplikasi (misal: https://vendra-crm.vercel.app)
2. Update environment variable `NEXTAUTH_URL` di Vercel Dashboard
3. Redeploy (Vercel akan auto-redeploy)

### Test Aplikasi
1. Buka URL aplikasi
2. Login dengan akun yang ada di database
3. Test semua fitur

## 🔧 Troubleshooting

### Build Error: Prisma
Jika ada error Prisma saat build:
- Pastikan `prisma generate` ada di build command
- Check DATABASE_URL sudah benar

### Database Connection Error
- Pastikan firewall database allow connection dari Vercel
- Test koneksi manual dengan:
```bash
mysql -h localhost -u username -ppassword -P 3306 vendra_crm
```

### NextAuth Error
- Pastikan NEXTAUTH_URL sesuai dengan domain Vercel
- Pastikan NEXTAUTH_SECRET sudah di-set

## 🎯 Custom Domain (Opsional)

1. Di Vercel Dashboard → Settings → Domains
2. Add your custom domain
3. Update DNS records sesuai instruksi Vercel
4. Update NEXTAUTH_URL dengan domain baru

## 📊 Monitoring

- Vercel Dashboard: https://vercel.com/dashboard
- Analytics: Real-time traffic & performance
- Logs: Debugging production issues

## 🔄 Auto Deployment

Setiap kali push ke GitHub branch `main`:
- Vercel otomatis build & deploy
- Preview deployment untuk branch lain
- Rollback mudah jika ada masalah

---

**Ready to deploy? Push to GitHub and connect to Vercel!** 🚀
