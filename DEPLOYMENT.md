# 🚀 Panduan Deployment Vendra CRM ke Arenhost.com

## 📋 Prasyarat

### Yang Anda Butuhkan:
- ✅ **VPS / Cloud Server di Arenhost** (BUKAN Shared Hosting)
- ✅ Minimal Spesifikasi VPS:
  - RAM: 1GB (Recommended: 2GB)
  - CPU: 1 Core (Recommended: 2 Cores)
  - Storage: 20GB SSD
  - OS: Ubuntu 20.04 atau 22.04 LTS
- ✅ Domain name (opsional, bisa pakai IP dulu)
- ✅ Akses SSH ke VPS

---

## 📦 Langkah 1: Setup VPS di Arenhost

### 1.1 Order VPS
1. Login ke **arenhost.com**
2. Pilih paket **VPS** atau **Cloud Server**
3. Pilih OS: **Ubuntu 22.04 LTS**
4. Selesaikan pembayaran
5. Catat kredensial SSH yang dikirim via email

### 1.2 Connect ke VPS via SSH
```bash
# Dari komputer lokal Anda (PowerShell/CMD/Terminal)
ssh root@IP_ADDRESS_VPS_ANDA

# Masukkan password yang diberikan arenhost
```

---

## 🔧 Langkah 2: Install Dependencies di VPS

### 2.1 Update System
```bash
sudo apt update && sudo apt upgrade -y
```

### 2.2 Install Node.js 20.x
```bash
# Install NodeSource repository
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -

# Install Node.js
sudo apt install -y nodejs

# Verify installation
node --version  # Should show v20.x.x
npm --version   # Should show v10.x.x
```

### 2.3 Install MySQL
```bash
# Install MySQL Server
sudo apt install -y mysql-server

# Secure MySQL installation
sudo mysql_secure_installation

# Login ke MySQL
sudo mysql

# Buat database dan user
CREATE DATABASE vendra_crm_production;
CREATE USER 'vendra_user'@'localhost' IDENTIFIED BY 'PASSWORD_ANDA_YANG_KUAT';
GRANT ALL PRIVILEGES ON vendra_crm_production.* TO 'vendra_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 2.4 Install PM2 (Process Manager)
```bash
sudo npm install -g pm2
```

### 2.5 Install Build Dependencies (untuk canvas library)
```bash
sudo apt install -y build-essential libcairo2-dev libpango1.0-dev libjpeg-dev libgif-dev librsvg2-dev
```

### 2.6 Install Git
```bash
sudo apt install -y git
```

---

## 📁 Langkah 3: Upload Project ke VPS

### Opsi A: Via Git (Recommended)
```bash
# Di VPS, buat folder untuk aplikasi
mkdir -p /var/www
cd /var/www

# Clone repository Anda
git clone https://github.com/USERNAME/vendra.git
cd vendra

# Atau jika private repo, gunakan HTTPS dengan token
git clone https://YOUR_TOKEN@github.com/USERNAME/vendra.git
```

### Opsi B: Via SFTP/SCP (Manual Upload)
```bash
# Dari komputer lokal, upload via SCP
# Compress dulu folder project
tar -czf vendra.tar.gz /path/to/vendra

# Upload ke VPS
scp vendra.tar.gz root@IP_VPS:/var/www/

# Di VPS, extract
cd /var/www
tar -xzf vendra.tar.gz
mv vendra-kasir vendra  # Sesuaikan nama folder
```

---

## ⚙️ Langkah 4: Konfigurasi Project

### 4.1 Install Dependencies
```bash
cd /var/www/vendra
npm install --production
```

### 4.2 Setup Environment Variables
```bash
# Copy template .env.production
cp .env.production.example .env

# Edit file .env
nano .env
```

**Edit nilai-nilai berikut di file `.env`:**
```bash
# Database - sesuaikan dengan MySQL yang dibuat tadi
DATABASE_URL="mysql://vendra_user:PASSWORD_ANDA@localhost:3306/vendra_crm_production"

# Domain/URL production
NEXTAUTH_URL="http://IP_VPS_ANDA:3001"  # atau "https://yourdomain.com"
APP_URL="http://IP_VPS_ANDA:3001"

# Generate secret baru
NEXTAUTH_SECRET="hasil_dari_openssl_rand_base64_32"

# Origins
ALLOWED_ORIGINS="http://IP_VPS_ANDA:3001,https://yourdomain.com"

# NODE_ENV harus production
NODE_ENV="production"
```

**Generate NEXTAUTH_SECRET:**
```bash
openssl rand -base64 32
# Copy hasil output ke .env di bagian NEXTAUTH_SECRET
```

### 4.3 Setup Database dengan Prisma
```bash
# Generate Prisma Client
npm run db:generate

# Push schema ke database
npm run db:push

# (Opsional) Seed data awal
npm run db:seed
```

### 4.4 Build Project
```bash
# Build Next.js untuk production
npm run build
```

---

## 🚀 Langkah 5: Run dengan PM2

### 5.1 Buat Folder Logs
```bash
mkdir -p /var/www/vendra/logs
```

### 5.2 Start Aplikasi dengan PM2
```bash
cd /var/www/vendra

# Start dengan PM2
pm2 start ecosystem.config.js

# Lihat status
pm2 status

# Lihat logs
pm2 logs vendra-crm
```

### 5.3 Setup PM2 Auto-Start saat VPS Reboot
```bash
# Generate startup script
pm2 startup systemd

