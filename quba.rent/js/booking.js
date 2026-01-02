// Booking Form Handler - WhatsApp Integration
// Processes the booking form and opens WhatsApp with pre-filled message

document.addEventListener('DOMContentLoaded', function() {
    const bookingForm = document.getElementById('booking-form');
    
    if (!bookingForm) {
        console.log('Booking form not found on this page');
        return;
    }
    
    // Get current language (from URL or filename)
    function getCurrentLang() {
        const path = window.location.pathname;
        if (path.includes('-ar.html')) return 'ar';
        if (path.includes('-en.html')) return 'en';
        if (path.includes('-ru.html')) return 'ru';
        return 'az';
    }
    
    // Translations
    const translations = {
        az: {
            nameLabel: 'Adınız Soyadınız',
            phoneLabel: 'Telefon Nömrəsi',
            checkInLabel: 'Giriş Tarixi',
            checkOutLabel: 'Çıxış Tarixi',
            guestsLabel: 'Qonaq Sayı',
            commentsLabel: 'Əlavə Qeydlər',
            commentsPlaceholder: 'Xüsusi istəkləriniz, suallarınız...',
            submitBtn: '📱 WhatsApp ilə Göndərin',
            guestOptions: ['1 nəfər', '2 nəfər', '3 nəfər', '4 nəfər', '5 nəfər', '6+ nəfər'],
            validationFillAll: 'Zəhmət olmasa bütün məlumatları doldurun!',
            validationInvalidDates: 'Çıxış tarixi giriş tarixindən sonra olmalıdır!',
            confirmation: '✅ Bron sorğunuz hazırlandı! WhatsApp açılacaq.',
            support: '📞 Dəstək: +994 70 255 59 09 (Neriman) | 07:00 - 24:00',
            nights: 'gecə',
            nights_one: 'geecə'
        },
        ru: {
            nameLabel: 'Ваше имя',
            phoneLabel: 'Номер телефона',
            checkInLabel: 'Дата заезда',
            checkOutLabel: 'Дата выезда',
            guestsLabel: 'Количество гостей',
            commentsLabel: 'Дополнительные заметки',
            commentsPlaceholder: 'Ваши пожелания, вопросы...',
            submitBtn: '📱 Отправить в WhatsApp',
            guestOptions: ['1 гость', '2 гостя', '3 гостя', '4 гостя', '5 гостей', '6+ гостей'],
            validationFillAll: 'Пожалуйста, заполните все данные!',
            validationInvalidDates: 'Дата выезда должна быть позже даты заезда!',
            confirmation: '✅ Ваш запрос отправлен! Откроется WhatsApp.',
            support: '📞 Поддержка: +994 70 255 59 09 (Нериман) | 07:00 - 24:00',
            nights: 'ночей',
            nights_one: 'ночь'
        },
        en: {
            nameLabel: 'Your Name',
            phoneLabel: 'Phone Number',
            checkInLabel: 'Check-in Date',
            checkOutLabel: 'Check-out Date',
            guestsLabel: 'Number of Guests',
            commentsLabel: 'Additional Notes',
            commentsPlaceholder: 'Your preferences, questions...',
            submitBtn: '📱 Send via WhatsApp',
            guestOptions: ['1 guest', '2 guests', '3 guests', '4 guests', '5 guests', '6+ guests'],
            validationFillAll: 'Please fill in all required fields!',
            validationInvalidDates: 'Check-out date must be after check-in date!',
            confirmation: '✅ Your booking request is ready! WhatsApp will open.',
            support: '📞 Support: +994 70 255 59 09 (Neriman) | 07:00 - 24:00',
            nights: 'nights',
            nights_one: 'night'
        },
        ar: {
            nameLabel: 'اسمك',
            phoneLabel: 'رقم الهاتف',
            checkInLabel: 'تاريخ الوصول',
            checkOutLabel: 'تاريخ المغادرة',
            guestsLabel: 'عدد الضيوف',
            commentsLabel: 'ملاحظات إضافية',
            commentsPlaceholder: 'تفضيلاتك، أسئلتك...',
            submitBtn: '📱 إرسال عبر واتساب',
            guestOptions: ['ضيف واحد', 'ضيفان', '3 ضيوف', '4 ضيوف', '5 ضيوف', '6+ ضيوف'],
            validationFillAll: 'يرجى ملء جميع الحقول المطلوبة!',
            validationInvalidDates: 'يجب أن يكون تاريخ المغادرة بعد تاريخ الوصول!',
            confirmation: '✅ طلب الحجز جاهز! سيُفتتح واتساب.',
            support: '📞 الدعم: +994 70 255 59 09 (نيريمان) | 07:00 - 24:00',
            nights: 'ليالٍ',
            nights_one: 'ليلة'
        }
    };
    
    const lang = getCurrentLang();
    const t = translations[lang];
    
    // Set guest options
    const guestsSelect = document.getElementById('guests');
    if (guestsSelect) {
        guestsSelect.innerHTML = '';
        t.guestOptions.forEach((option, index) => {
            const opt = document.createElement('option');
            opt.value = index + 1;
            opt.textContent = option;
            if (index === 1) opt.selected = true;
            guestsSelect.appendChild(opt);
        });
    }
    
    // Set placeholder for comments
    const commentsField = document.getElementById('comments');
    if (commentsField) {
        commentsField.placeholder = t.commentsPlaceholder;
    }
    
    // Set minimum date to today
    const today = new Date().toISOString().split('T')[0];
    const checkInField = document.getElementById('checkin');
    const checkOutField = document.getElementById('checkout');
    
    if (checkInField) {
        checkInField.setAttribute('min', today);
    }
    if (checkOutField) {
        checkOutField.setAttribute('min', today);
    }
    
    // Update checkout min date when checkin changes
    if (checkInField && checkOutField) {
        checkInField.addEventListener('change', function() {
            const checkInDate = new Date(this.value);
            checkInDate.setDate(checkInDate.getDate() + 1);
            checkOutField.setAttribute('min', checkInDate.toISOString().split('T')[0]);
        });
    }
    
    // Form submission handler
    bookingForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Collect form data
        const guestName = document.getElementById('guest-name')?.value.trim();
        const guestPhone = document.getElementById('guest-phone')?.value.trim();
        const checkIn = checkInField?.value;
        const checkOut = checkOutField?.value;
        const guests = guestsSelect?.value;
        const comments = commentsField?.value.trim();
        
        // Validate required fields
        if (!guestName || !guestPhone || !checkIn || !checkOut) {
            alert(t.validationFillAll);
            return;
        }
        
        // Validate dates
        if (new Date(checkOut) <= new Date(checkIn)) {
            alert(t.validationInvalidDates);
            return;
        }
        
        // Calculate number of nights
        const nights = Math.ceil((new Date(checkOut) - new Date(checkIn)) / (1000 * 60 * 60 * 24));
        
        // Format dates for display
        const formatDate = (dateStr) => {
            if (!dateStr) return '';
            const date = new Date(dateStr);
            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            if (lang === 'ru') return date.toLocaleDateString('ru-RU', options);
            if (lang === 'az') return date.toLocaleDateString('az-AZ', options);
            if (lang === 'ar') return date.toLocaleDateString('ar-EG', options);
            return date.toLocaleDateString('en-US', options);
        };
        
        // Get guest text (always in Azerbaijani)
        const guestTextAz = ['1 nəfər', '2 nəfər', '3 nəfər', '4 nəfər', '5 nəfər', '6+ nəfər'][parseInt(guests) - 1];
        
        // Language name in Azerbaijani for the comment indicator
        const langNamesAz = {
            az: 'Azərbaycanca',
            ru: 'Rusca',
            en: 'İngiliscə',
            ar: 'Ərəbcə'
        };
        
        // Build WhatsApp message - ALWAYS in Azerbaijani
        let message = `🏔️ *Quba Dağ Evi - Bron Sorğusu*\n\n`;
        message += `👤 *Ad:* ${guestName}\n`;
        message += `📞 *Telefon:* ${guestPhone}\n`;
        message += `📅 *Giriş:* ${formatDate(checkIn)}\n`;
        message += `🚪 *Çıxış:* ${formatDate(checkOut)}\n`;
        message += `🌙 *Gecə sayı:* ${nights} gecə\n`;
        message += `👥 *Qonaq sayı:* ${guestTextAz}\n`;
        
        if (comments) {
            message += `\n📝 *Qeydlər (${langNamesAz[lang] || lang}):*\n${comments}`;
        }
        
        // Add timestamp
        const now = new Date();
        const timestamp = now.toLocaleDateString('az-AZ', {
            year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit'
        });
        message += `\n\n⏰ ${timestamp}`;
        
        // Encode message for WhatsApp URL
        const encodedMessage = encodeURIComponent(message);
        
        // WhatsApp phone number (owner)
        const phoneNumber = '994702555909';
        
        // Open WhatsApp with pre-filled message
        const whatsappUrl = `https://wa.me/${phoneNumber}?text=${encodedMessage}`;
        window.open(whatsappUrl, '_blank');
        
        // Show confirmation
        console.log('Booking request prepared and WhatsApp opened!');
        alert(t.confirmation);
    });
});
