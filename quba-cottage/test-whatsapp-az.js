// Updated WhatsApp Booking Message Simulator (Azerbaijani Only)
// Shows how messages look regardless of customer's language

function generateWhatsAppBookingMessageAz(lang, bookingData) {
    const { guestName, guestPhone, checkIn, checkOut, guests, comments } = bookingData;
    
    // Calculate number of nights
    const nights = Math.ceil((new Date(checkOut) - new Date(checkIn)) / (1000 * 60 * 60 * 24));
    
    // Format dates for display (Azerbaijani format)
    const formatDate = (dateStr) => {
        if (!dateStr) return '';
        const date = new Date(dateStr);
        return date.toLocaleDateString('az-AZ', { year: 'numeric', month: 'long', day: 'numeric' });
    };
    
    // Guest options in Azerbaijani
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
        // Add language indicator for comments
        message += `\n📝 *Qeydlər (${langNamesAz[lang] || lang}):*\n${comments}`;
    }
    
    // Add timestamp (Azerbaijani format)
    const now = new Date();
    const timestamp = now.toLocaleDateString('az-AZ', {
        year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit'
    });
    message += `\n\n⏰ ${timestamp}`;
    
    return message;
}

// Test data
const testBooking = {
    guestName: 'Иван Иванов',
    guestPhone: '+7 999 123 45 67',
    checkIn: '2026-01-15',
    checkOut: '2026-01-18',
    guests: '4',
    comments: 'Мы хотим забронировать дом на выходные. Нам нужна детская кроватка для ребенка 2 года. Можно ли организовать трансфер из аэропорта?'
};

console.log('🧪 WhatsApp Booking System - АЗЕРБАЙДЖАНСКИЙ ЯЗЫК');
console.log('='.repeat(70));
console.log('Теперь ВСЕ сообщения отправляются на АЗЕРБАЙДЖАНСКОМ языке!');
console.log('Независимо от того, на каком языке клиент заполнил форму.\n');

// Test different customer languages
const testScenarios = [
    { lang: 'az', customerLang: 'азербайджанец', flag: '🇦🇿', comment: 'Hörmətli Neriman, biz sizin dağ evinizə gəlmək istəyirik. Ailəmiz ilə birlikdə 3 gün qalmağı planlaşdırırıq.' },
    { lang: 'ru', customerLang: 'русский', flag: '🇷🇺', comment: 'Мы хотим забронировать дом на выходные. Нам нужна детская кроватка для ребенка 2 года. Можно ли организовать трансфер из аэропорта?' },
    { lang: 'en', customerLang: 'англичанин', flag: '🇬🇧', comment: 'We would like to book your mountain house for our family vacation. We need a baby crib for our 2 year old child. Is airport transfer available?' },
    { lang: 'ar', customerLang: 'араб', flag: '🇸🇦', comment: 'نريد حجز بيت الجبال لعطلتنا العائلية. نحتاج سرير طفل عمره سنتان. هل يتوفر نقل من المطار؟' }
];

for (const scenario of testScenarios) {
    const testData = { ...testBooking, comments: scenario.comment };
    
    console.log(`\n${scenario.flag} Клиент говорит на ${scenario.customerLang} языке:`);
    console.log(`Комментарий клиента: "${scenario.comment.substring(0, 60)}..."`);
    console.log('-'.repeat(70));
    
    const message = generateWhatsAppBookingMessageAz(scenario.lang, testData);
    console.log(message);
    console.log('');
}

console.log('='.repeat(70));
console.log('📊 ИТОГ:');
console.log('='.repeat(70));
console.log('✅ Структура сообщения ВСЕГДА на азербайджанском');
console.log('✅ Даты в азербайджанском формате');
console.log('✅ Количество гостей на азербайджанском');
console.log('✅ Комментарии клиента сохранены как есть');
console.log('✅ Добавлена пометка о языке комментария');
console.log('\n💡 Владелец получит сообщение на родном языке и сможет');
console.log('   понять суть запроса, даже если написан на другом языке!');
console.log('\n🔗 Прямая ссылка для теста:');
const testMessage = generateWhatsAppBookingMessageAz('ru', testBooking);
console.log('https://wa.me/994702555909?text=' + encodeURIComponent(testMessage));