# Copy dan jalankan command yang muncul (biasanya dimulai dengan sudo env...)

# Save PM2 process list
pm2 save
```

---

## 🌐 Langkah 6: Setup Nginx (Reverse Proxy)

### 6.1 Install Nginx
```bash
sudo apt install -y nginx
```

### 6.2 Konfigurasi Nginx
```bash
# Buat config file
sudo nano /etc/nginx/sites-available/vendra-crm
```

**Paste konfigurasi berikut:**
```nginx
server {
    listen 80;
    server_name IP_VPS_ANDA yourdomain.com www.yourdomain.com;

    # Increase upload size limit
    client_max_body_size 50M;

    location / {
        proxy_pass http://localhost:3001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
        proxy_read_timeout 300s;
        proxy_connect_timeout 300s;
    }
}
```

### 6.3 Aktifkan Konfigurasi
```bash
# Buat symbolic link
sudo ln -s /etc/nginx/sites-available/vendra-crm /etc/nginx/sites-enabled/

# Test konfigurasi
sudo nginx -t

# Restart Nginx
sudo systemctl restart nginx

# Enable Nginx auto-start
sudo systemctl enable nginx
```

---

## 🔒 Langkah 7: Setup SSL (HTTPS) dengan Let's Encrypt

### 7.1 Install Certbot
```bash
sudo apt install -y certbot python3-certbot-nginx
```

### 7.2 Generate SSL Certificate
```bash
# Pastikan domain sudah pointing ke IP VPS Anda
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Follow the prompts
# Pilih opsi redirect HTTP ke HTTPS
```

### 7.3 Update .env dengan HTTPS
```bash
nano /var/www/vendra/.env

# Update:
NEXTAUTH_URL="https://yourdomain.com"
APP_URL="https://yourdomain.com"
ALLOWED_ORIGINS="https://yourdomain.com,https://www.yourdomain.com"

# Restart aplikasi
pm2 restart vendra-crm
```

---

## 🔥 Langkah 8: Setup Firewall

```bash
# Allow SSH, HTTP, HTTPS
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'

# Enable firewall
sudo ufw enable

# Check status
sudo ufw status
```

---

## 📊 Monitoring & Maintenance

### Useful PM2 Commands
```bash
# Lihat status aplikasi
pm2 status

# Lihat logs real-time
pm2 logs vendra-crm

# Restart aplikasi
pm2 restart vendra-crm

# Stop aplikasi
pm2 stop vendra-crm

# Monitor resource usage
pm2 monit
```

### Update Aplikasi
```bash
# Pull latest code
cd /var/www/vendra
git pull origin main

# Install new dependencies (if any)
npm install --production

# Rebuild
npm run build

# Generate Prisma if schema changed
npm run db:generate
npm run db:push

# Restart
pm2 restart vendra-crm
```

### Backup Database
```bash
# Manual backup
mysqldump -u vendra_user -p vendra_crm_production > backup_$(date +%Y%m%d).sql

# Restore from backup
mysql -u vendra_user -p vendra_crm_production < backup_20250130.sql
```

### Setup Automatic Backups (Cron)
```bash
# Edit crontab
crontab -e

# Tambahkan line ini untuk backup harian jam 2 pagi
0 2 * * * mysqldump -u vendra_user -pPASSWORD vendra_crm_production > /var/backups/vendra_$(date +\%Y\%m\%d).sql
```

---

## 🐛 Troubleshooting

### Aplikasi tidak bisa diakses
```bash
# Check PM2 status
pm2 status

# Check logs
pm2 logs vendra-crm

# Check port 3001
netstat -tulpn | grep 3001

# Restart aplikasi
pm2 restart vendra-crm
```

### Database connection error
```bash
# Check MySQL status
sudo systemctl status mysql

# Test MySQL connection
mysql -u vendra_user -p -e "SHOW DATABASES;"

# Check DATABASE_URL di .env
cat /var/www/vendra/.env | grep DATABASE_URL
```

### Build error (canvas library)
```bash
# Install build dependencies
sudo apt install -y build-essential libcairo2-dev libpango1.0-dev libjpeg-dev libgif-dev librsvg2-dev

# Rebuild
npm rebuild canvas
npm run build
```

### Permission errors
```bash
# Fix ownership
sudo chown -R $USER:$USER /var/www/vendra

# Fix permissions
chmod -R 755 /var/www/vendra
```

---

## ✅ Checklist Deployment

- [ ] VPS sudah aktif dan bisa SSH
- [ ] Node.js 20.x terinstall
- [ ] MySQL terinstall dan database dibuat
- [ ] PM2 terinstall global
- [ ] Build dependencies terinstall
- [ ] Project sudah di-upload ke VPS
- [ ] Dependencies npm terinstall
- [ ] File .env sudah dikonfigurasi dengan benar
- [ ] Database schema di-push dengan Prisma
- [ ] Build Next.js berhasil
- [ ] PM2 running dan auto-restart enabled
- [ ] Nginx terinstall dan dikonfigurasi
- [ ] SSL certificate terinstall (jika pakai domain)
- [ ] Firewall dikonfigurasi
- [ ] Aplikasi bisa diakses dari browser

---

## 📞 Support

Jika ada masalah saat deployment:
1. Check logs: `pm2 logs vendra-crm`
2. Check Nginx error: `sudo tail -f /var/log/nginx/error.log`
3. Check MySQL: `sudo journalctl -u mysql`

**Selamat! Aplikasi Vendra CRM Anda sekarang sudah live! 🎉**
