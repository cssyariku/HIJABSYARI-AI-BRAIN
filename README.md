# HIJABSYARI-AI-BRAIN

**Project:** Hijab Syari Indonesia  
**Instagram:** `@hijabsyaricoid`  
**Type:** AI-first, faceless digital hijab media  
**Repository role:** Single Source of Truth (SSOT) untuk strategi, produksi konten, eksperimen, KPI, dan handoff lintas sesi/akun ChatGPT.  
**Version:** 1.0  
**Initialized:** 18 September 2026

---

## 1. START HERE

Repository ini adalah "otak" operasional Hijab Syari Indonesia. Tujuannya agar project tidak bergantung pada satu sesi chat, satu akun ChatGPT, atau ingatan percakapan.

Ketika memulai sesi baru, AI harus membaca dokumen dengan urutan:

1. `README.md`
2. `MASTER.md`
3. `CURRENT_STATE.md`
4. Dokumen spesifik sesuai tugas:
   - strategi/produksi → `CONTENT_SYSTEM.md`
   - visual, image/video AI, caption → `PROMPT_LIBRARY.md`
   - ide/topik → `CONTENT_BACKLOG.md`
   - riwayat perubahan → `CHANGELOG.md`

### Source-of-truth priority

Jika ada konflik:

1. Instruksi terbaru pengguna
2. `CURRENT_STATE.md`
3. `MASTER.md`
4. `CONTENT_SYSTEM.md`
5. `PROMPT_LIBRARY.md`
6. `CONTENT_BACKLOG.md`
7. `CHANGELOG.md`

`CURRENT_STATE.md` adalah status hidup project. Jangan menganggap rencana lama masih aktif jika CURRENT_STATE mengatakan sebaliknya.

---

## 2. PROJECT MISSION

Membangun kembali `@hijabsyaricoid` sebagai media digital hijab Indonesia yang:

- mudah ditemukan;
- berguna dan layak disimpan/dibagikan;
- memiliki identitas editorial;
- dapat diproduksi tanpa model/manpower besar;
- menggunakan AI secara bertanggung jawab;
- membangun audience dan trust sebelum monetisasi;
- pada fase matang dapat melakukan affiliate, kolaborasi brand, atau commerce tanpa merusak editorial trust.

Prinsip:

> **Traffic → Engagement → Trust → Community → Authority → Monetization**

Fase awal **bukan toko** dan **bukan hard-selling account**.

---

## 3. COMMAND PROTOCOL

Perintah berikut boleh digunakan dari chat mana pun.

### `/start HIJABSYARI`
Baca README → MASTER → CURRENT_STATE. Ringkas hanya informasi yang diperlukan untuk tugas saat ini. Jangan meminta user menjelaskan ulang informasi yang sudah ada.

### `/research-week`
Cari peluang konten terbaru. Pisahkan:
- tren terverifikasi;
- pertanyaan/problem audience;
- evergreen;
- eksperimen.

Jangan mengarang data Instagram atau tren.

### `/plan-week`
Buat rencana 7 hari berdasarkan CURRENT_STATE, winner/loser terbaru, backlog, dan kapasitas produksi.

### `/make-carousel [TOPIK]`
Hasilkan production package: objective, target, hook variants, selected hook, slide-by-slide copy, visual direction, AI prompts, caption, CTA, SEO keywords/hashtags, Stories derivative, KPI.

### `/make-reel [TOPIK]`
Hasilkan: objective, hook 0–2 detik, storyboard, shot list, image prompts, image-to-video prompts, on-screen text, VO opsional, caption, CTA, thumbnail, KPI.

### `/viralize [IDE]`
Perbaiki packaging tanpa membuat klaim palsu/clickbait murahan.

### `/repurpose [CONTENT]`
Ubah satu ide menjadi carousel + Reel + Stories + text/Threads-style derivative tanpa sekadar copy-paste.

### `/visual [IDE]`
Buat art direction dan prompt AI production-ready sesuai visual system.

### `/clone-winner [CONTENT]`
Identifikasi mekanisme keberhasilan lalu buat 5 turunan yang cukup berbeda agar tidak repetitif.

### `/analyze`
Analisis data Insights yang diberikan user. Bandingkan konten sejenis, gunakan median/baseline akun, tentukan WIN/NORMAL/UNDERPERFORM hanya berdasarkan data yang memadai.

### `/handoff`
Susun snapshot terbaru untuk memperbarui `CURRENT_STATE.md`.

---

## 4. CROSS-CHAT WORKFLOW

Contoh:

- **Chat A — Strategy/Planner:** research, `/plan-week`, eksperimen.
- **Chat B — Production:** `/make-carousel`, `/make-reel`.
- **Chat C — Visual Studio:** `/visual`, prompt image/video.
- **Chat D — Analytics:** `/analyze`, rekomendasi eksperimen.
- **Chat E — Handoff:** update CURRENT_STATE + CHANGELOG.

Semua chat bekerja dari SSOT yang sama.

---

## 5. FILE MAP

| File | Fungsi | Frekuensi perubahan |
|---|---|---|
| `MASTER.md` | PRD, positioning, audience, guardrails, roadmap | Rendah |
| `CURRENT_STATE.md` | Status project terbaru | Tinggi |
| `CONTENT_SYSTEM.md` | Sistem editorial, format, workflow, KPI | Sedang |
| `PROMPT_LIBRARY.md` | Prompt produksi AI dan template output | Sedang |
| `CONTENT_BACKLOG.md` | Bank ide dan series | Tinggi |
| `CHANGELOG.md` | Audit perubahan strategis | Saat ada perubahan |
| `CONTENT/` | Paket produksi per day: copywriting, aset siap unggah, dan pratinjau | Setiap konten selesai |

---

## 6. RULE FOR AI

Jangan:
- mengubah positioning diam-diam;
- menjadikan akun katalog produk pada fase awal;
- mengarang competitor metrics;
- menganggap semua konten viral cocok untuk brand;
- menyimpulkan dari satu post;
- mengorbankan trust demi views;
- membuat fake testimonial atau fake product experience;
- menganggap AI visual sebagai bukti kejadian nyata.

Selalu:
- prioritaskan value dan audience fit;
- gunakan data terbaru bila keputusan bergantung pada tren;
- bedakan fakta, observasi, hipotesis, dan rekomendasi;
- update CURRENT_STATE ketika keputusan penting berubah.

---

## 7. SUCCESS DEFINITION

Hijab Syari Indonesia berhasil ketika memiliki sistem yang secara konsisten menghasilkan:

**relevant attention + useful content + returning audience + recognizable editorial identity**, kemudian monetisasi yang mengikuti trust tersebut.

Bukan sekadar follower besar.
